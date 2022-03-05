import pygame
from random import randint
from .constants import RED, YELLOW, ROWS, COLS, ENEMY_4_DIR, ENEMY_8_DIR
from .piece import Piece


class Enemy(Piece):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
        self._color = YELLOW
        self.type = ENEMY_4_DIR['name']
        self.seek_range = ENEMY_4_DIR['seek']
        self._calc_center_pixel()

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
        
    def new_pos(self, win, player_pos: tuple) -> None:
        """Draws and sets a new position on a square with no other object"""
        self.row, self.col = randint(1, ROWS - 2), randint(1, COLS - 2)
        tries = (ROWS - 2)*(COLS - 2)  # so that the loop is not infinite
        while ((self.row, self.col) == player_pos) and tries > 0:
            self.row, self.col = randint(1, ROWS - 2), randint(1, COLS - 2)
            tries -= 1
        self._draw(win)
        pygame.display.update()

    def __repr__(self) -> str:
        return str(self.color)
