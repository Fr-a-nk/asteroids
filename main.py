import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event

def main():
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)  
    Asteroid.containers = (asteroids, updatable, drawable) 
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)  


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game Loop
    while True:
        log_state()
        
        # Pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
    
        screen.fill("black")

 




        
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        for thing in drawable:
            thing.draw(screen)

        # asteroids
        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for ast in asteroids:
            for shot in shots:
                if ast.collides_with(shot):
                    log_event("asteroid_shot")
                    ast.split()
                    shot.kill()
        

        # End of Game Loop
        pygame.display.flip()

        


if __name__ == "__main__":
    main()
