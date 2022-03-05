import pygame


# display window
HEIGHT, WIDTH = 702, 702
ROWS, COLS = 14, 14
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
