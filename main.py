import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from player import Player
import constants


def main():
      # Initialize the game
      pygame.init()
      #dt = dt / 1000.0
      screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
      print(f"Starting Asteroids! \n Screen width: {constants.SCREEN_WIDTH} \n Screen height: {constants.SCREEN_HEIGHT}")
      clock = pygame.time.Clock()  # Create a Clock object to manage frame rate
      shots = pygame.sprite.Group()
      asteroids = pygame.sprite.Group()
      updatable = pygame.sprite.Group()
      drawable = pygame.sprite.Group()
      AsteroidField.containers = updatable
      asteroid_field = AsteroidField()
      Shot.containers = shots, updatable, drawable
      Asteroid.containers = asteroids, updatable, drawable
      Player.containers = updatable, drawable
      player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
      while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            dt = clock.tick(60) / 1000.0
            screen.fill((0, 0, 0))
            updatable.update(dt)
            # Check for collisions
            for asteroid in asteroids:
                if player.collide(asteroid):
                    print("Game Over!")
                    pygame.quit()
            for asteroid in asteroids:
                for shot in shots:
                    if shot.collide(asteroid):
                        asteroid.splitting()ls
                        
                        shot.kill()
                    # Handle collision (e.g., end game, reduce health, etc.)
            for sprite in drawable:
                sprite.draw(screen)
            pygame.display.flip()

if __name__ == "__main__":
    main()
