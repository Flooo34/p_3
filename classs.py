#! /usr/bin/env python 3
# coding : utf-8

'''
Class necessary for the game
'''
import pygame
from pygame.locals import *
#from random import *
import random
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
        #test = pygame.image.load(groundtest_picture).convert()
        guardian = pygame.image.load(guardian_picture).convert_alpha()
        ether = pygame.image.load(ether_picture).convert_alpha()
        plastic = pygame.image.load(plastic_picture).convert_alpha()
        needle = pygame.image.load(needle_picture).convert_alpha()

        '''LIST = ["o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o",
        "o","o","o","o","o","o","o","o","o","o","o"]

        al_choice = random.sample(LIST, 3)      # 3 choice for object
        al_choice = al_choice.pop()
        print(al_choice)'''

        num_line = 0
        counter = 0
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
                #elif sprite == "t":
                    #windows.blit(test, (x,y))   #test case
                elif sprite == "f":
                    windows.blit(finish, (x,y)) # finish case

                elif sprite == "o":
                    #booléène
                    if counter == 0:
                        windows.blit(ether, (x,y))
                        counter += 1
                    elif counter == 1:
                        windows.blit(plastic, (x,y))
                        counter += 1
                    elif counter == 2:
                        windows.blit(needle, (x,y))
                        counter += 1
                    else:
                        pass




                    #list_element = [ether, plastic, needle]
                    #list_element.set_position(random.randint(size_sprite))
                    #display_element = list[random.randint(size_sprite)]
                    #display_element = pygame.transform.scale(display_element,(size_sprite, size_sprite))

                num_case += 1
            num_line += 1


class Character:
    '''
    Class to moove the character on the game
    '''

    def __init__(self, right, left, top, bot):
        self.right = pygame.image.load("pictures/MacGyver.png").convert_alpha()
        self.left = pygame.image.load("pictures/MacGyver.png").convert_alpha()
        self.top = pygame.image.load("pictures/MacGyver.png").convert_alpha()
        self.bot = pygame.image.load("pictures/MacGyver.png").convert_alpha()
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

    def moove(self, direction):
        if direction == "right":
            if self.case_x < (number_sprite_side -1):
                if self.game.structure[self.case_y][self.case_x+1] != "w":
                    self.case_x += 1
                    self.x = self.case_x * size_sprite
            self.direction = self.right

        if direction == "left":
            if self.case_x > 0:
                if self.game.structure[self.case_y][self.case_x-1] != "w":
                    self.case_x -=1
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
                    self.x = self.case_y * size_sprite
            self.direction = self.bot
