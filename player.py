import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    # Player's health:
    health = 100

    def __init__(self, sprite, x_initial, y_initial):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()

        # Sets initial position:
        self.rect.x = x_initial
        self.rect.y = y_initial

    def move(self, direction):
        if direction == "right":
            self.rect.x += 5
        elif direction == "left":
            self.rect.x -= 5

    def getDamage(self, weapon_damage):
        self.health -= weapon_damage
