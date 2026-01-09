import pygame
import sys
from entities.player import Player
from entities.enemy import Enemy
from entities.projectile import Projectile

class Game:
    def __init__(self, player_name):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Shoot Them Up")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.in_menu = True
        self.font = pygame.font.Font(None, 50)

        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        
        self.player = Player(self.screen_width // 2, self.screen_height - 100, player_name)
        self.all_sprites.add(self.player)

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
            
            if self.in_menu:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.in_menu = False
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.shoot()

    def shoot(self):
        p = Projectile(self.player.rect.centerx, self.player.rect.top)
        self.all_sprites.add(p)
        self.projectiles.add(p)

    def update(self):
        if self.in_menu:
            return
            
        self.all_sprites.update()
        pygame.sprite.groupcollide(self.projectiles, self.enemies, True, True)

    def draw(self):
        self.screen.fill((0, 0, 0))

        if self.in_menu:
            text = self.font.render("PRESS ENTER TO START", True, (255, 255, 255))
            rect = text.get_rect(center=(self.screen_width//2, self.screen_height//2))
            self.screen.blit(text, rect)
        else:
            self.all_sprites.draw(self.screen)
            
        pygame.display.flip()