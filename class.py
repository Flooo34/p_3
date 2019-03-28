#! /usr/bin/env python 3
# coding : utf-8

'''
Class necessary for the game
'''
import pygame
from pygame.locals import *
import constant

class Game:
    def __init__(self, folder):
        self.folder = folder
        self.structure = 0

    def generate(self):
        '''
        Generate the game with the folder map.txt
        '''
        with open(self.folder, "r") as folder:
            structure_nivel = []
            for line in folder:
                line_nivel = []
                #structure sprite
                for sprite in line:
                    if sprite != '\n':
                        line_nivel.append(sprite)
                structure_nivel.append(line_nivel)
            self.structure = structure_nivel


    def show(self, windows):
        '''
        method to show the windows's game
        '''
        wall = pygame.image.load(wall_picture).convert()
        start = pygame.image.load(start_picture).convert()
        finish = pygame.image.load(start_picture).convert()
        rip = pygame.image.load(rip_picture).convert()
        staircase_up = pygame.image.load(staircase_up).convert()
        staircase_down = pygame.image.load(staircase_down).convert()
        test = pygame.image.load(groundtest_picture).convert()
        guardian = pygame.image.load(guardian_picture).convert()
