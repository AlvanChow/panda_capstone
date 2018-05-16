#Import Necessary Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from PIL import Image
import keras

#Initialize Neural Network as Sequential Network
from keras.models import Sequential
from keras.models import model_from_json
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


# load json and create model

def import_and_load_model(json_file_import = 'classifier_3_layer.json', h5_file_import = 'classifier_3_layer.h5'):
    # load json and create model
    json_file = open(json_file_import, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(h5_file_import)
    print("Loaded model from disk")

    return loaded_model

# import_and_load_model()


def predict_panda(import_image = 'animal_dataset/prediction_set/dog.jpeg'):
    loaded_model = import_and_load_model()
    test_image = image.load_img(import_image, target_size=(64,64))
    plt.imshow(test_image)
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = loaded_model.predict(test_image)
    if result[0][0] == 1:
        prediction = 'panda'
    elif result[0][0] == 0:
        prediction = 'not panda'
    print(prediction)

predict_panda()
