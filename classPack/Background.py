from classPack.Entity import Entity
from classPack.Const import *

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name,'bgSpace', position, (WIN_WIDTH, WIN_HEIGHT))

    def move(self, speed:tuple):
        fator : float = ENTITY_SPEED.get(self.name, 0)
        
        if fator == 0:
            return

        self.pos_x -= speed[0] * fator
        self.pos_y -= speed[1] * fator
        
        if self.pos_x + WIN_WIDTH < 0:
            self.pos_x += WIN_WIDTH * 3
        elif self.pos_x > WIN_WIDTH * 2:
            self.pos_x -= WIN_WIDTH * 3
        
        if self.pos_y + WIN_HEIGHT < 0:
            self.pos_y += WIN_HEIGHT * 3
        elif self.pos_y > WIN_HEIGHT * 2:
            self.pos_y -= WIN_HEIGHT * 3

        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)
        
        # self.rect.centery += ENTITY_SPEED[self.name]
        # if self.rect.top >= WIN_HEIGHT:
        #     self.rect.bottom = 0
