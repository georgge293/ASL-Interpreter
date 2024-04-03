import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import LabelEncoder

# Load data from pickle file
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
    X = data['landmarkData']  # Features
    y = data['labels']  # Labels

y = list(map(int, y))
X = np.array(X, dtype=float)  # Assuming your features are numerical
y = np.array(y, dtype=int)  # Assuming your labels are already encoded as integers or one-hot encoded


# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, stratify=y)

# Define the model
model = models.Sequential([
    layers.Dense(64, activation='relu', input_shape=(len(X_train[0]),)),
    layers.Dropout(0.5),
    layers.Dense(32, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(29, activation='softmax')  # Output layer for 29 classes
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',  # Use this loss function for integer labels
              metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=100, validation_split=0.2)

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f'\nTest accuracy: {test_acc}, Test loss: {test_loss}')

f = open('modelT.p', 'wb')
pickle.dump({'modelT': model}, f)
f.close()