from collections import defaultdict
import pygame
from random import randint
from .constants import RED, YELLOW, ROWS, COLS, ENEMY_4_DIR, ENEMY_8_DIR
from .piece import Piece


class Enemy(Piece):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
        self.color = YELLOW
        self.type = ENEMY_4_DIR['name']
        self.seek_range = ENEMY_4_DIR['seek']
        self._calc_center_pixel()

    def upgrade(self, win) -> None:
        """Upgrades the enemy from weak to strong"""
        self.color = RED
        self.type = ENEMY_8_DIR['name']
        self.seek_range = ENEMY_8_DIR['seek']
        self.draw(win)

    def enemy_move(self, win, board) -> None:
        """Moves the enemy depending on player pos. Also, changes position in window"""
        valid_moves = defaultdict(list)
        for (r_seek, c_seek) in self.seek_range:
            x, y = self.row + r_seek, self.col + c_seek
            sq_val = board.board_matrix[x][y]
            if sq_val != 0:
                valid_moves[sq_val].append((x, y))
        # TODO: implement which max value move will enemy take. rn it takes 0th move
        print(valid_moves)
        x, y = valid_moves[max(valid_moves.keys())][0]
        self.move(win, board, (x - self.row, y - self.col))

    def new_pos(self, player_pos: tuple) -> None:
        """Draws and sets a new position on a square with no other object"""
        self.row, self.col = randint(1, ROWS - 2), randint(1, COLS - 2)
        tries = (ROWS - 2)*(COLS - 2)  # so that the loop is not infinite
        while ((self.row, self.col) == player_pos) and tries > 0:
            self.row, self.col = randint(1, ROWS - 2), randint(1, COLS - 2)
            tries -= 1

    def __repr__(self) -> str:
        return str(self.color)
