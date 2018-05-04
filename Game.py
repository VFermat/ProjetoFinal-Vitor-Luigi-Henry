# -*- coding: utf-8 -*-
"""
Created on Thu May  3 21:59:22 2018

@author: Vitor Eller
"""

import projectile_class
import player
import pygame
import random

# ============= Initializing ============= 
pygame.init()

screen = pygame.display.set_mode((1664, 1040), 0, 32)
pygame.display.set_caption("WOOOORMS")

background = pygame.image.load("Sprite/background.png").convert()

player_1 = player.Player("Sprites/fox_1.png", random.randint(50, 150), 100)
player_2 = player.Player("Sprites/fox_2.png", random.randint(650, 750), 100)

player_group = pygame.sprite.Group()
player_group.add(player_1)
player_group.add(player_2)

# ===============   LOOPING PRINCIPAL   ===============
relogio = pygame.time.Clock()

running = True
turn = 1

while running:
    
    for event in pygame.event.get():  
        if event.type == QUIT:      
            running = False 
    
    pressed_keys = pygame.key.get_pressed()
    if turn % 2 == 0: #Player_2 Turn
        while not pressed_keys[K_SPACE]:
            if pressed_keys[K_a]:
                player_2.move("left")
            elif pressed_keys[K_d]:
                player_2.move("right")
            projectile = projectile_class.Ball((1664, 1040), "Sprites/pokeball.png",
                                           player_2.rect.x, player_2.rect.y)
            if pressed_keys[K_q]:
                projectile.speed -= 5
            elif pressed_keys[K_e]:
                projectile.speed += 5
            elif pressed_keys[K_w]:
                projectile.angle += 5
            elif pressed_keys[K_s]:
                projectile.angle -= 5
                
        projectile.moving = True
        projectile.move()
        
    elif turn % 2 == 1: #Player_1 Turn
        while not pressed_keys[K_SPACE]:
            if pressed_keys[K_a]:
                player_1.move("left")
            elif pressed_keys[K_d]:
                player_1.move("right")
            projectile = projectile_class.Ball((1664, 1040), "Sprites/pokeball.png",
                                           player_2.rect.x, player_2.rect.y)
            if pressed_keys[K_q]:
                projectile.speed -= 5
            elif pressed_keys[K_e]:
                projectile.speed += 5
            elif pressed_keys[K_w]:
                projectile.angle += 5
            elif pressed_keys[K_s]:
                projectile.angle -= 5
                
        projectile.moving = True
        projectile.move()
        
    #Getting Responses
    screen.blit(background, (0, 0))
    player_group.draw(screen)
    pygame.display.update()
    #mudando o turno 
    turn += 1
    
pygame.display.quit()  
            
        
                
        
