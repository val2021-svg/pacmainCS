import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
import calcul
from math import *
import sign
from settings import sw, sh
import pygame

BLACK = (0, 0, 0)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
WHITE = (255, 255, 255)


pygame.init()


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
