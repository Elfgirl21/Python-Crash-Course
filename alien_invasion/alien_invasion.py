import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button

class AlienInvasion:
    """Overview class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings() 

        self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #create instance to store game stats
        # and scoreboard
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)

        self.ship = Ship(self) #instance of Ship, selfparamenter gives Ship to game resources
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #make play button
        self.play_button = Button(self, "play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
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

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #reset game settings
            self.settings.initialize_dynamic_settings()

            #reset game stats
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            #Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #Hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_p:
            self.stats.game_active = True
        elif event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False

    def _create_fleet(self):
        """Create fleet of aliens."""
        #make an alien and find number of aliens in a row
        #dpsving between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        num_aliens_x = available_space_x // (2 * alien_width)

        #Determine number of rows of aliens to fit on the screen
        ship_height = self.ship.rect.width
        available_space_y = (self.settings.screen_height -
                                (3 * alien_height) - ship_height)
        num_rows = available_space_y //(2 * alien_height)

        #create full fleet of aliens
        for row_num in range(num_rows):
            for alien_number in range(num_aliens_x):
                self._create_alien(alien_number, row_num)

    def _create_alien(self, alien_number, row_num): 
        #create alien and place it in the row
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
            self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        """Create new bullet and add it to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #Update bullet position
        self.bullets.update()

        #Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        #Remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values(): #making sure to score all hits
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens: #where individual aliens are destoryed - reason why this is here
            #Destory existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """check if fleet is at edge, then update positions of aliens in fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #look for aliens hitting the botto of screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to ship being hit by alien."""
        if self.stats.ships_left > 0:
            #decrement ships_left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #Create a new fleet and center ship
            self._create_fleet()
            self.ship.center_ship()

            #Pause
            sleep(0.5) #after updates to all game element but before drawn to screen. after function ends, update_screen will excute
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True) #make cursor vivble again when game is inactive


    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat this the same as if the ship got hit
                self._ship_hit()
                break

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #draw score info
        self.sb.show_score()

        #draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and ran the game
    ai = AlienInvasion()
    ai.run_game()