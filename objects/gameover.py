import firebasescore
#from mainmenu import usertext
from sympy import false
import constants
import pygame,sys
from constants import BLACK, WHITE, WIN, RED, BLUE, GREEN, YELLOW
from constants import FONT as font


clock = pygame.time.Clock()
pygame.display.set_caption("Main-Menu")
win = constants.WIN
font = constants.FONT
quittext = 'QUIT'
restarttext = 'CLICK HERE TO RESTART...'
pygame.init()

restart_rect = pygame.Rect(200,200,300,50)
quit_rect = pygame.Rect(200,300,150,50)


def showscreen(win):
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(event.pos):
                    #firebasescore.senddata(usertext, 10)
                    pygame.quit()
                    sys.exit()
                if restart_rect.collidepoint(event.pos):
                    pass

        win.fill(BLACK)
        pygame.draw.rect(win, RED, quit_rect, 2)
        pygame.draw.rect(win, YELLOW, restart_rect, 2)

        textsurface = font.render(restarttext, True, WHITE)
        win.blit(textsurface, (restart_rect.x + 10, restart_rect.y + 15))
        textsurface = font.render(quittext, True, WHITE)
        win.blit(textsurface, (quit_rect.x + 40, quit_rect.y + 15))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    showscreen(win)
