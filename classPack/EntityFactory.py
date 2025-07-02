from classPack.Background import Background
from classPack.Entity import Entity
from classPack.Asteroid import Asteroid
from classPack.Player import Player
from classPack.Const import *


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0)):
        match entity_name:
            case 'Player1':
                return Player("Player1", position)
            case 'Player2':
                return Player("Player2", position)
            case 'Asteroid':
                return Asteroid("Asteroid", position)
            case 'Background':
                listBgs = []
                for i in range(3):
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            x = dx * WIN_WIDTH
                            y = dy * WIN_HEIGHT
                            listBgs.append(Background(f"bkgd_{i}", (x, y)))
                return listBgs