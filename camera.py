# -*- coding: utf-8 -*-
"""
Created on Thu May 27 11:53:27 2021

@author: piyus
"""

import numpy as np
import cv2
from model import ExpressionClassifier

faceDetector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

classifier = ExpressionClassifier('model.json', 'weights.h5')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Exiting ...")
        break

    frame = cv2.flip(frame, 1)
    # detection
    face_img = np.array([])
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = faceDetector.detectMultiScale(
        gray, scaleFactor=1.23, minNeighbors=5)
    for (x, y, w, h) in rects:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # input preprocessing
        face_img = gray[y:y+h, x:x+w]
        roi = cv2.resize(face_img, (48, 48))
        roi = roi[np.newaxis, :, :, np.newaxis]

        emotion = classifier.return_emotions(roi)
        print(emotion)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
