import pygame
from pygame.font import Font
from pygame.surface import Surface
from classPack.Const import *
from pygame.rect import Rect
from classPack.EntityMediator import EntityMediator
from classPack.EntityFactory import EntityFactory

class Level:
    def __init__(self, window: pygame.Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        # self.name = name
        # self.game_mode = game_mode
        # self.entity_list: list[Entity] = []
        # self.timeout = TIMEOUT_LEVEL  # 20 seconds)
        # listBgs = EntityFactory.get_entity(self.name + 'Bg')
        # player = EntityFactory.get_entity('Player1')
        # pygame.time.set_timer(EVENT_ENEMY, ENEMY_SPAWN_RATE)
        # pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STAP)
        pass

    def run(self, player_score: list[int]):
        pass

    def Level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
        pass