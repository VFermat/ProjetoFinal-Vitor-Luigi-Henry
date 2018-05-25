# -*- coding: utf-8 -*-
"""
Created on Thu May 24 08:58:11 2018

@author: Vitor Eller
"""

import pygame
import random
import math

class Terrain:
    
    black = (0, 0, 0)
    
    def __init__(self, background_rect, rect_height, s=35):
        self.rect = background_rect
        # maxHeight sets that the maximum of the terrain column to half of the background height
        self.maxHeight = round(rect_height*random.uniform(1, 2)/2)
        self.smoothFactor = s
        self.ter = self.generateTerrain()
        self.changed = True
        
    def generateTerrain(self):
        
        # Generates a different height for each width in the background rect
        heights = [random.randint(1, self.maxHeight) for p in range(self.rect.width)]
        for i in range(len(heights)):
            # Randomizes the Height a bit more
            heights[i] += round(math.sin(6 * math.pi / len(heights) * i) * 30)
        
        # Smoothes the Terrain
        # This loop sets the amount of times you will run the smoothen alrogithm
        for i in range(self.smoothFactor):
            # This loop smoothes the terrain by averaging the column with its adjacents columns
            for n in range(2, len(heights) - 1):
                heights[n] = sum(heights[n - 2: n + 3])/5       
        # Since we coulnd't average heights[0], heights[1] and heights[-1] we do it outside of the loop
        heights[0] = sum(heights[0: 5])/5
        heights[1] = sum(heights[0: 5])/5
        heights[len(heights) - 1] = sum(heights[len(heights) - 5: len(heights)])/5
        
        s_height = self.rect.height
        s_width = self.rect.width
        pixel_array = [[] for e in range(s_width)]
        for e in range(s_width):
            for h in range(s_height):
                h_difference = s_height - heights[e]
                if h < h_difference:
                    pixel_array[e].append(0)
                else:
                    pixel_array[e].append(1)
                    
        return pixel_array
    
    def drawTerrain(self, screen, picture):
        
        for width in range(len(self.ter)):
            for height in range(len(self.ter[width])):
                if self.ter[width][height] == 1:
                    #pygame.draw.rect(screen, self.black, pygame.Rect(width, height, 1, 1))
                    screen.blit(picture, (width, height))