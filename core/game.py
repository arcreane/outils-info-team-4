import pygame
import sys
from entities.player import Player
from entities.enemy import Enemy

class Game:
    def __init__(self, player_name):
        pygame.init()
        # ecran
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Shoot Them Up")
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        # etat menu
        self.in_menu = True
        # police
        self.font = pygame.font.Font(None, 50)

        # sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        # joueur
        self.player = Player(self.screen_width // 2, self.screen_height - 100, player_name)
        self.all_sprites.add(self.player)

        # ennemis
        for _ in range(5):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

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
            
            # validation menu
            if self.in_menu and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.in_menu = False

    def update(self):
        # pause si menu
        if self.in_menu:
            return
            
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

        if self.in_menu:
            # texte menu
            text = self.font.render("PRESS ENTER TO START", True, (255, 255, 255))
            rect = text.get_rect(center=(self.screen_width//2, self.screen_height//2))
            self.screen.blit(text, rect)
        else:
            # jeu
            self.all_sprites.draw(self.screen)
            
        pygame.display.flip()