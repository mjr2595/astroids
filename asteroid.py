import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # small asteroids are not split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # larger asteroids split into two smaller ones

        # random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # rotate the velocity vector by the random angle
        new_vector1 = self.velocity.rotate(random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)

        # new radius is half the current radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create two new asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # new asteroids go faster
        new_asteroid1.velocity = new_vector1 * 1.2
        new_asteroid2.velocity = new_vector2 * 1.2
