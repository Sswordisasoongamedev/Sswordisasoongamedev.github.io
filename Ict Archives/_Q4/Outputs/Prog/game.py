import pygame
import sys
import random
import asyncio
import time
from typing import Tuple

# Initialize Pygame
pygame.init()
Coordinates = Tuple[int,int]
# Set up the screen
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("WIP GAME(Bullets)")
enemy:pygame.Rect
bullet:pygame.Rect
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
# Player
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height
player_speed = 15
bullet:pygame.Rect
# Bullets
bullet_width = 5
bullet_height = 15
bullet_height_backup = 15
bullet_speed = 10
bullets = []
text_x = int(0.7 * SCREEN_WIDTH)  # 70% of the screen width
text_y = 0  # Position at the top of the screen

bullet_color = YELLOW
#ENEMIES
enemy_width = 50
enemy_height = 40
enemy_speed = 1
enemy_y = 0
enemies = [] 
enemies_hp_list = [int]
# Clock
clock = pygame.time.Clock()
time_since_last_spawn = 0
spawn_interval = 3000
bullet_damage = 1
exp:float = 0
def make_enemy():
    enemies.append(pygame.Rect(random.randint(1,SCREEN_WIDTH - enemy_width),enemy_y,enemy_width,enemy_height))
    
total_spawned = 0 
# Main game loop
killed:int = 0 #type:int
def show_end_message():
    font = pygame.font.SysFont(None, 50,italic=True)
    game_over_text = font.render(f"Game over! You have passed: {total_spawned} and killed {killed}", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.key == pygame.K_q:
            sys.exit()
def printin(screen: pygame.Surface, Astr: str, size: int, pos: Coordinates, *args, **kwargs):
    font = pygame.font.SysFont(None, size=size, bold=False, italic=True)
    text = font.render(Astr, True, (255, 255, 255))  # Assuming WHITE is defined elsewhere
    text_rect = text.get_rect()
    text_rect.topleft = pos
    screen.blit(text, text_rect)

running = True

from pygame.event import Event
event:list[Event]
while running:
    # Handle events
    
    time_current = pygame.time.get_ticks()
    time_elapsed = time_current - time_since_last_spawn
    if time_elapsed >= spawn_interval:
        make_enemy()
        exp += .5
        time_since_last_spawn = time_current
        enemy_speed += total_spawned / 20
        total_spawned += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot a bullet when spacebar is pressed
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))
            if event.key == pygame.K_ESCAPE:
                running = False
            
            if bullet_color == WHITE:
                bullet_width = 1
                bullet_height = bullet_height_backup
                bullet_speed = 50
                bullet_damage = 1
            elif bullet_color == BLUE:
                 bullet_speed = 1
                 bullet_width = 10
                 bullet_height = 20
                 bullet_damage = 5
            elif bullet_color == RED:
                 bullet_height = SCREEN_HEIGHT
                 bullet_speed = 200
                 bullet_width = 5
                 bullet_damage = 20

            elif bullet_color == GREEN:
                 bullet_speed = 100
                 bullet_width = 1
                 bullet_height = 100
                 bullet_damage = 1000
            elif bullet_color == YELLOW:
                 bullet_speed = 100
                 bullet_width = 1
                 bullet_height = 100
                 bullet_damage = 100
    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed
    # Move player up
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y > SCREEN_HEIGHT - player_height:
        player_y += player_speed
    
    
    # Move bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
    for enemy in enemies:
       
        enemy.y +=  enemy_speed
    for bullet in bullets:
         for enemy in enemies:
              if bullet.colliderect(enemy):
                   #on kill:
                   bullets.remove(bullet)
                   enemies.remove(enemy)
                   
                   killed = killed + 1
                   exp += 1
            

    
    # Remove bullets that have gone off-screen
    bullets = [bullet for bullet in bullets if bullet.y > 0]
    bullet = []
    # Clear the screen
    screen.fill(BLACK)

    # Draw player
    player =pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    for enemy in enemies:
        # if got killed by enemy:
        if enemy.colliderect(player):
            print(f"Game over!\n you have passed: {total_spawned} and killed {killed}")
            
            show_end_message()
            running = False
    for enemy in enemies:
         pygame.draw.rect(screen,WHITE,enemy)
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)

    # Update display
    pygame.display.flip()

    if exp == 2:
        bullet_color = WHITE
    
    elif exp == 10:
        bullet_color = BLUE
    elif exp == 20:
        bullet_color = RED
    elif exp == 40:
        bullet_color = YELLOW
    elif exp == 100:
        bullet_color = GREEN


# Call the printin function to print the text at the specified position
    printin(screen, f"{exp}", 100, (text_x, text_y))
    # Cap the frame rate
    clock.tick(60)
    
# Quit Pygame
pygame.quit()
