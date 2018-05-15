import pygame
import math
from pygame.locals import *


class Projectile(pygame.sprite.Sprite):

    def __init__(self, screen_size, imageFile, name, posx, posy, damage, max_speed):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()

        # Projectile name:
        self.name = name

        # Screen size:
        self.screen_w, self.screen_h = screen_size

        # Sets initial position:
        self.rect.x = posx
        self.rect.y = posy

        # Sets initial speed and angle, startx and starty:
        self.speed = 0
        self.angle = 0
        self.startx = 0
        self.starty = 0

        # Sets movement:
        self.moving = False

        # Sets time:
        self.time = 0

        # Sets projectile damage:
        self.damage = damage
        
        # Sets the Max Speed for the projectile
        self.max_speed = max_speed

    def move(self):
        # Calculates Vx:
        velocity_x = math.cos(math.radians(self.angle)) * self.speed
        # Calculates Vy
        velocity_y = math.sin(math.radians(self.angle)) * self.speed

        # Calculates total distance traveled on X axis:
        distance_x = velocity_x * self.time
        # Calculates total distance traveled on Y axis:
        distance_y = (velocity_y * self.time) + ((-9.81 * (self.time ** 2)) / 2)

        # Calculates new coord on X axis:
        new_x = round(self.startx + distance_x)
        # Calculates new coord on Y axis:
        new_y = round(self.starty - distance_y)

        # Adds to the object time:
        self.time += 0.1

        # Checks if the sprite is above the window's bottom, if so:
        if new_y <= self.screen_h - self.rect.height\
                and new_x >= 0\
                and new_x <= self.screen_w - self.rect.width:
            self.rect.x = new_x
            self.rect.y = new_y
        else:
            self.moving = False
            self.time = 0
            self.rotate_angle = 0
            self.rect.y = self.screen_h - self.rect.height

    def stop_movement(self):
        # Stops the sprite movement and resets it's attributes:
        self.moving = False
        self.time = 0
        self.rotate_angle = 0
        self.rect.y = self.screen_h - self.rect.height

    def reset_stats(self):
        # Stops the sprite movement and resets it's attributes:
        self.moving = False
        self.time = 0
        self.rotate_angle = 0
        self.rect.x = 0
        self.rect.y = 0


    def update(self):
        if self.moving == True:  # Checks if the ball is moving, if so:
            self.move()  # Moves the ball once
