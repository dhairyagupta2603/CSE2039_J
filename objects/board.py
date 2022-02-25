from ast import Num
import pygame
from random import randint
from .constants import BLACK, GREEN, GREEN_NAME, GREY, GREY_NAME, ROWS, COLS, SQUARE_SIZE, PLAYER_SQUARE_VALUE
from pprint import pprint


class Board:
    __OUTLINE = 2

    def __init__(self) -> None:
        self.board_colors = [([GREEN_NAME]*COLS) for _ in range(ROWS)]
        self._board_values = [([0]*COLS) for _ in range(ROWS)]
        # self.__outer_values = [0 for _ in range(2*(HEIGHT - 2) + 2(WIDTH - 4))]
        self.__num_enemies = 1

    def draw_squares(self, win) -> None:
        """Draw the visual representaion of board. Also, initializes board square colors as a matrix"""
        win.fill(BLACK)
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if (row % 2 == 0 and col % 2 == 0) or (row % 2 != 0 and col % 2 != 0):
        #             pygame.draw.rect(win, DARKER_GREEN, (row*SQUARE_SIZE + self.__OUTLINE, col*SQUARE_SIZE + self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE))
        #         if (row == 0 or row == ROWS - 1) or (col == 0 or col == COLS - 1):
        #             pygame.draw.rect(win, GREY, (row*SQUARE_SIZE + self.__OUTLINE, col*SQUARE_SIZE + self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE))
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE,
                                              col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                if (row == 0 or row == ROWS - 1) or (col == 0 or col == COLS - 1):
                    pygame.draw.rect(win, GREY, (row*SQUARE_SIZE + self.__OUTLINE, col*SQUARE_SIZE +
                                                 self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE))
                    self.board_colors[row][col] = GREY_NAME
                else:
                    pygame.draw.rect(win, GREEN, (row*SQUARE_SIZE + self.__OUTLINE, col*SQUARE_SIZE +
                                                  self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE))

    def draw_single_square(self, win, row: int, col: int, color: tuple) -> None:
        """Darws a single square on window at the specified place

        Args:
            row (int): row of board
            col (int): column of board
        """
        pygame.draw.rect(win, color, (col*SQUARE_SIZE + self.__OUTLINE, row*SQUARE_SIZE +
                                      self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE, SQUARE_SIZE - self.__OUTLINE))

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
        # if self._board_values[row][col] == 0:
                # return 0;
                # self.draw_single_square(WIN, row, col, GREEN)
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
                square_val = self.__square_vs_player_pos(px, py, row, col)
                self._board_values[row][col] = square_val
        
        pprint(self._board_values)

    def get_square_value(self, row: int, col: int) -> int:
        """Returns the value of specified square"""
        print('got square value: ', (row, col))
        return self._board_values[row][col]

    def update_walls_pos(self, win, player_pos, prize_pos) -> None:
        __num_walls = 7
        for row in range(1, ROWS - 2):
            for col in range(1, COLS - 2):
                if ((row, col) != player_pos) and ((row, col) != prize_pos):
                    if self._board_values[row][col] == 0:
                        self.draw_single_square(win, row, col, GREEN)
                        self.board_colors[row][col] = GREEN_NAME
                    if (randint(1, ROWS*COLS) <= __num_walls):
                        __num_walls-=1
                        self._board_values[row][col] = 0
                        self.draw_single_square(win, row, col, GREY)
                        self.board_colors[row][col] = GREY_NAME
        pprint(self.board_colors)
        # pygame.display.update()