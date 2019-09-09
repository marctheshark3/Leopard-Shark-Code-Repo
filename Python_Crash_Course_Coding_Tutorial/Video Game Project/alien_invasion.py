import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    '''Class to manage game assesst'''

    def __init__(self):
        ''' Start the game'''

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        ''' Start the main loop for the game'''

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        ''' Respond to keypress and moust events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        ''' Updating for keydown events'''
        if event.key == pygame.K_RIGHT:
            # move the ship to the right
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        ''' Updating for keyup events'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''creates a new nullet and adds it to the bullets group'''
        if len(self.bullets) < self.settings.bullet_allowed:

            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        ''' Updating images on the screen and flip to the new screen'''
        # Redraw screen with for the background color
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # make the most recently drawn screen visible
        pygame.display.flip()

    def _update_bullets(self):
        ''' updating the position of the bullet
        and getting ride of those at the top of the screen'''
        #updating bullets position
        self.bullets.update()

        #remove the disappeared bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _create_fleet(self):
        '''creating the fleet of aliens!'''
        #creating an alien and find the number of of aliens in a row
        #spacing between each alien is the width of one alien
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        num_aliens_x = available_space_x // (2 * alien_width)

        #creating the first row
        for alien_num in range(num_aliens_x):
            self._create_alien(alien_num)

    def _create_alien(self,alien_num):
        # creating an alien and then placing it in a row
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_num
        alien.rect.x = alien.x
        self.aliens.add(alien)


if __name__ == '__main__':
    ''' Make a game instance, and run the game'''

    ai = AlienInvasion()
    ai.run_game()