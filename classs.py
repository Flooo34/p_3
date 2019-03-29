#! /usr/bin/env python 3
# coding : utf-8

'''
Class necessary for the game
'''
import pygame
from pygame.locals import *
from constant import *

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
        rip = pygame.image.load(rip_picture).convert_alpha()
        #staircase_up = pygame.image.load(staircase_up_picture).convert()
        #staircase_down = pygame.image.load(staircase_down_picture).convert()
        test = pygame.image.load(groundtest_picture).convert()
        guardian = pygame.image.load(guardian_picture).convert()

        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * size_sprite
                y = num_line * size_sprite
                if sprite == "w":
                    windows.blit(wall, (x,y))   #wall
                elif sprite == "s":
                    windows.blit(start, (x,y))  #Start
                #elif sprite == "u":
                    #windows.blit(staircase_up, (x,y))   #staircase up
                #elif sprite == "d":
                    #windows.blit(staircase_down, (x,y)) #staircase down
                elif sprite == "r":
                    windows.blit(rip, (x,y))    #rip case
                elif sprite == "g":
                    windows.blit(guardian, (x,y))   #Guardian
                elif sprite == "t":
                    windows.blit(test, (x,y))   #test case
                elif sprite == "f":
                    windows.blit(finish, (x,y)) # finish case
                num_case += 1
            num_line += 1
