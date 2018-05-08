# -*- coding: utf-8 -*-
"""
Created on Thu May 3 2018

@author: Henry Rocha, Vitor Eller, Luigi Portugal
"""

import projectile
import player
import pygame
import random
from pygame.locals import *

import os  # Import needed to center PyGame's window
os.environ['SDL_VIDEO_CENTERED'] = '1'  # Code to center PyGame window on the screen


def displayTopRight_two(text, variable1, variable2):
    font = pygame.font.SysFont("None", 36)  # Declares the font to be used by the text
    text = font.render(text.format(variable1, variable2), True, (255, 255, 255))  # Renders the text by the font chosen before
    text_posX, text_posY, text_lenght, text_height = text.get_rect()  # Gets dimensions of the text
    screen.blit(text, (0, 0))  # Sticks the text to the middle of the screen


def checkPressedKeys(event):
    if event.key == pygame.K_UP:
        if projectile.moving == False:  # Checks is the ball is moving, if not:
            projectile.angle += 1  # Adds to the ball angle
            if projectile.angle >= 360:  # Limits the angle to a maximum of 180
                projectile.angle = 360


# ============= Initializing =============
# PyGame initialization:
pygame.init()
pygame.font.init()
pygame.display.set_caption("Foxes")

# Screen settings:
screen_width, screen_height = 832, 520
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

# Setting up FPS:
clock = pygame.time.Clock()
framesPerSecond = 60

# Background settings:
background = pygame.image.load("Sprites/bg_mountains_832x520.png").convert()

# Player settings:
player_red = player.Player("Sprites/Fiona_Red_Right.png", random.randint(50, 150), 410)
player_yellow = player.Player("Sprites/Fiona_Blue_Left.png", random.randint(650, 750), 410)

player_group = pygame.sprite.Group()
player_group.add(player_red)
player_group.add(player_yellow)

# Projectile settings:
projectile_pokeball = projectile.Projectile(screen_size, "Sprites/pokeball.png", 0, 0)
projectile_purpleball = projectile.Projectile(screen_size, "Sprites/purple_ball_50x50.png", 0, 0)
projectile_group = pygame.sprite.Group()
projectile_group.add(projectile_pokeball)

# Variables:
done = None
playerTurn = "red"
projectile = projectile_pokeball

# ===============   LOOPING PRINCIPAL   ===============
running = True
while running:
    # Sets game FPS:
    time = clock.tick(framesPerSecond)

    # Checking for events:
    for event in pygame.event.get():  # Loops through game events
        if event.type == QUIT:  # If event is QUIT (Window close)
            running = False  # Sets playing state to false, thus quitting the main loop
        if event.type == pygame.KEYDOWN:
            projectile.checkPressedKeys(event)

            if event.key == pygame.K_1:
                projectile = projectile_pokeball
                if projectile_pokeball not in projectile_group:
                    projectile_group.remove(projectile_purpleball)
                    projectile_group.add(projectile_pokeball)

            if event.key == pygame.K_2:
                projectile = projectile_purpleball
                if projectile_purpleball not in projectile_group:
                    projectile_group.remove(projectile_pokeball)
                    projectile_group.add(projectile_purpleball)

    # Players turn:
    if playerTurn == "red":
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_a]:
            player_red.move("left")
        if pressed_keys[K_d]:
            player_red.move("right")
        if pressed_keys[K_SPACE]:
            if projectile.moving == False:
                projectile.rect.x, projectile.rect.y = player_red.rect.x, player_red.rect.y
                projectile.startx, projectile.starty = player_red.rect.x, player_red.rect.y
                projectile.moving = True
                done = False

        if done == False:
            if projectile.moving == False:
                projectile = projectile_pokeball
                playerTurn = "yellow"
                done = True

    if playerTurn == "yellow":
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_a]:
            player_yellow.move("left")
        if pressed_keys[K_d]:
            player_yellow.move("right")
        if pressed_keys[K_SPACE]:
            if projectile.moving == False:
                projectile.rect.x, projectile.rect.y = player_yellow.rect.x, player_yellow.rect.y
                projectile.startx, projectile.starty = player_yellow.rect.x, player_yellow.rect.y
                projectile.moving = True
                done = False

        if done == False:
            if projectile.moving == False:
                projectile = projectile_pokeball
                playerTurn = "red"
                done = True

    # Drawing stuff on the screen:
    screen.blit(background, (0, 0))
    player_group.draw(screen)
    displayTopRight_two("Speed: {0}, Angle: {1}", projectile.speed, projectile.angle)

    # Will only draw the projectile on the screen if it is moving:
    if projectile.moving == True:
        projectile_group.draw(screen)
        projectile.update()

    # Updates display:
    pygame.display.update()

# Quits the game:
pygame.display.quit()
