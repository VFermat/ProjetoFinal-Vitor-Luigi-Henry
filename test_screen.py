# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:56:16 2018

@author: Vitor Eller
"""

import pygame
import Terrain
from pygame.locals import *

windowTitle = "Foxy"

black = (0, 0, 0)

background = pygame.image.load("Sprites/flat_background_1280x640.png")

pygame.init()
pygame.font.init()
pygame.display.set_caption(windowTitle)

# Screen settings:
screen_width, screen_height = 1280, 640
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size, 0, 32)
screen.blit(background, (0, 0))

dirt = pygame.image.load("Sprites/dirt.bmp")
pygame.transform.scale(dirt, (1, 1))

terrain = Terrain.Terrain(background.get_rect(), 640)

for width in range(len(terrain.ter)):
    for height in range(len(terrain.ter[width])):
        if terrain.ter[width][height] == 1:
#            position = (width, height)
#            screen.blit(dirt, position)
            pygame.draw.rect(screen, black, pygame.Rect(width, height, 1, 1))
         
running = True

while running == True:
    
    events = pygame.event.get()
    # Loops through game events
    for event in events:
        # If event is QUIT (Window close)
        if event.type == QUIT:
            running == False
        
    pygame.display.update()
            
pygame.display.quit()      
