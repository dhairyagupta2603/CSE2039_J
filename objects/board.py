import pygame
from .constants import DARKER_GREEN, GREEN, GREY, HEIGHT, ROWS, COLS, SQUARE_SIZE, WIDTH
from .enemies import Enemy
from .player import Player

class Board:
    def __init__(self) -> None:
        self.board_values = [([0]*COLS) for _ in range(ROWS)]
        self.outer_values = [0 for _ in range(2*(HEIGHT - 2) + 2(WIDTH - 4))]
        self.num_enemies = 1

    def draw_squares(self, win) -> None:
        win.fill(GREEN)
        for row in range(ROWS):
            for col in range(COLS):
                if (row % 2 == 0 and col % 2 == 0) or (row % 2 != 0 and col % 2 != 0):
                    pygame.draw.rect(
                        win, DARKER_GREEN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                if (row == 0 or row == ROWS - 1) or (col == 0 or col == COLS - 1):
                    pygame.draw.rect(
                        win, GREY, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def _add_enemy(self) -> None:
        self.num_enemies += 1
        # TODO: a function to get position of new enemy

    def create_board(self) -> None:
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                pass
