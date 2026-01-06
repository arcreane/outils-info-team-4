ARCHITECTURE DU PROJET SHOOT THEM UP



1\. DECOUPAGE DES MODULES

\- core : Contient la boucle de jeu et la gestion de la fenetre.

\- entities : Contient le code du Joueur et des Ennemis.

\- weapons : Gere les projectiles et les tirs.

\- ui : Gere l'affichage du score et des menus.

\- assets : Dossier pour les images et les sons.

\- utils : Outils techniques et constantes.



2\. HIERARCHIE DES CLASSES (POO)

Classe Entity (Parent) :

Elle definit ce qui est commun a tous les objets (position, image, mise a jour).



-> Classe Player (Enfant de Entity) :

Elle ajoute la gestion des touches clavier pour bouger et tirer.



-> Classe Enemy (Enfant de Entity) :

Elle ajoute un deplacement automatique et une intelligence artificielle simple.



3\. JUSTIFICATION DE L'ARCHITECTURE

Nous utilisons l'heritage (Entity) pour ne pas recoder deux fois la gestion de l'image et de la position.

Cette structure en dossiers permet de separer la logique du jeu (entities) de l'affichage (ui).

Cela facilite le travail en equipe car chacun peut travailler sur un dossier different sans creer de conflits.

