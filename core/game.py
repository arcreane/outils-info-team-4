import pygame
import sys
from entities.player import Player

class Game:
    def __init__(self, player_name):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Shoot Them Up")
        
        self.clock = pygame.time.Clock()
        self.running = True

        # Gestion des sprites
        self.all_sprites = pygame.sprite.Group()
        
        
        self.player = Player(self.screen_width // 2, self.screen_height - 100, player_name)
        self.all_sprites.add(self.player)

    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0)) # Fond noir
        self.all_sprites.draw(self.screen)
        pygame.display.flip()