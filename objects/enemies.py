import pygame
from random import randint
from .constants import RED, YELLOW, ROWS, COLS, ENEMY_4_DIR, ENEMY_8_DIR
from .piece import Piece


class Enemy(Piece):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col, YELLOW)
        self.color = YELLOW
        self.type = ENEMY_4_DIR['name']
        self.seek_range = ENEMY_4_DIR['seek']
        self._calc_pos()


    def upgrade(self, win) -> None:
        self.color = RED
        self.type = ENEMY_8_DIR['name']
        self.seek_range = ENEMY_8_DIR['seek']
        self.draw(win)


    def enemy_move(self, direction)->None:
        seek_r, seek_c = direction
        self.move(seek_r, seek_c)


    def __repr__(self) -> str:
        return str(self.color)
