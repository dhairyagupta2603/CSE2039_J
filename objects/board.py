import pygame
from random import randint
from .constants import DARKER_GREEN, GREEN, GREY, ROWS, COLS, SQUARE_SIZE, PLAYER_SQUARE_VALUE
from pprint import pprint


class Board:
    def __init__(self) -> None:
        self.board_values = [([0]*COLS) for _ in range(ROWS)]
        self.board_colors = [([GREEN]*COLS) for _ in range(ROWS)]
        # self.outer_values = [0 for _ in range(2*(HEIGHT - 2) + 2(WIDTH - 4))]
        self.num_enemies = 1


    def draw_squares(self, win) -> None:
        win.fill(GREEN)
        for row in range(ROWS):
            for col in range(COLS):
                if (row % 2 == 0 and col % 2 == 0) or (row % 2 != 0 and col % 2 != 0):
                    pygame.draw.rect(
                        win, DARKER_GREEN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    self.board_colors[row][col] = DARKER_GREEN
                if (row == 0 or row == ROWS - 1) or (col == 0 or col == COLS - 1):
                    pygame.draw.rect(
                        win, GREY, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    self.board_colors[row][col] = GREY


    def draw_single_square(self, win, row, col)->None:
        pygame.draw.rect(win, DARKER_GREEN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    def _add_enemy(self) -> None:
        self.num_enemies += 1
        # TODO: a function to get position of new enemy


    def _square_vs_player_pos(self, px: int, py: int, row: int, col: int) -> int:
        if (row == 0 or row == ROWS - 1) or (col == 0 or col == COLS - 1):
            return 0
        if row <= px and col <= py:
            return min(PLAYER_SQUARE_VALUE - px + row,
                       PLAYER_SQUARE_VALUE - py + col)
        elif row <= px and col >= py:
            return min(PLAYER_SQUARE_VALUE - px + row,
                       PLAYER_SQUARE_VALUE + py - col)
        elif row >= px and col <= py:
            return min(PLAYER_SQUARE_VALUE + px - row,
                       PLAYER_SQUARE_VALUE - py + col)
        elif row >= px and col >= py:
            return min(PLAYER_SQUARE_VALUE + px - row,
                       PLAYER_SQUARE_VALUE + py - col)


    def get_board_matrix(self, player_pos) -> None:
        px, py = player_pos
        self.board_values[px][py] = PLAYER_SQUARE_VALUE
        for row in range(ROWS):
            for col in range(COLS):
                if randint(0, 100) < 5:
                    square_val = 0
                else:
                    square_val = self._square_vs_player_pos(px, py, row, col)
                self.board_values[row][col] = square_val
        pprint(self.board_values)


    def get_square_value(self, row, col) -> int:
        return self.board_values[row][col]
