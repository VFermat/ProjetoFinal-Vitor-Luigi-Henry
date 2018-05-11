import pygame
from pygame.locals import *


def displayTopRight_two(text, variable1, variable2, screen):
    # Declares the font to be used by the text
    font = pygame.font.SysFont("None", 36)
    # Renders the text by the font chosen before
    text = font.render(text.format(variable1, variable2), True, (255, 255, 255))
    # Gets dimensions of the text
    text_posX, text_posY, text_lenght, text_height = text.get_rect()
    # Sticks the text to the middle of the screen
    screen.blit(text, (0, 0))


def reset_projectile(group, default_projectile):
    projectile = default_projectile
    group.empty()
    group.add(default_projectile)

    return group, projectile
