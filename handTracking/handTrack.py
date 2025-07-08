import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('Camera is not opened')

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    

    cv.imshow('Video', img)
    k = cv.waitKey(1)
    if k == ord('q'):
        break

    
cap.release()
cv.destroyAllWindows()