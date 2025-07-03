from classPack.Const import *
from classPack.Asteroid import Asteroid
from classPack.Bullet import Bullet
from classPack.Entity import Entity
from classPack.Player import Player

class EntityMediator:
    
    @staticmethod
    def __verity_collision_window(ent: Entity):
        if isinstance(ent, Bullet):
            if (ent.rect.right < 0 or ent.rect.left > WIN_WIDTH or
                ent.rect.bottom < 0 or ent.rect.top > WIN_HEIGHT):
                return True
               
        return False
    
    @staticmethod
    def wrep_position(ent: Entity):
        if isinstance(ent, (Player, Asteroid)):
            if ent.rect.right < 0:
                ent.pos_x = WIN_WIDTH
            elif ent.rect.left > WIN_WIDTH:
                ent.pos_x = -ent.rect.width

            if ent.rect.bottom < 0:
                ent.pos_y = WIN_HEIGHT
            elif ent.rect.top > WIN_HEIGHT:
                ent.pos_y = -ent.rect.height

            ent.rect.x = int(ent.pos_x)
            ent.rect.y = int(ent.pos_y)
    
    @staticmethod
    def __verity_collision_entity(ent: Entity, ent2: Entity, entity_list: list[Entity]):
        valid_interaction = False
        if isinstance(ent, Asteroid) and isinstance(ent2, Bullet):
            valid_interaction = True
        elif isinstance(ent, Bullet) and isinstance(ent2, Asteroid):
            valid_interaction = True
        elif isinstance(ent, Player) and isinstance(ent2, Asteroid):
            valid_interaction = True
        elif isinstance(ent, Asteroid) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if ent.rect.colliderect(ent2.rect):
                offcet = (ent2.rect.x - ent.rect.x, ent2.rect.y - ent.rect.y)
                if ent.mask.overlap(ent2.mask, offcet):
                    if isinstance(ent, (Player, Asteroid)):
                        if (isinstance(ent2, (Bullet, Asteroid))):
                            ent.health -= ent2.damage
                            entity_list.remove(ent2)
                            if isinstance(ent, Asteroid):
                                ent.last_damage = ent2.name

    @staticmethod
    def __give_score(asteroid: Asteroid, entity_list: list[Entity]):
        for i in range(1,3):
            if asteroid.last_damage == f'bulletPlayer{i}':
                for ent in entity_list:
                    if ent.name == f'Player{i}':
                        if isinstance(ent, Player):
                            ent.score += asteroid.score


    @staticmethod
    def verify_colision(entity_list: list[Entity]):
        for ent in entity_list:
            
            EntityMediator.wrep_position(ent)
            
            if EntityMediator.__verity_collision_window(ent):
                entity_list.remove(ent)
            for ent2 in entity_list:
                if ent == ent2:
                    continue
                EntityMediator.__verity_collision_entity(ent, ent2, entity_list)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        to_remove = []
        for ent in entity_list:
            if isinstance(ent, (Player, Asteroid)):
                if ent.health <= 0:
                    if isinstance(ent, Asteroid):
                        EntityMediator.__give_score(ent, entity_list)
                    to_remove.append(ent)

        for ent in to_remove:
            entity_list.remove(ent)
