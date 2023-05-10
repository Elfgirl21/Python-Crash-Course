import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, sg_game): #ai_game current instance of the AlienInvasion class
        """Initialize the ship and set its starting position."""
        self.screen = sg_game.screen
        self.settings = sg_game.settings
        self.screen_rect = sg_game.screen.get_rect() #place ship in correct location

        #Load the ship image and get its rect.
        self.image = pygame.image.load('alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect() #rectangle - rect

        
        self.rect.left = self.screen_rect.left

        #store a decimal value for the ship's horiztonal position
        self.y = float(self.rect.y)

        #Movement flags
        self.moving_up = False
        self.moving_down = False
    
    def update(self): #not a helper method, called through instance of Ship
        """Update the ship's position based on the movement flag."""
        #Update the ship's x value, not the rect
        if self.moving_up and self.rect.top < self.screen_rect.top: 
            self.y += self.settings.ship_speed
        if self.moving_down and self.rect.bottom >= 0:
            self.y -= self.settings.ship_speed

       #Update rect object from self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y= float(self.rect.y)