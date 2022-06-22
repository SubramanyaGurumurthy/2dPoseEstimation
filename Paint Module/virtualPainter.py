from sre_constants import SUCCESS
import cv2
from cv2 import determinant
from matplotlib import image
import mediapipe as mp
import numpy as np
import os
import time

from requests import head
import HandTrackingModule as htm


################################
brushThickness = 15
eraserThickness = 75
################################

folderPath = "images"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    cv2.resize(image, [125, 1280])
    overlayList.append(image)

print(len(overlayList))
header = overlayList[0]
drawColor = (255, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon= 0.85)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    # step1: import images
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # step2: Find hand landmarks
    img = detector.findHands(img, False)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # print(lmList)

        # index finger tip
        x1, y1 = lmList[8][1:]
        # middle finger tip
        x2, y2 = lmList[12][1:]

        # step3: Check which fingers are up

        fingers = detector.fingersUp()
        # print(fingers)

        # step4: selection mode - when 2 fingers are up
        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            cv2.rectangle(img, (x1, y1-25), (x2, y2+25), (255, 0, 255), cv2.FILLED)
            print("selection mode")
            if y1 < 125:
                if 150 < x1 < 350: 
                    header = overlayList[0]
                    cv2.rectangle(img, (150, 0), (350, 125), (255, 0, 255), 10)
                    drawColor = (255, 0, 255)
                
                elif 450 < x1 < 650: 
                    header = overlayList[1]
                    cv2.rectangle(img, (450, 0), (650, 125), (255, 0, 255), 10)
                    drawColor = (255, 0, 0)

                elif 750 < x1 < 950: 
                    header = overlayList[2]
                    cv2.rectangle(img, (750, 0), (950, 125), (255, 0, 255), 10)
                    drawColor = (0, 255, 0)

                elif 1050 < x1 < 1200: 
                    header = overlayList[3]
                    cv2.rectangle(img, (1020, 0), (1200, 125), (255, 0, 255), 10)
                    drawColor = (0, 0, 0)
            
            cv2.rectangle(img, (x1, y1-25), (x2, y2+25), drawColor, cv2.FILLED)

        # step5: If drawing mode, when index finger is up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            print("drawing mode")
            
            if xp ==0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)                
            
            cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
            cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
            xp, yp = x1, y1
            

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # setting the header image
    img[0:125, 0:1280] = header
    img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
    cv2.imshow("image",img)
    # cv2.imshow("canvas",imgCanvas)
    cv2.waitKey(1)