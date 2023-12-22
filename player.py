import pygame

class Player:
    def __init__(self, screen):
        # Making screen
        self.screen = screen

        # Loading image and making rectangle of it
        self.player_img = pygame.image.load("images/player.png")
        self.player_rect = self.player_img.get_rect()

        # Setting position of player
        self.player_rect.centerx = screen.get_rect().centerx
        self.player_rect.bottom = screen.get_rect().bottom

        # Set moving or not 
        self.moving_right = False
        self.moving_left = False
    
    def draw_player(self):
        self.screen.blit(self.player_img, self.player_rect)
    
    def move_ship(self, all_settings):
            if self.moving_right and self.player_rect.right < 800:
                self.player_rect.centerx += all_settings.player_speed
    
            elif self.moving_left and self.player_rect.left > 0:
                self.player_rect.centerx -= all_settings.player_speed