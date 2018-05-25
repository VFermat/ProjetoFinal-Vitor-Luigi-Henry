# -*- coding: utf-8 -*-
"""
Created on Fri May 25 08:53:06 2018

@author: Vitor Eller
"""

import pygame
from sprites import dirt_scaled

class TerrainSprite(pygame.sprite.Sprite):
    
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = dirt_scaled
        self.rect = self.image.get_rect()
        
        self.rect.x = x_pos
        self.rect.y = y_pos