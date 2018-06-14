import pygame
import text_input as ti
from sprites import *
from settings import *
from functions import *
from pygame.locals import *

import class_textDisplay as textDisplay
text = textDisplay.TextDisplay()

# Import needed to center PyGame's window
import os
# Code to center PyGame window on the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# INITIALIZING
# ==============================================================================
# PyGame initialization:
pygame.init()
pygame.display.set_caption(windowTitle)

# Screen settings:
screen = pygame.display.set_mode(screen_size, 0, 32)

# Setting up FPS:
clock = pygame.time.Clock()

# Player walk setting:
spriteCount = 0

# Bomb settings:
bomb = bomb_pokeball

bombHit = None

# MAIN LOOP
# ==============================================================================
running = True
while running:
    # Sets game FPS:
    clock.tick(framesPerSecond)

    # Main screen:
    if game_screen == "Main Screen":
        # Loops through game events
        for event in pygame.event.get():
            # If event is QUIT (Window close)
            if event.type == QUIT:
                # Sets playing state to false, thus quitting the main loop
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.buttonClick():
                    game_screen = "Player 1 Name"

                if settings_button.buttonClick():
                    pass

                if exit_button.buttonClick():
                    running = False

        # Drawing the background:
        screen.fill(GRAY)
        button_group.draw(screen)

        text.displayTextMainMenu("Avengers", WHITE, screen, screen_size, "top_center2")

        # Updates stuff:
        pygame.display.update()

    # Player 1 name screen:
    elif game_screen == "Player 1 Name":

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
                        game_screen = "Player 2 Name"

        # Drawing the background:
        screen.fill(GRAY)

        # Displaying basic text:
        text.displayTextNameScreen("Please input player's 1 name (Press ENTER when ready):",
                                   WHITE, screen, screen_size, "center_top3")

        # Displaying and getting player's name:
        player_1.name = ti.textInputBox(player_1.name, WHITE,
                                        screen, screen_size, events, text.font_36)

        # Updates stuff:
        pygame.display.update()

    # Player 2 name screen:
    elif game_screen == "Player 2 Name":

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
                        game_screen = "Playing"

        # Drawing the background:
        screen.fill(GRAY)

        # Displaying basic text:
        text.displayTextNameScreen("Please input player's 2 name (Press ENTER when ready):",
                                   WHITE, screen, screen_size, "center_top3")

        # Displaying and getting player's name:
        player_2.name = ti.textInputBox(player_2.name, WHITE,
                                        screen, screen_size, events, text.font_36)

        # Updates stuff:
        pygame.display.update()

    # Playing screen:
    elif game_screen == "Playing":

        # Checking for collisions with the terrain:
        if terrainCollision == True:
            if pygame.sprite.spritecollide(player_1, terrain.terrain_group, False):
                player_1.rect.y -= 4
                player_1.standing = True

            else:
                player_1.standing = False

            if pygame.sprite.spritecollide(player_2, terrain.terrain_group, False):
                player_2.rect.y -= 4
                player_2.standing = True

            else:
                player_2.standing = False

            if pygame.sprite.spritecollide(bomb, terrain.terrain_group, False):
                lastBombPosition = bomb.rect.center
                bombHit = True
                bomb.stop_movement()

        # Gets mouse position:
        mousePosition = pygame.mouse.get_pos()

        # Checking for pressed keys:
        pressed_keys = pygame.key.get_pressed()

        # Loops through game events
        for event in pygame.event.get():
            # If event is QUIT (Window close)
            if event.type == QUIT:
                # Sets playing state to false, thus quitting the main loop
                running = False

            # Checks if there was a mouse button press:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bomb.moving == False:
                    if playerTurn == "1":
                        # Gets bomb's stats and launches it:
                        getBombStats(bomb, player_1, mousePosition)
                        # Sets the current play as not done yet:
                        done = False

                    elif playerTurn == "2":
                        # Gets bomb's stats and launches it:
                        getBombStats(bomb, player_2, mousePosition)
                        # Sets the current play as not done yet:
                        done = False

            # Checks if there was a key press:
            if event.type == pygame.KEYDOWN:
                # Checks if the key pressed was the number 1:
                if event.key == pygame.K_1:
                    if bomb.moving == False:
                        bomb = bomb_pokeball
                        bomb_group.empty()
                        bomb_group.add(bomb_pokeball)

                # Checks if the key pressed was the number 2:
                if event.key == pygame.K_2:
                    if bomb.moving == False:
                        bomb = bomb_purpleball
                        bomb_group.empty()
                        bomb_group.add(bomb_purpleball)

                if event.key == pygame.K_3:
                    if bomb.moving == False:
                        bomb = bomb_crazy
                        bomb_group.empty()
                        bomb_group.add(bomb_crazy)

                if event.key == pygame.K_4:
                    if bomb.moving == False:
                        bomb = bomb_neutron
                        bomb_group.empty()
                        bomb_group.add(bomb_neutron)

                if event.key == pygame.K_5:
                    if bomb.moving == False:
                        bomb = bomb_crash
                        bomb_group.empty()
                        bomb_group.add(bomb_crash)

        # Players turn:
        if playerTurn == "1":
            # If pressed key is D:
            if pressed_keys[K_d] and not bomb.moving:
                player_1.move("right")
            # If pressed key is A:
            if pressed_keys[K_a] and not bomb.moving:
                player_1.move("left")

            # Drawing the line between player and mouse position:
            get_distance(player_1.rect.center, mousePosition)
            pygame.draw.line(screen, INFINANCE, player_1.rect.center, mousePosition, 5)

            # Checks for collision, if theres is any, stops bomb movement and
            # does damage to the enemy:
            if pygame.sprite.collide_rect(bomb, player_2):
                lastBombPosition = bomb.rect.center
                bombHit = True
                bomb.stop_movement()
                player_2.health -= bomb.damage
                # Checks if there is a winner
                if player_2.health <= 0:
                    player_2.health = 0
                    winner = player_1.name
                    loser = player_2.name
                    game_screen = "Winner Screen"

            if done == False:
                if bomb.moving == False:
                    bomb.reset_stats()
                    bomb_group, bomb = reset_bomb(bomb_group, bomb_pokeball)
                    playerTurn = "2"
                    done = True

            speed = round(get_distance(player_1.rect.center, mousePosition), 2)
            if speed > bomb.maxSpeed:
                speed = bomb.maxSpeed
            angle = round(get_angle(player_1.rect.center, mousePosition, "degrees"), 2)
            text.displayDistance(WHITE, screen, speed, angle, mousePosition)

        elif playerTurn == "2":
            # If pressed key is RIGHT arrow:
            if pressed_keys[K_RIGHT] and not bomb.moving:
                player_2.move("right")
            # If pressed key is LEFT arrow:
            if pressed_keys[K_LEFT] and not bomb.moving:
                player_2.move("left")

            # Drawing the line between player and mouse position:
            get_distance(player_1.rect.center, mousePosition)
            pygame.draw.line(screen, INFINANCE, player_2.rect.center, mousePosition, 5)

            # Checks for collision, if theres is any, stops bomb movement and
            # does damage to the enemy:
            if pygame.sprite.collide_rect(bomb, player_1):
                lastBombPosition = bomb.rect.center
                bombHit = True
                bomb.stop_movement()
                player_1.health -= bomb.damage
                # Checks if there is a winner
                if player_1.health <= 0:
                    player_1.health = 0
                    winner = player_2.name
                    loser = player_1.name
                    game_screen = "Winner Screen"

            if done == False:
                if bomb.moving == False:
                    bomb.reset_stats()
                    bomb_group, bomb = reset_bomb(bomb_group, bomb_pokeball)
                    playerTurn = "1"
                    done = True

            # Blits distance:
            speed = round(get_distance(player_2.rect.center, mousePosition), 2)
            if speed > bomb.maxSpeed:
                speed = bomb.maxSpeed
            angle = round(get_angle(player_2.rect.center, mousePosition, "degrees"), 2)
            text.displayDistance(WHITE, screen, speed, angle, mousePosition)

        # Drawing the background:
        screen.blit(background.image, (0, 0))

        # Draws the terrain:
        terrain.terrain_group.draw(screen)

        # Draws the action bar:
        actionBar_group.draw(screen)

        # Draws bomb selection indicator:
        if showBombSelector == True:
            if bomb.name == "pokeball":
                selectorPos = (round(actionBar.slot1[0]), round(actionBar.slot1[1]))
                selectorRadius = round(actionBar.rect.height/2.5)
                pygame.draw.circle(screen, BLUE, selectorPos, selectorRadius, 2)

            elif bomb.name == "purpleball":
                selectorPos = (round(actionBar.slot2[0]), round(actionBar.slot2[1]))
                selectorRadius = round(actionBar.rect.height/2.5)
                pygame.draw.circle(screen, BLUE, selectorPos, selectorRadius, 2)

            elif bomb.name == "crazy":
                selectorPos = (round(actionBar.slot3[0]), round(actionBar.slot3[1]))
                selectorRadius = round(actionBar.rect.height/2.5)
                pygame.draw.circle(screen, BLUE, selectorPos, selectorRadius, 2)

            elif bomb.name == "neutron":
                selectorPos = (round(actionBar.slot4[0]), round(actionBar.slot4[1]))
                selectorRadius = round(actionBar.rect.height/2.5)
                pygame.draw.circle(screen, BLUE, selectorPos, selectorRadius, 2)

            elif bomb.name == "crash":
                selectorPos = (round(actionBar.slot5[0]), round(actionBar.slot5[1]))
                selectorRadius = round(actionBar.rect.height/2.5)
                pygame.draw.circle(screen, BLUE, selectorPos, selectorRadius, 2)

        # Drawing the players:
        players_group.draw(screen)

        # Drawing the bomb:
        if bomb.moving == True:
            bomb_group.draw(screen)

        # Drawing the explosion:
        if bombHit == True:
            explosion.animate(lastBombPosition)
            if explosion.displayNumber == 12:
                bombHit = False

        # Displaying names and health:
        text.displayHealthAndName(WHITE, player_1, screen, screen_size)
        text.displayHealthAndName(WHITE, player_2, screen, screen_size)

        # Updates stuff:
        bomb.update()
        explosion_group.draw(screen)
        player_1.gravityFall()
        player_2.gravityFall()
        pygame.display.update()

    # Winner's screen:
    elif game_screen == "Winner Screen":
        # Loops through game events
        for event in pygame.event.get():
                # If event is QUIT (Window close)
            if event.type == QUIT:
                    # Sets playing state to false, thus quitting the main loop
                running = False

            # Checks if there was a key press:
            if event.type == pygame.KEYDOWN:
                # Checks if the key pressed was the ENTER key:
                if event.key == pygame.K_RETURN:
                    # Resets player's health:
                    player_1.resetHealth()
                    player_2.resetHealth()

                    # Changes screen:
                    game_screen = "Main Screen"

        # Drawing the background:
        screen.fill(GRAY)

        # Displaying basic text:
        text.displayTextWinnerScreen("Congratulations!",
                                     WHITE, screen, screen_size, "center_top3")
        # Displaying who won:
        text.displayWhoWon(GREEN, winner, loser, screen, screen_size,
                           "center_top")

        # Updates stuff:
        pygame.display.update()


# Quits the game:
pygame.display.quit()
