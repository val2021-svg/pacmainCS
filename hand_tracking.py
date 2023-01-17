import mediapipe as mp
import cv2
from math import *
import sign
import settings
import time
import draw

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
rd_list = sign.random_signs(settings.list_of_signs)


######################################## DRAW HANDS ###############################################
cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands = settings.nb_max_hands, min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    steps = [0]*7
    i, weight = 0, 0
    
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

        # Rendering results
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks : 
                if rd_list[i] == 'arpege':
                    print('arpege', steps)
                    if steps[6] == 0 : 
                        sign.find_sign_func(rd_list[i], image, results, steps)
                    else : 
                        steps = [0]*7
                        weight += 1
                        time.sleep(4)
                        
                        if weight == 4 :
                            i += 1 
                            weight = 0
                            time.sleep(4)
                else :
                    print(rd_list[i], steps)
                    if steps[1] == 0:
                        sign.find_sign_func(rd_list[i], image, results, steps)
                    else : 
                        steps = [0]*7
                        weight += 1
                        time.sleep(4)
                        
                        if weight == 4 :
                            i += 1 
                            weight = 0
                            time.sleep(4)
            
                

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('x') or i == len(rd_list): # type 'x' on your keyboard to close the window                                                          
            break                                                   # or finish the game

cap.release()
cv2.destroyAllWindows()
