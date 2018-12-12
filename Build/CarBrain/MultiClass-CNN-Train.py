

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense


model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape = (50, 50, 3), activation = 'relu'))

model.add(MaxPooling2D(pool_size = (2, 2)))


model.add(Conv2D(32, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))


model.add(Flatten())


model.add(Dense(units = 128, activation = 'relu'))
model.add(Dense(units = 4, activation = 'sigmoid'))


model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])



train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

training_set = train_datagen.flow_from_directory('/Users/prajwalseth/Desktop/Programming/CNN/all3/',
                                                 target_size = (50, 50),
                                                 batch_size = 32,

model.fit_generator(training_set,
                         steps_per_epoch = 150,
                         epochs = 20,
                         validation_steps = 75)


model_json = model.to_json()
with open("./model.json","w") as json_file:
  json_file.write(model_json)

model.save_weights("./model.h5")

print("Classifier trained Successfully!")
