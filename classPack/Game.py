import pygame
from classPack.Const import *
from classPack.Menu import Menu
from classPack.Level import Level
from classPack.Score import Score
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    

    def run(self):

        while True:
            # score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
