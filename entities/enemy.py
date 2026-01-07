import pygame
import random
from entities.entity import Entity

class Enemy(Entity):
    def __init__(self):
        # position aleatoire
        x = random.randint(0, 750)
        y = random.randint(-150, -50)
        super().__init__(x, y, 40, 40)
        
        # rouge
        self.image.fill((255, 0, 0))
        # vitesse
        self.speed = 3

    def update(self):
        # descend
        self.rect.y += self.speed
        
        # remonte si bas atteint
        if self.rect.top > 600:
            self.rect.y = random.randint(-150, -50)
            self.rect.x = random.randint(0, 750)