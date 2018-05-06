import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):

    health = 100

    def __init__(self, sprite, x_initial, y_initial):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()

        # Sets initial position:
        self.rect.x = x_initial
        self.rect.y = y_initial

        # Gets sprite size:
        self.width, self.height = self.image.get_size()

    def move(self, direction):
        if direction == "right":
            self.rect.x += 1
        else:
            self.rect.x -= 1

    def getDamage(self, weapon_damage):
        self.health -= weapon_damage
