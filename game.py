#! /usr/bin/#!/usr/bin/env python3
#coding : utf-8

'''
Game MacGiver Project 3 OpenClassRooom
type labyrinth

'''

import pygame
from pygame.locals import *

from class import *
from constant import*

# Start pygame
pygame.init()

#Music
pygame.mixer.music.load("sound/mc.wav")
son.play()
pygame.mixer.music.get_volume(0.3)

#start windows game
windows = pygame.display.set_mode((side_windows, side_windows))
icon = pygame.image.load(picture_icon)
pygame.display.set_caption(title_windows)
