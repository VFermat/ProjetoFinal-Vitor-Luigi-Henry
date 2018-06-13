import pygame
from settings import *
from pygame.locals import *
import class_bomb as bomb
import class_player as player
import class_button as button
import class_terrain as terrain
import class_actionBar as actionBar
import class_background as background
import class_bombDisplay as bombDisplay

# Background settings:
background = background.Background("Sprites/BG_StarryNight_1280x640.png", 0, 0)

# Player settings:
player1Right = []
for counter in range(1, 5):
    imagePath = 'Sprites/Captain America Sprites/CaptainAmerica_Right_' + str(counter) + '.png'
    image = pygame.image.load(imagePath)
    rect = image.get_rect()
    new_scale = (rect.width * playerScale, rect.height * playerScale)

    image = pygame.transform.scale(image, new_scale)
    player1Right.append(image)

player1Left = []
for counter in range(1, 5):
    imagePath = 'Sprites/Captain America Sprites/CaptainAmerica_Left_' + str(counter) + '.png'
    image = pygame.image.load(imagePath)
    rect = image.get_rect()
    new_scale = (rect.width * playerScale, rect.height * playerScale)

    image = pygame.transform.scale(image, new_scale)
    player1Left.append(image)

player_1 = player.Player(player1Right, player1Left,
                         0, 0,
                         screen_size,
                         100,
                         "Captain America")


player2Right = []
for counter in range(1, 5):
    imagePath = 'Sprites/Iron Man Sprites/IronMan_Right_' + str(counter) + '.png'
    image = pygame.image.load(imagePath)
    rect = image.get_rect()
    new_scale = (rect.width * playerScale, rect.height * playerScale)

    image = pygame.transform.scale(image, new_scale)
    player2Right.append(image)

player2Left = []
for counter in range(1, 5):
    imagePath = 'Sprites/Iron Man Sprites/IronMan_Left_' + str(counter) + '.png'
    image = pygame.image.load(imagePath)
    rect = image.get_rect()
    new_scale = (rect.width * playerScale, rect.height * playerScale)

    image = pygame.transform.scale(image, new_scale)
    player2Left.append(image)

player_2 = player.Player(player2Right, player2Left,
                         600, 0,
                         screen_size,
                         100,
                         "Iron Man")

players_group = pygame.sprite.Group()
players_group.add(player_1)
players_group.add(player_2)

# Action Bar:
actionBar = actionBar.ActionBar("Sprites/ActionBar5_210x41.png", screen_size,
                                actionBarScale, actionBarPosition)
actionBar_group = pygame.sprite.Group()
actionBar_group.add(actionBar)

# Bomb 1:
iconPokeball = bombDisplay.BombDisplay("Sprites/pokeball.png", iconPokeballScale)
iconPokeball.rect.center = actionBar.slot1

actionBar_group.add(iconPokeball)

# Bomb 2:
iconPurpleball = bombDisplay.BombDisplay("Sprites/Purple_Ball_50x50.png", iconPurpleballScale)
iconPurpleball.rect.center = actionBar.slot2

actionBar_group.add(iconPurpleball)

# Bomb 3:
iconCrazyball = bombDisplay.BombDisplay("Sprites/bomba_loca.png", iconCrazyballScale)
iconCrazyball.rect.center = actionBar.slot3

actionBar_group.add(iconCrazyball)

# Bomb 4:
iconNeutronball = bombDisplay.BombDisplay("Sprites/grav_bomb.png", iconNeutronballScale)
iconNeutronball.rect.center = actionBar.slot4

actionBar_group.add(iconNeutronball)

# Bomb 5:
iconCrashball = bombDisplay.BombDisplay("Sprites/bomba_crash.png", iconCrashballScale)
iconCrashball.rect.center = actionBar.slot5

actionBar_group.add(iconCrashball)

# Terrain:
terrain = terrain.Terrain("Sprites/DirtBlock_70x70.png", blockScale, screen_size, smooth_factor)
if terrainGenRandom == True:
    terrain.generateHeightsRandom(minTerrainHeight, maxTerrainHeight)
else:
    terrain.generateHeightsPreset(terrainPreset)

# Buttons:
button_group = pygame.sprite.Group()

start_button = button.Button("Sprites/Buttons/Start_Button.png", screen_size, 1, "center_top3")
button_group.add(start_button)
settings_button = button.Button("Sprites/Buttons/Settings_Button.png", screen_size, 1, "center_top")
button_group.add(settings_button)
exit_button = button.Button("Sprites/Buttons/Exit_Button.png", screen_size, 1, "center_bottom2")
button_group.add(exit_button)

# Projectile settings:
bomb_crash = bomb.Bomb(screen_size,
                       "Sprites/bomba_crash.png",
                       0.1,
                       "crash",
                       0, 0,
                       5,
                       200)

bomb_pokeball = bomb.Bomb(screen_size,
                          "Sprites/pokeball.png",
                          0.7,
                          "pokeball",
                          0, 0,
                          10,
                          150)

bomb_purpleball = bomb.Bomb(screen_size,
                            "Sprites/purple_ball_50x50.png",
                            0.35,
                            "purpleball",
                            0, 0,
                            15,
                            120)

bomb_crazy = bomb.Bomb(screen_size,
                       "Sprites/bomba_loca.png",
                       0.06,
                       "crazy",
                       0, 0,
                       20,
                       100)

bomb_neutron = bomb.Bomb(screen_size,
                         "Sprites/grav_bomb.png",
                         0.06,
                         "neutron",
                         0, 0,
                         25,
                         50)

bomb_group = pygame.sprite.Group()
bomb_group.add(bomb_pokeball)

# Explosion animation:
explosionFrames = []
for counter in range(1, 13):
    imagePath = 'Sprites/Explosion/Explosion_' + str(counter) + '.png'
    image = pygame.image.load(imagePath)
    rect = image.get_rect()
    new_scale = (rect.width * explosionScale, rect.height * explosionScale)

    image = pygame.transform.scale(image, new_scale)
    explosionFrames.append(image)
