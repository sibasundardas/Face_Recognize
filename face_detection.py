import pickle

with open(r"C:\Users\sibas\OneDrive\Desktop\Face Detection\Face_Detection\data\images.p","rb") as f:
  images = pickle.load(f)

with open(r"C:\Users\sibas\OneDrive\Desktop\Face Detection\Face_Detection\data\labels.p","rb") as f:
  labels = pickle.load(f)

print(images.shape)
print(labels.shape)

set(labels)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

labels = le.fit_transform(labels)

set(labels)

le.inverse_transform([0,1])

p = len(set(labels))
print("Total number of Persons : ",p)

import matplotlib.pyplot as plt
plt.imshow(images[15],cmap='gray')
plt.show()

import cv2

def preprocessing(img):
  img = cv2.equalizeHist(img)
  img = img.reshape(100,100,1)
  img = img/255
  return img

import numpy as np

images = np.array(list(map(preprocessing,images)))
print("Shape of Input : ",images.shape)

from keras.utils import to_categorical
labels = to_categorical(labels)

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

from keras.layers import Conv2D, MaxPooling2D, Flatten

#Model Training
def Lenet_Model():
  model = Sequential()
  #Convolutional and ReLU Layer
  model.add(Conv2D(30,(5,5),input_shape=(100,100,1),activation='relu'))
  #MaxPooling Layer
  model.add(MaxPooling2D(pool_size=(2,2)))

  #Convolutional and ReLU Layer
  model.add(Conv2D(15,(3,3),activation='relu'))
  #MaxPooling Layer
  model.add(MaxPooling2D(pool_size=(2,2)))

  #Flatten Layer/Input Layer
  model.add(Flatten())

  #Hidden Layers
  model.add(Dense(50,activation='relu'))
  model.add(Dense(30,activation='relu'))

  #Output Layer
  model.add(Dense(p,activation='softmax'))
  model.compile(Adam(learning_rate=0.01),loss='categorical_crossentropy',metrics=['accuracy'])
  return model

model = Lenet_Model()
model.summary()

h = model.fit(images,labels,validation_split=0.1,epochs=25)

model.save('facedetection_model.h5')

