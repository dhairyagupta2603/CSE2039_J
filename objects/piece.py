import pygame
from .constants import BLACK, SQUARE_SIZE


class Piece:
    """Base class for making player and enemy pieces"""
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row: int, col: int, color: tuple) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.x = self.y = 0
        self._calc_pos()

    def _calc_pos(self) -> None:
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win) -> None:
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
