import pygame
from .entity import Entity

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill((0, 0, 255)) #couleur du joueur
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed