# MOUSSE Carel Brian, Master IA 1 Jan23
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import requests
import os
import sys
import shutil

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def plot_x_squared():
    x = np.linspace(-10, 10, 100)
    y = x**2
    plt.plot(x, y)
    plt.title("Courbe d'équation x^2")
    plt.xlabel("x")
    plt.ylabel("y = x^2")
    plt.show()

def plot_x_cubed():
    x = np.linspace(-10, 10, 100)
    y = x**3
    plt.plot(x, y)
    plt.title("Courbe d'équation x^3")
    plt.xlabel("x")
    plt.ylabel("y = x^3")
    plt.show()

def main():
    # Tracer les deux courbes
    plot_x_squared()
    plot_x_cubed()

# Fonction pour créer une issue sur GitHub
def create_github_issue(username, access_token, repo_name, title, body):
    url = f"https://api.github.com/repos/{username}/{repo_name}/issues"
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {"title": title, "body": body}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Issue '{title}' créée avec succès.")
    else:
        print("Erreur lors de la création de l'issue.")

# Fonction pour déclencher workflow
def trigger_workflow(username, repo_name, workflow_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/actions/workflows/{workflow_name}/dispatches"
    headers = {
        "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json",
    }
    payload = {"ref": "main"}  # Assurez-vous que la branche est correcte

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 204:
        print("Workflow déclenché avec succès.")
    else:
        print("Erreur lors du déclenchement du workflow. Code de statut : {response.status_code}")
        print(response.text)


# Fonction pour créer un repertoire
def create_directory(path):
    os.makedirs(path, exist_ok=True)

# Fonction pour créer un fichier
def create_file(path, content=""):
    with open(path, "w") as f:
        f.write(content)

# Fonction pour effectuer un commit Git
def git_commit(directory, message):
    subprocess.run(["git", "add", "."], cwd=directory)
    # Afficher l'état du dépôt avant de commettre
    subprocess.run(["git", "status"], cwd=directory)
    subprocess.run(["git", "commit", "-m", message], cwd=directory)


# Fonction pour effectuer un push Git
def git_push(directory, branch="main"):
    subprocess.run(["git", "push", "origin", branch], cwd=directory)

# Fonction pour configurer les dossiers du projet
def setup_directories(target_directory):
    create_directory(target_directory)
    create_directory(os.path.join(target_directory, "docs"))


# Fonction pour configurer le fichier README.md
def setup_readme(target_directory):
    readme_content = """
        # Application conçu dans le cadre de l'examen DevOps

        Ceci est une description du projet effectué dans le cadre du devoir de DevOps.


        ## Explication du Code Python

        Le programme crée un ensemble de fonctions nécessaires fichiers readme, .gitignore, LICENSE, un fichier yml pour les actions github, un programme main.py
        et décrit les 5 commits et tickets correspondants sont créés.
        
        Le programme si on l’execute effectue les tâches suivantes à l’aide de Github Actions :
        • tracer la courbe d’équation x²
        • tracer la courbe d’équation x³


        ### Importation des modules

        Les modules sont importés au début du script.

        Les fonctions sont créées ensuite


        ### Fichier Github Actions

            name: Tracer les courbes

            on:
            push:
                branches:
                - main

            jobs:
            build:
                runs-on: ubuntu-latest

                steps:
                - name: Checkout du code
                    uses: actions/checkout@v2

                - name: Configurer Python
                    uses: actions/setup-python@v2
                    with:
                    python-version: 3.8

                - name: Installer les dépendances
                    run: |
                    python -m pip install --upgrade pip
                    pip install matplotlib

                - name: Exécuter le script x_squared
                    run: python main.py x_squared

                - name: Exécuter le script x_cubed
                    run: python main.py x_cubed

                - name: Déclencher les actions
                    run: |
                    python main.py trigger_workflow
                

        ## Configuration

        Avant d'exécuter le script, assurez-vous d'avoir configuré correctement votre environnement. Suivez les étapes ci-dessous pour préparer l'environnement :

        1. **Créez un jeton d'accès personnel sur GitHub :**
            - Allez sur votre compte GitHub et accédez aux paramètres du compte.
            - Dans la section "Developer settings", cliquez sur "Personal access tokens".
            - Générez un nouveau jeton avec les autorisations appropriées (au moins "repo").
            - Copiez ce jeton, car vous en aurez besoin plus tard.

            
        2. **Clonez le dépôt :**
            - Clonez ce dépôt GitHub sur votre machine en exécutant la commande suivante dans le terminal :
              ```
              git clone https://github.com/VOTRE-NOM-D-UTILISATEUR/github-project.git
              ```

        3. **Créez un environnement virtuel :**
            - Ouvrez votre projet dans Visual Studio Code.
            - Ouvrez le terminal intégré en allant dans le menu View > Terminal 
              ou en utilisant le raccourci Ctrl + .
            - Dans le terminal, accédez au répertoire de votre projet en utilisant la commande cd (change directory). 
              Par exemple, si votre projet est dans le dossier "github-project", vous pouvez utiliser la commande suivante pour vous y rendre :
              ```
              cd chemin/vers/votre/projet/github-project
              ```
            - Créez un environnement virtuel en exécutant :
              ```
              python -m venv venv
              ```
            - Activez l'environnement virtuel :
                - Sur Windows :
                  ```
                  venv\Scripts\activate
                  ```
                - Sur macOS et Linux :
                  ```
                  source venv/bin/activate
                  ```

        4. **Installez les dépendances :**
            - Installez les dépendances requises en exécutant :
              ```
              pip install -r requirements.txt
              ```

        ## Utilisation

        Suivez ces étapes pour exécuter le script et créer votre projet sur GitHub :

        1. **Exécutez le script :**
            - Ouvrez un terminal et accédez au répertoire du projet.
            - Exécutez le script en utilisant la commande suivante :
              ```
              python github_project_setup.py
              ```
   
        2. **Suivez les instructions :**
            - Le script vous guidera tout au long du processus en vous demandant diverses informations.
            - Fournissez les informations demandées, telles que le nom du répertoire, le nom d'utilisateur GitHub, etc.

            
        3. **Créez des tickets :**
            - Le script créera automatiquement des tickets pour chaque tâche à effectuer.
            - Vous pouvez vérifier les tickets créés sur la page du dépôt GitHub.

            
        4. **Personnalisez le projet :**
            - Personnalisez le contenu des fichiers créés selon vos besoins.

            
        5. **Déployez le projet :**
            - Le projet sera automatiquement déployé sur votre compte GitHub.

            
           ## NB:Installation des dépendances

           Une fois que vous avez configuré la structure du projet à l'aide du fichier `github_project_setup.py`, vous devrez également 
           installer les dépendances nécessaires. Les dépendances sont répertoriées dans le fichier `requirements.txt`.

           - Ouvrez le fichier `requirements.txt` nouvellement créé après avoir exécuté `github_project_setup.py`.

           - Ajoutez les noms des packages dont vous avez besoin, chaque nom de package sur une ligne distincte.

           - Ouvrez un terminal dans VS Code et exécutez la commande suivante pour installer les dépendances à partir du fichier `requirements.txt` :
             ```
             pip install -r requirements.txt
             ```
           - Assurez-vous d'installer les dépendances avant d'exécuter le code ou les notebooks de votre projet. 


           ### Variable d'environnement
   
           La variable d'environnement "GITHUB_ACCESS_TOKEN" est une variable que vous devez créer dans votre système d'exploitation ou 
           dans votre environnement de développement. Voici comment vous pouvez la créer :

           - Système d'exploitation (Windows) :

            - Cliquez avec le bouton droit sur l'icône "Ordinateur" ou "Ce PC" sur votre bureau.
	 
            - Sélectionnez "Propriétés".
	 
            - Cliquez sur "Paramètres système avancés" dans le volet de gauche.
	 
            - Dans l'onglet "Avancé", cliquez sur le bouton "Variables d'environnement".
	 
            - Sous la section "Variables système", cliquez sur "Nouvelle".
	 
            - Dans le champ "Nom de la variable", entrez "GITHUB_ACCESS_TOKEN".
	 
            - Dans le champ "Valeur de la variable", entrez votre jeton d'accès GitHub.
	 
            - Cliquez sur "OK" pour fermer les fenêtres de dialogue.
	 

          - Système d'exploitation (macOS) :

            - Ouvrez le terminal.
	 
            - Utilisez une commande comme echo 'export GITHUB_ACCESS_TOKEN=YOUR_ACCESS_TOKEN' >> ~/.bash_profile en remplaçant YOUR_ACCESS_TOKEN par votre jeton d'accès GitHub.
	 
            - Exécutez source ~/.bash_profile pour mettre à jour les variables d'environnement.
	 

          - Système d'exploitation (Linux) :

            - Ouvrez un terminal.
	 
            - Utilisez une commande comme echo 'export GITHUB_ACCESS_TOKEN=YOUR_ACCESS_TOKEN' >> ~/.bashrc en remplaçant YOUR_ACCESS_TOKEN par votre jeton d'accès GitHub.
	 
            - Exécutez source ~/.bashrc pour mettre à jour les variables d'environnement.
	 
            - L'idée est de définir cette variable d'environnement avec la valeur de votre jeton d'accès GitHub afin que votre code puisse l'utiliser pour l'authentification.


            
        ## LICENSE

        MIT License

        Droit d'auteur (c) 2023 Carel Brian MOUSSE

        La permission est par la présente accordée, gratuitement, à toute personne obtenant une copie
        de ce logiciel et des fichiers de documentation associés (le "Logiciel"), d'utiliser le Logiciel
        sans restriction, notamment les droits d'utiliser, de copier, de modifier, de fusionner, de publier,
        de distribuer, de sous-licencier et/ou de vendre des copies du Logiciel, ainsi que d'autoriser
        les personnes à qui le Logiciel est fourni à en faire de même, sous réserve des conditions suivantes :

        [Ici, vous pouvez ajouter des termes et conditions spécifiques de la licence, tels que :]

        - Il n'est pas autorisé d'utiliser ce logiciel à des fins commerciales sans la permission écrite explicite de l'auteur.
        - Vous devez attribuer l'auteur original dans toute œuvre dérivée basée sur ce logiciel.
        - Toutes les modifications apportées au logiciel doivent être clairement documentées et indiquées dans le code source.
        - Ce logiciel est fourni "tel quel", et l'auteur n'assume aucune responsabilité pour les dommages ou les responsabilités résultant de son utilisation.

        LE LOGICIEL EST FOURNI "TEL QUEL", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE,
        NOTAMMENT SANS GARANTIE DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET D'ABSENCE
        DE CONTREFAÇON. EN AUCUN CAS, LES AUTEURS OU LES TITULAIRES DU DROIT D'AUTEUR NE SERONT
        RESPONSABLES DES RÉCLAMATIONS, DOMMAGES OU AUTRES RESPONSABILITÉS, QUE CE SOIT DANS UNE ACTION
        EN CONTRAT, UN DÉLIT OU AUTRE, DÉCOULANT DE, OU EN LIEN AVEC LE LOGICIEL OU SON UTILISATION
        OU D'AUTRES RELATIONS DANS LE LOGICIEL.


        ## .gitignore 




        
        ## Auteurs

            - Carel Brian MOUSSE - [@CarelBrian](https://github.com/CarelBrian)

        """
    readme_path = os.path.join(target_directory, "README.md")
    create_file(readme_path, readme_content)

# Fonction pour configurer le requirements.txt
def setup_gitignore(target_directory):
    gitignore_content = """
    # Fichiers temporaires
    *.log
    *.swp
    *.tmp

    # Répertoires générés
    _pycache_/
    venv/
    node_modules/

    # Fichiers de configuration spécifiques à l'utilisateur
    .DS_Store
    Thumbs.db

    # Fichiers d'environnement
    .env
    .env.local

    # Fichiers de sortie ou de build
    /build/
    /dist/
    /out/

    # Fichiers de dépendances Python
    *.pyc
    *.pyo

    # Fichiers spécifiques à certains éditeurs ou IDE
    .vscode/
    .idea/
    .sublime-

        """
    gitignore_path = os.path.join(target_directory, ".gitignore")
    create_file(gitignore_path, gitignore_content)

# Fonction pour configurer la licence
def setup_license(target_directory):
    license_content = """
        MIT License

        Droit d'auteur (c) 2023 Carel Brian MOUSSE

        La permission est par la présente accordée, gratuitement, à toute personne obtenant une copie
        de ce logiciel et des fichiers de documentation associés (le "Logiciel"), d'utiliser le Logiciel
        sans restriction, notamment les droits d'utiliser, de copier, de modifier, de fusionner, de publier,
        de distribuer, de sous-licencier et/ou de vendre des copies du Logiciel, ainsi que d'autoriser
        les personnes à qui le Logiciel est fourni à en faire de même, sous réserve des conditions suivantes :

        [Ici, vous pouvez ajouter des termes et conditions spécifiques de la licence, tels que :]

        - Il n'est pas autorisé d'utiliser ce logiciel à des fins commerciales sans la permission écrite explicite de l'auteur.
        - Vous devez attribuer l'auteur original dans toute œuvre dérivée basée sur ce logiciel.
        - Toutes les modifications apportées au logiciel doivent être clairement documentées et indiquées dans le code source.
        - Ce logiciel est fourni "tel quel", et l'auteur n'assume aucune responsabilité pour les dommages ou les responsabilités résultant de son utilisation.

        LE LOGICIEL EST FOURNI "TEL QUEL", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE,
        NOTAMMENT SANS GARANTIE DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET D'ABSENCE
        DE CONTREFAÇON. EN AUCUN CAS, LES AUTEURS OU LES TITULAIRES DU DROIT D'AUTEUR NE SERONT
        RESPONSABLES DES RÉCLAMATIONS, DOMMAGES OU AUTRES RESPONSABILITÉS, QUE CE SOIT DANS UNE ACTION
        EN CONTRAT, UN DÉLIT OU AUTRE, DÉCOULANT DE, OU EN LIEN AVEC LE LOGICIEL OU SON UTILISATION
        OU D'AUTRES RELATIONS DANS LE LOGICIEL.

        """
    license_path = os.path.join(target_directory, "docs", "LICENSE.txt")
    create_file(license_path, license_content)

# Fonction pour copier le fichier main.yaml
def setup_makefile(target_directory):
    makefile_content = """
    name: Tracer les courbes

    on:
    push:
        branches:
        - main

    jobs:
    build:
        runs-on: ubuntu-latest

        steps:
        - name: Checkout du code
            uses: actions/checkout@v2

        - name: Configurer Python
            uses: actions/setup-python@v2
            with:
            python-version: 3.8

        - name: Installer les dépendances
            run: |
            python -m pip install --upgrade pip
            pip install matplotlib

        - name: Exécuter le script x_squared
            run: python main.py x_squared

        - name: Exécuter le script x_cubed
            run: python main.py x_cubed

        - name: Déclencher les actions
            run: |
            python main.py trigger_workflow

        """
    
    makefile_path = os.path.join(target_directory, "main.yaml")
    create_file(makefile_path, makefile_content)

    # Fonction pour copier le fichier main.py 
def setup_mainfile(target_directory):
    # Create the file if it does not exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Copy the main.py file
    source_path = os.path.join(os.path.dirname(__file__), "main.py")
    destination_path = os.path.join(target_directory, "docs", "main.py")
    shutil.copyfile(source_path, destination_path)



if __name__ == "__main__":
    main()
    # Remplacez ces valeurs par les informations appropriées
    username = "CarelBrian"
    access_token = "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"
    repo_name = "m1_exam_devops"
    target_directory = "m1_exam_devops"

     # Dictionnaire des tâches à effectuer avec leur description
    tasks = {
        "Ajoute du fichier des actions Github main.yaml": setup_makefile,
        "Ajouter du fichier readme": setup_readme,
        "Ajouter le contenu du fichier gitignore": setup_gitignore,
        "Configurer la licence": setup_license,
        "Ajouter le fichier du programme et déclencher les actions" : setup_mainfile
    }
    issue_number = 1 # Initialiser le numéro de l'issue
    for task, setup_function in tasks.items():
        # Créer une issue sur GitHub pour la tâche en cours
        issue_title = f"Travail sur la tâche : {task}"
        create_github_issue(username, access_token, repo_name, task, issue_title)

        # Affichage du message de confirmation
        print(f"Issue '{issue_title}' créée avec succès.")

        # Effectuer la configuration de la tâche
        setup_function(target_directory)

        # Effectuer un commit local avec le message de la tâche
        git_commit(target_directory, f"{task}\n\nFixes #{issue_number}")

        # Pousser les changements vers le dépôt distant
        git_push(target_directory)

        # Incrémenter le numéro de l'issue pour la tâche suivante
        issue_number += 1


    if len(sys.argv) > 1:
        if sys.argv[1] == "x_squared":
            plot_x_squared()
            trigger_workflow(username, repo_name, "main.yaml")
        elif sys.argv[1] == "x_cubed":
            plot_x_cubed()
            trigger_workflow(username, repo_name, "main.yaml")
    else:
        print("Utilisation : python main.py x_squared | x_cubed")

    