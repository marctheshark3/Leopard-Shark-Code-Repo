import pygame

class Ship:

    def __init__(self,ai_game):
        '''Initializing the ship and setting its start position'''

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        #loading ship

        self.image = pygame.image.load('/Users/marctheshark/Documents/GitHub/Leopard-Shark-Code-Repo/Python_Crash_Course_Coding_Tutorial/Video Game Project/images/super_mario_rocket.bmp')
        self.rect = self.image.get_rect()

        #start with each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #value for ships horizontal position
        self.x = float(self.rect.x)


        #movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        '''updating ships position based on the movement flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            #self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            #self.rect.x -= 1
            self.x -= self.settings.ship_speed
        #update rect object from self.x
        self.rect.x = self.x



    def blitme(self):
        '''draw the ship at its current location'''

        self.screen.blit(self.image, self.rect)