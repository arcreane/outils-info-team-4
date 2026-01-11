from entity import Entity


class Player(Entity):
    def __init__(self, health, x, y, name):
        super().__init__(health, x, y)
        self.name = name

    def attack(self, enemy):
        if enemy.is_alive():
            enemy.health -= 10
