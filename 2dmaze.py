# This code is not intended to be used for the project, it is just a small 2d template for the game
# Make sure to have pygame installed before running the code

# Written by Yves-AB
# Most recent date modified: 5/27/2023


import pygame
import os
from pygame import gfxdraw

##the code will consist of 2 classes , one for the player ( u control ) and one for the walls
class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)
    
class Wall(object):
    def __init__(self,position):
        walls.append(self)
        self.rect = pygame.rect(position[0],position[1],16,16)
        
walls=[]