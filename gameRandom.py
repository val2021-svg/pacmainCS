import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
import calcul
from math import *
import sign
import settings

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

[victory, arpege, fing_spread, wrap_fing]

cap = cv2.VideoCapture(0)
root_wind= 'main';
cv2.namedWindow(root_wind)

with mp_hands.Hands(max_num_hands = settings.nb_max_hands, min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():

        cv2.imshow
    
        if cv2.waitKey(10) & 0xFF == ord('x'):
                break