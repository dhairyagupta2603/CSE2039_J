from random import randint
from .constants import BLUE, ROWS, COLS
from .piece import Piece


class Player(Piece):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col, BLUE)
        self.color = BLUE
        self.x = self.y = 0
        self._calc_pos()

    def __repr__(self) -> str:
        return str(self._calc_pos())
