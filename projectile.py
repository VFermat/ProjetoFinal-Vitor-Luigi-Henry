import pygame
import math
from pygame.locals import *


class Projectile(pygame.sprite.Sprite):

    def __init__(self, screen_size, imageFile, posx, posy):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()

        # Screen size:
        self.screen_w, self.screen_h = screen_size

        # Sprite size:
        self.width, self.height = self.image.get_size()

        # Sprite center:
        self.center = (self.rect.x + self.width / 2, self.rect.y + self.height / 2)

        # Sets initial position:
        self.rect.x = posx
        self.rect.y = posy

        # Sets initial speed and angle, startx and starty:
        self.speed = 0
        self.angle = 0
        self.startx = 0
        self.starty = 0

        # Sets movement:s
        self.moving = False

        # Sets time:
        self.time = 0

    def move(self):
        velocity_x = math.cos(math.radians(self.angle)) * self.speed  # Calculates Vx
        velocity_y = math.sin(math.radians(self.angle)) * self.speed  # Calculates Vy

        distance_x = velocity_x * self.time  # Calculates total distance traveled on X axis
        distance_y = (velocity_y * self.time) + ((-9.81 * (self.time ** 2)) / 2)  # Calculates total distance traveled on Y axis

        new_x = round(self.startx + distance_x)  # Calculates new coord on X axis
        new_y = round(self.starty - distance_y)  # Calculates new coord on Y axis

        self.time += 0.1  # Adds to the object time

        if new_y <= self.screen_h - self.height:  # Checks if the sprite is above the window's bottom, if so:
            self.rect.x = new_x
            self.rect.y = new_y
        else:
            self.moving = False
            self.time = 0
            self.rotate_angle = 0
            self.rect.y = self.screen_h - self.height

    def calculateCenter(self):
        # Calculates sprite center:
        self.center = (self.rect.x + self.width / 2, self.rect.y + self.height / 2)

    def checkPressedKeys(self, event):
        if event.key == pygame.K_UP:
            if self.moving == False:  # Checks is the ball is moving, if not:
                self.angle += 5  # Adds to the ball angle
                if self.angle >= 360:  # Limits the angle to a maximum of 180
                    self.angle = 360
        if event.key == pygame.K_DOWN:  # Checks if pressed key is the down arrow
            if self.moving == False:  # Checks is the ball is moving, if not:
                self.angle -= 5  # Subtracts to the ball angle
                if self.angle <= 0:  # Limits the angle to a minimum of 0
                    self.angle = 0
        if event.key == pygame.K_LEFT:  # Checks if pressed key is the left arrow
            if self.moving == False:  # Checks is the ball is moving, if not:
                self.speed -= 5  # Subtracts to the ball speed
                if self.speed <= 0:  # Limits the speed to a minimum of 0
                    self.speed = 0
        if event.key == pygame.K_RIGHT:  # Checks if pressed key is the right arrow
            if self.moving == False:  # Checks is the ball is moving, if not:
                self.speed += 5  # Adds to the ball speed
                if self.speed >= 150:  # Limits the speed to a maximum of 150
                    self.speed = 150

    def update(self):
        if self.moving == True:  # Checks if the ball is moving, if so:
            self.move()  # Moves the ball once
