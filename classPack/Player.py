from classPack.Entity import Entity
from classPack.Const import *
from classPack.Bullet import Bullet


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name,'player',position)
        self.health = ENTITY_HEALTH[self.name]
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
        self.score = 0

    def move(self):
        pass
