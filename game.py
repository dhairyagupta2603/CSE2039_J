import pygame
from random import randint
from objects.board import Board
from objects.player import Player
from objects.enemies import Enemy
from objects.constants import ROWS, COLS


class Game:
    def __init__(self) -> None:
        player = Player(randint(1, ROWS - 2), randint(1, COLS - 2))
        enemies = [Enemy()]

    def _calc_enemy_pos() -> None:
        pass
