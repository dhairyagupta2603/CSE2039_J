import firebasescore
from sympy import false
import constants
import pygame,sys
from constants import BLACK, WHITE, WIN, RED, BLUE, GREEN, PINK

input_text = 'Enter your username:'
starttext = 'START'
endtext = 'QUIT'

title = ' P A C - M O U S E'

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Main-Menu")
win = constants.WIN
font = constants.FONT
titlefont = constants.TITLE_FONT
usertext = ''
input_rect = pygame.Rect(300,200,200,50)
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
                firebasescore.senddata(usertext, 30)
                pygame.quit()
                sys.exit()
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active == True:
                if len(usertext) <= 20: #limit no of characters
                    if event.type == pygame.K_BACKSPACE:
                        usertext = usertext[0:-1]
                    elif event.type == pygame.K_KP_ENTER:
                        #start the game
                        pass
                    else:
                        usertext += event.unicode
    win.fill(BLACK)

    pygame.draw.rect(win, RED, input_rect, 2)
    pygame.draw.rect(win, (50,145,113), start_rect)
    pygame.draw.rect(win, BLUE, quit_rect)


    text_surface = titlefont.render(title, True, PINK)
    win.blit(text_surface, (input_rect.x - 100, input_rect.y - 100))
    text_surface = font.render(usertext, True, WHITE)
    win.blit(text_surface, (input_rect.x + 10, input_rect.y+10))
    text_surface = font.render(input_text, True, WHITE)
    win.blit(text_surface, (input_rect.x - 250, input_rect.y + 10))
    text_surface = font.render(starttext, True, WHITE)
    win.blit(text_surface, (start_rect.x + 10, start_rect.y+10))
    text_surface = font.render(endtext, True, WHITE)
    win.blit(text_surface, (quit_rect.x + 10, quit_rect.y+10))

    input_rect.w = max(250,text_surface.get_width()+50)

    pygame.display.flip()
    clock.tick(60)