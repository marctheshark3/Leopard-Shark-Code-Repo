import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):

    def __init__(self,ai_game):
        ''' Creating bullet class to manage the bullets fired'''

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #creating bullet rect at (0,0) and set its proper position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midbottom = ai_game.myalien.rect.midbottom

        #store the bullets position as a decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move the nullets up the screen"""

        #update the decimal position of the bullet
        self.y -= self.settings.bullet_speed

        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        '''' Draw the bullet'''

        pygame.draw.rect(self.screen, self.color, self.rect)


