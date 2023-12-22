#enemy.py
import pygame
import random
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, screen):
        super().__init__()
        # making rectangle of the screen
        self.screen = screen

        # Loading enemy image and getting rectangle of it
        self.enemy = pygame.image.load("images/enemy.png").convert_alpha()
        self.enemy_rect = self.enemy.get_rect()

        # setting the position of the enemy
        self.enemyX = random.randint(0, 400)
        self.enemyY = random.randint(0, 150)

        # Move right or not
        self.move_right = True
    
    def draw_enemy(self):
        self.screen.blit(self.enemy, (self.enemyX, self.enemyY))
    
    def move_enemy(self, ai_settings):
        if self.move_right:
            self.enemyX += ai_settings.x_speed
            if self.enemyX >= 770:
                self.enemyY += ai_settings.y_speed
                self.move_right = False
        
        elif not self.move_right:
            self.enemyX -= ai_settings.x_speed
            if self.enemyX <= 0:
                self.enemyY += ai_settings.y_speed
                self.move_right = True
    
    def set_enemy_y(self):
        self.enemyY = 0