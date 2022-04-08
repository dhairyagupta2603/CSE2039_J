import pygame

# firebase user details
gamescore = 10
username = ''
# display window
HEIGHT, WIDTH = 682, 682
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
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
VIOLET = (127, 0, 255)

# display text
pygame.font.init()
FONT = pygame.font.Font('freesansbold.ttf', 20)
SCORE_COORD = (20, 10)

# piece objects
PLAYER = {
    'name': 'Player',
    'seek': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
}

ENEMY_4_DIR = {
    'name': 'Weak Enemy',
    'seek': [(-1, 0), (0, -1), (0, 1), (1, 0)]
}

ENEMY_8_DIR = {
    'name': 'Strong Enemy',
    'seek': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
}

ENEMY_DIAG = {
    'name': 'Diagonal Enemy',
    'seek': [(-1, -1), (-1, 1), (1, -1), (1, 1)]
}

# movement
PLAYER_SQUARE_VALUE = max(ROWS, COLS)

# board sections
RHIGH, CHIGH = (ROWS - 2)//3, (COLS - 2)//3

WALL_SQUARES = [
    (2, 3), (2, 5), (2, 6), (2, 10), (2, 11), (2, 13),
    (3, 2), (3, 14),
    (4, 4), (4, 12),
    (5, 2), (5, 14),
    (6, 2), (6, 14),
    (7, 8),
    (8, 7), (8, 9),
    (9, 8),
    (10, 2), (10, 14),
    (11, 2), (11, 14),
    (12, 4), (12, 12),
    (13, 2), (13, 14),
    (14, 3), (14, 5), (14, 6), (14, 10), (14, 11), (14, 13)
]
