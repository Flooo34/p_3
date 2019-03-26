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

#start windows game
windows = pygame.display.set_mode((side_windows, side_windows))
icon = pygame.image.load(picture_icon)
pygame.display.set_caption(title_windows)
