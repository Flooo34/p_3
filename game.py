#! /usr/bin/#!/usr/bin/env python3
#coding : utf-8

'''
Game MacGiver Project 3 OpenClassRooom
type labyrinth

'''

import pygame
from pygame.locals import *
from random import *

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

Mac = Character('pictures/MacGyver.png', 'pictures/MacGyver.png', 'pictures/MacGyver.png', 'pictures/MacGyver.png')# !!!!!!!!!!!!!!!!
windows.blit(Mac, (0,0))
pygame.display.flip()
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
    windows.blit(Mac, (0,0))


    nivel = Game('map.txt')
    nivel.generate()
    nivel.show(windows)
    icon = pygame.image.load(picture_icon)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continue_game = 0

            if event.key == K_RIGHT:
                Mac.moove("right")
            if event.key == K_LEFT:
                Mac.moove("left")
            if event.key == K_UP:
                Mac.moove("top")
            if event.key == K_DOWN:
                Mac.moove("bot")

    windows.blit(background, (0,0))
    nivel.show(windows)
    windows.blit(Mac, (0,0))
    pygame.display.flip()

    # Test de si il a les 3 objets pour win

    #Victory
    #if Game.line_nivel[Mac.case_y][Mac.case_x] == "f":
        #continue_game = 0
