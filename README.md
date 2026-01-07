PROJET SHOOT THEM UP

Description :
Ce projet est un jeu de tir développe en Python avec Pygame

EQUIPE

* Ezechiel
* Antonin



ARCHITECTURE DU PROJET
Rangement des fichier/dossiers :

* core : Contient la boucle de jeu (GameLoop) et la gestion de la fenêtre.
* entities : Dossier qui contient les objets du jeu. 
* weapons : Gere les armes et les projectiles (pour l'instant vide)
* ui : Gere l'affichage tête haute (Score) et les menus.
* assets : Dossier de stockage pour les images et les sons.
* &nbsp; - main.py : Sert uniquement a lancer le jeu.
* &nbsp; - entity.py : La base commune (position, image).
* &nbsp; - player.py : Le code du joueur.
* &nbsp; - enemy.py : Le code des ennemis.





REGLES DE COLLABORATION



1\. BRANCHES

Ne jamais travailler directement sur la branche main.

Créer une branche par tache (exemple : feat/player-movement).



2\. COMMITS

Nous utilisons la convention angular : type(scope): message



Les types :

feat : pour une nouvelle fonctionnalité

fix : pour une correction de bug

docs : pour la documentation



Le scope :

C'est  le nom du fichier ou du dossier que tu as modifie.

Cela permet de savoir tout de suite ou a eu lieu le changement.



Exemples de scope :

\- Si tu modifies player.py > feat(player): ajout de la vie

\- Si tu modifies game.py > fix(core): correction du lag

\- Si tu modifies le readme > docs(readme): mise a jour des règles



3\. WORKFLOW

Toujours effectuer un "git pull" avant de commencer a coder pour éviter les problèmes.

Lien Trello :



https://trello.com/invite/b/695d2050f690da68b2918f25/ATTI171a36cb782ed7b9bb4efc927541b18e1E9AFDF5/projet-shoot-them-up

