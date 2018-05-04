import pygame
import math
from pygame.locals import *


class Ball(pygame.sprite.Sprite):

    def __init__(self, screen_size, imageFile, posx, posy):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.original_image = self.image  # Saving the original image orientation
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
        self.rotation_angle = 0

    def move(self):
        velocity_x = math.cos(math.radians(self.angle)) * self.speed  # Calculates Vx
        velocity_y = math.sin(math.radians(self.angle)) * self.speed  # Calculates Vy

        distance_x = velocity_x * self.time  # Calculates total distance traveled on X axis
        distance_y = (velocity_y * self.time) + ((-9.81 * (self.time ** 2)) / 2)  # Calculates total distance traveled on Y axis

        new_x = round(self.startx + distance_x)  # Calculates new coord on X axis
        new_y = round(self.starty - distance_y)  # Calculates new coord on Y axis

        self.time += 0.1  # Adds to the object time

        if new_y <= self.screen_h - self.height:  # Checks if the sprite is above the window's bottom, if so:
            if new_x > 0 and new_x < self.screen_w - self.width:  # Checks if the sprite is within the window's borders on the X axis, if so:
                self.rect.x = new_x
                self.rect.y = new_y
            else:
                if new_x > self.screen_w - self.width:  # Checks if the sprite went over the screen right border, if so:
                    self.rect.x = self.screen_w - self.width
                    self.rect.y = new_y
                else:
                    self.rect.x = 0
                    self.rect.y = new_y
        else:
            self.moving = False
            self.time = 0
            self.rotate_angle = 0
            self.rect.y = self.screen_h - self.height

    def reset(self):
        self.time = 0  # Resets the time attribute
        self.moving = False  # Sets moving attribute
        self.rect.x = self.screen_w / 2 - self.width / 2  # Moves the sprite to the bottom of the window
        self.rect.y = self.screen_h - self.height  # Moves the sprite to the bottom of the window

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, self.rotation_angle, 1)  # Rotates the image
        self.rect = self.image.get_rect(center=self.rect.center)  # Sets the rectangle to the new image

    def calculateCenter(self):
        # Calculates sprite center:
        self.center = (self.rect.x + self.width / 2, self.rect.y + self.height / 2)

    def checkPressedKeys(self):
        # Checking for pressed keys:
        pressed_keys = pygame.key.get_pressed()  # Gets pressed keys:
        if pressed_keys[K_r]:  # Checks if pressed key is the letter R
            self.reset()  # Resets the object variables
        if pressed_keys[K_SPACE]:  # Checks if pressed key is the space bar
            if self.moving == False:  # Checks is the ball is moving, if not:
                self.moving = True  # Sets moving to true, so it starts moving on the next loop
                self.startx, self.starty = self.rect.x, self.rect.y  # Sets starting position for the ball
        if pressed_keys[K_UP]:  # Checks if pressed key is the up arrow
            if self.moving == False:  # Checks is the ball is moving, if not:
                self.angle += 5  # Adds to the ball angle
                if self.angle >= 180:  # Limits the angle to a maximum of 180
                    self.angle = 180
        if pressed_keys[K_DOWN]:  # Checks if pressed key is the down arrow
            if self.moving == False:  # Checks is the ball is moving, if not:
                self.angle -= 5  # Subtracts to the ball angle
                if self.angle <= 0:  # Limits the angle to a minimum of 0
                    self.angle = 0
        if pressed_keys[K_LEFT]:  # Checks if pressed key is the left arrow
            if self.moving == False:  # Checks is the ball is moving, if not:
                self.speed -= 5  # Subtracts to the ball speed
                if self.speed <= 0:  # Limits the speed to a minimum of 0
                    self.speed = 0
        if pressed_keys[K_RIGHT]:  # Checks if pressed key is the right arrow
            if self.moving == False:  # Checks is the ball is moving, if not:
                self.speed += 5  # Adds to the ball speed
                if self.speed >= 150:  # Limits the speed to a maximum of 150
                    self.speed = 150

    def displayTopRight_two(self, text, variable1, variable2):
        font = pygame.font.SysFont("None", 36)  # Declares the font to be used by the text
        text = font.render(text.format(variable1, variable2), True, (255, 255, 255))  # Renders the text by the font chosen before
        text_posX, text_posY, text_lenght, text_height = text.get_rect()  # Gets dimensions of the text
        screen.blit(text, (0, 0))  # Sticks the text to the middle of the screen

    def update(self):
        #self.displayTopRight_two("Angle: {0} | Speed: {1}", self.angle, self.speed)
        self.checkPressedKeys()
        self.calculateCenter()

        if self.moving == True:  # Checks if the ball is moving, if so:
            self.move()  # Moves the ball once
        self.rotation_angle += 2  # Changes rotation_angle
        self.rotate()
