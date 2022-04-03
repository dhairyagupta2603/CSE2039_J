from collections import defaultdict
from math import sqrt
from random import randint
from .constants import RED, VIOLET, YELLOW, ROWS, COLS, ENEMY_DIAG, ENEMY_4_DIR, ENEMY_8_DIR, RHIGH, CHIGH, WALL_SQUARES
from .piece import Piece


class Enemy(Piece):
    def __init__(self, row: int, col: int) -> None:
        super().__init__(row, col)
        if randint(0, 1) == 1:
            self.color = YELLOW
            self.type = ENEMY_4_DIR['name']
            self.seek_range = ENEMY_4_DIR['seek']
        else:
            self.color = VIOLET
            self.type = ENEMY_DIAG['name']
            self.seek_range = ENEMY_DIAG['seek']
        self._calc_center_pixel()

    def upgrade(self, win) -> None:
        """Upgrades the enemy from weak to strong"""
        self.color = RED
        self.type = ENEMY_8_DIR['name']
        self.seek_range = ENEMY_8_DIR['seek']
        self.draw(win)
        
    def __pick_fn(self, moves, other_enemies, player_pos)->tuple:
        px, py = player_pos[0], player_pos[1]
        if (
            (px > 0 and px < CHIGH and py > 0 and py < RHIGH) or # upper left
            (px > 0 and px < CHIGH and py > 2*RHIGH and py < 3*RHIGH) or # upper right
            (px > 2*CHIGH and px < 3*CHIGH and py > 0 and py < RHIGH) or # lower left
            (px > 2*CHIGH and px < 3*CHIGH and py > 2*RHIGH and py < 3*RHIGH) # lower right
        ):
            # minimize distance
            d_min = 3*sqrt(RHIGH**2 + CHIGH**2)
            min_move = (moves[0])
            for (mx, my) in moves:
                for (ex, ey) in other_enemies:
                    d = sqrt((mx-ex)**2 + (my-ey)**2)
                    if d < d_min and d != 0: 
                        d_min = d
                        min_move = (mx, my)
            return min_move
        
        elif px > CHIGH and px < 2*CHIGH and py > RHIGH and py < 2*RHIGH:
            # maximize distance
            d_max = 0
            max_move = (moves[0])
            for (mx, my) in moves:
                for (ex, ey) in other_enemies:
                    d = sqrt((mx-ex)**2 + (my-ey)**2)
                    if d > d_max and d != 0: 
                        d_max = d
                        max_move = (mx, my)
            return max_move        
        
        else:
            return moves[randint(0, len(moves) - 1)]

    def enemy_move(self, win, board, other_enemies_pos: tuple, prize_pos: tuple, player_pos: tuple) -> None:
        """Moves the enemy depending on player pos. Also, changes position in window"""
        valid_moves = defaultdict(list)
        for (r_seek, c_seek) in self.seek_range:
            x, y = self.row + r_seek, self.col + c_seek
            sq_val = board.board_matrix[x][y]
            if sq_val != 0 and (x, y) != prize_pos and (x, y) not in other_enemies_pos:
                valid_moves[sq_val].append((x, y))
        print('Enemy moves: ', valid_moves)
        if len(valid_moves) < 1:
            return
        if len(other_enemies_pos) > 1:
            x, y = self.__pick_fn(valid_moves[max(valid_moves.keys())], other_enemies_pos, player_pos)
        else:
            x, y = valid_moves[max(valid_moves.keys())][0]
        print(f'Valid moves: {valid_moves[max(valid_moves.keys())]}')
        self.move(win, board, (x - self.row, y - self.col))
        self.row, self.col = x, y
        print((self.row, self.col))

    def new_pos(self, player_pos: tuple, other_enemies: tuple, prize_pos: tuple) -> None:
        """Draws and sets a new position on a square with no other object"""
        self.row, self.col = randint(1, ROWS - 2), randint(1, COLS - 2)
        tries = (ROWS - 2)*(COLS - 2)  # so that the loop is not infinite
        while ((self.row, self.col) == player_pos or (self.row, self.col) in other_enemies or (self.row, self.col) == prize_pos or (self.row, self.col) in WALL_SQUARES) and tries > 0:
            self.row, self.col = randint(1, ROWS - 2), randint(1, COLS - 2)
            tries -= 1

    def __repr__(self) -> str:
        return str(self.color)
