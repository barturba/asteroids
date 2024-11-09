from constants import *
from player import *

import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize FPS clock
    clock = pygame.time.Clock()
    dt = 0  # Delta time

    # Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Initialize a Player object
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        pygame.Surface.fill(screen, (0, 0, 0))

        # Run the update loop
        for sprite in updatable:
            sprite.update(dt)

        # Run the drawing loop
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000  # Run at a max FPS of 60


if __name__ == "__main__":
    main()
