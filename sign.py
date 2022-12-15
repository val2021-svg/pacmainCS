import cv2
import mediapipe as mp
import calcul
import settings
from math import *
import draw
from google.protobuf.json_format import MessageToDict

def victory(image, results):
    pos = calcul.pos_hand_landmarks(image,results)
    draw.draw_HAND(image, pos)

    #Victory or not
    a = calcul.eucli_length(pos[8],pos[12])
    b = calcul.eucli_length(pos[8],pos[0])
    c = calcul.eucli_length(pos[0],pos[12])            

    #Right or Left hand
    if calcul.handedness(results) == 'Right':

        if calcul.cos_alkashi(a,b,c) < cos(calcul.radian(10)) and calcul.cos_alkashi(a,b,c) > cos(calcul.radian(45)) and pos[12][0] > pos[8][0]:
            hand_status = "V"
            cv2.putText(image, hand_status, (50,80), 0, 1.5, (0,0,255), 2)
            cv2.putText(image, calcul.handedness(results), (settings.sh,80), 0, 1.5, (0,0,255), 2)
    
    else : 

        if calcul.cos_alkashi(a,b,c) < cos(calcul.radian(10)) and calcul.cos_alkashi(a,b,c) > cos(calcul.radian(25)) and pos[8][0] > pos[12][0]:
            hand_status = "V"
            cv2.putText(image, hand_status, (50,80), 0, 1.5, (0,0,255), 2)
            cv2.putText(image, calcul.handedness(results), (settings.sh,80), 0, 1.5, (0,0,255), 2)

def fing_spread(image, results):
    
    cv2.putText(image, "Spread your fingers", (50,80), 0, 1, (0,0,255), 2)
    cv2.putText(image, calcul.handedness(results), (settings.sh,80), 0, 1.5, (0,0,255), 2)
    pos = calcul.pos_hand_landmarks(image,results)
    draw.draw_HAND(image, pos)

    #distances to the wrist
    thumb = calcul.eucli_length(pos[0],pos[4])
    ind_fing = calcul.eucli_length(pos[0],pos[8])
    mid_fing = calcul.eucli_length(pos[0],pos[12])
    ring_fing = calcul.eucli_length(pos[0],pos[16])
    little_fing = calcul.eucli_length(pos[0],pos[20])

    #distances between fingers
    thumb_to_ind = calcul.eucli_length(pos[4],pos[8])
    ind_to_mid = calcul.eucli_length(pos[8],pos[12])
    mid_to_ring = calcul.eucli_length(pos[12],pos[16])
    ring_to_little = calcul.eucli_length(pos[16],pos[20])

    #spreaded or not
    if calcul.cos_alkashi(thumb_to_ind,thumb,ind_fing) < cos(calcul.radian(5)) and calcul.cos_alkashi(thumb_to_ind,thumb,ind_fing) > cos(calcul.radian(45)) :
        if calcul.cos_alkashi(ind_to_mid,mid_fing,ind_fing) < cos(calcul.radian(5)) and calcul.cos_alkashi(ind_to_mid,mid_fing,ind_fing) > cos(calcul.radian(45)) :
                if calcul.cos_alkashi(mid_to_ring,mid_fing,ring_fing) < cos(calcul.radian(5)) and calcul.cos_alkashi(mid_to_ring,mid_fing,ring_fing) > cos(calcul.radian(45)) :
                        if calcul.cos_alkashi(ring_to_little,ring_fing,little_fing) < cos(calcul.radian(5)) and calcul.cos_alkashi(ring_to_little,ring_fing,little_fing) > cos(calcul.radian(45)) :
                            cv2.putText(image, "GREAT!", (settings.sw//2,settings.sh//2), 0, 1, settings.GREEN, 6)
                            for i in range(21):
                                draw.color_pos(image, pos[i], settings.RED)


def arpege(image, results, steps):

    cv2.putText(image, "Match the red dots", (50,80), 0, 1, (0,0,255), 2)
    cv2.putText(image, calcul.handedness(results), (settings.sh,80), 0, 1.5, (0,0,255), 2)
    pos = calcul.pos_hand_landmarks(image,results)
    draw.draw_HAND(image, pos)
    
    #Condition of the cycle's end
    if steps[6] == 1 : 
        draw.draw_HAND(image, pos)

    #step1
    if steps[0] == 0 :
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[6], settings.RED)

    if calcul.eucli_length(pos[4],pos[6]) <= 40 and steps[0] == 0 :
        draw.draw_HAND(image, pos)
        steps[0] = 1
        
    #step2
    if steps[0] == 1 and steps[1] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[8], settings.RED)
        if calcul.eucli_length(pos[4],pos[8]) <= 40 :
            draw.draw_HAND(image, pos)
            steps[1] = 1
    
    #step3
    if steps[1] == 1 and steps[2] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[12], settings.RED)
        if calcul.eucli_length(pos[4],pos[12]) <= 40 :
            draw.draw_HAND(image, pos)
            steps[2] = 1
    
    #step4
    if steps[2] == 1 and steps[3] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[16], settings.RED)
        if calcul.eucli_length(pos[4],pos[16]) <= 40 :
            draw.draw_HAND(image, pos)
            steps[3] = 1

    #step4
    if steps[3] == 1 and steps[4] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[20], settings.RED)
        if calcul.eucli_length(pos[4],pos[20]) <= 40 :
            draw.draw_HAND(image, pos)
            steps[4] = 1
    
    #step5
    if steps[4] == 1 and steps[5] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[19], settings.RED)
        if calcul.eucli_length(pos[4],pos[19]) <= 40 :
            draw.draw_HAND(image, pos)
            steps[5] = 1
    
    #step6
    if steps[5] == 1 and steps[6] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[17], settings.RED)
        if calcul.eucli_length(pos[4],pos[13]) <= 40 :
            draw.draw_HAND(image, pos)
            steps[6] = 1
            

    
            
