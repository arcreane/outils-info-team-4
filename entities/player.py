from entities.entity import Entity

class Player(Entity):
    def __init__(self, x, y, name): 
        super().__init__(x, y, 50, 50)
        
        self.image.fill((0, 0, 255))
        
        self.name = name 
        self.score = 0
        self.max_health = 100
        self.current_health = 100