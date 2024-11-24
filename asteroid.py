import pygame
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        # sub-classes must override
        #pygame.draw.polygon(screen, (255,255,255),self.triangle(),2)
        pygame.draw.circle(screen, (255,255,255),self.position,self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            angle_1 = self.velocity.rotate(random_angle)
            angle_2 = self.velocity.rotate(-random_angle)
            new_asteroid_1 = Asteroid(self.position[0],self.position[1],self.radius-ASTEROID_MIN_RADIUS)
            new_asteroid_1.velocity = angle_1*1.2
            new_asteroid_2 = Asteroid(self.position[0],self.position[1],self.radius-ASTEROID_MIN_RADIUS)
            new_asteroid_2.velocity = angle_2*1.2
        