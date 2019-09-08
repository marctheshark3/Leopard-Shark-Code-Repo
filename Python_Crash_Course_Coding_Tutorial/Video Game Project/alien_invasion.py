import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Class to manage game assesst'''

    def __init__(self):
        ''' Start the game'''

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        #setting the background color
        self.backgr_color = (230,230,230)

    def run_game(self):
        ''' Start the main loop for the game'''

        while True:
            #watch keyboard and mouse for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw screen with for the background color
            self.screen.fill(self.settings.backgr_color)
            self.ship.blitme()

            #make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    ''' Make a game instance, and run the game'''

    ai = AlienInvasion()
    ai.run_game()