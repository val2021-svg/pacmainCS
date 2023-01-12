import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
import calcul
from math import *
import sign
import settings
import pygame

BLACK = (0, 0, 0)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
WHITE = (255, 255, 255)
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


pygame.init()

hands=mp_hands.Hands(max_num_hands = settings.nb_max_hands, min_detection_confidence=0.8, min_tracking_confidence=0.5)

class Menu():
    def __init__(self):
        self.initalize()
        self.run()

    def initalize(self):
        self.screen = pygame.display.set_mode((400, 800))
        self.screen.fill(BLUE)
        self.text1 = pygame.font.render('Arial', True, WHITE)

    def run(self):
        while True:

            pygame.display.update()

class Square(pygame.sprite.Sprite):
    def __init__(self,screen,size=(100,100),pos=(50,50),border_size=10,color=settings.BLUE,bordercolor=settings.RED):
        self.size=size
        self.pos=pos
        self.incolor=color
        self.bordercolor=bordercolor
        self.selected=False
        self.inrect=pygame.Rect(pos,size).inflate(-border_size,-border_size)
        self.outrect=pygame.Rect(pos,size)
        pygame.draw.rect(screen, color, self.outrect)

    def select(self,screen):
        self.outline(screen, not self.selected)
        self.selected=not self.selected

    def outline(self,screen,bool):
        if bool:
            self.color(screen,self.bordercolor)
        else:
            self.color(screen,self.incolor)

    def color(self,screen,bordercolor):
        pygame.draw.rect(screen,bordercolor,self.outrect)
        pygame.draw.rect(screen,self.incolor,self.inrect)

    def who(self):
        print("Size : "+str(self.size) + "\nPosition : " + str(self.pos))

def checkpos(square,x,y):
    #print("Checking if {},{} is between {},{} and {},{}".format(x,y,square.pos[0],square.pos[0]+square.size[0],square.pos[1],square.pos[1]+square.size[1]))
    return x>=square.pos[0] and x<=square.pos[0]+square.size[0] and y>=square.pos[1] and y<=square.pos[1]+square.size[1]

def test():
    run=True
    #create pygame screen and set it to black
    screen = pygame.display.set_mode((settings.sw, settings.sh))    
    screen.fill(settings.BLACK)

    square=Square(screen)
    square.who()
    while run:
    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                print(x,y)
                print(checkpos(square,x,y))
                if checkpos(square,x,y):
                    square.select(screen)
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.flip()

#display a menu that enables sign selection among those possible
def sign_selection_menu():

    run=True
    #create pygame screen and set it to black
    screen = pygame.display.set_mode((settings.sw, settings.sh))    
    screen.fill(settings.BLACK)

    #create different surface for each signe    
    sign1 = pygame.Surface((100, 100))

    sign1.fill(settings.BLUE)

    pos_sign1=(50,50)
    pos_text1=(50,200)
    font = pygame.font.SysFont(None,24)
    text1 = font.render("Button1",True, settings.WHITE)
    rect1=text1.get_rect()
    screen.blit(text1,pos_text1)
    screen.blit(sign1,pos_sign1)



    

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.flip()


if __name__=="__main__":
    test()
    #sign_selection_menu()