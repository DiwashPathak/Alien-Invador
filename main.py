#main.py
import pygame
from player import Player
import gamefunctions as gf
from settings import Settings
from pygame.sprite import Group


# Intalize pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))
# Setting title of game
pygame.display.set_caption("Space Attack")
# Setting our icon
icon = pygame.image.load("images/player.png")
pygame.display.set_icon(icon)   

# Creating settings object
all_settings = Settings()

# Creating our player object
player = Player(screen)

# Background
background = pygame.image.load("images/background.png").convert_alpha()

# Creating enemy object
enemies = Group()

# Bullet object
bullets = Group()


# Adding enemy to enemies Group
gf.make_enemies(enemies, all_settings, screen)

# Setting score
# score_value = 0
# font = pygame.font.Font('freesansbold.ttf' , 32 )


while True:

    # Checking recent events
    gf.check_events(player, bullets, screen)

    # Move our ship according to instruction of moving_right/left 
    player.move_ship(all_settings)
    
    # Filling screen with background
    screen.blit(background, (0, 0))

    # Rendering Font 
    # score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    # screen.blit(score, (20, 10))
    
    # Draw bullet
    gf.bullet_operations(bullets, all_settings)
    
    # Detect collision
    gf.detect_collision(bullets  , enemies)

    # Drawing player to screen
    player.draw_player()

    # Draw enemies 
    gf.enemy_operations(enemies, all_settings)

    # Updating screen
    pygame.display.flip()