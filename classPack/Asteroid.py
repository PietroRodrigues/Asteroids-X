from classPack.Entity import Entity
from classPack.Const import *
import os
import random
import pygame

class Asteroid(Entity):
    def __init__(self, name: str, sizeAsteroid : str, position: tuple, direction: pygame.Vector2):
        size = (1,1)
        files_in_dir = len(os.listdir(os.path.join("Assets",'asteroids', sizeAsteroid.lower())))
        if sizeAsteroid == 'Large': size = (180,140)
        elif sizeAsteroid == 'Medium': size = (80,80)
        elif sizeAsteroid == 'Small': size = (52,52)
        super().__init__(f'{name}{sizeAsteroid.capitalize()} ({random.randint(1, files_in_dir)})', f'asteroids/{sizeAsteroid.lower()}', position, size)
        self.name = f'{name}{sizeAsteroid.capitalize()}'
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_damage = ''
        self.score = ENTITY_SCORE[self.name]
        self.direction = direction if direction else pygame.Vector2(0, 1)
        self.speed: float = ENTITY_SPEED[self.name]

    def move(self):
        self.pos_x += self.direction.x * self.speed
        self.pos_y += self.direction.y * self.speed

        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)


