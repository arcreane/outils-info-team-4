PROJET SHOOT THEM UP

Description :
Ce projet est un jeu de tir developpe en Python avec Pygame

EQUIPE
- Ezechiel 
- Antonin


ARCHITECTURE DU PROJET
Nous avons organise le code en modules independants :
- core : Contient la boucle de jeu (GameLoop) et la gestion de la fenetre.
- entities : Contient les objets vivants (Joueur, Ennemis) heritant de la classe Entity.
- weapons : Gere les armes et les projectiles.
- ui : Gere l'affichage tete haute (Score) et les menus.
- assets : Dossier de stockage pour les images et les sons.

REGLES DE COLLABORATION
Pour garantir la qualite du projet, l'equipe suit ces regles :

1. BRANCHES
Ne jamais travailler directement sur la branche main.
Creer une branche par tache (exemple : feat/player-movement).

2. COMMITS
Nous utilisons la convention Angular pour les messages :
- feat(scope) : pour une nouvelle fonctionnalité
- fix(scope) : pour une correction de bug
- docs(scope) : pour la documentation

3. WORKFLOW
Toujours effectuer un "git pull" avant de commencer a coder pour eviter les conflits.