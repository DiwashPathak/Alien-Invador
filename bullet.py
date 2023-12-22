#bullet.py
import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):
    def __init__(self, player, screen):
        super().__init__()
        self.screen = screen
        self.bullet_img = pygame.image.load('images/bullet.png').convert_alpha()
        self.bulletX = player.player_rect.centerx - 15
        self.bulletY = 550
        
    def draw_bullet(self):
        self.screen.blit(self.bullet_img, (self.bulletX, self.bulletY))
    
    def move_bullet(self, all_settings):
        # Bring bullet upwards
        self.bulletY -= all_settings.bullet_speed