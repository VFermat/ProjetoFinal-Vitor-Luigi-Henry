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
from Functions import displayTopRight_two, reset_projectile

import os  # Import needed to center PyGame's window
os.environ['SDL_VIDEO_CENTERED'] = '1'  # Code to center PyGame window on the screen

# ============= Initializing =============
# PyGame initialization:
pygame.init()
pygame.font.init()
pygame.display.set_caption("Foxes")

# Screen settings:
screen_width, screen_height = 1280, 640
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

# Setting up FPS:
clock = pygame.time.Clock()
framesPerSecond = 60

# Background settings:
background = pygame.image.load("Sprites/flat_background_1280x640.png").convert()

# Player settings:
player_1 = player.Player("Sprites/Fiona_Red_Right.png", random.randint(50, 150), 490)
player_2 = player.Player("Sprites/Fiona_Blue_Left.png", random.randint(650, 750), 490)

player_group = pygame.sprite.Group()
player_group.add(player_1)
player_group.add(player_2)

# Projectile settings:
projectile_pokeball = projectile.Projectile(screen_size, "Sprites/pokeball.png", 0, 0, 10)
projectile_purpleball = projectile.Projectile(screen_size, "Sprites/purple_ball_50x50.png", 0, 0, 15)
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
            if event.key == pygame.K_UP:
                projectile.change_angle("angle up")

            if event.key == pygame.K_DOWN:
                projectile.change_angle("angle down")

            if event.key == pygame.K_RIGHT:
                projectile.change_speed("speed up")

            if event.key == pygame.K_LEFT:
                projectile.change_speed("speed down")

            if event.key == pygame.K_1:
                projectile = projectile_pokeball
                projectile_group.empty()
                projectile_group.add(projectile_pokeball)

            if event.key == pygame.K_2:
                projectile = projectile_purpleball
                projectile_group.empty()
                projectile_group.add(projectile_purpleball)

    # Players turn:
    if playerTurn == "red":
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_a]:
            player_1.move("left")
        if pressed_keys[K_d]:
            player_1.move("right")
        if pressed_keys[K_SPACE]:
            if projectile.moving == False:
                projectile.rect.x, projectile.rect.y = player_1.rect.x, player_1.rect.y
                projectile.startx, projectile.starty = player_1.rect.x, player_1.rect.y
                projectile.moving = True
                done = False

        if done == False:
            if projectile.moving == False:
                projectile_group, projectile = reset_projectile(projectile_group, projectile_pokeball)
                playerTurn = "yellow"
                done = True

    if playerTurn == "yellow":
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_a]:
            player_2.move("left")
        if pressed_keys[K_d]:
            player_2.move("right")
        if pressed_keys[K_SPACE]:
            if projectile.moving == False:
                projectile.rect.x, projectile.rect.y = player_2.rect.x, player_2.rect.y
                projectile.startx, projectile.starty = player_2.rect.x, player_2.rect.y
                projectile.moving = True
                done = False

        if done == False:
            if projectile.moving == False:
                projectile_group, projectile = reset_projectile(projectile_group, projectile_pokeball)
                playerTurn = "red"
                done = True

    # Drawing stuff on the screen:
    screen.blit(background, (0, 0))
    player_group.draw(screen)
    displayTopRight_two("Speed: {0}, Angle: {1}", projectile.speed, projectile.angle, screen)

    # Will only draw the projectile on the screen if it is moving:
    if projectile.moving == True:
        projectile_group.draw(screen)
        projectile.update()

    # Updates display:
    pygame.display.update()

# Quits the game:
pygame.display.quit()
