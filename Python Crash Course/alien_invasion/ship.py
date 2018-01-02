import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initiate the ship and set the initial position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the spaceship image and get the outer rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put the new ship in the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store float value in ship attitude center
        self.center = float(self.rect.centerx)

        # moving tag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """draw the ship on assigned position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """adjust ship position according to moving tag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect according to self.center
        self.rect.centerx = self.center

    def center_ship(self):
        """put the ship in the center bottom of the screen"""
        self.center = self.screen_rect.centerx
