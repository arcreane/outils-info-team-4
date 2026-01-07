import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__() # Initialise la classe Sprite de Pygame
        
        # 1. Visuel (Placeholder)
        # un rectangle temporaire (remplacé par un sprite plus tard)
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255)) 
        
        # 2. Position physique (Hitbox)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # 3. Stats communes (Vie, Vitesse)
        self.health = 100
        self.speed = 5

    def update(self):
        # Cette méthode sera remplie dans les enfants (Player/Enemy)
        pass