import cv2
import numpy as np
from keras.models import load_model

classifier = cv2.CascadeClassifier(r"C:\Users\sibas\OneDrive\Desktop\Face Detection\Face_Detection\haarcascade_frontalface_default.xml")
model = load_model(r"C:\Users\sibas\OneDrive\Desktop\Face Detection\Face_Detection\facedetection_model.h5")

def get_pred_label(pred):
    labels = ["Pritam", "Santosh", "Siba", "Sonu"]
    return labels[pred]

def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (100, 100))
    img = cv2.equalizeHist(img)
    img = img.reshape(1, 100, 100, 1)
    img = img / 255
    return img

cap = cv2.VideoCapture(0)  # Use default webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = classifier.detectMultiScale(frame, 1.5, 5)

    for x, y, w, h in faces:
        face = frame[y:y + h, x:x + w]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        pred = model.predict(preprocess(face))
        label = get_pred_label(np.argmax(pred))
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("capture", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
