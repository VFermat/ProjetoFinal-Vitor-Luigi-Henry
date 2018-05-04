# -*- coding: utf-8 -*-
"""
Created on Thu May  3 21:59:22 2018

@author: Vitor Eller
"""

import projectile_class
import player
import pygame

# ============= Initializing ============= 
pygame.init()
tela = pygame.display.set_mode((334, 151), 0, 32)
fundo = pygame.image.load("Sprites_no_background/Background.jpg").convert()

pygame.display.set_caption('Worm')

player_1 = player.Player("Sprites_no_background/fox_no_background1.png", 100, 100)
player_1_group = pygame.sprite.Group()
player_1_group.add(player_1)

player_2 = player.Player("Sprites_no_background/fox_no_background2.png", 500, 100)
player_2_group = pygame.sprite.Group()
player_2_group.add(player_2)

relogio = pygame.time.Clock()

rodando = True
while rodando:
  tempo = relogio.tick(120)
  
  pressed_keys = pygame.key.get_pressed()
  if pressed_keys[K_RIGHT]:
    player_1.move("right")
  elif pressed_keys[K_LEFT]:
    player_1.move("left") 
  elif pressed_keys[K_d]:
    player_2.move("right")
  elif pressed_keys[K_a]:
    player_2.move("left") 
  
  for event in pygame.event.get():  #pega lista de eventos
    if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
      rodando = False            #executa a função de sistema "exit"
  #move a bola pela tela
        
  #gera saídas
  tela.blit(fundo, (0, 0))
  player_1_group.draw(tela)
  player_2_group.draw(tela)
  pygame.display.update()      #coloca a tela na janela
    
pygame.display.quit()