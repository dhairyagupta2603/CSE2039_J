import pygame
from random import randint
from objects.board import Board
from objects.player import Player
from objects.enemies import Enemy
from objects.constants import ROWS, COLS


class Game:
    def __init__(self, win) -> None:
        self.board = Board()
        self.board.draw_squares(win)
        # self.player = Player(randint(1, ROWS - 2), randint(1, COLS - 2))
        self.player = Player(2, 2)
        self.player._draw(win)
        # self.enemies = [Enemy(randint(1, ROWS - 2), randint(1, COLS - 2))]
        # self.enemies[0]._draw(win)
        # self.board.get_board_matrix(self.player.get_pos())
        pygame.display.update()

    # def update(self)->None:
    #     sef.board.

    def _calc_enemy_pos() -> None:
        pass


    def player_move_control(self, event)->None:
        if event.type == pygame.KEYDOWN:
            self.player.valid_moves_calc()
            if event.key == pygame.K_KP1 and (1, -1) in self.player.valid_moves:
                self.player.player_move((1, -1))
            elif event.key == pygame.K_KP2 and (1, 0) in self.player.valid_moves:
                self.player.player_move((1, 0))
            elif event.key == pygame.K_KP3 and (1, 1) in self.player.valid_moves:
                self.player.player_move((1, 1))
            elif event.key == pygame.K_KP4 and (0, -1) in self.player.valid_moves:
                self.player.player_move((0, -1))
            elif event.key == pygame.K_KP6 and (0, 1) in self.player.valid_moves:
                self.player.player_move((0, 1))
            elif event.key == pygame.K_KP7 and (-1, -1) in self.player.valid_moves:
                self.player.player_move((-1, -1))
            elif event.key == pygame.K_KP8 and (-1, 0) in self.player.valid_moves:
                self.player.player_move((-1, 0))
            elif event.key == pygame.K_KP9 and (-1, 1) in self.player.valid_moves:
                self.player.player_move((-1, 1))
            else:
                print('Invalid key press among valid options')
        self.player.clear_valid_moves()