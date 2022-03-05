from .constants import BLUE, PLAYER
from .piece import Piece


class Player(Piece):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
        self._color = BLUE
        self.seek_range = PLAYER['seek']
        self._calc_center_pixel()
        self.valid_moves_calc()
        self.board.get_board_matrix(self.get_pos())

    def player_move(self, win, direction: tuple) -> None:
        """Moves the player to specified loaction. also, changes position in window

        Args:
            direction (tuple): the direction which the player should move
        """
        self.move(win, direction)
        self.board.get_board_matrix(self.get_pos())

    def __repr__(self) -> str:
        return str(self._calc_center_pixel())
