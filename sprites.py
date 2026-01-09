class Enemy:
    def __init__(self, x, y):
        # Charger l'image du sprite ennemi
        self.image = pygame.image.load('smilie_cookie.png').convert_alpha()

        # Redimensionner le sprite (ajustez la taille selon vos besoins)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
