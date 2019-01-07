# Setup guide

##User File Manual :
AutoDrive Engine :
Drive.py : Main python script to be able to execute all the necessary functionalities.
Move.py : Contains the functions that allow the car to be able to drive, is used as an utility script.
Prediction.py : Contains the code that makes the prediction from the saved model, for a given image captured at a certain point in the path.

Car Brain :
# PROJECT REPORT

## DESI TESLA

```
Contributors : 

Debargha Ganguly
Prajwal Seth
Shekhar Chatterjee
Sarthak Dangwal
```
### Abstract : ​​ In this paper, we hypothesize and test a development platform to learn, prototype,

_experiment with building a scaled down version of autonomous vehicles. The final objective of
the project was to be able to drive around a track, based on previous training. Due to hardware
limitations, and track inconsistencies, the vehicle wasn’t very accurate with it’s path planning
and lane following activities, however our results prove that with cleaner data and hardware with
better capabilities, this prototype could successfully be used as a testing platform for
autonomous vehicles._
**Introduction:**
An autonomous car can operate without human and does not require any human intervention.
The modern autonomous vehicles can sense their local environment, classify different kinds of
objects that they detect, can interpret sensory information to identify appropriate navigation
paths whilst obeying transportation rules. Considerable advancements have been made in
giving an appropriate response to unanticipated circumstances where either a backlash can
occur in the vehicular system or some medium in the external environment may not behave as
predicted by internal prototypes.
A self-driving car, also known as a robot car, autonomous car, auto, or driverless car, is a
vehicle that is capable of sensing its environment and moving with little or no human input.
Autonomous cars combine a variety of sensors to perceive their surroundings, such as radar,
computer vision, Lidar, sonar, GPS, odometry and inertial measurement units. Advanced control
systems interpret sensory information to identify appropriate navigation paths, as well as
obstacles and relevant signage. Potential benefits include reduced costs, increased safety,
increased mobility, increased customer satisfaction and reduced crime. Safety benefits include
a reduction in traffic collisions, resulting in injuries and related costs, including for insurance.
Automated cars are predicted to increase traffic flow; provide enhanced mobility for children, the
elderly, disabled, and the poor; relieve travellers from driving and navigation chores; lower fuel
consumption; significantly reduce needs for parking space; reduce crime; and facilitate business
models for transportation as a service, especially via the sharing economy.



**Getting Started :**
The hardware we’ve used:
1.)1/18 scale Remote Control Car
a.)Two brushed motors.
b.)Steering mechanism.
2.)Raspberry Pi 3 B+
3.)L298D Dual H Bridge Motor Driver.
4.)5,000 mAh Battery. X (2)
5.)PiCam 5MP Module R1.
**User File Manual :
AutoDrive Engine :**
Drive.py : Main python script to be able to execute all the necessary functionalities.
Move.py : Contains the functions that allow the car to be able to drive, is used as an utility script.
Prediction.py : Contains the code that makes the prediction from the saved model, for a given
image captured at a certain point in the path.
**Car Brain :**
MultiClass-CNN-Train.py : Training script for the convolutional neural network to create a model
from the training images and their relevant classifications. This model is then saved in JSON
format, which can be used for prediction by the AutoDrive Engine.
**Data Gathering :**
DataCollection.py : Collects images with the associated direction steering angle with a delay of
0.25 seconds.
Namecut.sh : Shell script to cut the label out of the name for the test data for the model.
PinRead.py : Helper Python script that reads the direction of the steering by monitoring signals
being transmitted through memory mapped I/O. ( They’re shorted with each other )
SortByDirection.py : Python script to split the data 70:30 and put into the required directory
structure.
SortByDirection.sh : Shell script to generally split the images in a 70:30 ratio.
SplitFolders.sh : Shell script to be able to split the data into 70:30 ratio, by the label into training
and test data.
**Datasets:**
'4 Dec - Ignore' :
'Clean Data'
'Clean Data - FL'
'Clean Data - NN'
'5 Dec FR - Ignore'
'Clean Data - FF'
'Clean Data - FR'


