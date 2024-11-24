import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)


    def draw(self, screen):
        # sub-classes must override
        #pygame.draw.polygon(screen, (255,255,255),self.triangle(),2)
        pygame.draw.circle(screen, (255,255,255),self.position,self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity * dt