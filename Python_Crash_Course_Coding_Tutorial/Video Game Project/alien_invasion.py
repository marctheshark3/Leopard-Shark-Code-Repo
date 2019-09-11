import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from score_board import Scoreboard
class AlienInvasion:
    '''Class to manage game assesst'''

    def __init__(self):
        ''' Start the game'''

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #instance to store game stats
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, 'Play')



    def run_game(self):
        ''' Start the main loop for the game'''

        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


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

        elif event.key == pygame.K_p:
            self._restart_game()

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

        #draw score info
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

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
        self._check_bullet_alien_collision()


    def _check_bullet_alien_collision(self):
        '''response to impacts'''
        # check if any bullets hit the aliens
        # if so lets remove the bullet and alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            self.stats.score += self.settings.alien_points
            print('collide')
            self.sb.prep_score()
            print('reset score ')

        if not self.aliens:
            # destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()


    def _create_fleet(self):
        '''creating the fleet of aliens!'''
        #creating an alien and find the number of of aliens in a row
        #spacing between each alien is the width of one alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (3 * alien_width)
        num_aliens_x = available_space_x // (3 * alien_width)

        #determine how many rows we can add
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height ) - ship_height)
        num_rows = available_space_y // (2 * alien_height)

        #create the full fleet!
        for row_num in range(num_rows):
            for alien_num in range(num_aliens_x):
                self._create_alien(alien_num,row_num)

    def _create_alien(self,alien_num,row_num):
        # creating an alien and then placing it in a row
        alien = Alien(self)
        alien_width ,alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_num
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
        self.aliens.add(alien)

    def _update_aliens(self):
        '''Check if the fleet is at the edge
        and Update the position of the aliens in the fleet'''
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            #print('Ship hit!!!')
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        '''respond to the event of the fleet hitting the edge of the screen'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''drop the fleet and change its direction'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        '''response if ship is hit by alien'''
        if self.stats.ships_left > 0:
            # you lose a ship
            self.stats.ships_left -= 1

            # get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        '''see if there are any aliens on the bottom'''

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_play_button(self,mouse_pos):
        ''' start a new game when play is clicked'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self._restart_game()


    def _restart_game(self):
        # reset game stats

        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()


        # remove any of the bullets and aliens
        self.aliens.empty()
        self.bullets.empty()

        # create new fleet
        self._create_fleet()
        self.ship.center_ship()

        # hide mouse cursor
        pygame.mouse.set_visible(False)

if __name__ == '__main__':
    ''' Make a game instance, and run the game'''

    ai = AlienInvasion()
    ai.run_game()