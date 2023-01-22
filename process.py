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
import sign2


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def process_frame(frame,sign,results,screen,state,last_state,count):
     

    if sign[0]=="Ouverture de la main":
        #using fing_spread from sign2.py to check if the fingers are spread
        if results.multi_hand_landmarks:
            state=sign2.fing_spread(frame, results)
            if state and not last_state:
                print('fingers opened')
                count -=1
            elif not state and last_state:
                print('fingers closed')
            last_state=state

    if sign[0]=="Fermeture du poing":
        if results.multi_hand_landmarks:
            state=sign2.wrap_fing(frame,results)
            if not state and last_state:
                print('fingers closed')
                count -=1
            elif state and not last_state:
                print('fingers opened')
            last_state=state
    
            
    return frame, state, last_state, count

    