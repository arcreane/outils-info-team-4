import pygame
from entities.entity import Entity
from entities.projectile import Projectile

class Player(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, 50, 50)
        self.image.fill((0, 0, 255))
        
        self.name = name
        self.score = 0
        self.max_health = 100
        self.current_health = 100
        self.speed = 5
        
        # Obligatoire pour stocker les tirs
        self.all_projectiles = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800

    def launch_projectile(self):
        # Création simple du projectile
        projectile = Projectile(self.rect.centerx, self.rect.top)
        self.all_projectiles.add(projectile)