from abc import ABC, abstractmethod
import pygame
from classPack.Const import *
import os 

class Entity(ABC):
    
    def __init__(self, name: str, directorio: str, position: tuple = (0, 0), size: tuple | None = None):
        self.name = name
        self.surf = pygame.image.load(os.path.join("Assets", directorio, f"{name}.png")).convert_alpha()

        if size:
            self.surf = pygame.transform.scale(self.surf, size)

        self.mask = pygame.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(center=position)
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        
    @abstractmethod
    def move(self):
        pass