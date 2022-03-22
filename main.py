import pygame
from objects.constants import WIDTH, HEIGHT
from game import Game


def main():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    FPS = 30
    run = True
    Clock = pygame.time.Clock()
    pygame.display.set_caption('Kingdom of Circles')

    game = Game(WIN)

    while run:
        Clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and game.player_turn == True:
                game.player_move_control(event, WIN)
                game.update_prize_pos(WIN)
                game.player_turn = False

            if game.player_turn == False:
                game.move_enemies(WIN)
                # if game.player_killed == True:
                #     run = False
                game.player_turn = True

    pygame.quit()


if __name__ == '__main__':
    main()
