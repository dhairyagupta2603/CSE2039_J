import pygame
from .constants import BLACK, SQUARE_SIZE, WIN
from .board import Board

board = Board()


class Piece:
    """Base class for making player and enemy pieces"""
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row: int, col: int, color: tuple) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.valid_moves = []
        self.x = self.y = 0
        self._calc_pos()

    def _calc_pos(self) -> None:
        """Calculates center pixel coordinate of square on which piece resides"""
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def get_pos(self) -> tuple:
        """Returns row and column of piece as tuple"""
        return (self.row, self.col)

    def _draw(self, win) -> None:
        """Draws the piece on the square"""
        self._calc_pos()
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self._color, (self.x, self.y), radius)

    def _valid_moves_calc(self) -> None:
        """Generates a list of valid moves"""
        for r_seek in self.seek_range:
            for c_seek in self.seek_range:
                if r_seek == c_seek == 0:
                    continue
                x, y = self.row + r_seek, self.col + c_seek
                if board.get_square_value(x, y) != 0:
                    self.valid_moves.append((r_seek, c_seek))

    def move(self, direction: tuple) -> None:
        """Base function to move a piece. Changes the piece coordinates, draws square on previous position and draws piece on new position

        Args:
            direction (tuple): previous row and column of piece
        """
        seek_r, seek_c = direction
        board.draw_single_square(WIN, self.row, self.col)
        self.row, self.col = self.row + seek_r, self.col + seek_c
        self._draw(self, WIN)
