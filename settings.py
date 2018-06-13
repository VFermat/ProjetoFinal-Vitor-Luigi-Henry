import pygame
from pygame.locals import *

# Sets the window's title:
windowTitle = "Avengers"

# Sets the screen settings:
screen_width, screen_height = 1260, 640
screen_size = (screen_width, screen_height)

# Sets the game's FPS:
framesPerSecond = 90

# Color settings:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (64, 64, 64)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
PINK = (255, 0, 255)
INFINANCE = (172, 58, 56)

# Player settings:
playerScale = 1
playerTurn = "1"

# Terrain Settings:
terrainCollision = True
blockScale = 0.15
terrainPreset = 1
terrainGenRandom = True
minTerrainHeight = 1
maxTerrainHeight = 40
smooth_factor = 5

# Action Bar settings:
showBombSelector = True

actionBarScale = 1.5
actionBarPosition = "top_center"

iconPokeballScale = 1
iconPurpleballScale = 0.75
iconCrazyballScale = 0.1
iconNeutronballScale = 0.1
iconCrashballScale = 0.17

# Game settings:
done = None
winner = None
loser = None

# Bomb settings:
lastBombPosition = (0, 0)

# Explosion settings:
explosionScale = 1

# Main Screen:
game_screen = "Main Screen"
