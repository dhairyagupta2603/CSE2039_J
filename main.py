import sys
import pygame
from objects.constants import GREEN, WIN, BLACK, RED, WHITE, LIGHT_BLUE, CENTER_H, CENTER_W, GAME_NAME, PINK, BOTTLE_GREEN
import firebasescore
from game import Game


def game_play(win, clock, fps: int) -> int:
    game = Game(win)
    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

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


def game_over(win, clock, fps: int, score: int, is_same_player: bool, is_playing: bool) -> bool:
    # define rectangle dimensions
    game_over_rect = pygame.Rect(CENTER_W - 250, CENTER_H - 250, 500, 100)
    score_rect = pygame.Rect(CENTER_W - 110, CENTER_H - 150, 220, 65)
    restart_rect = pygame.Rect(CENTER_W - 55, CENTER_H, 110, 50)
    quit_rect = pygame.Rect(CENTER_W - 55, CENTER_H + 70, 110, 50)

    run = True
    while run:
        clock.tick(fps)

        # draw textures
        win.fill(BLACK)
        pygame.draw.rect(win, BLACK, game_over_rect, 2)
        pygame.draw.rect(win, BLACK, score_rect, 2)
        pygame.draw.rect(win, GREEN, restart_rect)
        pygame.draw.rect(win, RED, quit_rect)

        textsurface = pygame.font.Font(
            'freesansbold.ttf', 75).render('GAME OVER', True, RED)
        win.blit(textsurface, (game_over_rect.x + 15, game_over_rect.y + 15))
        textsurface = pygame.font.Font('freesansbold.ttf', 40).render(
            f'SCORE: {score}', True, LIGHT_BLUE)
        win.blit(textsurface, (score_rect.x + 10, score_rect.y + 15))
        textsurface = pygame.font.Font(
            'freesansbold.ttf', 20).render('RESTART', True, WHITE)
        win.blit(textsurface, (restart_rect.x + 10, restart_rect.y + 15))
        textsurface = pygame.font.Font(
            'freesansbold.ttf', 20).render('QUIT', True, WHITE)
        win.blit(textsurface, (quit_rect.x + 30, quit_rect.y + 15))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    is_same_player = True
                    run = False
                if quit_rect.collidepoint(event.pos):
                    is_same_player = False
                    run = False

    return is_same_player


def main_menu(win, clock, fps: int, is_playing) -> bool:
    input_text = 'Enter your username:'
    starttext = 'START'
    endtext = 'QUIT'
    title = GAME_NAME.upper()
    usertext = ''
    font = pygame.font.Font('freesansbold.ttf', 20)
    titlefont = pygame.font.Font('C:\Windows\Fonts\courbd.ttf', 50)
    title_rect = pygame.Rect(CENTER_W - 280, CENTER_H - 250, 560, 70)
    input_rect = pygame.Rect(CENTER_W - 15, CENTER_H - 120, 200, 50)
    start_rect = pygame.Rect(CENTER_W - 50, CENTER_H, 100, 50)
    quit_rect = pygame.Rect(CENTER_W - 50, CENTER_H + 80, 100, 50)

    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                elif start_rect.collidepoint(event.pos):
                    # start the game
                    is_playing = True
                    username = usertext
                    print(username)
                    run = False
                elif quit_rect.collidepoint(event.pos):
                    is_playing = False
                    pygame.quit()
                    sys.exit()
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if len(usertext) <= 20:  # limit no of characters
                        if event.type == pygame.K_BACKSPACE:
                            usertext = usertext[0:-1]
                        elif event.type == pygame.K_KP_ENTER:
                            # start the game
                            pass
                        else:
                            usertext += event.unicode

        # draw textures
        win.fill(BLACK)
        pygame.draw.rect(win, BLACK, title_rect, 2)
        pygame.draw.rect(win, RED, input_rect, 2)
        pygame.draw.rect(win, BOTTLE_GREEN, start_rect)
        pygame.draw.rect(win, RED, quit_rect)

        text_surface = titlefont.render(title, True, PINK)
        win.blit(text_surface, (title_rect.x + 10, title_rect.y + 10))
        text_surface = font.render(usertext, True, WHITE)
        win.blit(text_surface, (input_rect.x + 10, input_rect.y + 10))
        text_surface = font.render(input_text, True, WHITE)
        win.blit(text_surface, (input_rect.x - 230, input_rect.y + 15))
        text_surface = font.render(starttext, True, WHITE)
        win.blit(text_surface, (start_rect.x + 17, start_rect.y + 15))
        text_surface = font.render(endtext, True, WHITE)
        win.blit(text_surface, (quit_rect.x + 24, quit_rect.y + 15))
        input_rect.w = max(250, text_surface.get_width()+50)
        pygame.display.update()
        
    return is_playing


def main():
    FPS = 30
    Clock = pygame.time.Clock()
    pygame.display.set_caption(GAME_NAME)

    is_playing = main_menu(WIN, Clock, FPS, True)
    is_same_player = True
    while is_playing:
        if is_same_player == True:
            score = game_play(WIN, Clock, FPS)
            is_same_player = game_over(
                WIN, Clock, FPS, score, is_same_player, is_playing)
        else:
            is_same_player = True
            is_playing = main_menu(WIN, Clock, FPS, is_playing)

    # score = game_play(WIN, Clock, FPS)
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main()
