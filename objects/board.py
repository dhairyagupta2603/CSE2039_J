import pygame
from .constants import DARKER_GREEN, GREEN, GREY, ROWS, COLS, SQUARE_SIZE


class Board:
    def __init__(self) -> None:
        self.board = []
        self.num_enemies = 1

    def draw_squares(self, win):
        win.fill(GREEN)
        for row in range(ROWS):
            for col in range(COLS):
                if (row % 2 == 0 and col % 2 == 0) or (row % 2 != 0 and col % 2 != 0):
                    pygame.draw.rect(
                        win, DARKER_GREEN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                if (row == 0 or row == ROWS - 1) or (col == 0 or col == COLS - 1):
                    pygame.draw.rect(
                        win, GREY, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        pass
