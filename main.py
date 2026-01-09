from core.game import Game

def main():
    print("--------------------------------")
    print("   BIENVENUE DANS SHOOT THEM UP   ")
    print("--------------------------------")
    
    # On demande le nom
    player_name = input("Entrez votre nom de pilote : ")
    
    print(f"Lancement de la mission pour {player_name}...")
    
    # On lance le jeu
    # C'est ici que pygame.init() sera appelé (dans le constructeur de Game)
    game = Game(player_name)
    game.run()

if __name__ == "__main__":
    main()