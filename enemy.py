from entity import Entity


class Enemy(Entity):
    def __init__(self, health, x, y, level):
        super().__init__(health, x, y)
        self.level = level

    def attack(self, player):
        if player.is_alive():
            player.health -= 5 * self.level