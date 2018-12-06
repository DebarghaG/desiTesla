
# Please make sure OpenCV, Numpy and Keras are satisfied as dependencies.
from keras.models import model_from_json
import cv2
import numpy as np

def Initialise_Model():
    #Loading the model from the JSON model.
    json_file = open('./model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    #Loading the model weights.
    loaded_model.load_weights("./model.h5")
    print("Done loading the model...")

    #Compiling the data from the weights.
    loaded_model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    #Loading the image that needs to be tested and scaling down to a 50 by 50 pixel image.
    image = cv2.imread('/Users/prajwalseth/Downloads/all/train/a.0.jpg')
    image = cv2.resize(image, (50,50))
    image = image.reshape(1, 50, 50, 3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Predict():
    #Doing the prediction
    result = loaded_model.predict_classes(image)
    print(result)
    print (result[0][0])
    if(result[0][0] == 1):
        print("Direction : Go Right")
    else:
        print("Direction : Go Left")

Initialise_Model()
Predict()
