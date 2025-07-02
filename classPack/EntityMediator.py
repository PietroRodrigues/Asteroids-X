from classPack.Const import *
from classPack.Asteroid import Asteroid
from classPack.Bullet import Bullet
from classPack.Entity import Entity
from classPack.Player import Player

class EntityMediator:
    
    @staticmethod
    def __verity_collision_window(ent: Entity):
        if isinstance(ent, Asteroid):
            if ent.rect.right < 0:
                return True
        if isinstance(ent, Bullet):
            if ent.rect.left >= WIN_WIDTH:
                return True
        
        
        return False
    
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
            if (ent.rect.right >= ent2.rect.left and
                ent.rect.left <= ent2.rect.right and
                ent.rect.top <= ent2.rect.bottom and
                    ent.rect.bottom >= ent2.rect.top):

                if isinstance(ent, (Player, Asteroid)):
                    if (isinstance(ent2, (Bullet, Asteroid))):
                        ent.health -= ent2.damage
                        entity_list.remove(ent2)
                        if isinstance(ent, Asteroid):
                            ent.last_damage = ent2.name

    @staticmethod
    def __give_score(asteroid: Asteroid, entity_list: list[Entity]):
        for i in range(1,3):
            if asteroid.last_damage == f'Bullet{i}':
                for ent in entity_list:
                    if ent.name == f'Player{i}':
                        if isinstance(ent, Player):
                            ent.score += asteroid.score


    @staticmethod
    def verify_colision(entity_list: list[Entity]):
        for ent in entity_list:
            if EntityMediator.__verity_collision_window(ent):
                entity_list.remove(ent)
            for ent2 in entity_list:
                if ent == ent2:
                    continue
                EntityMediator.__verity_collision_entity(ent, ent2, entity_list)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
             if isinstance(ent, (Player, Asteroid)):
                  if ent.health <= 0:
                        if isinstance(ent, Asteroid):
                            EntityMediator.__give_score(ent, entity_list)
                        entity_list.remove(ent)
