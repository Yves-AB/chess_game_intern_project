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

    #function of collision of player with wall
    def collide(self,x,y):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if x > 0:
                    self.rect.right = wall.rect.left
                if x < 0:
                    self.rect.left = wall.rect.right
                if y > 0:
                    self.rect.bottom = wall.rect.top
                if y < 0:
                    self.rect.top = wall.rect.bottom

    #moves player on either x axis or y axis , helper method for move()
    def moveAxis(self,x,y):
        self.rect.x +=x
        self.rect.y +=y
        self.collide(self,x,y)

    def move(self,x,y):
        if x != 0:
            self.moveAxis(self,x,0)
        if y != 0:
            self.moveAxis(self,0,y)


class Wall(object):
    def __init__(self,position):
        walls.append(self)
        self.rect = pygame.rect(position[0],position[1],16,16)


# now we initialize the environment
os.environ["SDL_VIDEO_CENTERED"] = "1" #centers the game window on the screen
pygame.init()  # initiliazes pygame library for use

walls=[]