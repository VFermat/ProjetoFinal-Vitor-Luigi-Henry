import pygame
import string
from pygame.locals import *

ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "


def textInputBox(name, COLOR, screen, screen_size, events, font, max_lenght=15):
    # Gets the screen size, so we can have the window's dimensions:
    screen_lenght, screen_height = screen_size

    # Getting player's name:
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return name
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.unicode in ACCEPTED:
                if len(name) < max_lenght:
                    name += event.unicode

    # Rendering player's name and getting its dimensions:
    player_name = font.render(name, True, COLOR)
    name_posX, name_posY, name_lenght, name_height = player_name.get_rect()
    namePosition = (screen_lenght/2 - name_lenght/2,
                    screen_height/2 - name_height)

    # Blitting the player Name
    screen.blit(player_name, namePosition)

    return name
