import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """alien person"""
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #init position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """draw"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = int(self.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True