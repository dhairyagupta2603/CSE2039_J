import firebasescore
from sympy import false
import constants
import pygame,sys
from constants import BLACK, WHITE, WIN, RED, BLUE, GREEN

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Main-Menu")
win = constants.WIN
font = constants.FONT
usertext = ''
input_rect = pygame.Rect(200,200,200,50)
start_rect = pygame.Rect(200,300,200,50)
quit_rect = pygame.Rect(200,400,200,50)

active = false

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            elif start_rect.collidepoint(event.pos):
                #start the game
                constants.username = usertext
                print(constants.username)
            elif quit_rect.collidepoint(event.pos):
                firebasescore.senddata(usertext, 10)
                pygame.quit()
                sys.exit()
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active == True:
                if len(usertext) < 50: #limit no of characters 
                    if event.type == pygame.K_BACKSPACE:
                        usertext = usertext[0:-1]
                    else:
                        usertext += event.unicode
    win.fill(BLACK)

    pygame.draw.rect(win, RED, input_rect, 2)
    pygame.draw.rect(win, GREEN, start_rect)
    pygame.draw.rect(win, BLUE, quit_rect)


    text_surface = font.render(usertext, True, WHITE)
    win.blit(text_surface, (input_rect.x + 10, input_rect.y+10))

    input_rect.w = max(150,text_surface.get_width()+20)

    pygame.display.flip()
    clock.tick(60)