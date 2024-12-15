import cv2 as cv
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from sklearn.preprocessing import LabelEncoder
import pickle
import tensorflow as tf
from keras_facenet import FaceNet

# Initialize FaceNet model
facenet = FaceNet()

# Load face embeddings and labels
faces_embeddings = np.load("faces_dataset.npz")
X, Y = faces_embeddings['arr_0'], faces_embeddings['arr_1']

# Initialize label encoder and fit it with labels
encoder = LabelEncoder()
encoder.fit(Y)

# Load Haarcascade face detector
haarcascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load pre-trained SVM model
model = pickle.load(open("svm_model.pkl", 'rb'))

# Start video capture
cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    res, frame = cap.read()
    if not res:
        break

    # Convert frame to RGB and grayscale
    rgb_img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = haarcascade.detectMultiScale(gray_img, 1.3, 5)

    for (x, y, w, h) in faces:
        # Extract the face from the RGB image
        img = rgb_img[y:y+h, x:x+w]
        img = cv.resize(img, (160, 160))
        img = np.expand_dims(img, axis=0)

        # Get the embedding for the face
        embedding = facenet.embeddings(img)

        # Predict the face name using the SVM model
        face_name = model.predict(embedding)
        final_name = encoder.inverse_transform(face_name)[0]

        # Draw a rectangle around the face and put the predicted name
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
        cv.putText(frame, final_name, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2, cv.LINE_AA)

    # Display the resulting frame
    cv.imshow("Face Recognition", frame)

    # Exit the loop when 'q' key is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv.destroyAllWindows()
