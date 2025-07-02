

from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d, K_SPACE, K_RETURN, USEREVENT

# W
WIN_WIDTH = 800
WIN_HEIGHT = 800

# C
C_WHITE = (255, 255, 255)
C_RED_NEON = (255, 46, 99)
C_CYAN_NEON = (102, 252, 241)
C_PURPLE_ELECTRIC = (157, 0, 255)

# M
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "NEW GAME 2P - COMPETITIVE",
               "SCORE",
               "EXIT")


ENTITY_SPEED = {
    "bkgd_0": 0.3,
    "bkgd_1": 0.4,
    "bkgd_2": 0.6,
    "Player1": 5,
    "Player2": 5,
    "Bullet": 10,
    "Asteroid": 2,
}
ENTITY_HEALTH = {
    "Player1": 100,
    "Player2": 100,
    "Asteroid": 10,
}

# TIMEOUT_LEVEL = 10000  # 100000 #100 seconds
# EVENT_TIMEOUT = USEREVENT + 2
# TIMEOUT_STAP = 100
# EVENT_ENEMY = USEREVENT + 1
# ENEMY_SPAWN_RATE = 2000  # milliseconds

PLAYER_KEY_UP = {
    "Player1": K_w,
    "Player2": K_UP
}
PLAYER_KEY_DOWN = {
    "Player1": K_s,
    "Player2": K_DOWN
}
PLAYER_KEY_LEFT = {
    "Player1": K_a,
    "Player2": K_LEFT
}
PLAYER_KEY_RIGHT = {
    "Player1": K_d,
    "Player2": K_RIGHT
}

PLAYER_KEY_SHOOT = {
    "Player1": K_SPACE,
    "Player2": K_RETURN
}

ENTITY_SHOOT_DELAY = {
    "Player1": 20,
    "Player2": 20,
}

ENTITY_DAMAGE = {
    "Bullet": 10,
    "Asteroid": 100,
}

ENTITY_SCORE = {
    "Asteroid": 100
}

VOLUME = {
    "music": 0.07,
    "sound": 0.1
}

# SCORE_POS = {
#     "title": (WIN_WIDTH / 2, 50),
#     "score": (WIN_WIDTH / 2, 90),
#     "label": (WIN_WIDTH / 2, 110),
#     "name": (WIN_WIDTH / 2, 130),
#     0: (WIN_WIDTH / 2, 130),
#     1: (WIN_WIDTH / 2, 150),
#     2: (WIN_WIDTH / 2, 170),
#     3: (WIN_WIDTH / 2, 190),
#     4: (WIN_WIDTH / 2, 210),
#     5: (WIN_WIDTH / 2, 230),
#     6: (WIN_WIDTH / 2, 250),
#     7: (WIN_WIDTH / 2, 270),
#     8: (WIN_WIDTH / 2, 290),
#     9: (WIN_WIDTH / 2, 310),
# }
