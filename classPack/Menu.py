from classPack.Const import *
from classPack.EntityFactory import EntityFactory
import pygame
import sys
from classPack.Entity import Entity
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect
import os

class Menu:
    def __init__(self,window: pygame.Surface):
        self.window = window
        self.entity_list: list[Entity] = []
        listBgs = EntityFactory.get_entity('Background')
       
        if isinstance(listBgs, list):
            self.entity_list.extend(listBgs)
        
    def run(self):
        menu_option = 0
        pygame.mixer_music.load(os.path.join("Assets", "sondes", "Menu.mp3"))
        pygame.mixer_music.set_volume(VOLUME['music'])
        pygame.mixer_music.play(-1)

        while True:            
            for bgEntity in self.entity_list:
                bgEntity.move((1,1))
                self.window.blit(bgEntity.surf, bgEntity.rect)

            self.Menu_text(370, "X", C_RED_NEON, (WIN_WIDTH/2, 250))
            self.Menu_text(150, "ASTEROIDS", C_CYAN_NEON, (WIN_WIDTH/2, 290))
            self.Menu_text(30, "DEMO", C_CYAN_NEON, (WIN_WIDTH/2, 340))
            
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.Menu_text(32, MENU_OPTION[i], C_PURPLE_ELECTRIC, (WIN_WIDTH/2, 500 + i * 50))
                else:
                    self.Menu_text(32, MENU_OPTION[i], C_CYAN_NEON, (WIN_WIDTH/2, 500 + i * 50))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN:
                        return menu_option
            
            pygame.display.flip()
            
    def Menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size,bold=True)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
