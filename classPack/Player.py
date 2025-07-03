from classPack.Entity import Entity
from classPack.Const import *
from classPack.Bullet import Bullet
import pygame
import math

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name,'player',position, (60, 60))
        self.health = ENTITY_HEALTH[self.name]
        self.shoot_delay = 1
        self.score = 0
        self.angle = 0                 
        self.speed = 0.0             
        self.max_speed = ENTITY_SPEED[self.name]
        self.acceleration = 0.1
        self.rotation_speed = ENTITY_SPEED[self.name]
        self.direction = pygame.Vector2(0, -1)  

    def move(self):
        press_keys = pygame.key.get_pressed()

        if press_keys[PLAYER_KEY_LEFT[self.name]]:
            self.angle -= self.rotation_speed
        if press_keys[PLAYER_KEY_RIGHT[self.name]]:
            self.angle += self.rotation_speed

        if press_keys[PLAYER_KEY_UP[self.name]]:
            self.speed += self.acceleration
            if self.speed > self.max_speed:
                self.speed = self.max_speed

        elif press_keys[PLAYER_KEY_DOWN[self.name]]:
            self.speed -= self.acceleration
            if self.speed < -self.max_speed:
                self.speed = -self.max_speed
        else:
            if self.speed > 0:
                self.speed -= self.acceleration / 4
                if self.speed < 0:
                    self.speed = 0
            elif self.speed < 0:
                self.speed += self.acceleration / 4
                if self.speed > 0:
                    self.speed = 0

        red = math.radians(self.angle)
        self.direction = pygame.Vector2(math.sin(red), -math.cos(red))
        

        self.pos_x += self.direction.x * self.speed
        self.pos_y += self.direction.y * self.speed

        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)

    def draw(self, window : pygame.Surface):
        rotated_image = pygame.transform.rotate(self.surf, -self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        window.blit(rotated_image, rotated_rect)

    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay <= 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            press = pygame.key.get_pressed()
            if press[PLAYER_KEY_SHOOT[self.name]]:
                # Calcular direção com base no ângulo atual da nave
                rad = math.radians(self.angle)
                # eixo Y invertido no pygame
                direction = pygame.Vector2(math.sin(rad), -math.cos(rad))
                return Bullet(f"bullet{self.name}", self.rect.center, direction,self.angle)
