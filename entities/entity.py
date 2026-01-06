import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path=None):
        super().__init__()
        if image_path:
            self.image = pygame.image.load(image_path)
        else:
            self.image = pygame.Surface((32, 32))
            self.image.fill((255, 0, 0))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 0

    def update(self):
        pass