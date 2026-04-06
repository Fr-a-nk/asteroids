import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Game Loop
    while True:
        log_state()
        
        # Pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
    
        screen.fill("black")

        player.draw(screen)

        dt = clock.tick(60) / 1000
        # End of Game Loop
        pygame.display.flip()

        


if __name__ == "__main__":
    main()
