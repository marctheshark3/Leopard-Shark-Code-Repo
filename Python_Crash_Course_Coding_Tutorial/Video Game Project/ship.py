import pygame

class Ship:

    def __init__(self,ai_game):
        '''Initializing the ship and setting its start position'''

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #loading ship

        self.image = pygame.image.load('/Users/marctheshark/Documents/GitHub/Leopard-Shark-Code-Repo/Python_Crash_Course_Coding_Tutorial/Video Game Project/images/super_mario_rocket.bmp')
        self.rect = self.image.get_rect()

        #start with each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''draw the ship at its current location'''

        self.screen.blit(self.image, self.rect)