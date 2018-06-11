import pygame
import random
from pygame.locals import *


class Block(pygame.sprite.Sprite):

    def __init__(self, sprite, scale):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()

        # Scaling the sprite:
        self.new_scale = (round(self.rect.width * scale),
                          round(self.rect.height * scale))
        self.image = pygame.transform.scale(self.image, self.new_scale)
        self.rect = self.image.get_rect()


class Terrain(pygame.sprite.Sprite):

    def __init__(self, sprite, scale, screen_size, smooth_factor):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()

        # Scaling the sprite:
        self.scale = scale
        self.new_scale = (round(self.rect.width * scale),
                          round(self.rect.height * scale))
        self.image = pygame.transform.scale(self.image, self.new_scale)
        self.rect = self.image.get_rect()

        self.original_width = self.rect.width
        self.original_height = self.rect.height

        self.screen_width, self.screen_height = 1260, 640

        self.terrain_group = pygame.sprite.Group()

        self.smooth_factor = smooth_factor

    def generateHeightsRandom(self, minHeight, maxHeight):
        # Gets the X position for each "block":
        widths = [width
                  for width in range(0, round(self.screen_width/self.original_width))]
        print("Len widths: ", len(widths))

        # Creates random heights for each "block":
        heights = [random.randint(minHeight, maxHeight)
                   for counter in widths]
        print("Len heights: ", len(heights))
        print(heights)

        for i in range(self.smooth_factor):
            for n in range(2, len(heights) - 3):
                heights[n] = sum(heights[n-2: n+3])/5

        for i in range(self.smooth_factor):
            heights[0] = sum(heights[:5])/5
            heights[1] = sum(heights[:5])/5
            heights[len(heights) - 3] = sum(heights[len(heights)-5:])/5
            heights[len(heights) - 2] = sum(heights[len(heights)-5:])/5
            heights[len(heights) - 1] = sum(heights[len(heights)-5:])/5

        heights = [int(i) for i in heights]

        counter = 0
        while counter < len(widths):
            if heights[counter] == 1:
                image = Block(self.sprite, self.scale)
                image.rect.x = counter * self.original_width
                image.rect.y = self.screen_height - self.original_height

                self.terrain_group.add(image)

            else:
                for i in range(1, heights[counter] + 1):
                    image = Block(self.sprite, self.scale)
                    image.rect.x = counter * self.original_width
                    image.rect.y = self.screen_height - self.original_height * i

                    self.terrain_group.add(image)

            counter += 1

    def generateHeightsPreset(self, preset):
        # Gets the X position for each "block":
        widths = [width
                  for width in range(0, round(self.screen_width/self.original_width))]
        print("Len widths: ", len(widths))

        # Creates random heights for each "block":
        if preset == 1:
            heights = [2, 2, 2, 3, 4, 5, 5, 6, 6, 6, 4, 3, 2, 1, 1, 1, 2, 2, 4, 4, 4, 5, 5, 6, 7, 5, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2]

        print("Len heights: ", len(heights))
        print(heights)
        counter = 0
        while counter < len(widths):
            if heights[counter] == 1:
                image = Block(self.sprite, self.scale)
                image.rect.x = counter * self.original_width
                image.rect.y = self.screen_height - self.original_height

                self.terrain_group.add(image)

            else:
                for i in range(1, heights[counter] + 1):
                    image = Block(self.sprite, self.scale)
                    image.rect.x = counter * self.original_width
                    image.rect.y = self.screen_height - self.original_height * i

                    self.terrain_group.add(image)

            counter += 1
