import cv2
import time
import numpy as np
import HandTrackingModule

##########################
wCam,hCam=640,480
##########################

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,wCam)
pTime=0
cTime=0

while True:
    success,img=cap.read()

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,f'FPS:{int(fps)}',(40,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,255),3)

    cv2.imshow("Img",img)
    cv2.waitKey(1)