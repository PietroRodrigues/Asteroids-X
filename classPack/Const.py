

from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d, K_SPACE, K_RETURN, USEREVENT

# W
WIN_WIDTH = 720
WIN_HEIGHT = 720

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
    "Player1": 3,
    "Player2": 3,
    "bulletPlayer1": 8,
    "bulletPlayer2": 8,
    "AsteroidLarge": 1,
    "AsteroidMedium": 2,
    "AsteroidSmall": 3,
}
ENTITY_HEALTH = {
    "Player1": 100,
    "Player2": 100,
    "AsteroidLarge": 10,
    "AsteroidMedium": 10,
    "AsteroidSmall": 10,
}

TIMEOUT_LEVEL = 10000  # 100000 #100 seconds
EVENT_TIMEOUT = USEREVENT + 2
TIMEOUT_STAP = 100
EVENT_ASTEROIDS = USEREVENT + 1
ASTEROIDS_SPAWN_RATE = 2000  # milliseconds

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
    "bulletPlayer1": 10,
    "bulletPlayer2": 10,
    "AsteroidLarge": 100,
    "AsteroidMedium": 100,
    "AsteroidSmall": 100,
}


ENTITY_SCORE = {
    "AsteroidLarge": 100,
    "AsteroidMedium": 100,
    "AsteroidSmall": 100,
}

VOLUME = {
    "music": 0.07,
    "sound": 0.1
}

SCORE_POS = {
    "title": (WIN_WIDTH / 2, 100),
    "score": (WIN_WIDTH / 2, 120),
    "label": (WIN_WIDTH / 2, 200),
    "name": (WIN_WIDTH / 2, 220),
    0: (WIN_WIDTH / 2, 230),
    1: (WIN_WIDTH / 2, 260),
    2: (WIN_WIDTH / 2, 290),
    3: (WIN_WIDTH / 2, 320),
    4: (WIN_WIDTH / 2, 350),
    5: (WIN_WIDTH / 2, 380),
    6: (WIN_WIDTH / 2, 410),
    7: (WIN_WIDTH / 2, 440),
    8: (WIN_WIDTH / 2, 470),
    9: (WIN_WIDTH / 2, 500),
    
    
}
