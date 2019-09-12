import pygame
import random
from pygame.sprite import Sprite
import random as rand
class Alien(Sprite):
    '''A class to represent a single alien in the fleet'''

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the alien image and setting the rect attribute

        self.image = pygame.image.load('/Users/marctheshark/Documents/GitHub/Leopard-Shark-Code-Repo/Python_Crash_Course_Coding_Tutorial/Video Game Project/images/alien.bmp')
        self.rect = self.image.get_rect()

        #set each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store each aliens position
        self.x = float(self.rect.x)

        #representing the firepower of aliens
        self.firepower = False

    def update(self):
        ''' move the aliens to the right or left'''

        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        ''' return true if alien is at edge of screen'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or screen_rect.left <= 0:
            return True

    def get_alien_weapons(self):
        """determine randomly which aliens will have the firepower"""
        # roughly 30 percent of aliens will have firepower
        firepower = random.randint(1,10)
        if firepower <= 5:
            return True
        else:
            return False

