import pygame
from pygame.locals import *


class TextDisplay():

    def __init__(self):
        # Initializes font:
        pygame.font.init()

        # Declares the font to be used by the text
        self.font_56 = pygame.font.SysFont("None", 56)
        self.font_46 = pygame.font.SysFont("None", 46)
        self.font_36 = pygame.font.SysFont("None", 36)
        self.font_26 = pygame.font.SysFont("None", 26)
        self.font_16 = pygame.font.SysFont("None", 16)

    def setPosition(self, position, screen_size, text):
        # Gets screen dimensions:
        screen_width, screen_height = screen_size

        # Gets dimensions of the text
        text_posX, text_posY, text_lenght, text_height = text.get_rect()

        # Checks for the position to display the text:
        if type(position) is str:
            if position != "":
                if position == "screen_center":
                    # Puts the text on the center of the screen:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 - text_height/2)
                elif position == "center_top":
                    # Puts the text on the center of the screen:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 - text_height)
                elif position == "center_top2":
                    # Puts the text on the center of the screen:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 - text_height*2)
                    print("help")
                elif position == "center_top3":
                    # Puts the text on the center of the screen:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 - text_height*3)
                elif position == "center_bottom":
                    # Puts the text on the center of the screen:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2)
                elif position == "center_bottom2":
                    # Puts the text on the center of the screen:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 + text_height*2)
                elif position == "center_bottom3":
                    # Puts the text on the center of the screen:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 + text_height*3)
                elif position == "center_bottom4":
                    # Puts the text on the center of the screen:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 + text_height*4)
                elif position == "center_bottom5":
                    # Puts the text on the center of the screen:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 + text_height*5)
                elif position == "top_center":
                    # Puts the text centered on the top of the screen:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    0)
                elif position == "top_center2":
                    # Puts the text centered on the top of the screen:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    text_height)

        elif type(position) is tuple:
            textPosition = position

        return textPosition

    def displayTextMainMenu(self, text, COLOR, screen, screen_size, position):
        # Renders the text by the font chosen before
        text = self.font_56.render(text, True, COLOR)

        # Sets the text position:
        textPosition = self.setPosition(position, screen_size, text)

        # Sticks the text to the screen:
        screen.blit(text, textPosition)

    def displayHealthAndName(self, COLOR, player, screen, screen_size):
        # Gets screen dimensions:
        screen_width, screen_height = screen_size

        name = "{0}".format(player.name)
        health = "Health: {0}".format(player.health)

        # Renders the text by the font chosen before
        health = self.font_26.render(health, True, COLOR)
        # Gets dimensions of the text
        health_posX, health_posY, health_lenght, health_height = health.get_rect()
        healthPosition = (player.rect.centerx - health_lenght/2,
                          player.rect.centery - health_height*2 - 10)

        # Renders the text by the font chosen before
        name = self.font_26.render(name, True, (255, 255, 255))
        # Gets dimensions of the text
        name_posX, name_posY, name_lenght, name_height = name.get_rect()
        namePosition = (player.rect.centerx - name_lenght/2,
                        player.rect.centery - name_height*3 - 10)

        # Sticks the name to the screen:
        screen.blit(name, namePosition)
        # Sticks the health to the screen:
        screen.blit(health, healthPosition)

    def displayTextNameScreen(self, text, COLOR, screen, screen_size, position):
        # Renders the text by the font chosen before
        text = self.font_36.render(text, True, COLOR)

        # Sets the text position:
        textPosition = self.setPosition(position, screen_size, text)

        # Sticks the text to the screen:
        screen.blit(text, textPosition)

    def displayTextWinnerScreen(self, text, COLOR, screen, screen_size, position):
        # Renders the text by the font chosen before
        text = self.font_36.render(text, True, COLOR)

        # Sets the text position:
        textPosition = self.setPosition(position, screen_size, text)

        # Sticks the text to the screen:
        screen.blit(text, textPosition)

    def displayWhoWon(self, COLOR, winner, loser, screen, screen_size, position):
        # Creates the text string:
        text = "{0} has defeated {1}!".format(winner, loser)

        # Renders the text by the font chosen before
        text = self.font_36.render(text, True, COLOR)

        # Sets the text position:
        textPosition = self.setPosition(position, screen_size, text)

        # Sticks the text to the screen:
        screen.blit(text, textPosition)
        
    def displayDistance(self, COLOR, screen, distance, angle, mouse_position):
        # Creates the text string:
        text = "Distance: {0}".format(distance)
        text2 = "Angle: {0}".format(angle)
        
        # Renders the text by the font chosen before
        text = self.font_26.render(text, True, COLOR)
        text2 = self.font_26.render(text2, True, COLOR)
        text_2_x = mouse_position[0]
        text_2_y = mouse_position[1] + text2.get_rect()[3]
        text_2_pos = (text_2_x, text_2_y)
        
        # Blits the text:
        screen.blit(text, mouse_position)
        screen.blit(text2, text_2_pos)
        
    def displayMovementsLeft(self, COLOR, screen, movements_left):
        # Creates the text string:
        text = "Movimentos: {0}".format(movements_left)
        
        # Renders the text by the font chosen before
        text = self.font_26.render(text, True, COLOR)
        
        # Gets Position:
        textPosition = (0, 0)
        
        # Blits the text:
        screen.blit(text, textPosition)