from constants import *
from player import *

import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize FPS clock
    clock = pygame.time.Clock()
    dt = 0  # Delta time

    # Initialize a Player object
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        pygame.Surface.fill(screen, (0, 0, 0))

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000  # Run at a max FPS of 60


if __name__ == "__main__":
    main()
