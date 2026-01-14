import pygame
from entities.player import Player
from entities.enemy import Enemy

class Game:
    def __init__(self, player_name):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Shoot Them Up")
        
        self.running = True
        self.is_playing = False # On commence sur l'écran d'accueil
        
        self.player = Player(400, 500, player_name)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        
        self.all_enemies = pygame.sprite.Group()
        self.spawn_enemies() 

        self.font = pygame.font.SysFont("Arial", 40, bold=True)

    def spawn_enemies(self):
        for _ in range(5): 
            enemy = Enemy()
            self.all_enemies.add(enemy)
            self.all_sprites.add(enemy)

    def reset_game(self):
        for enemy in self.all_enemies:
            enemy.kill()
        self.spawn_enemies()
        self.player.rect.x = 400
        self.is_playing = True

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                # Si on joue : ESPACE pour tirer
                if self.is_playing:
                    if event.key == pygame.K_SPACE:
                        self.player.launch_projectile()
                
                # Si on ne joue pas : ENTREE pour lancer
                else:
                    if event.key == pygame.K_RETURN:
                        self.reset_game()

    def update(self):
        self.screen.fill((0, 0, 0)) # Fond noir

        if self.is_playing:
            # --- JEU EN COURS ---
            self.player.update()
            self.all_enemies.update()
            
            # Collisions
            pygame.sprite.groupcollide(self.player.all_projectiles, self.all_enemies, True, True)
            
            # Vérification Victoire
            if len(self.all_enemies) == 0:
                self.is_playing = False

            self.all_sprites.draw(self.screen)
            self.player.all_projectiles.draw(self.screen)
            self.player.all_projectiles.update()

        else:
            # --- ECRAN ACCUEIL / FIN ---
            if len(self.all_enemies) > 0:
                msg = f"Bienvenue {self.player.name} ! Entrée pour jouer"
            else:
                msg = "GG LE SANG ! Entrée pour rejouer"

            text_surf = self.font.render(msg, True, (255, 255, 255))
            self.screen.blit(text_surf, text_surf.get_rect(center=(400, 300)))

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.handle_input()
            self.update()
            clock.tick(60)
        
        pygame.quit()