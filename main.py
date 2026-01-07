from core.game import Game

if __name__ == "__main__":
    #Interface de lancement (tempo)
    print("--------------------------------")
    print("   BIENVENUE DANS SHOOT THEM UP  ")
    print("--------------------------------")
    
    pseudo = input("Entrez votre nom de pilote : ")
    
    if pseudo == "":
        pseudo = "Pilote Inconnu" # Nom par défaut si vide

    print(f"Lancement de la mission pour {pseudo}...")

    # ÉTAPE 2 : Démarrage du moteur graphique avec le nom choisi
    game = Game(pseudo)
    game.run()