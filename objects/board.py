import pygame
from random import randint
from .constants import DARKER_GREEN, GREEN, GREY, ROWS, COLS, SQUARE_SIZE, PLAYER_SQUARE_VALUE, BLACK
from pprint import pprint


class Board:
    def __init__(self) -> None:
        self.board_colors = [([GREEN]*COLS) for _ in range(ROWS)]
        self._board_values = [([0]*COLS) for _ in range(ROWS)]
        # self.__outer_values = [0 for _ in range(2*(HEIGHT - 2) + 2(WIDTH - 4))]
        self.__num_enemies = 1

    def draw_squares(self, win) -> None:
        """Draw the visual representaion of board. Also, initializes board square colors as a matrix"""
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
        # pprint(self.board_colors)

    def draw_single_square(self, win, row: int, col: int) -> None:
        """Darws a single square on window at the specified place with a specified color

        Args:
            row (int): row of board
            col (int): column of board
        """
        # why ??? needed
        for rowi in range(ROWS):
            for colj in range(COLS):
                if (rowi % 2 == 0 and colj % 2 == 0) or (rowi % 2 != 0 and colj % 2 != 0):
                    pygame.draw.rect(
                        win, DARKER_GREEN, (rowi*SQUARE_SIZE, colj*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    self.board_colors[rowi][colj] = DARKER_GREEN
                if (rowi == 0 or rowi == ROWS - 1) or (colj == 0 or colj == COLS - 1):
                    pygame.draw.rect(
                        win, GREY, (rowi*SQUARE_SIZE, colj*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    self.board_colors[rowi][colj] = GREY
        # pprint(self.board_colors)
        # pprint(self.board_colors[col][row])
        sq_color = self.board_colors[col][row]
        # why opposite printing of row and column
        pygame.draw.rect(win, sq_color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def add_enemy(self) -> None:
        self.__num_enemies += 1
        # TODO: a function to get position of new enemy

    def __square_vs_player_pos(self, px: int, py: int, row: int, col: int) -> int:
        """Handler function for get_board_matrix(). checks the row and column value against the given player position

        Args:
            px and py (int): player row and column
            row and col (int): square to be checked

        Returns:
            int: square value wrt player
        """
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

    def get_board_matrix(self, player_pos: tuple) -> None:
        """Sets the value of squares on board wrt the current position of player in a matrix

        Args:
            player_pos (tuple): position of player
        """
        px, py = player_pos
        self._board_values[px][py] = PLAYER_SQUARE_VALUE
        for row in range(ROWS):
            for col in range(COLS):
                if randint(0, 100) < 5:
                    square_val = 0
                else:
                    square_val = self.__square_vs_player_pos(px, py, row, col)
                self._board_values[row][col] = square_val
        pprint(self._board_values)

    def get_square_value(self, row: int, col: int) -> int:
        """Returns the value of specified square"""
        return self._board_values[row][col]
