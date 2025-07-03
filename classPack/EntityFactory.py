from classPack.Background import Background
from classPack.Asteroid import Asteroid
from classPack.Player import Player
from classPack.Const import *
import random
import pygame

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0), level_name: str = '', sizeAsteroid: str = '', dir45: int = 0, direction: pygame.Vector2 | None = None):
        match entity_name:
            case 'Player1':
                return Player("Player1", (WIN_HEIGHT/2, WIN_WIDTH/2))
            case 'Player2':
                return Player("Player2", (WIN_HEIGHT/2 + 60, WIN_WIDTH/2))
            case 'Asteroid':
                if direction is None:
                    pos = random_spawner_poss()
                    direction = pygame.Vector2(WIN_WIDTH/2 - pos[0], WIN_HEIGHT/2 - pos[1]).normalize()
                else:
                    pos = position

                if dir45 in [45, -45]:
                    direction = direction.rotate(dir45).normalize()

                return Asteroid("Asteroid", sizeAsteroid, pos, direction)
            case 'Background':
                listBgs = []
                for i in range(3):
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            x = dx * WIN_WIDTH
                            y = dy * WIN_HEIGHT
                            if level_name == "Level2" and i == 0:
                                listBgs.append(Background(f"level2bkgd_{i}", (x, y)))
                            else:
                                listBgs.append(Background(f"bkgd_{i}", (x, y)))

                return listBgs
    
   
def random_spawner_poss():
    x, y = random.choice([
        (-50, random.randint(0, WIN_HEIGHT)),                
        (WIN_WIDTH + 50, random.randint(0, WIN_HEIGHT)),    
        (random.randint(0, WIN_WIDTH), -50),                
        (random.randint(0, WIN_WIDTH), WIN_HEIGHT + 50)  
    ])
    return (x, y)