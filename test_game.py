import pygame
import sys
from player import Player
from enemy import Enemy

# ---------- INIT ----------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot'em up - Refactor test")
clock = pygame.time.Clock()

# ---------- GAME OBJECTS ----------
player = Player(100, 375, 500, "Hero")
enemy = Enemy(50, 375, 50, 1)

player_speed = 5
enemy_speed = 3
bullets = []

# ---------- MAIN LOOP ----------
running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.x + 20, player.y, 10, 20))

    # Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.move(-player_speed, 0)
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 50:
        player.move(player_speed, 0)

    # Enemy movement
    enemy.move(enemy_speed, 0)
    if enemy.x <= 0 or enemy.x >= WIDTH - 50:
        enemy_speed *= -1

    # Bullets
    for bullet in bullets[:]:
        bullet.y -= 8
        if bullet.bottom < 0:
            bullets.remove(bullet)

        enemy_rect = pygame.Rect(enemy.x, enemy.y, 50, 50)
        if bullet.colliderect(enemy_rect) and enemy.is_alive():
            bullets.remove(bullet)
            enemy.health -= 10

    # Draw player / enemy / bullets
    pygame.draw.rect(screen, (0, 255, 0), (player.x, player.y, 50, 50))

    if enemy.is_alive():
        pygame.draw.rect(screen, (255, 0, 0), (enemy.x, enemy.y, 50, 50))

    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet)

    pygame.display.flip()

pygame.quit()
sys.exit()
