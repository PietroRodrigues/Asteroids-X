
import pygame
from classPack.Const import *
from classPack.Entity import Entity
from classPack.EntityFactory import EntityFactory
import sys
import os
from datetime import datetime
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.font import Font
from classPack.DBProxy import DBProxy

class Score:
    def __init__(self, window: pygame.Surface):
       self.window = window
       self.entity_list: list[Entity] = []
       listBgs = EntityFactory.get_entity('Background')

       if isinstance(listBgs, list):
           self.entity_list.extend(listBgs)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load(os.path.join("Assets", "sondes", "Menu.mp3"))
        pygame.mixer_music.set_volume(VOLUME['music'])
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy("./DBScore.db")
        name = ''

        while True:
            for bgEntity in self.entity_list:
                bgEntity.move()
                self.window.blit(bgEntity.surf, bgEntity.rect)
            
            self.score_text(text_size=120, text="YOU WIN!!",text_color= C_CYAN_NEON, text_center_pos=SCORE_POS["title"])
            if game_mode == MENU_OPTION[0]:
                text = 'Enter your name (3 characters):'
                score = player_score[0]
            elif game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter team name (3 characters):'
            elif game_mode == MENU_OPTION[2]:
                score = max(player_score)
                if player_score[0] > player_score[1]:
                    text = 'Player 1 enter your name (3 characters):'
                elif player_score[1] > player_score[0]:
                    text = 'Player 2 enter your name(3 characters):'
                else:
                    text = 'Draw'

            if text != 'Draw':
                self.score_text(text_size=62, text=f'Score: {str(score)}', text_color=C_RED_NEON, text_center_pos=SCORE_POS["score"])
            
            self.score_text(text_size=42, text=text, text_color=C_PURPLE_ELECTRIC, text_center_pos=SCORE_POS["label"])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) >= 1:
                        if (score > 0 and text != 'Draw'):
                            db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                            self.show()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 3 and event.unicode.isalpha():
                            name += event.unicode

            self.score_text(text_size=120, text=name, text_color=C_CYAN_NEON, text_center_pos=SCORE_POS["name"])
            
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load(os.path.join("Assets", "sondes", "Menu.mp3"))
        pygame.mixer_music.set_volume(VOLUME['music'])
        pygame.mixer_music.play(-1)

        db_proxy = DBProxy("./DBScore.db")
        list_scores = db_proxy.relative_top10()
        db_proxy.close()

        while True:
            for bgEntity in self.entity_list:
                bgEntity.move()
                self.window.blit(bgEntity.surf, bgEntity.rect)

            # Títulos fixos
            self.score_text(text_size=80, text="TOP 10 SCORE",
                            text_color=C_RED_NEON, text_center_pos=SCORE_POS["title"])
            self.score_text(text_size=50, text="        Name         SCORE          DATE            ",
                            text_color=C_PURPLE_ELECTRIC, text_center_pos=SCORE_POS["label"])

            # Desenha os scores corretamente
            for index, player_score in enumerate(list_scores):
                id, name, score, date = player_score
                text = f"    {index + 1:02d}°- {name.ljust(3, '_')}               {int(score):08d}           {date}"
                self.score_text(text_size=32, text=text,
                                text_color=C_CYAN_NEON, text_center_pos=SCORE_POS[index])

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.flip()

    def score_text(self, text: str, text_size: int, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)

def get_formatted_date():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%d/%m/%Y")
    return f"{current_time} - {current_date}"
