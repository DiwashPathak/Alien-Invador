#game_functions.py
#gamefunctions.py
import pygame
import sys
import math
from bullet import Bullet
from enemy import Enemy
from pygame import mixer

def check_events(player, bullets, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        # When any key is pressed
        elif event.type == pygame.KEYDOWN:
            # Check which key is pressed
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            
            elif event.key == pygame.K_LEFT:
                player.moving_left = True
            
            elif event.key == pygame.K_SPACE:
                if len(bullets) < 3:
                    new_bullet = Bullet(player, screen)
                    bullets.add(new_bullet)
                # Bullet sound
                bullet_sound = mixer.Sound('sounds/laser.wav')
                bullet_sound.set_volume(0.3)
                bullet_sound.play()
        
        # When key is leaved
        elif event.type == pygame.KEYUP:
            # Check which key is leaved
            if event.key == pygame.K_RIGHT:
                player.moving_right = False

            elif event.key == pygame.K_LEFT:
                player.moving_left = False

def detect_collision(bullets , enemies):
    # Setting 
    for enemy in enemies.sprites():
        enemy_x = enemy.enemyX
        enemy_y = enemy.enemyY

        for bullet in bullets.sprites():
             # Settings bullet x and y 
             bullet_x = bullet.bulletX
             bullet_y = bullet.bulletY
    
             # Calculating distance
             distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y) **2)
    
             # Check if collided
             if distance < 20:
                 enemy.set_enemy_y()
                 bullets.remove(bullet)
                 # Playing sound
                 explosion_sound = mixer.Sound('sounds/explosion.wav')
                 explosion_sound.set_volume(0.3)
                 explosion_sound.play()

                 
                

def bullet_operations(bullets, all_settings):
    # Draw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        bullet.move_bullet(all_settings)
        if bullet.bulletY < 0 :
            bullets.remove(bullet)

def make_enemies(enemies,  all_settings, screen):
    for i in range(all_settings.enemy_n):
        new_enemy = Enemy(screen)
        enemies.add(new_enemy)

def enemy_operations(enemies, all_settings):
    for enemy in enemies.sprites():
        enemy.draw_enemy()
        enemy.move_enemy(all_settings)