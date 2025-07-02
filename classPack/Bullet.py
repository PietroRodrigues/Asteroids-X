from classPack.Entity import Entity
from classPack.Const import *

class Bullet(Entity):
    def __init__(self, name: str, EmisorName: str, position: tuple):
        super().__init__(name, 'Player', position)
        self.damage = ENTITY_DAMAGE[self.name]
        self.EmisorName = EmisorName

    def move(self , speed:tuple):
        pass