**Proof Of Concepts**
Cascade Classifier : Proof of Concept that a Haar-Cascade classifier that detects stop lights and
traffic lights. ( XML pre-trained (1))
Direction Classifier : Proof of concept that a CNN can be used to predict steering directions for a
given image.
Image Processing : Proof of Concept : applies a range of image processing methods to the
images to be able to better extract meaningful information from it.
**Tests**
Test-Camera.py : Diagnostic script to check if the website is working.
Test-Controls.py : Diagnostic script to make sure all the motors are working and up to scratch.
**Website**
The website has been designed using Bootstrap, Swiper, Owl Carousel, jQuery, CSS and
JavaScript.
**Setup for the Car :**
The following
connections have to
be set up for writing
control to the pins
and reading the
direction for the
specific pins.
We’re using a L298D motor
driver to be able to control the
motors according the pulses sent
by the on-board Raspberry Pi.
Since the power drawn is
substantially high, an external
power source is needed to be
connected to be able to provide
enough power to the motors.
( 2 A - 7 V - 14 Watts at peak.)


**Approach adopted towards solving the problem :
● The track :**
We have chosen to replicate the Monza circuit, one of the most famous grand prix in the world
notorious for its long sweeping bends and it’s few tight corners followed by high speed
straights.
This seemed like the ultimate ambitious challenge to solve for our self driving car, and as it
turns out, the lack of guiding lanes for it to follow along the bends where the track was thicker
made it hard for us to get accurate results about when exactly to take a turn. This resulted in a
poorly labelled dataset causing issues with the accuracy and on-track driving.
**● The Car : and the subsequent problem with the hardware.**
We initially decided to implement the algorithm from Nvidia’s landmark paper to predict
the steering angles from the image. It was extremely hard to find a remote control car
here in Delhi that could have the feature of proportional steering. (A servo that can be
used to control the front steering instead of the motor in the front of the car.)
As a result of this, we had to settle for hardware where we just could execute a full lef
turn, a full right turn or a full ahead.
This means that at the turns, we had to execute stepwise maneuvers to control the angle of the
car while driving manually to train it. This again led to a lot of mislabelled images which has
subsequently led to a substantial drop in the accuracy.
**● Dataset :**
Custom created dataset, contains approximately 600 images of the track captured during
training rounds with the associated steering direction in the form of labels. ( FF, FR, FL, NN)
Sample image and the associated image processing has been provided in the proof of concept
results. This dataset has been split 70:30 for training and test datasets with the help of several
scripts. ( Please note that the file names are the labels, with a timestamp )
**Issues that we’ve observed in the dataset :**
1.)Bad Labelling. : Due to the inability to control the angle of the direction of the car, during
turns of varying angles, the turning has to be in steps. For example a mild right turn is a
conjunction of FF and FR. However when it is collecting the data in the form of the
images and the associated direction at certain timestamps, it sometimes ends up picking
up the FF in places where there is a clear right turn.
2.)Presence of other objects in the field of vision : Pillars and other features around the
track are a part of the images, along with on certain occasions drains running around the
track. These parallel images look very close to lane lines after image processing, and
edge detection and since they move around in the frame as the car moves around, a
region of interest algorithm isn’t effective.


**● Neural Network :**
We’ve used a convolutional neural network, as a method for our Deep Learning. It is a class of
deep neural networks, which is mostly used to be able to analyze visual imagery. CNNs use a
variation of multilayer perceptrons designed to require minimal preprocessing.
The design of ConvNets are inspired by nature, and the connectivity of the neurons are made is
such a way that it resembles an animal’s visual cortex.
Sequential Model in CNN ( Keras ) :
It allows sequential layers to be easily stacked ( or other kinds of layers ) of the network in order
from input to output.
Convolutional Layer :
Convolutional layers apply a convolution operation to the input, passing the result to the next
layer. The convolution emulates the response of an individual neuron to visual stimuli. (
Mathematical combination of two functions to create a new function, in CNNs it is done with the
help of some kind of filter or kernel to create feature map )
Pooling :
Pooling layers are used to be able to reduce the spatial size of the representation which helps
reduce the amount of parameters and computation in the network.
Flattening : I’ve had to use flattening so that I can use dense layers afterwards, sequentially.
A dense function / Fully connected Layer : It is a linear operation in which every input is connected to
every output with a given weight.
Activation function : Usually a non-linear activation function such as Sigmoid or Softmax are used.
**Sequentially → One Convolutional Layer → Second Convolutional Layer → Pooling →
Flattening → Two Dense Layers of 128 and 4 size each.**
Using Sigmoid as an activation function on the last layer :
Loss : 0.
Accuracy : 0.
Using Softmax as an activation function on the last layer
Loss : 0.
Accuracy : 0.
Please note that the 4 output neurons correspond to our classification, allowing us to be able to
make a decision for a given image state. ( FF, FL, FR , NN )


