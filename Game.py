# -*- coding: utf-8 -*-
"""
Created on Thu May  3 21:59:22 2018

@author: Vitor Eller
"""

import projectile_class
import player
import pygame
import random
from pygame.locals import *

# ============= Initializing ============= 
pygame.init()

screen = pygame.display.set_mode((1664, 1040), 0, 32)
pygame.display.set_caption("WOOOORMS")

background = pygame.image.load("Sprites/background.png").convert()

player_1 = player.Player("Sprites/fox_1.png", random.randint(50, 150), 100)
player_2 = player.Player("Sprites/fox_2.png", random.randint(650, 750), 100)

player_group1 = pygame.sprite.Group()
player_group1.add(player_1)

player_group2 = pygame.sprite.Group()
player_group2.add(player_2)

# ===============   LOOPING PRINCIPAL   ===============
relogio = pygame.time.Clock()

running = True
turn = 1

while running:
    
    for event in pygame.event.get():  
        if event.type == QUIT:      
            running = False 
    

    if turn % 2 == 0: #Player_2 Turn
        launched = False
        projectile = projectile_class.Ball((1664, 1040), "Sprites/pokeball.png",
                                           player_2.rect.x, player_2.rect.y)
        while not launched:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_a]:
                player_2.move("left")
            elif pressed_keys[K_d]:
                player_2.move("right")
                
            projectile.update()
            if projectile.moving == True:
               launched = True
               
            screen.blit(background, (0, 0))
            player_group1.draw(screen)
            player_group2.draw(screen)
            pygame.display.update()
        
    elif turn % 2 == 1: #Player_1 Turn
        launched = False
        projectile = projectile_class.Ball((1664, 1040), "Sprites/pokeball.png",
                                           player_2.rect.x, player_2.rect.y)
        while not launched:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_a]:
                player_1.move("left")
            elif pressed_keys[K_d]:
                player_1.move("right")
                
            projectile.update()
            if projectile.moving == True:
               launched = True
               
            screen.blit(background, (0, 0))
            player_group1.draw(screen)
            player_group2.draw(screen)
            pygame.display.update()
            
            
        
    #Getting Responses
    screen.blit(background, (0, 0))
    player_group1.draw(screen)
    player_group2.draw(screen)
    pygame.display.update()
    #mudando o turno 
    turn += 1
    
pygame.display.quit()  
            
        
                
        
