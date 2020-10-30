# django imports 
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


# Imports neccessary for the machine learning model
import cv2 as cv
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Class name for prediction of the model
class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']


def index(request):
    context = {"a" : 1}
    return render(request, 'index.html', context)



def predictImage(request):
    # File is being loaded and saved 
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name ,fileObj)
    filePathName = fs.url(filePathName)
    testimage='.'+filePathName


    # Model is loaded and saved into a variable
    saved_model = load_model('models/image-classifier.h5')

    # test image is given and preprocessed accordingly
    img = cv.imread(testimage)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    new_image = cv.resize(img, (32,32))

    # Predict function is executed and output is stored in a variable
    prediction = saved_model.predict(np.array([new_image])/255)
    index = np.argmax(prediction)
    prediction_label = class_names[index]


    context={'filePathName':filePathName,'predictedLabel':prediction_label}
    return render(request, 'index.html', context)
