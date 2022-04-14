import pygame
from objects.constants import WIN, BLACK, RED, YELLOW,WHITE, LIGHT_BLUE, CENTER_H, CENTER_W
import firebasescore
from game import Game


def game_play(win, clock, fps: int)->int:
    game = Game(win)
    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and game.player_turn == True:
                game.player_move_control(event, win)
                game.update_prize_pos(win)
                game.player_turn = False

            if game.player_turn == False:
                game.move_enemies(win)
                if game.player_killed == True:
                    run = False
                    break
                game.player_turn = True
    # firebasescore.send_data('Dhairya', game.score)
    return game.score


def main_menu(win):
    pass


def game_over(win, clock, fps: int, score: int, is_same_player: bool, is_playing: bool)->bool:
    # define rectangle dimensions
    game_over_rect = pygame.Rect(CENTER_W - 250, CENTER_H - 250, 500,100)
    score_rect = pygame.Rect(CENTER_W - 110,CENTER_H - 150, 220, 65)
    restart_rect = pygame.Rect(CENTER_W - 55, CENTER_H, 110,50)
    quit_rect = pygame.Rect(CENTER_W - 55, CENTER_H + 70, 110,50)
    run = True
    while run:
        clock.tick(fps)
        
        # draw textures
        win.fill(BLACK)
        pygame.draw.rect(win, BLACK, game_over_rect, 2)
        pygame.draw.rect(win, BLACK, score_rect, 2)
        pygame.draw.rect(win, YELLOW, restart_rect, 2)
        pygame.draw.rect(win, RED, quit_rect, 2)
        
        textsurface = pygame.font.Font('freesansbold.ttf', 75).render('GAME OVER', True, RED)
        win.blit(textsurface, (game_over_rect.x + 15, game_over_rect.y + 15))
        textsurface = pygame.font.Font('freesansbold.ttf', 40).render(f'SCORE: {score}', True, LIGHT_BLUE)
        win.blit(textsurface, (score_rect.x + 10, score_rect.y + 15))
        textsurface = pygame.font.Font('freesansbold.ttf', 20).render('RESTART', True, WHITE)
        win.blit(textsurface, (restart_rect.x + 10, restart_rect.y + 15))
        textsurface = pygame.font.Font('freesansbold.ttf', 20).render('QUIT', True, WHITE)
        win.blit(textsurface, (quit_rect.x + 30, quit_rect.y + 15))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    is_same_player = True
                    run = False
                if quit_rect.collidepoint(event.pos):
                    is_same_player = False
                    run = False

    return is_same_player


def main():
    FPS = 30
    run = True
    Clock = pygame.time.Clock()
    pygame.display.set_caption('Kingdom of Circles')

    is_playing = True
    is_same_player = True
    while is_playing:
        if is_same_player == True:
            score = game_play(WIN, Clock, FPS)
            is_same_player = game_over(WIN, Clock, FPS, score, is_same_player, is_playing)
        else:
            is_playing = False
            
    # score = game_play(WIN, Clock, FPS)
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main()
