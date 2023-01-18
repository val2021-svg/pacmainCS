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

hands = mp_hands.Hands(max_num_hands=settings.nb_max_hands,
                       min_detection_confidence=0.8, min_tracking_confidence=0.5)


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

#an image that can be selected
class ClickableIcon(pygame.sprite.Sprite):
    def __init__(self,screen,pos,path,rawtext,size=(70,70)):
        self.rawtext=rawtext
        self.pos = pos
        print(path)
        self.size=size
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, size)
        self.rect=image.get_rect()
        #set position of self.rect
        self.rect.x=self.pos[0]
        self.rect.y=self.pos[1]
        self.image=image
        self.selected = False
        self.screen = screen
        self.screen.blit(self.image,self.pos)
        #add the text text under the image
        self.font=pygame.font.SysFont(None,20)
        self.text=self.font.render(rawtext,True,settings.BLACK)
        text_rect=self.text.get_rect()
        self.text_pos=(self.pos[0]+(self.size[0]-text_rect[2])/2,self.pos[1]+self.size[1]+10)
        self.screen.blit(self.text,self.text_pos)
        self.screen.blit(self.image,self.pos)

    #when the image is selected, change the text color to red and draw it and change the boolean selected to True
    def update(self):
        if not self.selected:
            print("up")
            font=pygame.font.SysFont(None,20)
            text=font.render(self.rawtext,True,settings.RED)
            self.screen.blit(text,self.text_pos)
            self.selected=True
            print("done")
        else:
            self.text=self.font.render(self.rawtext,True,settings.BLACK)
            self.screen.blit(self.text,self.text_pos)
            self.selected=False

    def who(self):
        print("Size : "+str(self.size) + "\nPosition : " + str(self.pos))

#a class that represents a text that can be clicked on, inherits from pygame.sprite.Sprite
class ClickableText(pygame.sprite.Sprite):
    def __init__(self,text,pos,screen,size=40):
        super().__init__()
        self.pos=pos
        font=pygame.font.SysFont(None,size)
        self.text=font.render(text,True,settings.BLACK)

    #draws the text on the screen
    def draw(self,screen):
        screen.blit(self.text,self.pos)

    #update the text and print "text clicked on" when the mouse is on the text
    def update(self):
        print("text clicked on")

def checkpos(square, x, y):
    #print("Checking if {},{} is between {},{} and {},{}".format(x,y,square.pos[0],square.pos[0]+square.size[0],square.pos[1],square.pos[1]+square.size[1]))
    return x >= square.pos[0] and x <= square.pos[0]+square.size[0] and y >= square.pos[1] and y <= square.pos[1]+square.size[1]



def test():
    run = True
    # create pygame screen and set it to black
    screen = pygame.display.set_mode((settings.sw, settings.sh))
    screen.fill(settings.BLACK)

    square = ClickableImage(screen)
    square.who()
    while run:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                print(checkpos(square, x, y))
                if checkpos(square, x, y):
                    square.select(screen)
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()

# center text horizontally with given y setting


def center(text, screen, y):
    screen_width = screen.get_size()[0]
    rect_size = text.get_rect()
    screen.blit(text, ((screen_width-rect_size[2])//2, y))

# display a menu that enables sign selection among those possible


def sign_selection_menu():

    run = True
    # create pygame screen and set it to black
    screen = pygame.display.set_mode((settings.sw, settings.sh))
    screen.fill(settings.CYAN)

    # display main message "Selection des signes"
    font = pygame.font.SysFont(None, 50)
    maintext = font.render("Selection des signes", True, settings.BLACK)
    center(maintext, screen, 50)

    # create multiple squares that will each represent one sign
    sign_list = {}
    pos = []
    icon1=ClickableIcon(screen,pos=(50,50),rawtext="Signe1",path="images/logo.png")
    sign_list[1] = icon1
    while run:

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for square in sign_list.values():
                    if square.rect.collidepoint(x, y):
                        square.update()
        pygame.display.flip()

def instant_test_():
    screen=pygame.display.set_mode((settings.sw,settings.sh))
    screen.fill(settings.CYAN)
    path="images/logo.png"
    image=pygame.image.load(path).convert_alpha()
    size=(100,100)
    image = pygame.transform.scale(image, size)
    screen.blit(image,(100,100))
    pygame.display.flip()
    input()

if __name__ == "__main__":
    #test()
    sign_selection_menu()
    #instant_test_()
