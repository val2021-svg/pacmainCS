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


class Square():
    def __init__(self, screen, size=(100, 100), pos=(50, 50), border_size=10, color=settings.BLUE, bordercolor=settings.RED):
        self.size = size
        self.pos = pos
        self.incolor = color
        self.bordercolor = bordercolor
        self.selected = False
        self.screen = screen
        self.inrect = pygame.Rect(
            pos, size).inflate(-border_size, -border_size)
        self.outrect = pygame.Rect(pos, size)
        pygame.draw.rect(screen, color, self.outrect)

    def select(self):
        self.outline(not self.selected)
        self.selected = not self.selected

    def outline(self, bool):
        if bool:
            self.color(self.screen, self.bordercolor)
        else:
            self.color(self.screen, self.incolor)

    def color(self, screen, bordercolor):
        pygame.draw.rect(screen, bordercolor, self.outrect)
        pygame.draw.rect(screen, self.incolor, self.inrect)

    def who(self):
        print("Size : "+str(self.size) + "\nPosition : " + str(self.pos))


def checkpos(square, x, y):
    #print("Checking if {},{} is between {},{} and {},{}".format(x,y,square.pos[0],square.pos[0]+square.size[0],square.pos[1],square.pos[1]+square.size[1]))
    return x >= square.pos[0] and x <= square.pos[0]+square.size[0] and y >= square.pos[1] and y <= square.pos[1]+square.size[1]


def test():
    run = True
    # create pygame screen and set it to black
    screen = pygame.display.set_mode((settings.sw, settings.sh))
    screen.fill(settings.BLACK)

    square = Square(screen)
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
    screen.fill(settings.BLACK)

    # display main message "Selection des signes"
    font = pygame.font.SysFont(None, 30)
    maintext = font.render("Selection des signes", True, settings.WHITE)
    center(maintext, screen, 50)

    # create multiple squares that will each represent one sign
    sign_list = {}
    pos = []
    for i in range(10):
        sign_list["square"+str(i)] = Square(screen,
                                            size=(50, 50), border_size=5, pos=(40+100*i, 100))
    print(sign_list)
    while run:

        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for square in sign_list.values():
                    if checkpos(square, x, y):
                        square.select()
        pygame.display.flip()


if __name__ == "__main__":
    # test()
    sign_selection_menu()
