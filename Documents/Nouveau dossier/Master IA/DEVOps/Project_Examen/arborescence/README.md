
        # Application con�u dans le cadre du Devoir DevOps

        Ceci est une description du projet effectu� dans le cadre du devoir de DevOps.


        ## Explication du Code Python

        Ce projet est g�r� par un script Python (`github_project_setup.py`) qui automatise la cr�ation d'une arborescence pour un projet GitHub. 
        Voici une br�ve explication de certaines parties cl�s du code :

        ### Importation des modules

        Les modules sont import�s au d�but du script.

        
        ### `GitHubProject` Class

        La classe `GitHubProject` est responsable de l'interaction avec l'API GitHub. Elle comprend des m�thodes pour cr�er des r�pertoires, 
        des fichiers, effectuer des commits et cr�er des tickets. Ces fonctions sont les suivantes:

        - __init__(self, username, access_token, repo_name): Initialise la classe avec les informations n�cessaires pour interagir avec l'API GitHub.

        - create_directory(self, path): Cr�e un r�pertoire.

        - create_file(self, path, content=""): Cr�e un fichier avec un contenu donn�.

        - git_commit(self, directory, message): Effectue un commit Git dans un r�pertoire donn�.

        - create_issue(self, title, body): Cr�e un ticket GitHub avec un titre et un corps donn�s.


        ### `ProjectSetup` Class

        La classe `ProjectSetup` orchestre le processus de configuration et de cr�ation du projet. Elle cr�e les r�pertoires n�cessaires, 
        g�n�re le contenu du README.md, effectue des commits et cr�e des tickets. Ces fonctions sont les suivantes:

        - __init__(self, project, directory_name): Initialise la classe avec une instance de GitHubProject et le nom du r�pertoire.

        - setup_directories(self): Cr�e la structure de r�pertoire sp�cifi�e.

        - setup_readme(self): Cr�e le contenu du fichier README.md.

        - setup_repo(self): Initialise un d�p�t Git et effectue un commit initial.

        - create_tickets(self): Cr�e des tickets GitHub pour diff�rentes t�ches.


        ## Configuration

        Avant d'ex�cuter le script, assurez-vous d'avoir configur� correctement votre environnement. Suivez les �tapes ci-dessous pour pr�parer l'environnement :

        1. **Cr�ez un jeton d'acc�s personnel sur GitHub :**
            - Allez sur votre compte GitHub et acc�dez aux param�tres du compte.
            - Dans la section "Developer settings", cliquez sur "Personal access tokens".
            - G�n�rez un nouveau jeton avec les autorisations appropri�es (au moins "repo").
            - Copiez ce jeton, car vous en aurez besoin plus tard.

            
        2. **Clonez le d�p�t :**
            - Clonez ce d�p�t GitHub sur votre machine en ex�cutant la commande suivante dans le terminal :
              ```
              git clone https://github.com/VOTRE-NOM-D-UTILISATEUR/github-project.git
              ```

        3. **Cr�ez un environnement virtuel :**
            - Ouvrez votre projet dans Visual Studio Code.
            - Ouvrez le terminal int�gr� en allant dans le menu View > Terminal 
              ou en utilisant le raccourci Ctrl + .
            - Dans le terminal, acc�dez au r�pertoire de votre projet en utilisant la commande cd (change directory). 
              Par exemple, si votre projet est dans le dossier "github-project", vous pouvez utiliser la commande suivante pour vous y rendre :
              ```
              cd chemin/vers/votre/projet/github-project
              ```
            - Cr�ez un environnement virtuel en ex�cutant :
              ```
              python -m venv venv
              ```
            - Activez l'environnement virtuel :
                - Sur Windows :
                  ```
                  venv\Scriptsctivate
                  ```
                - Sur macOS et Linux :
                  ```
                  source venv/bin/activate
                  ```

        4. **Installez les d�pendances :**
            - Installez les d�pendances requises en ex�cutant :
              ```
              pip install -r requirements.txt
              ```

        ## Utilisation

        Suivez ces �tapes pour ex�cuter le script et cr�er votre projet sur GitHub :

        1. **Ex�cutez le script :**
            - Ouvrez un terminal et acc�dez au r�pertoire du projet.
            - Ex�cutez le script en utilisant la commande suivante :
              ```
              python github_project_setup.py
              ```
   
        2. **Suivez les instructions :**
            - Le script vous guidera tout au long du processus en vous demandant diverses informations.
            - Fournissez les informations demand�es, telles que le nom du r�pertoire, le nom d'utilisateur GitHub, etc.

            
        3. **Cr�ez des tickets :**
            - Le script cr�era automatiquement des tickets pour chaque t�che � effectuer.
            - Vous pouvez v�rifier les tickets cr��s sur la page du d�p�t GitHub.

            
        4. **Personnalisez le projet :**
            - Personnalisez le contenu des fichiers cr��s selon vos besoins.

            
        5. **D�ployez le projet :**
            - Le projet sera automatiquement d�ploy� sur votre compte GitHub.

            
           ## NB:Installation des d�pendances

           Une fois que vous avez configur� la structure du projet � l'aide du fichier `github_project_setup.py`, vous devrez �galement 
           installer les d�pendances n�cessaires. Les d�pendances sont r�pertori�es dans le fichier `requirements.txt`.

           - Ouvrez le fichier `requirements.txt` nouvellement cr�� apr�s avoir ex�cut� `github_project_setup.py`.

           - Ajoutez les noms des packages dont vous avez besoin, chaque nom de package sur une ligne distincte.

           - Ouvrez un terminal dans VS Code et ex�cutez la commande suivante pour installer les d�pendances � partir du fichier `requirements.txt` :
             ```
             pip install -r requirements.txt
             ```
           - Assurez-vous d'installer les d�pendances avant d'ex�cuter le code ou les notebooks de votre projet. 


           ### Variable d'environnement
   
           La variable d'environnement "GITHUB_ACCESS_TOKEN" est une variable que vous devez cr�er dans votre syst�me d'exploitation ou 
           dans votre environnement de d�veloppement. Voici comment vous pouvez la cr�er :

           - Syst�me d'exploitation (Windows) :

            - Cliquez avec le bouton droit sur l'ic�ne "Ordinateur" ou "Ce PC" sur votre bureau.
	 
            - S�lectionnez "Propri�t�s".
	 
            - Cliquez sur "Param�tres syst�me avanc�s" dans le volet de gauche.
	 
            - Dans l'onglet "Avanc�", cliquez sur le bouton "Variables d'environnement".
	 
            - Sous la section "Variables syst�me", cliquez sur "Nouvelle".
	 
            - Dans le champ "Nom de la variable", entrez "GITHUB_ACCESS_TOKEN".
	 
            - Dans le champ "Valeur de la variable", entrez votre jeton d'acc�s GitHub.
	 
            - Cliquez sur "OK" pour fermer les fen�tres de dialogue.
	 

          - Syst�me d'exploitation (macOS) :

            - Ouvrez le terminal.
	 
            - Utilisez une commande comme echo 'export GITHUB_ACCESS_TOKEN=YOUR_ACCESS_TOKEN' >> ~/.bash_profile en rempla�ant YOUR_ACCESS_TOKEN par votre jeton d'acc�s GitHub.
	 
            - Ex�cutez source ~/.bash_profile pour mettre � jour les variables d'environnement.
	 

          - Syst�me d'exploitation (Linux) :

            - Ouvrez un terminal.
	 
            - Utilisez une commande comme echo 'export GITHUB_ACCESS_TOKEN=YOUR_ACCESS_TOKEN' >> ~/.bashrc en rempla�ant YOUR_ACCESS_TOKEN par votre jeton d'acc�s GitHub.
	 
            - Ex�cutez source ~/.bashrc pour mettre � jour les variables d'environnement.
	 
            - L'id�e est de d�finir cette variable d'environnement avec la valeur de votre jeton d'acc�s GitHub afin que votre code puisse l'utiliser pour l'authentification.


            
        ## LICENSE

        MIT License

        Droit d'auteur (c) 2023 Carel Brian MOUSSE

        La permission est par la pr�sente accord�e, gratuitement, � toute personne obtenant une copie
        de ce logiciel et des fichiers de documentation associ�s (le "Logiciel"), d'utiliser le Logiciel
        sans restriction, notamment les droits d'utiliser, de copier, de modifier, de fusionner, de publier,
        de distribuer, de sous-licencier et/ou de vendre des copies du Logiciel, ainsi que d'autoriser
        les personnes � qui le Logiciel est fourni � en faire de m�me, sous r�serve des conditions suivantes :

        [Ici, vous pouvez ajouter des termes et conditions sp�cifiques de la licence, tels que :]

        - Il n'est pas autoris� d'utiliser ce logiciel � des fins commerciales sans la permission �crite explicite de l'auteur.
        - Vous devez attribuer l'auteur original dans toute �uvre d�riv�e bas�e sur ce logiciel.
        - Toutes les modifications apport�es au logiciel doivent �tre clairement document�es et indiqu�es dans le code source.
        - Ce logiciel est fourni "tel quel", et l'auteur n'assume aucune responsabilit� pour les dommages ou les responsabilit�s r�sultant de son utilisation.

        LE LOGICIEL EST FOURNI "TEL QUEL", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE,
        NOTAMMENT SANS GARANTIE DE QUALIT� MARCHANDE, D'AD�QUATION � UN USAGE PARTICULIER ET D'ABSENCE
        DE CONTREFA�ON. EN AUCUN CAS, LES AUTEURS OU LES TITULAIRES DU DROIT D'AUTEUR NE SERONT
        RESPONSABLES DES R�CLAMATIONS, DOMMAGES OU AUTRES RESPONSABILIT�S, QUE CE SOIT DANS UNE ACTION
        EN CONTRAT, UN D�LIT OU AUTRE, D�COULANT DE, OU EN LIEN AVEC LE LOGICIEL OU SON UTILISATION
        OU D'AUTRES RELATIONS DANS LE LOGICIEL.


        ## .gitignore 




        
        ## Auteurs

            - Carel Brian MOUSSE - [@CarelBrian](https://github.com/CarelBrian)

        