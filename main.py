import pygame
from objects.constants import ENEMY_4_DIR, ENEMY_8_DIR, PLAYER, WIN, FPS
from game import Game


def main():
    run = True
    Clock = pygame.time.Clock()
    pygame.display.set_caption('Kingdom of Circles')

    game = Game(WIN)

    while run:
        Clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and game.turn == PLAYER:
                game.player_move_control(event, WIN)
                game.update_prize_pos(WIN)
                game.turn = ENEMY_4_DIR
                
            if game.turn == ENEMY_8_DIR or game.turn == ENEMY_4_DIR:
                # movement of enemy
                game.update_turn()

    pygame.quit()


if __name__ == '__main__':
    main()
