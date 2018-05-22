# -*- coding: utf-8 -*-
"""
Created on Thu May 3 2018

@author: Henry Rocha, Vitor Eller, Luigi Portugal
"""

import projectiles_display
import projectile
import player
import pygame
import random
import math
import text_input as ti
from TextDisplay import *
from GameMechanics import *
from pygame.locals import *

# Import needed to center PyGame's window
import os
# Code to center PyGame window on the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# ============= Initializing =============
# PyGame initialization:
pygame.init()
pygame.font.init()
pygame.display.set_caption("Foxes")

# Screen settings:
screen_width, screen_height = 1280, 640
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size, 0, 32)

# Setting up FPS:
clock = pygame.time.Clock()
framesPerSecond = 60

# Background settings:
background = pygame.image.load("Sprites/flat_background_1280x640.png").convert()

# Player settings:
player_1 = player.Player("Sprites/Fiona_Red_Right.png",
                         10,
                         490)
player_2 = player.Player("Sprites/Fiona_Blue_Left.png",
                         1280 - 100,
                         490)

player_group = pygame.sprite.Group()
player_group.add(player_1)
player_group.add(player_2)

# Projectile settings:
projectile_pokeball = projectile.Projectile(screen_size,
                                            "Sprites/pokeball.png",
                                            "pokeball",
                                            0, 0,
                                            10,
                                            150)
projectile_purpleball = projectile.Projectile(screen_size,
                                              "Sprites/purple_ball_50x50.png",
                                              "purpleball",
                                              0, 0,
                                              15,
                                              120)
projectile_group = pygame.sprite.Group()
projectile_group.add(projectile_pokeball)


# Projectiles display settings:
projectilesDisplay = projectiles_display.Projectiles_Display(screen_size,
                                                             "Sprites/AllBombs_50x50.png",
                                                             0, 0)
projectilesDisplay_group = pygame.sprite.Group()
projectilesDisplay_group.add(projectilesDisplay)


# Variables:
done = None
playerHit = None
winner = None
playerTurn = "1"
projectile = projectile_pokeball
black = (0, 0, 0)
red = (182, 38, 37)

# Main Screen
main_text = ("Welcome to Foxy!",
             "Press Enter to Play.")

# Winner Text
winner_text = ("The Winner Is: {0}!!",
        "Congrats on Winning the Game!",
        "Please Press Enter and Restart the Game")

# Screen_type sets which screen we are using
screen_type = 1

"""
screen_type = 1 -> Initial Screen
screen_type = 2 -> Game Loop
screen_type = 3 -> End of Game Screen
screen_type = 4 -> Get Player 1 Name
screen_type = 5 -> Get Player 2 Name
"""

# ===============   LOOPING PRINCIPAL   ===============
running = True
while running:
    # Sets game FPS:
    time = clock.tick(framesPerSecond)

    # Main Menu
    if screen_type == 1:
        # Checking for events:
        for event in pygame.event.get():  # Loops through game events
            if event.type == QUIT:  # If event is QUIT (Window close)
                running = False  # Sets playing state to false, thus quitting the main loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset_player(player_1, player_2)
                    screen_type = 4
        
        screen.fill(black)
        welcomeScreen(main_text, screen, screen_size)

    # Game Loop
    elif screen_type == 2:
        # Checking for events:
        for event in pygame.event.get():  # Loops through game events
            if event.type == QUIT:  # If event is QUIT (Window close)
                running = False  # Sets playing state to false, thus quitting the main loop

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

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    if projectile.moving == False:
                        projectile = projectile_pokeball
                        projectile_group.empty()
                        projectile_group.add(projectile_pokeball)

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

            # Checks for collision, if theres is any, stops projectile movement and
            # does damage to the enemy:
            if pygame.sprite.collide_rect(projectile, player_2):
                projectile.stop_movement()
                player_2.health -= projectile.damage
                # Checks if there is a winner
                if player_2.health <= 0:
                    player_2.health = 0
                    winner = player_1.name
                    screen_type = 3

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

            # Checks for collision, if theres is any, stops projectile movement and
            # does damage to the enemy:
            if pygame.sprite.collide_rect(projectile, player_1):
                projectile.stop_movement()
                player_1.health -= projectile.damage
                # Checks if there is a winner
                if player_1.health <= 0:
                    player_1.health = 0
                    winner = player_2.name
                    screen_type = 3

            if done == False:
                if projectile.moving == False:
                    projectile.reset_stats()
                    projectile_group, projectile = reset_projectile(projectile_group, projectile_pokeball)
                    playerTurn = "1"
                    done = True

        # Drawing stuff on the screen:
        screen.blit(background, (0, 0))
        projectilesDisplay_group.draw(screen)
        player_group.draw(screen)

        get_projectileStats(screen, player_1, player_2, playerTurn, projectile)

        displayChosenBomb(projectilesDisplay, projectile, screen, screen_size)

        displayTopLeft_two("Speed: {0}, Angle: {1}",
                           projectile.speed,
                           projectile.angle,
                           screen)
        displayTopRight_two("Turn: Player {0}",
                            playerTurn,
                            "",
                            screen,
                            screen_size)
        displayHeathAndName(player_1, screen_size, screen)
        displayHeathAndName(player_2, screen_size, screen)

        # Will only draw the projectile on the screen if it is moving:
        if projectile.moving == True:
            projectile_group.draw(screen)
            projectile.update()

    elif screen_type == 3:

        for event in pygame.event.get():  # Loops through game events
            if event.type == QUIT:  # If event is QUIT (Window close)
                running = False  # Sets playing state to false, thus quitting the main loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reset_player(player_1, player_2)
                    screen_type = 1

        screen.fill(black)
        displayWinnerText(winner_text, winner, screen, screen_size)
    
    elif screen_type == 4:
        
        events = pygame.event.get()
        for event in events:  # Loops through game events
            if event.type == QUIT:  # If event is QUIT (Window close)
                running = False  # Sets playing state to false, thus quitting the main loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(player_1.name) != 0:
                        screen_type = 5                        
        
        player_1.name = ti.textInputBox(player_1.name, screen, screen_size, events, 1)        

    elif screen_type == 5:
        
        events = pygame.event.get()
        for event in events:  # Loops through game events
            if event.type == QUIT:  # If event is QUIT (Window close)
                running = False  # Sets playing state to false, thus quitting the main loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(player_2.name) != 0:
                        screen_type = 2
        
        player_2.name = ti.textInputBox(player_2.name, screen, screen_size, events, 2)        

    # Updates display:
    pygame.display.update()


# Quits the game:
pygame.display.quit()
