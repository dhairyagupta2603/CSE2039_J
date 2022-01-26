import pygame
from random import randint
from .constants import RED, YELLOW, ROWS, COLS, ENEMY_4_DIR, ENEMY_8_DIR
from .piece import Piece


class Enemy(Piece):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col, YELLOW)
        self._color = YELLOW
        self.type = ENEMY_4_DIR['name']
        self.seek_range = ENEMY_4_DIR['seek']
        self._calc_pos()

    def upgrade(self, win) -> None:
        """Upgrades the enemy from weak to strong"""
        self.color = RED
        self.type = ENEMY_8_DIR['name']
        self.seek_range = ENEMY_8_DIR['seek']
        self._draw(win)

    def enemy_move(self, direction: tuple) -> None:
        """Moves the enemy to specified loaction. also, changes position in window

        Args:
            direction (tuple): the direction which the enemy should move
        """
        # TODO: implement how enemy will move. so 'direction' argument will be useless
        self.move(direction)

    def __repr__(self) -> str:
        return str(self.color)
