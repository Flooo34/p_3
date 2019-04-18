#! /usr/bin/env python 3
# coding : utf-8

'''
Class necessary for the game
'''
import pygame
from pygame.locals import *

import random
from constant import *
from random import randint

class Game:
    def __init__(self, folder):
        self.folder = folder
        self.structure = 0

    def generate(self):
        '''
        Generate the game with the folder map.txt
        '''
        with open(self.folder, "r") as folder:
            structure_g = []
            for line in folder:
                line_g = []
                #structure sprite
                for sprite in line:
                    if sprite != '\n':
                        line_g.append(sprite)
                structure_g.append(line_g)
            self.structure = structure_g

    def element(self):
        for element in self.structure:
            for sprites in element:
                '''x = num_case * size_sprite
                y = num_line * size_sprite'''
                if element == "o":
                    alea = randit(0,8)
                    if alea == 1:
                        structure_g[x][y] = "e"
                    elif alea == 3:
                        structure_g[x][y] = "p"
                    elif alea == 7:
                        structure_g[x][y] = "n"


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
        #test = pygame.image.load(groundtest_picture).convert()
        guardian = pygame.image.load(guardian_picture).convert_alpha()
        ether = pygame.image.load(ether_picture).convert_alpha()
        plastic = pygame.image.load(plastic_picture).convert_alpha()
        needle = pygame.image.load(needle_picture).convert_alpha()


        num_line = 0
        #counter = 0

        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * size_sprite
                y = num_line * size_sprite

                if sprite == "w":
                    windows.blit(wall, (x,y))   #wall
                elif sprite == "s":
                    windows.blit(start, (x,y))  #Start

                elif sprite == "r":
                    windows.blit(rip, (x,y))    #rip case
                elif sprite == "g":
                    windows.blit(guardian, (x,y))   #Guardian
                #elif sprite == "t":
                    #windows.blit(test, (x,y))   #test case
                elif sprite == "f":
                    windows.blit(finish, (x,y)) # finish case
                elif sprite == "e":
                    windows.blit(ether, (x,y))  #ether
                elif sprite == "p":
                    windows.blit(plastic, (x,y))    # plastic
                elif sprite == "n":
                    windows.blit(needle, (x,y))     #needle

                '''elif sprite == "o":
                    #booléène
                    if counter == 0:
                        alea = randint(0,5)
                        if alea:
                            windows.blit(ether, (x,y))
                            counter += 1
                    elif counter == 1:
                        alea = randint(0,1)
                        if alea:
                            windows.blit(plastic, (x,y))
                            counter += 1
                    elif counter == 2:
                        alea = randint(0,1)
                        if alea:
                            windows.blit(needle, (x,y))
                            counter += 1

                    else:
                        pass'''



                num_case += 1
            num_line += 1


class Player:
    '''
    Class to move MacGyver in the game
    '''

    def __init__(self, right, left, top, bot, game ):
        self.game = game
        self.right = pygame.image.load("pictures/MacGyver.png").convert_alpha()
        self.left = pygame.image.load("pictures/MacGyver.png").convert_alpha()
        self.top = pygame.image.load("pictures/MacGyver.png").convert_alpha()
        self.bot = pygame.image.load("pictures/MacGyver.png").convert_alpha()
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.direction = self.right


    def move(self, direction):
        if direction == "right":
            if self.case_x < (number_sprite_side -1):
                if self.game.structure[self.case_y][self.case_x+1] != "w":
                    self.case_x += 1
                    self.x = self.case_x * size_sprite
            self.direction = self.right

        if direction == "left":
            if self.case_x > 0:
                if self.game.structure[self.case_y][self.case_x-1] != "w":
                    self.case_x -= 1
                    self.x = self.case_x * size_sprite
            self.direction = self.left

        if direction == "top":
            if self.case_y > 0:
                if self.game.structure[self.case_y-1][self.case_x] != "w":
                    self.case_y -= 1
                    self.y = self.case_y * size_sprite
            self.direction = self.top

        if direction == "bot":
            if self.case_y < (number_sprite_side -1):
                if self.game.structure[self.case_y+1][self.case_x] != "w":
                    self.case_y += 1
                    self.y = self.case_y * size_sprite
            self.direction = self.bot
