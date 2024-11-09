from constants import *

import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize FPS clock
    clock = pygame.time.Clock()
    dt = 0  # Delta time

    while True:
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000  # Run at a max FPS of 60


if __name__ == "__main__":
    main()
