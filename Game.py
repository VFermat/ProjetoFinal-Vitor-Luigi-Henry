# -*- coding: utf-8 -*-
"""
Created on Thu May 3 2018

@author: Henry Rocha, Vitor Eller, Luigi Portugal
"""

import Terrain
import projectile
import pygame
import text_input as ti
from TextDisplay import *
from GameMechanics import *
from pygame.locals import *

from settings import *
from sprites import *

# Import needed to center PyGame's window
import os
# Code to center PyGame window on the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# ============= Initializing =============
# PyGame initialization:
pygame.init()
pygame.font.init()
pygame.display.set_caption(windowTitle)

# Screen settings:
screen = pygame.display.set_mode(screen_size, 0, 32)

# Setting up FPS:
clock = pygame.time.Clock()

# Variables:
projectile = projectile_pokeball

# Fonts
font_55 = pygame.font.SysFont("None", 55)
font_35 = pygame.font.SysFont("None", 35)
font_25 = pygame.font.SysFont("None", 25)
font_20 = pygame.font.SysFont("None", 20)
font_16 = pygame.font.SysFont("None", 16)

# Terrain
terrain = Terrain.Terrain(background.get_rect(), screen_height)
terrain_group = terrain.drawTerrain(screen)

# ===============   LOOPING PRINCIPAL   ===============
running = True
while running:
    # Sets game FPS:
    clock.tick(framesPerSecond)

    # Main Menu:
    if screen_type == "Main Menu":

        # Getting game's events:
        events = pygame.event.get()
        # Loops through game events
        for event in events:
            # If event is QUIT (Window close)
            if event.type == QUIT:
                # Sets playing state to false, thus quitting the main loop
                running = False

            # Checks if there was a key press:
            if event.type == pygame.KEYDOWN:
                # Checks if the key pressed was the ENTER key:
                if event.key == pygame.K_RETURN:
                    # Resets the players stuff:
                    reset_player(player_1, player_2)
                    # Changes screen:
                    screen_type = "Player 1 Name"

        # Drawing stuff:
        screen.fill(black)

        # Writing text:
        welcomeScreen(main_text, screen, screen_size, font_55)

    # Player 1 name screen:
    elif screen_type == "Player 1 Name":

        # Getting game's events:
        events = pygame.event.get()
        # Loops through game events
        for event in events:
            # If event is QUIT (Window close)
            if event.type == QUIT:
                # Sets playing state to false, thus quitting the main loop
                running = False

            # Checks if there was a key press:
            if event.type == pygame.KEYDOWN:
                # Checks if the key pressed was the ENTER key:
                if event.key == pygame.K_RETURN:
                    # Only proceeds if the player typed something:
                    if len(player_1.name) != 0:
                        # Changes screen:
                        screen_type = "Player 2 Name"

        # Text input box:
        player_1.name = ti.textInputBox(player_1.name, screen, screen_size, events, 1, font_35)

    # Player 2 name screen:
    elif screen_type == "Player 2 Name":

        # Getting game's events:
        events = pygame.event.get()
        # Loops through game events
        for event in events:
            # If event is QUIT (Window close)
            if event.type == QUIT:
                # Sets playing state to false, thus quitting the main loop
                running = False

            # Checks if there was a key press:
            if event.type == pygame.KEYDOWN:
                # Checks if the key pressed was the ENTER key:
                if event.key == pygame.K_RETURN:
                    # Only proceeds if the player typed something:
                    if len(player_2.name) != 0:
                        # Changes screen:
                        screen_type = "Playing"

        # Text input box:
        player_2.name = ti.textInputBox(player_2.name, screen, screen_size, events, 2, font_35)

    # Game Loop:
    elif screen_type == "Playing":

        # Getting game's events:
        events = pygame.event.get()
        # Loops through game events
        for event in events:
            # If event is QUIT (Window close)
            if event.type == QUIT:
                # Sets playing state to false, thus quitting the main loop
                running = False

            # Checks if there was a mouse button press:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if projectile.moving == False:
                    if playerTurn == "1":
                        projectile.rect.x, projectile.rect.y = player_1.rect.center
                        projectile.startx, projectile.starty = player_1.rect.center

                        if projectile.speed > 150:
                            projectile.speed = 150

                        projectile.moving = True
                        done = False

                    if playerTurn == "2":
                        projectile.rect.x, projectile.rect.y = player_2.rect.center
                        projectile.startx, projectile.starty = player_2.rect.center

                        if projectile.speed > 150:
                            projectile.speed = 150

                        projectile.moving = True
                        done = False

            # Checks if there was a key press:
            if event.type == pygame.KEYDOWN:
                # Checks if the key pressed was the number 1:
                if event.key == pygame.K_1:
                    if projectile.moving == False:
                        projectile = projectile_pokeball
                        projectile_group.empty()
                        projectile_group.add(projectile_pokeball)

                # Checks if the key pressed was the number 2:
                if event.key == pygame.K_2:
                    if projectile.moving == False:
                        projectile = projectile_purpleball
                        projectile_group.empty()
                        projectile_group.add(projectile_purpleball)

        # Players turn:
        if playerTurn == "1":
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_a]:
                player_1.move("left", projectile.moving)
            if pressed_keys[K_d]:
                player_1.move("right", projectile.moving)

            # Checks for collision, if theres is any, stops projectile movement
            # and does damage to the enemy:
            if pygame.sprite.collide_rect(projectile, player_2):
                projectile.stop_movement()
                player_2.health -= projectile.damage
                # Checks if there is a winner
                if player_2.health <= 0:
                    player_2.health = 0
                    winner = player_1.name
                    screen_type = "Game End"

            if done == False:
                if projectile.moving == False:
                    projectile.reset_stats()
                    projectile_group, projectile = reset_projectile(projectile_group, projectile_pokeball)
                    playerTurn = "2"
                    done = True

        if playerTurn == "2":
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_a]:
                player_2.move("left", projectile.moving)
            if pressed_keys[K_d]:
                player_2.move("right", projectile.moving)

            # Checks for collision, if theres is any, stops projectile movement
            # and does damage to the enemy:
            if pygame.sprite.collide_rect(projectile, player_1):
                projectile.stop_movement()
                player_1.health -= projectile.damage
                # Checks if there is a winner
                if player_1.health <= 0:
                    player_1.health = 0
                    winner = player_2.name
                    screen_type = "Game End"

            if done == False:
                if projectile.moving == False:
                    projectile.reset_stats()
                    projectile_group, projectile = reset_projectile(projectile_group, projectile_pokeball)
                    playerTurn = "1"
                    done = True

        # Drawing stuff on the screen:
        screen.blit(background, (0, 0))
        terrain_group.draw(screen)
            
        projectilesDisplay_group.draw(screen)
        player_group.draw(screen)
        
        get_projectileStats(screen, player_1, player_2, playerTurn, projectile)

        displayChosenBomb(projectilesDisplay, projectile, screen, screen_size, font_16)

        displayTopLeft_two("Speed: {0}, Angle: {1}",
                           projectile.speed,
                           projectile.angle,
                           screen, font_20)
        displayTopRight_two("Turn: Player {0}",
                            playerTurn,
                            "",
                            screen,
                            screen_size, font_20)
        displayHeathAndName(player_1, screen_size, screen, font_25)
        displayHeathAndName(player_2, screen_size, screen, font_25)

        # Will only draw the projectile on the screen if it is moving:
        if projectile.moving == True:
            projectile_group.draw(screen)
            projectile.update()

    # Game end screen (Winner):
    elif screen_type == "Game End":

        # Getting game's events:
        events = pygame.event.get()
        # Loops through game events
        for event in events:
            # If event is QUIT (Window close)
            if event.type == QUIT:
                # Sets playing state to false, thus quitting the main loop
                running = False

            # Checks if there was a key press:
            if event.type == pygame.KEYDOWN:
                # Checks if the key pressed was the ENTER key:
                if event.key == pygame.K_RETURN:
                    # Resets the players stuff:
                    reset_player(player_1, player_2)
                    # Changes screen:
                    screen_type = "Main Menu"

        screen.fill(black)
        displayWinnerText(winner_text, winner, screen, screen_size, font_55)

    # Updates display:
    pygame.display.update()

# Quits the game:
pygame.display.quit()
