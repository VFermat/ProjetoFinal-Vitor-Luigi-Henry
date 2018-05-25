import pygame
from pygame.locals import *

import player
import projectile
import projectiles_display as proj_D
from settings import *

# Background settings:
background = pygame.image.load("Sprites/flat_background_1280x640.png")

# Player settings:
player_1 = player.Player("Sprites/Fiona_Red_Right.png",
                         10,
                         490)

player_2 = player.Player("Sprites/Fiona_Blue_Left.png",
                         1280 - 100,
                         490)

player_group = pygame.sprite.Group()
player_group.add(player_1, player_2)

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
projectilesDisplay = proj_D.Projectiles_Display(screen_size,
                                                "Sprites/AllBombs_50x50.png",
                                                0, 0)

projectilesDisplay_group = pygame.sprite.Group()
projectilesDisplay_group.add(projectilesDisplay)

# Dirt
dirt = pygame.image.load("Sprites/dirt.bmp")
dirt = pygame.transform.smoothscale(dirt, (1, 1))
