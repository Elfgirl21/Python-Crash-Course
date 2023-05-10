import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets fired from ship."""

    def __init__(self, ai_game):
        """Create bullet object at ship's current position."""
        super().__init__() #inhert properly from Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        #Update the decimal position of bullet
        self.y -= self.settings.bullet_speed
        #Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect) #draw.rect() fills screen definded by bullect's rect with color stored
