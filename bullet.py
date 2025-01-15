import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        """bullet near ship """
        super().__init__()
        self.screen = screen

        #create and set
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #position
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """up"""
        self.y -= self.speed_factor
        self.rect.y = int(self.y)

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)