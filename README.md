# Setup guide

##User File Manual :
AutoDrive Engine :
Drive.py : Main python script to be able to execute all the necessary functionalities.
Move.py : Contains the functions that allow the car to be able to drive, is used as an utility script.
Prediction.py : Contains the code that makes the prediction from the saved model, for a given image captured at a certain point in the path.

Car Brain :
MultiClass-CNN-Train.py : Training script for the convolutional neural network to create a model from the training images and their relevant classifications. This model is then saved in JSON format, which can be used for prediction by the AutoDrive Engine.

Data Gathering :
DataCollection.py : Collects images with the associated direction steering angle with a delay of 0.25 seconds.
Namecut.sh : Shell script to cut the label out of the name for the test data for the model.
PinRead.py : Helper Python script that reads the direction of the steering by monitoring signals being transmitted through memory mapped I/O. ( They’re shorted with each other )
SortByDirection.py : Python script to split the data 70:30 and put into the required directory structure.
SortByDirection.sh : Shell script to generally split the images in a 70:30 ratio.
SplitFolders.sh : Shell script to be able to split the data into 70:30 ratio, by the label into training and test data.

Datasets:
'4 Dec - Ignore' :
'Clean Data'
'Clean Data - FL'
'Clean Data - NN'
'5 Dec FR - Ignore'
'Clean Data - FF'
'Clean Data - FR'

Proof Of Concepts
Cascade Classifier : Proof of Concept that a Haar-Cascade classifier that detects stop lights and traffic lights. ( XML pre-trained (1))
Direction Classifier : Proof of concept that a CNN can be used to predict steering directions for a given image.
Image Processing : Proof of Concept : applies a range of image processing methods to the images to be able to better extract meaningful information from it.

Tests
Test-Camera.py : Diagnostic script to check if the website is working.
Test-Controls.py : Diagnostic script to make sure all the motors are working and up to scratch.





## Control
### Camera.py

### Move.py


## Tests :
### Camera.py
To check the functionality of the Camera module.

### Move.py
To check the basic motor movemement for the car.

## Machine Learning on Cloud
### Amazon Web Services API Gateway
To make our car faster and cost effective, the complete machine learning algorithm is running on Cloud. The device sends an API request to our instance on cloud through a URL and API Key, referred to as the "startpoint"

### Amazon Web Services Lambda
On receiving the API startpoint, the request is then forwarded to the AWS Lambda, where an instantaneous instance is spinned to serve our python code. The python code runs and logs the data in AWS CloudWatch. The result is returned to the API Return Node. The API Return Node return node data is finally received by the user.
