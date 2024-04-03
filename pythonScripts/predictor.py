import pickle
import cv2
import mediapipe
import numpy as np

def runCamera(frame):
    modelDict = pickle.load(open('./model.p', 'rb'))
    model = modelDict['modelT']


    hands = mediapipe.solutions.hands

    mpHands = hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

    labels_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25:'z', 26: ' ', 27: '\b', 28: 'C'}


    landmarkCoords = []
    x_ = []
    y_ = []


    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = mpHands.process(frame_rgb)
    if results.multi_hand_landmarks:

        for handLandmarks in results.multi_hand_landmarks:
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

        if len(landmarkCoords) == 42:
            landmarkCoords = np.expand_dims(landmarkCoords, axis=0)
            prediction = model([np.asarray(landmarkCoords)])
            predictedIndex = np.argmax(prediction[0])  # This finds the index of the highest probability
            predictedCharacter = labels_dict[predictedIndex]
            return predictedCharacter
    return ""

