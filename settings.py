import pygame
from pygame.locals import *

# Sets the window's title:
windowTitle = "Avengers"

# Sets the screen settings:
screen_width, screen_height = 1260, 640
screen_size = (screen_width, screen_height)

# Sets the game's FPS:
framesPerSecond = 60

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
blockScale = 0.2
terrainPreset = 1
terrainGenRandom = True
minTerrainHeight = 1
maxTerrainHeight = 35
smooth_factor = 4

# Action Bar settings:
showBombSelector = True

actionBarScale = 1.5
actionBarPosition = "top_center"

iconPokeballScale = 1
iconPurpleballScale = 0.75

# Game settings:
done = None
winner = None
loser = None

# Main Screen:
game_screen = "Main Screen"
