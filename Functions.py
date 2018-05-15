import pygame
import math
from pygame.locals import *

def displayWinnerText(text, winner, screen):
    # Declares the font to be used by the text
    font = pygame.font.SysFont("None", 55)
    # Renders the text by the font chosen before
    text = font.render(text.format(winner), True, (182, 38, 37))
    # Gets dimensions of the text
    text_posX, text_posY, text_lenght, text_height = text.get_rect()
    # Sticks the text to the middle of the screen
    screen.blit(text, (640, 320))

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


def get_angle(origin, destination):
    # Finds the angle between two points:
    x_dist = destination[0] - origin[0]
    y_dist = destination[1] - origin[1]
    return math.atan2(-y_dist, x_dist) % (2 * math.pi)


def get_distance(origin, destination):
    # Checks if x2 > x1:
    if destination[0] >= origin[0]:
        # Pythagoras Theorem to find distance between two points:
        x_dist = destination[0] - origin[0]
        y_dist = destination[1] - origin[1]
        distance = ((x_dist)**2 + (y_dist)**2)**(1/2)
        return distance
    # Checks if x2 < x1:
    elif destination[0] <= origin[0]:
        # Pythagoras Theorem to find distance between two points:
        x_dist = origin[0] - destination[0]
        y_dist = origin[1] - destination[1]
        distance = ((x_dist)**2 + (y_dist)**2)**(1/2)
        return distance


def reset_projectile(group, default_projectile):
    # Sets the projectile to the default projectile:
    projectile = default_projectile
    # Clears the projectile group:
    group.empty()
    # Adds the default projectile to the group:
    group.add(default_projectile)

    return group, projectile


def get_projectileStats(screen, player_1, player_2, playerTurn, projectile):
    # Checks if it is player's 1 turn:
    if playerTurn == "1":
        # Gets mouse current position:
        mouse_position = pygame.mouse.get_pos()
        # Gets player current center coordinates:
        player_1_center = player_1.rect.center
        # Gets angle between player's sprite center and mouse position, converts
        # it to degrees and rounds it:
        mouse_angle = math.degrees(get_angle(player_1_center, mouse_position))
        mouse_angle = round(mouse_angle)
        # Draws a line between the player's center and the mouse position:
        pygame.draw.line(screen, (0, 0, 0), player_1_center, mouse_position, 4)

        # Checks if the projectile if moving, if not it then changes it's
        # attributes every function call:
        if projectile.moving == False:
            # Gets the distance between player's sprite center and mouse
            # position, and rounds it:
            distancePlayerMouse = get_distance(player_1_center, mouse_position)/2
            distancePlayerMouse = round(distancePlayerMouse)

            projectile.speed = distancePlayerMouse
            projectile.angle = mouse_angle

            if projectile.speed > projectile.max_speed:
                projectile.speed = projectile.max_speed

    # Checks if it is player's 1 turn:
    if playerTurn == "2":
        # Gets mouse current position:
        mouse_position = pygame.mouse.get_pos()
        # Gets player current center coordinates:
        player_2_center = player_2.rect.center
        # Gets angle between player's sprite center and mouse position, converts
        # it to degrees and rounds it:
        mouse_angle = math.degrees(get_angle(player_2_center, mouse_position))
        mouse_angle = round(mouse_angle)
        # Draws a line between the player's center and the mouse position:
        pygame.draw.line(screen, (0, 0, 0), player_2_center, mouse_position, 4)

        # Checks if the projectile if moving, if not it then changes it's
        # attributes every function call:
        if projectile.moving == False:
            # Gets the distance between player's sprite center and mouse
            # position, and rounds it:
            distancePlayerMouse = get_distance(player_2_center, mouse_position)/2
            distancePlayerMouse = round(distancePlayerMouse)

            projectile.speed = distancePlayerMouse
            projectile.angle = mouse_angle

            if projectile.speed > projectile.max_speed:
                projectile.speed = projectile.max_speed
