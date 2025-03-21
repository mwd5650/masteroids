import sys
import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (bullets, updateable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
       
        for asteroid in asteroids:
            if player.detect_collision(asteroid):
                print("Game Over!")
                sys.exit()
            for bullet in bullets:
                if bullet.detect_collision(asteroid):
                    asteroid.split()
                    bullet.kill()

        screen.fill("black")
        
        for actor in drawable:
            actor.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()