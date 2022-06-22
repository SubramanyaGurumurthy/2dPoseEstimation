import imp
import cv2
import mediapipe as mp
import numpy as np
import time
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

######################
wCam, hCam = 1280, 720
######################

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volumeRange = volume.GetVolumeRange()

minVol = volumeRange[0]
maxVol = volumeRange[1]

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(detectionCon=0.7)
volBar = 400
vol = 0

volPer = np.interp(int(volume.GetMasterVolumeLevel()), [minVol, maxVol], [0, 100])


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) //2, (y1 + y2) //2 

        cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (0, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

        length = math.hypot(x2 - x1, y2-y1)
        print(volume.GetMasterVolumeLevel())
        
        
        # hand range 40 to 220
        # volume range -65 to 0
        vol = np.interp(length, [30, 260], [minVol, maxVol])
        volBar = np.interp(length, [30, 260], [400, 150])
        volPer = np.interp(length, [30, 260], [0, 100])
        # print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

    cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 50), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 0, 50), cv2.FILLED)
    cv2.putText(img, f'FPS: {int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 3)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime    

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow("img", img)
    cv2.waitKey(1)