import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MAX_RADIUS
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
    pygame.font.init()
    my_font = pygame.font.SysFont('PT Sans', 32)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    
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
                print(f"Thanks for playing! Score: {int(score)}")
                return
            pass
    
        screen.fill("black")
        
        dt = clock.tick(60) / 1000
        score += 6 * dt
        updatable.update(dt)
        
        for thing in drawable:
            thing.draw(screen)

        # asteroids
        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print(f"Game over! Score: {int(score)}")
                sys.exit()
        
        for ast in asteroids:
            for shot in shots:
                if ast.collides_with(shot):
                    log_event("asteroid_shot")
                    score += (ast.radius / ASTEROID_MAX_RADIUS) * 7
                    ast.split()
                    shot.kill()
        
        text_surface = my_font.render(f"Score: {int(score)}", False, (255, 255, 255))
        screen.blit(text_surface, (SCREEN_WIDTH / 2 - text_surface.get_width() / 2, 30))

        # End of Game Loop
        pygame.display.flip()

        


if __name__ == "__main__":
    main()
