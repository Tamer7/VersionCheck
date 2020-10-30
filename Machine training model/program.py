import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models
from PIL import Image



# We get the training dataset from the keras library
# We split the data into training and testing for better result of our model
(training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()

# Pre-processing the data
# We divide the image pixel of our data by 255 to make the image easier to work with
training_images, testing_images = training_images/255, testing_images/255

# Labels are defined in particular order as shown in the keras documentation
class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

# Creating the model
# Model is created for a 32 by 32 input and consists of a Convulutional and MaxPooling layers
model = models.Sequential()
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))


# Model is complied using adam optimizer and we show the metrics 
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Training images and labels are fitted into to model for training
# we set a number of epochs for how many times we want our data to keep loading in our model
model.fit(training_images, training_labels, epochs=15, validation_data=(testing_images, testing_labels), shuffle=True)

# Model is saved by using the .save method and can be used later
#  instead of training the whole neural network again
model.save('image-classifier.h5')

loss, accuracy = model.evaluate(testing_images, testing_labels)
print('Loss : ', loss)
print('Accuracy : ', accuracy)


# Model is loaded and saved into a variable
saved_model = models.load_model('image-classifier.h5')

# test image is given and preprocessed accordingly
img = cv.imread('Images/test6.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
new_image = cv.resize(img, (32,32))
plt.imshow(new_image, cmap=plt.cm.binary)

prediction = saved_model.predict(np.array([new_image])/255)
index = np.argmax(prediction)

# Prediction of the image is displayed
print("Prediction is : ", class_names[index])


