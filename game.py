#! /usr/bin/#!/usr/bin/env python3
#coding : utf-8

'''
Game MacGiver Project 3 OpenClassRooom
type labyrinth

'''

import pygame
from pygame.locals import *

from classs import *
from constant import*

# Start pygame
pygame.init()

#Music
sound = pygame.mixer.music.load("sound/mc.wav")
pygame.mixer.music.play()
volume = pygame.mixer.music.get_volume()
pygame.mixer.music.set_volume(0.05)

#start windows game
windows = pygame.display.set_mode((side_windows, side_windows))
icon = pygame.image.load(picture_icon)
pygame.display.set_caption(title_windows)


continue_game = 1

while continue_game:


    #reduct speed loop
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        #if quit the game
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continue_game = 0

    pygame.key.set_repeat(400, 30)

    background = pygame.image.load(background_picture).convert()
    windows.blit(background, (0,0))

    choice = 'map.txt'
    nivel = Game(choice)
    nivel.generate()
    nivel.show(windows)
    icon = pygame.image.load(picture_icon)
    pygame.display.flip()
