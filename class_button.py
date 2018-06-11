import pygame
from pygame.locals import *


class Button(pygame.sprite.Sprite):
    def __init__(self, imageFile, screen_size, buttonScale, position):
        # Sets sprite stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()

        # Scaling the sprite:
        self.new_scale = (round(self.rect.width * buttonScale),
                          round(self.rect.height * buttonScale))
        self.image = pygame.transform.scale(self.image, self.new_scale)
        self.rect = self.image.get_rect()

        # Gets screen dimensions:
        screen_width, screen_height = screen_size

        # Checks for the position to display the button:
        if position != "":
            if position == "screen_center":
                # Puts the text on the center of the screen:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 - self.rect.height/2)
            if position == "center_top":
                # Puts the text on the center of the screen:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 - self.rect.height)
            if position == "center_top2":
                # Puts the text on the center of the screen:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 - self.rect.height*2)
            if position == "center_top3":
                # Puts the text on the center of the screen:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 - self.rect.height*3)
            if position == "center_top4":
                # Puts the text on the center of the screen:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 - self.rect.height*4)
            if position == "center_top5":
                # Puts the text on the center of the screen:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 + self.rect.height*5)
            if position == "center_bottom":
                # Puts the text on the center of the screen:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2)
            if position == "center_bottom2":
                # Puts the text on the center of the screen:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 + self.rect.height)
            if position == "center_bottom3":
                # Puts the text on the center of the screen:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 + self.rect.height*2)
            if position == "center_bottom4":
                # Puts the text on the center of the screen:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 + self.rect.height*3)
            if position == "center_bottom5":
                # Puts the text on the center of the screen:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 + self.rect.height*4)

        self.buttonPosition = buttonPosition
        self.rect.x, self.rect.y = buttonPosition

    def setPosition(self, position):
        self.rect.x, self.rect.y = position

    def buttonClick(self):
        # Gets mouse position:
        mousePosition = pygame.mouse.get_pos()

        # Checks if mouse is within button area:
        if mousePosition[0] >= self.rect.x and mousePosition[0] <= self.rect.x + self.rect.width:
            if mousePosition[1] >= self.rect.y and mousePosition[1] <= self.rect.y + self.rect.height:

                return True
