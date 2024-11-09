from circleshape import *
from constants import Color


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, Color.WHITE, self.position.xy, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
