import pygame
from pygame.locals import *


class ActionBar(pygame.sprite.Sprite):

    def __init__(self, sprite, screen_size, spriteScale, position):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.rect = self.image.get_rect()

        # Scaling the sprite:
        self.new_scale = (round(self.rect.width * spriteScale),
                          round(self.rect.height * spriteScale))
        self.image = pygame.transform.scale(self.image, self.new_scale)
        self.rect = self.image.get_rect()

        # Sets screen size:
        self.screen_width, self.screen_height = screen_size
        self.screen_center = (self.screen_width/2, self.screen_height/2)

        if position != "":
            if position == "screen_center":
                # Puts the sprite on the center of the screen:
                self.rect.center = self.screen_center

            elif position == "top_center":
                # Puts the sprite on the center of the screen:
                self.rect.centerx = self.screen_width/2
                self.rect.y = 0

            elif position == "top_left":
                # Puts the sprite on the center of the screen:
                self.rect.x = 0
                self.rect.y = 0

            elif position == "top_right":
                # Puts the sprite on the center of the screen:
                self.rect.x = self.screen_width - self.rect.width
                self.rect.y = 0

            elif position == "bottom_center":
                # Puts the sprite on the center of the screen:
                self.rect.centerx = self.screen_width/2
                self.rect.y = self.screen_height - self.rect.height

            elif position == "bottom_left":
                # Puts the sprite on the center of the screen:
                self.rect.x = 0
                self.rect.y = self.screen_height - self.rect.height

            elif position == "bottom_right":
                # Puts the sprite on the center of the screen:
                self.rect.x = self.screen_width - self.rect.width
                self.rect.y = self.screen_height - self.rect.height

        self.slot1 = (self.rect.x + self.rect.width/5/2,
                      self.rect.y + self.rect.height/2)
        self.slot2 = (self.rect.x + self.rect.width/5/2 * 3,
                      self.rect.y + self.rect.height/2)
        self.slot3 = (self.rect.x + self.rect.width/5/2 * 5,
                      self.rect.y + self.rect.height/2)
        self.slot4 = (self.rect.x + self.rect.width/5/2 * 7,
                      self.rect.y + self.rect.height/2)
        self.slot5 = (self.rect.x + self.rect.width/5/2 * 9,
                      self.rect.y + self.rect.height/2)
