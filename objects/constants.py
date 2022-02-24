import pygame


# display window
HEIGHT, WIDTH = 402, 402
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
FPS = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# rgb
GREY = (127, 127, 127)
GREY_NAME = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GREEN_NAME = 1
DARKER_GREEN = (0, 225, 0)
BLUE = (0, 0, 255)

# piece objects
PLAYER = {'name': 'Player', 'seek': [-1, 0, 1]}
ENEMY_4_DIR = {'name': 'Weak Enemy', 'seek': [-1, 1]}
ENEMY_8_DIR = {'name': 'Strong Enemy', 'seek': [-1, 0, 1]}

# movement
PLAYER_SQUARE_VALUE = max(ROWS, COLS)
