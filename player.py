# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 08:29:17 2018

@author: Vitor Eller
"""

import pygame

class Player(pygame.sprite.Sprite):
    
    health = 100
    
    def __init__(self, sprite, x_initial, y_initial):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()
        self.rect.x = x_initial
        self.rect.y = y_initial
        
    def move(self, direction):
        if direction == "right":
            self.rect.x += 1
        else:
            self.rect.x -= 1
        
    def getDamage(self, weapon_damage):
        self.health -= weapon_damage