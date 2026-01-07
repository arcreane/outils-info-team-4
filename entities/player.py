from entities.entity import Entity

class Player(Entity):
    def __init__(self, name, x, y):
        # On appelle d'abord le constructeur du parent (Entity)
        super().__init__(x, y, 50, 50)
        
        # Couleur bleu (placeholder pour le sprite futur)
        self.image.fill((0, 0, 255))
        
        # Stats spécifiques
        self.name = name  
        self.score = 0
        self.max_health = 100
        self.current_health = 100