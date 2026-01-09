import pygame
class Projectile:
    def __init__(self, x, y, speed=8):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = 5
        self.color = (255, 0, 0)
        self.active = True

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.active = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def get_rect(self):
        return pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )


class Cube:
    def __init__(self, x, y, width=40, height=40, color=(0, 0, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot Them Up - Test")
clock = pygame.time.Clock()


player_x = WIDTH // 2
player_y = HEIGHT - 50
player_width = 40
player_height = 20
player_color = (0, 255, 0)

projectiles = []
enemies = [
    Cube(300, 200),
    Cube(500, 150),
    Cube(400, 300)
]


running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0)) 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Tirer un projectile depuis le centre du joueur
                projectiles.append(Projectile(player_x + player_width//2, player_y))


    for projectile in projectiles[:]:
        projectile.update()


        for enemy in enemies:
            if projectile.get_rect().colliderect(enemy.rect):
                projectile.active = False


        if not projectile.active:
            projectiles.remove(projectile)


    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))


    for projectile in projectiles:
        projectile.draw(screen)


    for enemy in enemies:
        enemy.draw(screen)

class Enemy:
    def __init__(self, x, y):
        # Charger l'image du sprite ennemi
        self.image = pygame.image.load('smilie_cookie.png').convert_alpha()

        # Redimensionner le sprite (ajustez la taille selon vos besoins)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    pygame.display.flip()

pygame.quit()

