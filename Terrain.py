# -*- coding: utf-8 -*-
"""
Created on Thu May 24 08:58:11 2018

@author: Vitor Eller
"""

import pygame
import random
import math

class Terrain:
    
    def __init__(self, background_rect, rect_height, s=25):
        self.rect = background_rect
        # maxHeight sets that the maximum of the terrain column to half of the background height
        self.maxHeight = rect_height/2
        self.smoothFactor = s
        self.ter = self.generateTerrain()
        self.changed = True
        
    def generateTerrain(self):
        
        # Generates a different height for each width in the background rect
        heights = [random.choice(range(1, self.maxHeight)) for p in range(self.rect.width)]
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
        
        # Creates an Array for all the pixels on screen
        pixel_array = [[0 for e in range(self.rect.width)] for i in range(self.rect.height)]
        
        # Checks pixel by pixel, and if it is inside the Terrain, sets it to 1 (True)
        # Otherwise, sets it to 0 (False)
        for e in range(self.rect.width):
            for i in range(self.rect.height):
                if self.rect.height - e < heights[i]:
                    pixel_array[e][i] = 1
                else:
                    pixel_array[e][i] = 0
                    
        return pixel_array