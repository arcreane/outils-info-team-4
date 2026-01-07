import pygame
import random
from entities.entity import Entity

class Enemy(Entity):
    def __init__(self):
        # position aleatoire en haut
        x = random.randint(0, 750)
        y = random.randint(-150, -50)
        
        # on init avec la classe mere taille 40x40
        super().__init__(x, y, 40, 40)
        
        # carre rouge pour l'instant
        self.image.fill((255, 0, 0))
        
        # vitesse de descente
        self.speed = 3

    def update(self):
        # ca descend
        self.rect.y += self.speed
        
        # si ca touche le bas on remet en haut
        if self.rect.top > 600:
            self.rect.y = random.randint(-150, -50)
            self.rect.x = random.randint(0, 750)