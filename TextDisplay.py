import pygame
import math
from pygame.locals import *

# ============= Game Loop Functions =============
def displayTopLeft_two(text, variable1, variable2, screen):
    # Declares the font to be used by the text
    font = pygame.font.SysFont("None", 25)
    # Renders the text by the font chosen before
    text = font.render(text.format(variable1, variable2), True, (0, 0, 0))
    # Gets dimensions of the text
    text_posX, text_posY, text_lenght, text_height = text.get_rect()
    # Sticks the text to the middle of the screen
    screen.blit(text, (0, 0))


def displayTopRight_two(text, variable1, variable2, screen, screen_size):
    # Declares the font to be used by the text
    font = pygame.font.SysFont("None", 25)
    # Renders the text by the font chosen before
    text = font.render(text.format(variable1, variable2), True, (0, 0, 0))
    # Gets dimensions of the text
    text_posX, text_posY, text_lenght, text_height = text.get_rect()
    # Sticks the text to the middle of the screen
    screen.blit(text, (screen_size[0] - text_lenght, 0))


def displayHeath(player, screen_size, screen):
    # Declares the font to be used by the text
    font = pygame.font.SysFont("None", 20)
    # Renders the text by the font chosen before
    text = font.render("Health: {0}".format(player.health), True, (0, 0, 0))
    # Gets dimensions of the text
    text_posX, text_posY, text_lenght, text_height = text.get_rect()
    # Centers the text on top of the sprite:
    text_position = (player.rect.x + player.rect.width/2 - text_lenght/2,
                     player.rect.y - text_height)
    # Sticks the text to the middle of the screen
    screen.blit(text, text_position)


def displayChosenBomb(projectilesDisplay, projectile, screen, screen_size):
    # Declares the font to be used by the text
    font = pygame.font.SysFont("None", 16)
    # Renders the text by the font chosen before
    text = font.render("Selected", True, (0, 0, 0))
    # Gets dimensions of the text
    text_posX, text_posY, text_lenght, text_height = text.get_rect()

    if projectile.name == "pokeball":
        # Centers the text below the projectiles display bar:
        text_position = (projectilesDisplay.rect.x +
                         projectilesDisplay.rect.width/4 - text_lenght/2,
                         projectilesDisplay.rect.y + projectilesDisplay.rect.height)
    elif projectile.name == "purpleball":
        # Centers the text below the projectiles display bar:
        text_position = (projectilesDisplay.rect.x +
                         projectilesDisplay.rect.width/4*3 - text_lenght/2,
                         projectilesDisplay.rect.y + projectilesDisplay.rect.height)

    # Sticks the text to the middle of the screen
    screen.blit(text, text_position)

# ============= Winner Screen Functions =============
def displayWinnerText(text, winner, screen, screen_size):
    # Declares the font to be used by the text
    font = pygame.font.SysFont("None", 55)
    # Renders the text by the font chosen before
    text1 = font.render(text[0].format(winner), True, (182, 38, 37))
    text2 = font.render(text[1], True, (182, 38, 37))
    text3 = font.render(text[2], True, (182, 38, 37))
    # Gets the size of the screen
    screen_length = screen_size[0]
    screen_height = screen_size[1]
    # Gets dimensions of the text
    text_posX1, text_posY1, text_lenght1, text_height1 = text1.get_rect()
    text_posX2, text_posY2, text_lenght2, text_height2 = text2.get_rect()
    text_posX3, text_posY3, text_lenght3, text_height3 = text3.get_rect()
    # Sticks the text to the middle of the screen
    screen.blit(text2, 
                (screen_length/2 - text_lenght2/2, screen_height/2 - text_height2/2))
    screen.blit(text1, 
                (screen_length/2 - text_lenght1/2, screen_height/2 - text_height2/2 - text_height1))
    screen.blit(text3,
                (screen_length/2 - text_lenght3/2, screen_height/2 + text_height2/2))