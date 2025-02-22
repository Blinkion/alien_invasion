import pygame

class Ship:

    def __init__(self,ai_settings,screen):
        """init ship"""
        self.screen = screen
        self.ai_settings = ai_settings

        #upload
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #include float
        self.center = float(self.rect.centerx)

        #moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """change the position by flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect
        self.rect.centerx = int(self.center)

    def blitme(self):
        """draw"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx