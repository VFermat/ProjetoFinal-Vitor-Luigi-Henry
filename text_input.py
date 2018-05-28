# -*- coding: utf-8 -*-

"""
Created on Thu May 20 2018

@author: Vitor Eller
"""

import pygame
import string
from pygame.locals import *

RED = (182, 38, 37)
BLACK = (0, 0, 0)
WHITE = (252, 252, 252)
<<<<<<< HEAD
=======
font_35 = pygame.font.SysFont("None", 35)
>>>>>>> f7eb39829f9ecf90d4eed08484a7c8178f758ea7

ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "

def textInputBox(name, screen, screen_size, events, turn, font, max_lenght=10):
    
    # Preparing the Screen
    screen.fill(BLACK)    
    
    # Rendering the basic texts
    if turn == 1:
        text1 = "Please Type Player 1's Name."
    else:
        text1 = "Please Type Player 2's Name."
    rendered_text1 = font_35.render(text1, True, RED)
    text2 = "Press Enter When You're Ready."
    rendered_text2 = font_35.render(text2, True, RED)
    
    # Gets the text rect, so we can center it to the screen
    screen_lenght = screen_size[0]
    screen_height = screen_size[1]
    
    text_posX1, text_posY1, text_lenght1, text_height1 = rendered_text1.get_rect()
    text_posX2, text_posY2, text_lenght2, text_height2 = rendered_text2.get_rect()
    
    # Blitting the basic texts on screen
    screen.blit(rendered_text1,
                (screen_lenght/2 - text_lenght1/2, screen_height/2 - text_height1))
    screen.blit(rendered_text2,
                (screen_lenght/2 - text_lenght2/2, screen_height/2))
    
    # Getting players name
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return name
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.unicode in ACCEPTED:
                if len(name) < max_lenght:
                    name += event.unicode
    
    # Rendering Player's name and getting its positions
    player_name = font_35.render(name, True, RED)
    name_posX, name_posY, name_lenght, name_height = player_name.get_rect()
    
    # Blitting the player Name
    screen.blit(player_name,
                (screen_lenght/2 - name_lenght/2, screen_height/2 + 100))
    
    return name
    
