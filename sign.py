import cv2
import calcul
import settings
from math import *
import draw
import random

def victory(image, results):

    pos = calcul.pos_hand_landmarks(image,results)
    draw.draw_HAND(image, pos)

    # Victory or not
    a = calcul.eucli_length(pos[8],pos[12])
    b = calcul.eucli_length(pos[8],pos[0])
    c = calcul.eucli_length(pos[0],pos[12])            

    # Right or Left hand
    if calcul.handedness(results) == 'Right':

        if calcul.cos_alkashi(a,b,c) < cos(calcul.radian(10)) and calcul.cos_alkashi(a,b,c) > cos(calcul.radian(45)) and pos[12][0] > pos[8][0]:
            hand_status = "V"
            cv2.putText(image, hand_status, (50,80), 0, 1.5, settings.RED, 2)
            cv2.putText(image, calcul.handedness(results), (settings.sh,80), 0, 1.5, settings.RED, 2)
    
    else : 

        if calcul.cos_alkashi(a,b,c) < cos(calcul.radian(10)) and calcul.cos_alkashi(a,b,c) > cos(calcul.radian(25)) and pos[8][0] > pos[12][0]:
            hand_status = "V"
            cv2.putText(image, hand_status, (50,80), 0, 1.5, settings.RED, 2)
            cv2.putText(image, calcul.handedness(results), (settings.sh,80), 0, 1.5, settings.RED, 2)
            

def fing_spread(image, results, steps):
    
    cv2.putText(image, "Spread your fingers", (50,80), 0, 1, settings.RED, 2)
    cv2.putText(image, calcul.handedness(results), (settings.sh,80), 0, 1.5, settings.RED, 2)
    pos = calcul.pos_hand_landmarks(image,results)
    draw.draw_HAND(image, pos)

    # spreaded or not
    if not calcul.little_wrap(pos):
        if calcul.spread(pos):
            cv2.putText(image, "GREAT!", (settings.sw//2,settings.sh//2), 0, 1, settings.GREEN, 6)
            for i in range(21):
                draw.color_pos(image, pos[i], settings.RED)
            steps[1] = 1
            draw.breakIm(image)

def wrap_fing(image, results, steps):

    cv2.putText(image, "Wrap your fingers", (50,80), 0, 1, settings.RED, 2)
    cv2.putText(image, calcul.handedness(results), (settings.sh,80), 0, 1.5, settings.RED, 2)
    pos = calcul.pos_hand_landmarks(image,results)
    draw.draw_HAND(image, pos)

    if pos[0][1]>pos[1][1]:
        if calcul.really_wrap(pos):
            cv2.putText(image, "MAGNIFICENT!", (settings.sw//2 - 30,settings.sh//2), 0, 1, settings.GREEN, 6)
            for i in range(21):
                draw.color_pos(image, pos[i], settings.RED)
            steps[1] = 1
            draw.breakIm(image)
        
        elif calcul.little_wrap(pos):
            cv2.putText(image, "GREAT!", (settings.sw//2 - 20,settings.sh//2), 0, 1, settings.GREEN, 6)
            for i in range(21):
                draw.color_pos(image, pos[i], settings.RED)


def arpege(image, results, steps):

    cv2.putText(image, "Match the red dots", (50,80), 0, 1, (0,0,255), 2)
    cv2.putText(image, calcul.handedness(results), (settings.sh,80), 0, 1.5, settings.RED, 2)
    pos = calcul.pos_hand_landmarks(image,results)
    draw.draw_HAND(image, pos)
    
    # Condition of the cycle's end
    if steps[6] == 1 : 
        draw.draw_HAND(image, pos)

    # step1
    if steps[0] == 0 :
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[6], settings.RED)

    if calcul.eucli_length(pos[4],pos[6]) <= 35 and steps[0] == 0 :
        draw.draw_HAND(image, pos)
        steps[0] = 1
        
    # step2
    if steps[0] == 1 and steps[1] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[8], settings.RED)
        if calcul.eucli_length(pos[4],pos[8]) <= 30 :
            draw.draw_HAND(image, pos)
            steps[1] = 1
    
    # step3
    if steps[1] == 1 and steps[2] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[12], settings.RED)
        if calcul.eucli_length(pos[4],pos[12]) <= 30 :
            draw.draw_HAND(image, pos)
            steps[2] = 1
    
    # step4
    if steps[2] == 1 and steps[3] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[16], settings.RED)
        if calcul.eucli_length(pos[4],pos[16]) <= 30 :
            draw.draw_HAND(image, pos)
            steps[3] = 1

    # step4
    if steps[3] == 1 and steps[4] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[20], settings.RED)
        if calcul.eucli_length(pos[4],pos[20]) <= 30 :
            draw.draw_HAND(image, pos)
            steps[4] = 1
    
    # step5
    if steps[4] == 1 and steps[5] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[19], settings.RED)
        if calcul.eucli_length(pos[4],pos[19]) <= 45 :
            draw.draw_HAND(image, pos)
            steps[5] = 1
    
    # step6
    if steps[5] == 1 and steps[6] == 0:
        draw.color_pos(image, pos[4], settings.RED)
        draw.color_pos(image, pos[17], settings.RED)
        if calcul.eucli_length(pos[4],pos[13]) <= 30 :
            draw.draw_HAND(image, pos)
            steps[6] = 1
            draw.breakIm(image)

            
def thumb_mouv(image, results, steps):
    cv2.putText(image, "Match the red dot with your thumb", (50,80), 0, 0.7, settings.RED, 2)
    cv2.putText(image, calcul.handedness(results), (settings.sh,80), 0, 1.5, settings.RED, 2)
    pos = calcul.pos_hand_landmarks(image,results)
    draw.draw_HAND(image, pos)

    thumb_angle = calcul.cos_alkashi(calcul.eucli_length(pos[4], pos[5]), calcul.eucli_length(pos[4], pos[0]), calcul.eucli_length(pos[5], pos[0]))

    if steps[1] == 1 :
        draw.draw_HAND(image, pos)

    # the red dot
    if steps[0] == 0 : 
        draw.color_pos(image, pos[17], settings.RED)

    # closed thumb
    if steps[0] == 0 and calcul.eucli_length(pos[4], pos[17]) < 60 : 
        draw.draw_HAND(image, pos)
        steps[0] = 1
        
    
    # opened thumb
    if steps[0] == 1 and steps[1] == 0 :
        cv2.putText(image, "Then stretch your thumb", (50,110), 0, 0.7, settings.RED, 2)
        draw.color_HAND(image, pos, settings.RED)

        if thumb_angle < cos(calcul.radian(35)) and thumb_angle > cos(calcul.radian(90)) :
            if calcul.handedness(results)=='Right' and pos[4][0] < pos[5][0]:
                steps[1] = 1
                draw.breakIm(image)
               
            elif calcul.handedness(results)=='Left' and pos[4][0] > pos[5][0]:
                steps[1] = 1
                draw.breakIm(image)
                

# randomizes the order of the exercises
def random_signs(sign_list):
    rd_list = []

    while len(sign_list) != 0:
        i = random.randint(0,len(sign_list)-1)
        rd_list.append(sign_list[i])
        del sign_list[i]

    return rd_list

# finds the correct function to execute
def find_sign_func(sign_name, image, results, steps):
    if sign_name == 'fing_spread':
        return fing_spread(image, results, steps)
    
    elif sign_name == 'wrap_fing':
        return wrap_fing(image, results, steps)

    elif sign_name == 'arpege':
        return arpege(image, results, steps)
    
    elif sign_name == 'thumb_mouv':
        return thumb_mouv(image, results, steps)




    


            
