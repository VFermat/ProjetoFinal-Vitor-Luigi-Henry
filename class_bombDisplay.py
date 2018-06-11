import pygame
from pygame.locals import *


class BombDisplay(pygame.sprite.Sprite):

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
