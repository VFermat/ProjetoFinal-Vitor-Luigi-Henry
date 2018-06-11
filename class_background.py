import pygame
from pygame.locals import *


class Background(pygame.sprite.Sprite):

    def __init__(self, sprite, initial_x, initial_y):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Sets initial position:
        self.rect.x = initial_x
        self.rect.y = initial_y
