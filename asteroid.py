from circleshape import *
from constants import ASTEROID_MIN_RADIUS, Color
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, Color.WHITE, self.position.xy, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        # Create two smaller asteroids
        random_angle = random.uniform(20.0, 50.0)

        angle1 = self.velocity.rotate(random_angle)
        angle2 = self.velocity.rotate(-random_angle)

        radius1 = self.radius - ASTEROID_MIN_RADIUS
        radius2 = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, radius1)
        asteroid2 = Asteroid(self.position.x, self.position.y, radius2)

        asteroid1.velocity = angle1 * 1.2
        asteroid2.velocity = angle2
