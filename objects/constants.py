import pygame


# display window
HEIGHT, WIDTH = 250, 250
ROWS, COLS = 5, 5
SQUARE_SIZE = WIDTH // COLS
FPS = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# rgb
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
DARKER_GREEN = (0, 225, 0)
BLUE = (0, 0, 255)

# piece objects
PLAYER = {'name': 'Player', 'seek': [-1, 0, 1]}
ENEMY_4_DIR = {'name': 'Weak Enemy', 'seek': [-1, 1]}
ENEMY_8_DIR = {'name': 'Strong Enemy', 'seek': [-1, 0, 1]}

# movement
PLAYER_SQUARE_VALUE = max(ROWS, COLS)
