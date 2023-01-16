import cv2
import os
import numpy as np
import urllib.request
from tensorflow import keras
from tensorflow.keras.preprocessing.image import img_to_array


model = keras.models.load_model('models')

method = int(input("Link of local image ( 1 for link, 2 for local image ) :"))

if method == 1:
    imagelinkinput = input("Paste the link ( must end with '.jpg', '.png', etc. ) :")
    req = urllib.request.urlretrieve(imagelinkinput, "result/photo.png")
    image = cv2.imread("result/photo.png")
    image = cv2.resize(image,(224,224),3)

    image = img_to_array(image)

    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    result = model.predict(image)

    prediction = model.predict(image)
    if prediction > 0.5:
        os.rename("result/photo.png", "result/dog.png")
        print("You have a dog on the image")
    else:
        os.rename("result/photo.png", "result/cat.png")
        print("You have a cat on the image")
else:
    imagedirectoryinput = input("Type the directory ( must end with '.jpg', '.png', etc. ) :")

    image = cv2.imread(imagedirectoryinput)
    image = cv2.resize(image,(224,224),3)

    image = img_to_array(image)

    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    result = model.predict(image)

    prediction = model.predict(image)
    if prediction > 0.5:
        print("You have a dog on the image")
    else:
        print("You have a cat on the image")