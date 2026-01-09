import pygame
from entities.entity import Entity

class Projectile(Entity):
    def __init__(self, x, y):
        # taille 10x20
        super().__init__(x, y, 10, 20)
        
        # jaune
        self.image.fill((255, 255, 0))
        self.speed = 10

    def update(self):
        # monte
        self.rect.y -= self.speed
        
        # suppression hors ecran
        if self.rect.bottom < 0:
            self.kill()