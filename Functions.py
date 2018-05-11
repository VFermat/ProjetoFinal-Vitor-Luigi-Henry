# -*- coding: utf-8 -*-
"""
Created on Fri May 11 07:50:27 2018

@author: Vitor Eller
"""
import pygame
from pygame.locals import *

def displayTopRight_two(text, variable1, variable2, screen):
    font = pygame.font.SysFont("None", 36)  # Declares the font to be used by the text
    text = font.render(text.format(variable1, variable2), True, (255, 255, 255))  # Renders the text by the font chosen before
    text_posX, text_posY, text_lenght, text_height = text.get_rect()  # Gets dimensions of the text
    screen.blit(text, (0, 0))  # Sticks the text to the middle of the screen