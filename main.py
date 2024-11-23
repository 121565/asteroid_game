# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *

from constants import *



def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0




    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    a=1
    while a>0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)            


        pygame.display.flip()        

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()