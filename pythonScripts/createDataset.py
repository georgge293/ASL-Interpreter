import os
import mediapipe
import sys
import pickle

import matplotlib.pyplot as plot
import cv2

hands = mediapipe.solutions.hands
drawing = mediapipe.solutions.drawing_utils
drawingStyles = mediapipe.solutions.drawing_styles

mpHands = hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data'

landmarkData = []
labels = []

for imgsList in os.listdir(DATA_DIR):
    imgList = os.listdir(os.path.join(DATA_DIR, imgsList))
    for imgPath in imgList:
        landmarkCoords = []
        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, imgsList, imgPath))
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        landmarks = mpHands.process(imgRGB)
        if landmarks.multi_hand_landmarks:
            for handLandmarks in landmarks.multi_hand_landmarks:
                for i in range(len(handLandmarks.landmark)):
                    x = handLandmarks.landmark[i].x
                    y = handLandmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(handLandmarks.landmark)):
                    x = handLandmarks.landmark[i].x
                    y = handLandmarks.landmark[i].y
                    landmarkCoords.append(x - min(x_))
                    landmarkCoords.append(y - min(y_))
                    
                


            landmarkData.append(landmarkCoords)
            labels.append(imgsList)
        

f = open('data.pickle', 'wb')
pickle.dump({'landmarkData': landmarkData, 'labels': labels}, f)
f.close()