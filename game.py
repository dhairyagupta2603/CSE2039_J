import pygame
from random import randint
from objects.board import Board
from objects.player import Player
from objects.enemies import Enemy
from objects.prize import Prize
from objects.constants import ROWS, COLS, PLAYER, MAX_NUM_ENEMIES


class Game:
    def __init__(self, win) -> None:
        # draw boardtill 
        self.board = Board()
        self.board.draw_squares(win)

        # initialize player
        self.player = Player(randint(1, ROWS - 2), randint(1, COLS - 2))
        self.player.draw(win)

        # initilize enemies and get position
        self.enemies = [Enemy(randint(1, ROWS - 2), randint(1, COLS - 2))]
        if self.enemies[0].get_pos() == self.player.get_pos():
            self.enemies[0].new_pos(self.player.get_pos(), (-1, 1), (-1, -1))
        self.enemies[0].draw(win)
        self.enemies_pos = [enemy.get_pos() for enemy in self.enemies]
        print(self.enemies_pos[0])
        self.num_enemies = 1

        # initialize prize
        self.prize = Prize(randint(1, ROWS - 2), randint(1, COLS - 2))
        if self.prize.get_pos() == self.enemies[0].get_pos() or self.prize.get_pos() == self.player.get_pos():
            self.prize.new_pos(self.player.get_pos(),
                               self.enemies_pos)
        self.prize.draw(win)

        self.board.get_board_matrix(self.player.get_pos())
        pygame.display.update()
        self.turn = PLAYER
        self.player_killed = False
        self.score = 0
        self.high_score = 0

    def move_enemies(self, win):
        for i, enemy in enumerate(self.enemies):
            enemy.enemy_move(win, self.board, self.enemies_pos, self.prize.get_pos(), self.player.get_pos())
            self.enemies_pos[i] = self.enemies[i].get_pos()
        if self.player.get_pos() in self.enemies_pos:
            self.player_killed = True

    def player_move_control(self, event, win) -> None:
        self.player.valid_moves_calc(self.board.board_matrix)
        if event.key == pygame.K_KP1 and (1, -1) in self.player.valid_moves:
            self.player.player_move(win, self.board, (1, -1))
        elif event.key == pygame.K_KP2 and (1, 0) in self.player.valid_moves:
            self.player.player_move(win, self.board, (1, 0))
        elif event.key == pygame.K_KP3 and (1, 1) in self.player.valid_moves:
            self.player.player_move(win, self.board, (1, 1))
        elif event.key == pygame.K_KP4 and (0, -1) in self.player.valid_moves:
            self.player.player_move(win, self.board, (0, -1))
        elif event.key == pygame.K_KP6 and (0, 1) in self.player.valid_moves:
            self.player.player_move(win, self.board, (0, 1))
        elif event.key == pygame.K_KP7 and (-1, -1) in self.player.valid_moves:
            self.player.player_move(win, self.board, (-1, -1))
        elif event.key == pygame.K_KP8 and (-1, 0) in self.player.valid_moves:
            self.player.player_move(win, self.board, (-1, 0))
        elif event.key == pygame.K_KP9 and (-1, 1) in self.player.valid_moves:
            self.player.player_move(win, self.board, (-1, 1))
        else:
            print('Invalid key press among valid options')
        self.player.valid_moves = []

    def update_prize_pos(self, win) -> None:
        if self.player.get_pos() == self.prize.get_pos():
            self.prize.new_pos(self.player.get_pos(),
                               self.enemies[0].get_pos())
            self.prize.draw(win)
            pygame.display.update()
            self.score += 1
            self.update_difficulty(win)
        print(self.score)

    def update_difficulty(self, win) -> None:
        if self.num_enemies < MAX_NUM_ENEMIES and randint(0, 100) < 50:
            self.num_enemies+=1;
            self.enemies.append(Enemy(randint(1, ROWS - 2), randint(1, COLS - 2)))
            if self.enemies[self.num_enemies-1].get_pos() == self.player.get_pos():
                self.enemies[self.num_enemies-1].new_pos(self.player.get_pos(), self.enemies_pos, self.prize.get_pos())
            self.enemies[self.num_enemies-1].draw(win)
            self.enemies_pos.append(self.enemies[self.num_enemies-1].get_pos())

    def is_player_dead(self) -> bool:
        pass
