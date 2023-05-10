import pygame

class Rocket:

    def __init__(self, rg_game):
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.screen_rect = rg_game.screen.get_rect()

        self.image = pygame.image.load('alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update rocket's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom > 0:
            self.y += self.settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw ship at its current location."""
        self.screen.blit(self.image, self.rect)