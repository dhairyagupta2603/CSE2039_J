from random import randint
from .piece import Piece
from .constants import WHITE, ROWS, COLS, WALL_SQUARES


class Prize(Piece):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
        self.color = WHITE
        self._calc_center_pixel()

    def new_pos(self, player_pos: tuple, enemies_pos: tuple) -> None:
        """Draws and sets a new position on a square with no other object"""
        self.row, self.col = randint(1, ROWS - 2), randint(1, COLS - 2)
        tries = (ROWS - 2)*(COLS - 2)  # so that the loop is not infinite
        while ((self.row, self.col) in player_pos or (self.row, self.col) in enemies_pos or (self.row, self.col) in WALL_SQUARES) and tries > 0:
            self.row, self.col = randint(1, ROWS - 2), randint(1, COLS - 2)
            tries -= 1
