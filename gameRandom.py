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

#[victory, arpege, fing_spread, wrap_fing]

cap = cv2.VideoCapture(0)
root_wind= 'main';
cv2.namedWindow(root_wind)
cv2.moveWindow(root_wind,400,0)


with mp_hands.Hands(max_num_hands = settings.nb_max_hands, min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        
        ret, frame = cap.read()
        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Flip on the horizontal
        image = cv2.flip(image, 1)
        # Set flag
        image.flags.writeable = False
        # Detections
        results = hands.process(image)
        # Set flag to True
        image.flags.writeable = True
        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


        cv2.imshow(root_wind,image)
        

        if cv2.waitKey(10) & 0xFF == ord('x'):
                break


cap.release()
cv2.destroyAllWindows()