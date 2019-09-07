import sys

import pygame

class AlienInvasion:
    '''Class to manage game assesst'''

    def __init__(self):
        ''' Start the game'''

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        ''' Start the main loop for the game'''

        while True:
            #watch keyboard and mouse for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    ''' Make a game instance, and run the game'''

    ai = AlienInvasion()
    ai.run_game()