**Model Prediction :**
The model was saved :
In JSON format, with the weights being stored in the form of an H5py file.
Once loaded, this model is being used to make a prediction, in the form of a class for a fed
image from the camera to decide the next direction to drive in.
**Case studies of a few problems we’ve faced and solved
Design - Architecture for
Scalability**
This is an an innovative
architecture to cluster
multiple single board linux
computers that allows
embedded autonomous
systems to scale and
monitor different
parameters. Multiple
programs are run on
different cores of different
single board linux
computers, and bound
together by a local network
and a network of memory
mapped IO. They work
parallely to monitor different
parameters for the system, and in the case of the detection of an anomaly can pass interrupts to
other nodes making control decisions for the autonomous system.


**Data Collection : Multi-processing to juice out the most out of the system.**
The connection to the blynk server to
control the car and the Data Gathering
program are designed to run continuously
at the same time as parallel processes with
system resources allocated to them
separately. This allows both the processes
to interact through one communication
channel only, the hardware short on the
GPIO pins. ( And the memory space
associated with the same)
The resultant method of shorting physical pins to interface different programs went on to be the
backbone of our ability to interface multiple computational nodes with different preset programs
running on them.
**DriveEngine**
Although in our program, we’re currently using a sequential flow of logic, multithreading
approaches were tried to get over the issue of time
required to get a prediction and take the action. We
discovered a bottleneck in the form of the Python
Global Interpreter Lock. This means that only one
thread is allowed to get control of system resources
to avoid a race condition in memory while storing
objects. This significantly reduces the amount of
computational time that can be saved by using
multithreading.
A workaround for the same would be the usage of
different processes, in which each of them would
get allocated their own system resources. However
this would mean that the programs have to
communicate through reading and writing in files.
Since we hypothesized that the I/O utilization is
already high and I/O would be a bottleneck, we didn’t use this approach. Instead, we have used
a sequential method of executing the same.


Hence we are currently just clicking a picture, predicting the direction by passing it through our
pre-trained model and on the basis of that executing the driving scripts.
**Haar-Cascade Classifier to detect traffic signs:**
Built only as a proof of concept to be able to detect traffic signs such as a stop signal or a traffic
light. We’re not using it anywhere in the code base right now while running the car.
Haar Cascade Classifiers are very effective for object detection. Initially, the algorithm needs a
lot of positive images (images of traffic signs ) and negative images (images without traffic
signs) to train the classifier. Then we need to extract features from it.
Although we attempted to train one ourselves, the program ran for a few hours and still didn’t
stop. Hence we resorted to using pre-trained classifiers which was used for some other projects
on Github. ( Source has been cited )


**Sample Image Processing Results : Image at 0 Labelled FF.**
_Top Left : Original Image
Top Right : Single Channel B/W
Centre Left : HSV image
Centre Right : Adaptive Gaussian Filtering with blur
Bottom Left : Hough Lines drawn on the image for lane detection.
Bottom Right : Canny edges to detect the edges of the road._
**Note : The reason we aren’t sending post-processed images through the CNN is that with
the addition of some blur ( from vibrations ), these edge detection algorithms break down
completely. CNNs anyways provide good results with minimal post-processing.**


## Machine Learning on Cloud

