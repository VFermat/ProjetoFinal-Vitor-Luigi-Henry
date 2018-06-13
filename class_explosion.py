import pygame
from pygame.locals import *


class Explosion(pygame.sprite.Sprite):
    def __init__(self, explosionFrames):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)

        # Sprites of the explosion (list):
        self.explosionFrames = explosionFrames

        # Sets frames:
        self.totalFrames = len(self.explosionFrames)
        self.frame = -1
        self.displayNumber = 0

        # Sets initial sprite:
        self.image = self.explosionFrames[0]
        self.rect = self.image.get_rect()

    def animate(self, lastBombPosition):
        self.rect.center = lastBombPosition

        if self.frame in range(1, 4):
            self.displayNumber = 0

        elif self.frame in range(4, 7):
            self.displayNumber = 1

        elif self.frame in range(7, 10):
            self.displayNumber = 2

        elif self.frame in range(10, 13):
            self.displayNumber = 3

        elif self.frame in range(13, 16):
            self.displayNumber = 4

        elif self.frame in range(16, 19):
            self.displayNumber = 5

        elif self.frame in range(19, 22):
            self.displayNumber = 6

        elif self.frame in range(22, 25):
            self.displayNumber = 7

        elif self.frame in range(25, 28):
            self.displayNumber = 8

        elif self.frame in range(28, 31):
            self.displayNumber = 9

        elif self.frame in range(31, 34):
            self.displayNumber = 10

        elif self.frame in range(34, 37):
            self.displayNumber = 11

        if self.frame > 37:
            self.frame = -1

        self.frame += 1

        self.image = self.explosionFrames[self.displayNumber]
