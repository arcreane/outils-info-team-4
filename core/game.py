import pygame
import sys
from entities.player import Player
from entities.enemy import Enemy

class Game:
    def __init__(self, player_name):
        pygame.init()
        # config ecran
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Shoot Them Up")
        
        self.clock = pygame.time.Clock()
        self.running = True

        # groupes de sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        # creation joueur
        self.player = Player(self.screen_width // 2, self.screen_height - 100, player_name)
        self.all_sprites.add(self.player)

        # creation des 5 ennemis
        for _ in range(5):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

    def run(self):
        # boucle du jeu
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def handle_input(self):
        # gestion fermeture fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # update de tout le monde
        self.all_sprites.update()

    def draw(self):
        # fond noir et dessin
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()