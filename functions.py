import pygame
import math
from pygame.locals import *


def getBombStats(bomb, player, mousePosition):
    # Sets the bomb starting position as the player's center:
    bomb.rect.x, bomb.rect.y = player.rect.center
    bomb.startx, bomb.starty = player.rect.center

    # Gets angle between player's sprite center and mouse position:
    bomb.angle = get_angle(player.rect.center, mousePosition, "degrees")

    # Gets the distance between player's sprite center and mouse position:
    bomb.speed = get_distance(player.rect.center, mousePosition)

    # Checks if the speed is above the bomb's speed limit:
    if bomb.speed > bomb.maxSpeed:
        bomb.speed = bomb.maxSpeed

    # Sets the bomb as moving:
    bomb.moving = True


def get_angle(origin, destination, type):
    if type == "degrees":
        # Finds the angle between two points:
        x_dist = destination[0] - origin[0]
        y_dist = destination[1] - origin[1]

        angle = math.atan2(-y_dist, x_dist) % (2 * math.pi)

        return math.degrees(angle)
    else:
        # Finds the angle between two points:
        x_dist = destination[0] - origin[0]
        y_dist = destination[1] - origin[1]

        angle = math.atan2(-y_dist, x_dist) % (2 * math.pi)

        return angle


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


def reset_bomb(group, default_bomb):
    # Sets the bomb to the default bomb:
    bomb = default_bomb
    # Clears the bomb group:
    group.empty()
    # Adds the default bomb to the group:
    group.add(default_bomb)

    return group, bomb
