from math import *
import mediapipe as mp
import settings
from google.protobuf.json_format import MessageToDict

#Computes the euclidian length between 2 points
def eucli_length(P1,P2):
    x1, y1, z1 = P1
    x2, y2, z2 = P2
    return sqrt((x1-x2)**2 + (y1-y2)**2 + (y1-y2)**2)

#Computes the cosinus opposed to the a segment with Alkashi's method
def cos_alkashi(a,b,c):
    return (b**2 + c**2 - a**2)/(2*b*c)

#Converts degrees into radians
def radian(x):
    return x*2*pi/360

#Creates an array composed of the 21 hand's landmarks 
def pos_hand_landmarks(image, results):
    for hand_landmarks in results.multi_hand_landmarks : 
        pos = []
        for i in range(21):
            xi, yi, zi = hand_landmarks.landmark[i].x*settings.sw, hand_landmarks.landmark[i].y*settings.sh, hand_landmarks.landmark[i].z*1500
            pos.append((xi, yi, zi))
    return pos

#Right or Left hand ? 
def handedness(results):
    for idx, hand_handedness in enumerate(results.multi_handedness):
                    handedness_dict = MessageToDict(hand_handedness)
                    whichHand =(handedness_dict['classification'][0]['label'])
                    return whichHand

        