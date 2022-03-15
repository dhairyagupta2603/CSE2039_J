import pygame
from random import randint
from .constants import BLACK, GREEN, GREY, ROWS, COLS, SQUARE_SIZE, PLAYER_SQUARE_VALUE, WALL_SQUARES
from pprint import pprint


class Board:
    __OUTLINE = 2
    def __init__(self) -> None:
        self.board_colors = [([GREEN]*COLS) for _ in range(ROWS)]
        self.board_matrix = [([0]*COLS) for _ in range(ROWS)]
        self.__num_enemies = 1

    def draw_squares(self, win) -> None:
        """Draw the visual representaion of board. Also, initializes board square colors as a matrix"""
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                if (row == 0 or row == ROWS - 1) or (col == 0 or col == COLS - 1) or (col, row) in WALL_SQUARES:
                    pygame.draw.rect(win, GREY, (row*SQUARE_SIZE + self.__OUTLINE, col*SQUARE_SIZE + self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE))
                    self.board_colors[row][col] = GREY
                else:
                    pygame.draw.rect(win, GREEN, (row*SQUARE_SIZE + self.__OUTLINE, col*SQUARE_SIZE + self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE))
        # pprint(self.board_colors)

    def draw_single_square(self, win, row: int, col: int) -> None:
        """Darws a single square on window at the specified place

        Args:
            row (int): row of board
            col (int): column of board
        """
        pygame.draw.rect(win, GREEN, (col*SQUARE_SIZE + self.__OUTLINE, row*SQUARE_SIZE + self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE))

    def __square_vs_player_pos(self, px: int, py: int, row: int, col: int) -> int:
        """Handler function for get_board_matrix(). checks the row and column value against the given player position

        Args:
            px and py (int): player row and column
            row and col (int): square to be checked

        Returns:
            int: square value wrt player
        """
        if (row == 0 or row == ROWS - 1) or (col == 0 or col == COLS - 1) or (col, row) in WALL_SQUARES:
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
        self.board_matrix[px][py] = PLAYER_SQUARE_VALUE
        for row in range(ROWS):
            for col in range(COLS):
                square_val = self.__square_vs_player_pos(px, py, row, col)
                self.board_matrix[row][col] = square_val
        pygame.display.update()
        pprint(self.board_matrix)
        
    