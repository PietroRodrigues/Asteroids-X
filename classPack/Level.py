import pygame
from pygame.font import Font
from pygame.surface import Surface
from classPack.Const import *
from pygame.rect import Rect
from classPack.Entity import Entity
from classPack.EntityFactory import EntityFactory
from classPack.EntityMediator import EntityMediator
from classPack.Player import Player
from classPack.Background import Background
from classPack.Asteroid import Asteroid 
from classPack.Bullet import Bullet
import sys
import random
import os

class Level:
    def __init__(self, window: pygame.Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = TIMEOUT_LEVEL
        self.asteroidsSpauneds = 0
        self.entity_list: list[Entity] = []
        listBgs = EntityFactory.get_entity('Background', level_name=self.name)
        player1 = EntityFactory.get_entity('Player1', (WIN_WIDTH/2 , WIN_HEIGHT/2))
        pygame.time.set_timer(EVENT_ASTEROIDS,ASTEROIDS_SPAWN_RATE)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STAP)

        if isinstance(listBgs, list):
            self.entity_list.extend(listBgs)

        if isinstance(player1, Player):
            player1.score = player_score[0]
            self.entity_list.append(player1)
        
        if (self.game_mode == MENU_OPTION[1] or self.game_mode == MENU_OPTION[2]):
            player2 = EntityFactory.get_entity('Player2')
            if isinstance(player2, Player):
                player2.score = player_score[1]
                self.entity_list.append(player2)
    

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(os.path.join("Assets", "sondes", f"{self.name}Song{random.randint(1, 2)}.mp3"))
        pygame.mixer_music.set_volume(VOLUME['music'])
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for ent in self.entity_list:
                if isinstance(ent, Player):
                    ent.move()
                    ent.draw(self.window)
                    shot = ent.shoot()
                    if shot:
                        self.entity_list.append(shot)
                    if ent.name == 'Player1':
                        self.Level_text(30, f'Player1 - Health:{ent.health} | Score: {ent.score}', C_RED_NEON, (10, WIN_HEIGHT - 50))
                    if ent.name == 'Player2':
                        self.Level_text(30, f'Player2 - Health:{ent.health} | Score: {ent.score}', C_CYAN_NEON, (10, WIN_HEIGHT - 20))
                elif isinstance(ent, Bullet):
                    ent.move()
                    ent.draw(self.window)
                else:
                    ent.move()
                    self.window.blit(ent.surf, ent.rect)            


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == EVENT_ASTEROIDS:
                    self.asteroidsSpauneds += 1
                    if self.asteroidsSpauneds <= ASTEROIDS_LIMIT[self.name]:                                        
                        asteroid = EntityFactory.get_entity('Asteroid',sizeAsteroid='Large')
                        if isinstance(asteroid, Asteroid):
                            self.entity_list.append(asteroid)
                
                for ent in self.entity_list:
                    if isinstance(ent, (Player)) and ent.name == 'Player1':
                            player_score[0] = ent.score
                    if isinstance(ent, (Player)) and ent.name == 'Player2':
                            player_score[1] = ent.score

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STAP
                    if(self.timeout <= 0):
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            self.Level_text(18, f'{self.name} - Timeout : {self.timeout / 1000:.1f}s', C_WHITE, (10, 10))
            self.Level_text(18, f'FPS: {clock.get_fps():.0f}', C_WHITE, (WIN_WIDTH/2, 10))
            self.Level_text(18, f'Entidades: {len(self.entity_list)}', C_WHITE, (WIN_WIDTH - 120, 10))

            pygame.display.flip()

            EntityMediator.verify_colision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)
            
        

    def Level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
        pass