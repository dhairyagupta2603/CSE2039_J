import pygame
from objects.constants import HEIGHT, WIDTH


FPS = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Kingdom of Circles')

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