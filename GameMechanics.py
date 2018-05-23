import pygame
import math


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


def reset_player(player_1, player_2):
    # Resseting Player 1
    player_1.health = 100
    player_1.rect.x = 10
    player_1.name = ""
    # Resseting Player 2
    player_2.rect.x = 1180
    player_2.health = 100
    player_2.name = ""


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
        mouse_angle = round(mouse_angle, 2)
        # Gets the distance between player's sprite center and mouse
        # position, and rounds it:
        distancePlayerMouse = get_distance(player_1_center, mouse_position)
        distancePlayerMouse = round(distancePlayerMouse)
        # Draws a line between the player's center and the mouse position:
        if distancePlayerMouse <= projectile.max_speed:
            pygame.draw.line(screen, (0, 0, 0), player_1_center, mouse_position, 4)
        else:
            pass
            
        # Checks if the projectile if moving, if not it then changes it's
        # attributes every function call:
        if projectile.moving == False:
            
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
        mouse_angle = round(mouse_angle, 2)
        # Gets the distance between player's sprite center and mouse
        # position, and rounds it:
        distancePlayerMouse = get_distance(player_2_center, mouse_position)
        distancePlayerMouse = round(distancePlayerMouse)
        # Draws a line between the player's center and the mouse position:
        if distancePlayerMouse <= projectile.max_speed:
            pygame.draw.line(screen, (0, 0, 0), player_2_center, mouse_position, 4)
        else:
            pass
        # Checks if the projectile if moving, if not it then changes it's
        # attributes every function call:
        if projectile.moving == False:
        
            projectile.speed = distancePlayerMouse
            projectile.angle = mouse_angle

            if projectile.speed > projectile.max_speed:
                projectile.speed = projectile.max_speed