**Amazon Web Services API Gateway**
To make our car faster and cost effective, the complete machine learning algorithm is running
on Cloud. The device sends an API request to our instance on cloud through a URL and API
Key, referred to as the "startpoint"
**Amazon Web Services Lambda**
On receiving the API startpoint, the request is then forwarded to the AWS Lambda, where an
instantaneous instance is spinned to serve our python code. The python code runs and logs the
data in AWS CloudWatch. The result is returned to the API Return Node. The API Return Node
return node data is finally received by the user.
**Amazon Web Services CloudWatch**
Amazon CloudWatch is a monitoring and
management service. CloudWatch provides us
with data and actionable insights to monitor our
platform, understand and respond to
system-wide performance changes, optimize
resource utilization, and get a unified view of
operational health. CloudWatch collects monitoring and operational data in the form of logs,
metrics, and events, providing us with a unified view of our platform.
**Amazon Web Services S3 Container**
Amazon Simple Storage Service (S3) is a object storage service. For our project, we have
stored all the training and test data set in a container of S3. We can connect this bucket to our
Elastic Compute Cloud (EC2) instance and run the training of our Convolutional Neural
Network. We are also pushing our deployment code from local machine to AWS S3, and then
calling the S3 files directly from AWS Lambda to run the processes. For training workloads
greater than 80MB, we are using our EC2 instance to train the network.
**Amazon Web Services Elastic Compute Cloud (EC2)**
Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable
compute capacity in the cloud. It is designed to make web-scale cloud computing easier for
developers. Amazon EC2’s simple web service interface allows us to obtain and configure
capacity with minimal friction. We are using EC2 to run heavy training workloads, that exceeds
the limit of 80MB of AWS Lambda



Member Contributions:

**1. Debargha Ganguly**
    a. Designed the system from ground up.
    b. Built cluster capable and scalable architecture.
    c. Wrote CoreDriving Engines.
    d. Wrote the Proof of Concepts
    e. Wrote all the code required for control of the car.
    f. Wrote the code for Data Gathering.
    g. Ran the tests to create the dataset.
    h. Designed the program workflow and application flow for optimized performance.
**2. Prajwal Seth**
    a. Wrote scripts to clean the data.
    b. Collaborated to primarily write the neural network for the driving engines and test
       it.
    c. Debugged and refined other’s code.
    d. Set up a local blynk server to reduce latency from 200ish ms to 10ms.
**3. Shekhar Chatterjee**
    a. Built Website
    b. Set up AWS Lambda serverless compute engine for API specific gateways.
    c. Track Designing Expert.
    d. Wrote Machine Learning on Cloud section of the report
**4. Sarthak Dangwal**
    a. Drew all the circuit diagrams on the project report
    b. Wrote a shell script to be able to clean filename data.
    c. Helped writing the project report


**Citations** ​​:
Bojarski, M. (2016). ​ _End to End Learning for Self-Driving Cars_ ​. [online] NVIDIA. Available at:
https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf
[Accessed 7 Dec. 2018].
Blyth, P. (2018). ​ _Driving the Self-Driving Vehicle_ ​. [online] International Symposium on Technology in
Society (ISTAS) Proceedings. Available at: https://artifex.org/~bonnie/ISTAS_Paper_ref_60_385.pdf
[Accessed 7 Dec. 2018].
Stanley, M. (2018). ​ _Self-Driving the New Auto Industry Paradigm_ ​. [online] Available at:
https://orfe.princeton.edu/~alaink/SmartDrivingCars/PDFs/Nov2013MORGAN-STANLEY-BLUE-PAPER-
AUTONOMOUS-CARS%EF%BC%9A-SELF-DRIVING-THE-NEW-AUTO-INDUSTRY-PARADIGM.pdf
[Accessed 7 Dec. 2018].
Multunus Software Pvt. Ltd., ​ _Autonomous-RC-Car_ ​, (2016), GitHub repository,
https://github.com/multunus/autonomous-rc-car [Accessed 7 Dec. 2018].
Rodrigo Cava, ​ _Mr. Robot,_ ​(2018), GitHub repository, https://github.com/rodrigocava/mrrobot
[Accessed 7 Dec. 2018].
Arnaldo Satoru Gunzi, ​ _CarND-VehicleDetection_ ​, (2016), GitHub repository,
https://github.com/asgunzi/CarND-VehicleDetection/ [Accessed 7 Dec. 2018].
Zheng Wang. (2018). ​ _Self Driving RC Car_ ​. [online] Available at:
https://zhengludwig.wordpress.com/projects/self-driving-rc-car/ [Accessed 7 Dec. 2018].



