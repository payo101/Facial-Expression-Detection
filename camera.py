# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:53:27 2021

@author: piyus
"""

import numpy as np
import cv2 as cv

faceDetector = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Exiting ...")
        break
    
    #detection
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rects = faceDetector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in rects:
    	cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
