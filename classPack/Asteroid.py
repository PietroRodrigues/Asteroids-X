from classPack.Entity import Entity
from classPack.Const import *

class Asteroid(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, 'asteroid', position)
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_damage = ''
        self.score = ENTITY_SCORE[self.name]



    def move(self , speed:tuple):
        pass

