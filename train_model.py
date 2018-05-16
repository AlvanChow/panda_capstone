#Import Necessary Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import os
from PIL import Image
import keras
#Initialize Neural Network as Sequential Network
from keras.models import Sequential
#Images are 2D arrays, so import Conv2D. If videos, import 3D with time as the third dimension
from keras.layers import Convolution2D
#Import Max Pooling because we need the highest value pixel from the area of interest
from keras.layers import MaxPooling2D
#Convert 2D arrays into a singular vector
from keras.layers import Flatten
#Perform full connection of neural network
from keras.layers import Dense
#Include random dropout nodes
from keras.layers import Dropout
#import image data generator library
from keras.preprocessing.image import ImageDataGenerator
#Image prepreprocessing
from keras.preprocessing import image


#Create Sequential Neural Network
classifier2 = Sequential()
#32 feature detectors of 3 by 3 dimensions, to create 32 feature maps
classifier2.add(Convolution2D(32,(3,3), input_shape=(64,64,3), activation='relu'))
#Pooling size 2 by 2, pick the largest value pixel
classifier2.add(MaxPooling2D(pool_size=(2,2)))
#Add second convolution
classifier2.add(Convolution2D(32,(3,3), input_shape=(64,64,3), activation='relu'))
#Pooling of second convolutional layer
classifier2.add(MaxPooling2D(pool_size=(2,2)))
#Add third convolution with 64 feature extractors
classifier2.add(Convolution2D(64,(3,3), input_shape=(64,64,3), activation='relu'))
#Pooling of third convolutional layer
classifier2.add(MaxPooling2D(pool_size=(3,3)))
#Flatten to feed into ANN
classifier2.add(Flatten())
#128 hidden nodes in the hidden layer
classifier2.add(Dense(units = 128, activation='relu'))
#Random dropout of 50% chance
# classifier2.add(Dropout(0.5))
#One final output
classifier2.add(Dense(units = 1, activation='sigmoid'))
#Adam optimizer: stochastic gradient descent algorithm
#Binary Cross Entropy Loss Function: because this corresponds to logarithmic loss used for classification
#Also because binary outcome
#If more than 2 outcomes, use categorical cross entropy
classifier2.compile(optimizer='adam', loss = 'binary_crossentropy', metrics=['accuracy'])
