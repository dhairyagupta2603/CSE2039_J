from .constants import BLUE, WIN
from .piece import Piece, board

class Player(Piece):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col, BLUE)
        self.color = BLUE
        self._calc_pos()
        self._valid_moves_calc()

    def _valid_moves_calc(self)->None:
        for r_seek in [-1, 0, 1]:
            for c_seek in [-1, 0, 1]:
                if r_seek == c_seek == 0:
                    continue
                x, y = self.row + r_seek, self.col + c_seek
                if board.get_square_value(x, y) != 0:
                    self.valid_moves.append([r_seek, c_seek])

    def player_move(self, direction)->None:
        seek_r, seek_c = direction
        self.move(seek_r, seek_c)
        board.get_board_matrix(self.get_pos())


    def __repr__(self) -> str:
        return str(self._calc_pos())
