class Entity:
    def __init__(self, health, x, y):
        self.health = health
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def is_alive(self):
        return self.health > 0