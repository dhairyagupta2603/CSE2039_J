import pygame
from random import randint
from objects.board import Board
from objects.player import Player
from objects.enemies import Enemy
from objects.prize import Prize
from objects.constants import ROWS, COLS, PLAYER, ENEMY_4_DIR, ENEMY_8_DIR


class Game:
    def __init__(self, win) -> None:
        self.board = Board()
        self.board.draw_squares(win)

        # self.prize = Prize(win, 5, 5)
        # self.player = Player(2, 2)
        self.prize = Prize(win, randint(1, ROWS - 2), randint(1, COLS - 2))
        self.player = Player(randint(1, ROWS - 2), randint(1, COLS - 2))
        self.player._draw(win)
        if self.player.get_pos() == self.prize.get_pos():
            self.prize.new_pos(win, self.player.get_pos())
        self.board.update_walls_pos(win, self.player.get_pos(), self.prize.get_pos())
        self.player.valid_moves_calc()
        
        # self.enemies = [Enemy(randint(1, ROWS - 2), randint(1, COLS - 2))]
        # self.enemies[0]._draw(win)
        # self.board.get_board_matrix(self.player.get_pos())
        pygame.display.update()
        self.turn = PLAYER
        self.score = 0
        self.high_score = 0

    # def update(self)->None:
    #     sef.board.

    def _calc_enemy_pos() -> None:
        pass

    def player_move_control(self, event, win) -> None:
        self.player.valid_moves_calc()
        if event.key == pygame.K_KP1 and (1, -1) in self.player.valid_moves:
            self.player.player_move(win, (1, -1))
        elif event.key == pygame.K_KP2 and (1, 0) in self.player.valid_moves:
            self.player.player_move(win, (1, 0))
        elif event.key == pygame.K_KP3 and (1, 1) in self.player.valid_moves:
            self.player.player_move(win, (1, 1))
        elif event.key == pygame.K_KP4 and (0, -1) in self.player.valid_moves:
            self.player.player_move(win, (0, -1))
        elif event.key == pygame.K_KP6 and (0, 1) in self.player.valid_moves:
            self.player.player_move(win, (0, 1))
        elif event.key == pygame.K_KP7 and (-1, -1) in self.player.valid_moves:
            self.player.player_move(win, (-1, -1))
        elif event.key == pygame.K_KP8 and (-1, 0) in self.player.valid_moves:
            self.player.player_move(win, (-1, 0))
        elif event.key == pygame.K_KP9 and (-1, 1) in self.player.valid_moves:
            self.player.player_move(win, (-1, 1))
        else:
            print('Invalid key press among valid options')
        self.player.clear_valid_moves()
        print(self.player.get_pos())
        

    def update_prize_pos(self, win)->None:
        """Sets and draws prize to a new location if player captures the prize"""
        if self.player.get_pos() == self.prize.get_pos():
            self.prize.new_pos(win, self.player.get_pos())
            self.score+=1
            self.board.get_board_matrix(self.player.get_pos())
            self.board.update_walls_pos(win, self.player.get_pos(), self.prize.get_pos())
        # print(self.score)
