# ASLtoTTS

https://github.com/georgge293/ASL-Interpreter/assets/58405210/ba323e71-c2dd-445b-8a9f-9b4c8b1b6b1b

<p align="center">
  Full-stack web application that utilizes the user's webcam to interpret American Sign Language (ASL) gestures. It continuously checks the webcam feed to recognize hand gestures and analyze the landmark positioning on the person's hand to determine the corresponding ASL letter. The interpreted letter is then displayed in a textbox using Text to Speech for accessibility.
</p>

## Features:
- Real-time hand gesture recognition using the webcam
- Analysis of landmark positioning for accurate ASL letter determination
- Output displayed in a textbox with Text to Speech functionality
- Users have the option to train the model for improved accuracy

## Tech Stack
- Frontend: [React](https://reactjs.org/)
- Backend: [Python](https://www.python.org/))
- Machine Learning: [TensorFlow](https://www.tensorflow.org/), [OpenCV](https://opencv.org/)

## Getting Started:

To run locally we must run the backend script and frontend seperately each in a different powershell tab

1. Clone this repository
```bash
git clone https://github.com/georgge293/ASL-Interpreter.git
```

2. Run backend script
```bash
cd pythonScripts
python main.py
```

3. Run Frontend react app
```bash
cd frontend
npm install
npm start
```
