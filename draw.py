import mediapipe as mp
import calcul
import settings
import cv2
import math
import time

# Draws the connexion between the hand's landmarks 
def draw_connex(image, pos):
    for i in range(4):
        cv2.line(image, (int(pos[i][0]), int(pos[i][1])), (int(pos[i+1][0]), int(pos[i+1][1])), settings.BLACK, 2)

    for i in range(3):
        cv2.line(image, (int(pos[i+5][0]), int(pos[i+5][1])), (int(pos[i+6][0]), int(pos[i+6][1])), settings.BLACK, 2)
        cv2.line(image, (int(pos[i+9][0]), int(pos[i+9][1])), (int(pos[i+10][0]), int(pos[i+10][1])), settings.BLACK, 2)
        cv2.line(image, (int(pos[i+13][0]), int(pos[i+13][1])), (int(pos[i+14][0]), int(pos[i+14][1])), settings.BLACK, 2)
        cv2.line(image, (int(pos[i+17][0]), int(pos[i+17][1])), (int(pos[i+18][0]), int(pos[i+18][1])), settings.BLACK, 2)

        cv2.line(image, (int(pos[4*i+5][0]), int(pos[4*i+5][1])), (int(pos[4*i+9][0]), int(pos[4*i+9][1])), settings.BLACK, 2)
    
    cv2.line(image, (int(pos[0][0]), int(pos[0][1])), (int(pos[5][0]), int(pos[5][1])), settings.BLACK, 2)
    cv2.line(image, (int(pos[0][0]), int(pos[0][1])), (int(pos[17][0]), int(pos[17][1])), settings.BLACK, 2)     

# Draws the hand's landmarks  
def draw_pos(image, pos):
    for (xi, yi, zi) in pos : 
        zi = math.floor(zi)
        cv2.circle(image, (int(xi), int(yi)), 5, (min(255, abs(zi)), 255 - min(255, abs(zi)), min(255, abs(zi))) , -1)

# Draws the hand
def draw_HAND(image, pos):
    draw_connex(image, pos)
    draw_pos(image, pos)

# Coloring a specific landmark
def color_pos(image, P, COLOR):
        x, y, z = P
        cv2.circle(image, (int(x), int(y)), 5, COLOR, -1)

# Coloring the hand in a specific color 
def color_HAND(image, pos, COLOR):
    for i in range(len(pos)):
            color_pos(image, pos[i], COLOR)

# Draw the good job image
def breakIm(image):
    cv2.rectangle(image, (0, 0), (settings.sw, settings.sh), settings.GREEN, -1)
    cv2.putText(image, "GREAT", (settings.sw // 2 - 20, settings.sh // 2), 0, 1, settings.WHITE, 4)


    
