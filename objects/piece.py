import pygame
from .constants import BLACK, SQUARE_SIZE
from .board import Board
from pprint import pprint


class Piece:
    """Base class for making player and enemy pieces"""
    __PADDING = 10
    __OUTLINE = 2

    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.valid_moves = []
        self.__x = self.__y = 0
        self._calc_center_pixel()
        self.board = Board()

    def _calc_center_pixel(self) -> None:
        """Calculates center pixel coordinate of square on which piece resides"""
        self.__x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.__y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def get_pos(self) -> tuple:
        """Returns row and column of piece as tuple"""
        return (self.row, self.col)

    def _draw(self, win) -> None:
        """Draws the piece on the square"""
        self._calc_center_pixel()
        radius = SQUARE_SIZE // 2 - self.__PADDING
        pygame.draw.circle(win, BLACK, (self.__x, self.__y),
                           radius + self.__OUTLINE)
        pygame.draw.circle(win, self._color, (self.__x, self.__y), radius)

    def valid_moves_calc(self) -> None:
        """Generates a list of valid moves"""
        for r_seek in self.seek_range:
            for c_seek in self.seek_range:
                if r_seek == c_seek == 0:
                    continue
                x, y = self.row + r_seek, self.col + c_seek
                if self.board.get_square_value(x, y) != 0:
                    # if self.board_matrix[x][y] != 0:
                    self.valid_moves.append((r_seek, c_seek))
        pprint(self.valid_moves)

    def move(self, win, direction: tuple) -> None:
        """Base function to move a piece. Changes the piece coordinates, draws square on previous position and draws piece on new position

        Args:
            direction (tuple): previous row and column of piece
        """
        seek_r, seek_c = direction
        self.board.draw_single_square(win, self.row, self.col)
        self.row, self.col = self.row + seek_r, self.col + seek_c
        self._draw(win)
        pygame.display.update()

    def clear_valid_moves(self) -> None:
        self.valid_moves = []
