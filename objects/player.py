from .constants import BLUE, PLAYER
from .piece import Piece
from pprint import pprint
import pygame

class Player(Piece):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
        self.color = BLUE
        self.texture = pygame.image.load(r"textures\user.png")
        self.seek_range = PLAYER['seek']
        self._calc_center_pixel()
        self.valid_moves = []
        # self.valid_moves_calc()

    def player_move(self, win, board, direction: tuple) -> None:
        """Moves the player to specified loaction. also, changes position in window

        Args:
            direction (tuple): the direction which the player should move
        """
        self.move(win, board, direction)
        board.get_board_matrix(self.get_pos())
        
    def valid_moves_calc(self, board_matrix: list) -> None:
        """Generates a list of valid moves"""
        for (r_seek, c_seek) in self.seek_range:
                x, y = self.row + r_seek, self.col + c_seek
                if board_matrix[x][y] != 0:
                    self.valid_moves.append((r_seek, c_seek))
        pprint(self.valid_moves)

    def __repr__(self) -> str:
        return str(self._calc_center_pixel())
