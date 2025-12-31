import pygame # type: ignore
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_angle = self.velocity.rotate(angle)
        second_angle = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first = Asteroid(self.position[0], self.position[1], new_radius)
        second = Asteroid(self.position[0], self.position[1], new_radius)
        first.velocity = first_angle * 1.2
        second.velocity = second_angle * 1.2