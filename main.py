# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import *
from asteroid import *
from asteroidfield import *

from constants import *
from shots import *



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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

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

        for one_asteroid in asteroids:
            if player.did_collide(one_asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.did_collide(one_asteroid):
                    shot.kill()
                    one_asteroid.split()     



        pygame.display.flip()        

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
