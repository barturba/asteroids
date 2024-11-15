import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField

import pygame


def main():
    print("Starting asteroids!")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize FPS clock
    clock = pygame.time.Clock()
    dt = 0  # Delta time

    # Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable

    Shot.containers = (shots, updatable, drawable)

    # Initialize a Player object
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroidField = AsteroidField()

    while True:
        pygame.Surface.fill(screen, (0, 0, 0))

        # Run the update loop
        for sprite in updatable:
            sprite.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if asteroid.collided(player):
                print("Game over!")
                sys.exit(0)

        # Check for shot collisions
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collided(asteroid):
                    asteroid.split()
                    bullet.kill()

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
