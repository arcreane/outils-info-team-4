import pygame
from entities.entity import Entity

class Player(Entity):
    def __init__(self, x, y, name):
        super().__init__(x, y, 50, 50)
        # bleu
        self.image.fill((0, 0, 255))
        
        self.name = name
        self.score = 0
        self.max_health = 100
        self.current_health = 100
        # vitesse deplacement
        self.speed = 5

    def update(self):
        # touches clavier
        keys = pygame.key.get_pressed()

        # gauche droite
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # limites ecran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800