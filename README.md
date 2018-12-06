# Setup guide

## Other Documentation 
1 - Collecting Data

The training round will go about for two minutes in which the camera attached will take in images in resolution - 640 X 480. Considering 250ms are taken to capture one image, about 480 images will be taken in the training time. 

In the training round the car will be trained wirelessly using the Blynk app. At the same time the data in GPIO pins will be read using two pin combinations. Which are - 
FF - Move Straight Forward
FL - Move Left Forward
FR - Move Right Forward
NN - No Movement

Here we will get both images and decisions to be taken when similar situation is encountered. 

2 - Data Processing 

The images thus collected will be now thresholded and then preprocessed to make the image data ready for Neural Networks. The dataset will be now divided into two parts. 70% of the dataset will go to the Training set and the remaining 30% will go to the Test set. 

3 - Learning 

Now the data in Training set will be sent to the neural network which will analyze the image data by either 2 layer deep ANN or 3 layer deep CNN and the decisions taken per image during the training. Now, the neural network learning from the dataset provided will produce labels (FF,FR,FL or NN) as per image. 

Now, the so obtained labels will be compared with the test set to calculate the percentage error.


Live -

Now, during this phase the camera will take in live images, make a decision at real time and then send the data to the hardware. The image taken by the camera will be first Thresholded and Preprocessed and then will be sent to our model which will analyze the images in real time and create a label (FF, FR,FL or NN). The instruction will be sent to the hardware making the car move. 



## Control
### Camera.py

### Move.py


## Tests :
### Camera.py
To check the functionality of the Camera module.

### Move.py
To check the basic motor movemement for the car.
