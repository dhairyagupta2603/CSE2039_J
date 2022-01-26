import pygame
from objects.constants import HEIGHT, WIDTH
from objects.board import Board
from objects.player import Player
from objects.enemies import Enemy


FPS = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Kingdom of Circles')

# board initialization
board = Board()
board.draw_squares(WIN)
pygame.display.update()
player = Player(1, 1)
board.get_board_matrix(player.get_pos())
enemy = Enemy(4, 8)
player.draw(WIN)
enemy.draw(WIN)
pygame.display.update()

def main():
    run = True
    Clock = pygame.time.Clock()
    
    while run:
        Clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        
    pygame.quit()


if __name__ == '__main__':
    main()
