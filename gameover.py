import firebasescore
import objects.constants
import pygame,sys
from objects.constants import BLACK, BLUE,LIGHT_BLUE, WHITE, WIN, RED, YELLOW, CENTER_H, CENTER_W

#g = Game(WIN)

clock = pygame.time.Clock()
pygame.display.set_caption("Msain-Menu")
win = WIN
quittext = 'QUIT'
restarttext = 'RESTART'
pygame.init()

game_over_rect = pygame.Rect(CENTER_W - 250, CENTER_H - 250, 500,100)
score_rect = pygame.Rect(CENTER_W - 110,CENTER_H - 150, 220, 65)
restart_rect = pygame.Rect(CENTER_W - 55, CENTER_H, 110,50)
quit_rect = pygame.Rect(CENTER_W - 55, CENTER_H + 70, 110,50)


def showscreen(win):
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(event.pos):
                    # firebasescore.senddata(usertext, g.score)
                    pygame.quit()
                    sys.exit()
                if restart_rect.collidepoint(event.pos):
                    pass

        win.fill(BLACK)
        pygame.draw.rect(win, BLACK, game_over_rect, 2)
        pygame.draw.rect(win, BLACK, score_rect, 2)
        pygame.draw.rect(win, YELLOW, restart_rect, 2)
        pygame.draw.rect(win, RED, quit_rect, 2)

        
        textsurface = pygame.font.Font('freesansbold.ttf', 75).render('GAME OVER', True, RED)
        win.blit(textsurface, (game_over_rect.x + 15, game_over_rect.y + 15))
        textsurface = pygame.font.Font('freesansbold.ttf', 40).render(f'SCORE: {0}', True, LIGHT_BLUE)
        win.blit(textsurface, (score_rect.x + 10, score_rect.y + 15))
        textsurface = pygame.font.Font('freesansbold.ttf', 20).render('RESTART', True, WHITE)
        win.blit(textsurface, (restart_rect.x + 10, restart_rect.y + 15))
        textsurface = pygame.font.Font('freesansbold.ttf', 20).render('QUIT', True, WHITE)
        win.blit(textsurface, (quit_rect.x + 30, quit_rect.y + 15))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    showscreen(win)
