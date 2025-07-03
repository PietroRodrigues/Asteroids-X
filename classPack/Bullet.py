from classPack.Entity import Entity
from classPack.Const import *
import pygame

class Bullet(Entity):
    def __init__(self, name: str, position: tuple, direction: pygame.Vector2 ,angle: float = 0):
        super().__init__(name, 'Player', position, (20, 20))
        self.damage = ENTITY_DAMAGE[self.name]
        self.direction = direction
        self.speed = ENTITY_SPEED[self.name]
        self.angle = angle

    def move(self):
        self.pos_x += self.direction.x * self.speed
        self.pos_y += self.direction.y * self.speed

        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)

    def draw(self, window: pygame.Surface):
        rotated_image = pygame.transform.rotate(self.surf, -self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        window.blit(rotated_image, rotated_rect)
