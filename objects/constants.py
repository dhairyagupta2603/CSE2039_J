import pygame


# display window
HEIGHT, WIDTH = 682, 682
ROWS, COLS = 17, 17
SQUARE_SIZE = WIDTH // COLS

# rgb
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
DARKER_GREEN = (0, 225, 0)
BLUE = (0, 0, 255)

# piece objects
PLAYER = {'name': 'Player',
          'seek': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
          }

ENEMY_4_DIR = {'name': 'Weak Enemy', 
               'seek': [(-1, 0), (0, -1), (0, 1), (1, 0)]
               }

ENEMY_8_DIR = {'name': 'Strong Enemy', 
               'seek': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
               }

MAX_NUM_ENEMIES = 3

# movement
PLAYER_SQUARE_VALUE = max(ROWS, COLS)

# board sections
RHIGH, CHIGH = (ROWS - 2)//3, (COLS - 2)//3
RANGE = {
    1 : ((0, RHIGH), (0, CHIGH)),
    2 : ((0, RHIGH), (CHIGH, 2*CHIGH)),
    3 : ((0, RHIGH), (2*CHIGH, 3*CHIGH)),
    4 : ((RHIGH, 2*RHIGH), (0, CHIGH)),
    5 : ((RHIGH, 2*RHIGH), (CHIGH, 2*CHIGH)),
    6 : ((RHIGH, 2*RHIGH), (2*CHIGH, 3*CHIGH)),
    7 : ((2*RHIGH, 3*RHIGH), (0, CHIGH)),
    8 : ((2*RHIGH, 3*RHIGH), (CHIGH, 2*CHIGH)),
    9 : ((2*RHIGH, 3*RHIGH), (2*CHIGH, 3*CHIGH))
}
