import pygame
from random import randint
from objects.constants import WIN, FPS, ROWS, COLS
from objects.board import Board
from objects.player import Player
from objects.enemies import Enemy
from game import Game

pygame.display.set_caption('Kingdom of Circles')
game = Game(WIN)

def main():
    run = True
    Clock = pygame.time.Clock()
    while run:
        Clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            game.player_move_control(event)

    pygame.quit()


if __name__ == '__main__':
    main()
