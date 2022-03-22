import pygame
from .constants import BLACK, SQUARE_SIZE

class Piece:
    """Base class for making player and enemy pieces"""
    __PADDING = 10
    __OUTLINE = 2

    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.__x = self.__y = 0
        self._calc_center_pixel()

    def _calc_center_pixel(self) -> None:
        """Calculates center pixel coordinate of square on which piece resides"""
        self.__x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.__y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def get_pos(self) -> tuple:
        """Returns row and column of piece as tuple"""
        return (self.row, self.col)

    def draw(self, win) -> None:
        """Draws the piece on the square"""
        self._calc_center_pixel()
        radius = SQUARE_SIZE // 2 - self.__PADDING
        pygame.draw.circle(win, BLACK, (self.__x, self.__y),
                           radius + self.__OUTLINE)
        pygame.draw.circle(win, self.color, (self.__x, self.__y), radius)

    def move(self, win, board, direction: tuple) -> None:
        """Base function to move a piece. Changes the piece coordinates, draws square on previous position and draws piece on new position

        Args:
            direction (tuple): previous row and column of piece
        """
        seek_r, seek_c = direction
        board.draw_single_square(win, self.row, self.col)
        self.row, self.col = self.row + seek_r, self.col + seek_c
        self.draw(win)
        pygame.display.update()
