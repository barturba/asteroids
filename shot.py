from circleshape import *
from constants import SHOT_RADIUS, Color


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, Color.WHITE, self.position.xy, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
