import pygame
import math
from pygame.locals import *


class Projectiles_Display(pygame.sprite.Sprite):

    def __init__(self, screen_size, imageFile, posx, posy):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()

        # Screen size:
        self.screen_w, self.screen_h = screen_size

        # Sets initial position:
        self.rect.x = self.screen_w/2 - self.rect.width/2
        self.rect.y = 0
