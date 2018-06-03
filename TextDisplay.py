import pygame
from pygame.locals import *

RED = (182, 38, 37)
BLACK = (0, 0, 0)
pygame.font.init()

# ============= Game Loop Functions =============
def welcomeScreen(text, screen, screen_size, font):
    # Renders the text by the font chosen before
    text1 = font.render(text[0], True, RED)
    text2 = font.render(text[1], True, RED)
    # Gets the size of the screen
    screen_length = screen_size[0]
    screen_height = screen_size[1]
    # Gets dimensions of the text
    text_posX1, text_posY1, text_lenght1, text_height1 = text1.get_rect()
    text_posX2, text_posY2, text_lenght2, text_height2 = text2.get_rect()
    # Blits the text
    screen.blit(text1,
                (screen_length/2 - text_lenght1/2, screen_height/2 - text_height1))
    screen.blit(text2,
                (screen_length/2 - text_lenght2/2, screen_height/2))


# ============= Game Loop Functions =============
def displayTopLeft_two(text, variable1, variable2, screen, font):
    # Renders the text by the font chosen before
    text = font.render(text.format(variable1, variable2), True, BLACK)
    # Gets dimensions of the text
    text_posX, text_posY, text_lenght, text_height = text.get_rect()
    # Sticks the text to the middle of the screen
    screen.blit(text, (0, 0))


def displayTopRight_two(text, variable1, variable2, screen, screen_size, font):
    # Renders the text by the font chosen before
    text = font.render(text.format(variable1, variable2), True, BLACK)
    # Gets dimensions of the text
    text_posX, text_posY, text_lenght, text_height = text.get_rect()
    # Sticks the text to the middle of the screen
    screen.blit(text, (screen_size[0] - text_lenght, 0))


def displayHeathAndName(player, screen_size, screen, font):
# ===============   DISPLAY HEALTH   ===============
    # Renders the text by the font chosen before
    text = font.render("Health: {0}".format(player.health), True, BLACK)
    # Gets dimensions of the text
    text_posX, text_posY, text_lenght, text_height = text.get_rect()
    # Centers the text on top of the sprite:
    text_position = (player.rect.x + player.rect.width/2 - text_lenght/2,
                     player.rect.y - text_height)
    # Sticks the text to the middle of the screen
    screen.blit(text, text_position)
# ===============   DISPLAY NAME   ===============
    name = font.render("{0}".format(player.name), True, BLACK)
    # Gets dimensions of the text
    name_posX, name_posY, name_lenght, name_height = name.get_rect()
    # Centers the text on top of the sprite:
    name_position = (player.rect.x + player.rect.width/2 - name_lenght/2,
                     player.rect.y - text_height - name_height)
    # Blits the name
    screen.blit(name, name_position)

def displayChosenBomb(projectilesDisplay, projectile, screen, screen_size, font):
    # Renders the text by the font chosen before
    text = font.render("Selected", True, BLACK)
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
def displayWinnerText(text, winner, screen, screen_size, font):
    # Renders the text by the font chosen before
    text1 = font.render(text[0].format(winner), True, RED)
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