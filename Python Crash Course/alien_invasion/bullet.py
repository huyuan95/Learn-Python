import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''a class to manage the bullets ejected by the ship'''

    def __init__(self, ai_settings, screen, ship):
        ''' create a bullet object in the ship position'''
        super(Bullet,self).__init__()
        self.screen = screen

        #create a rectangle to represent the bullet at (0,0) position
        #set the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store bullet position by float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''move bullet upward'''
        #update the float to represent bullet position
        self.y -= self.speed_factor
        #update bullet rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        '''draw the bullet on the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)
