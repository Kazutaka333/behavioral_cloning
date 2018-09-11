import csv

lines = []
# TODO: use other data too
# TODO: add data augmentation
with open('/opt/data/center1/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    lines = [line for line in reader]
    
from sklearn.model_selection import train_test_split
train_samples, valid_samples = train_test_split(lines, test_size=0.2)

import cv2
import numpy as np
import sklearn
from random import shuffle

def generator(samples, batch_size=32):
    num_samples = len(samples)
    while 1:
        shuffle(samples)
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]
            
            images = []
            angles = []
            for line in batch_samples:
                # data needs to be at /opt/data/
                current_path = line[0]
                image = cv2.imread(current_path)
                images.append(image)
                angle = float(line[3])
                angles.append(angle)
                
            X_train = np.array(images)
            y_train = np.array(angles)
            yield sklearn.utils.shuffle(X_train, y_train)

# Try bigger batch size to speed up
train_generator = generator(train_samples, batch_size=32)
valid_generator = generator(valid_samples, batch_size=32)

from keras.models import Sequential
from keras.layers import Flatten, Dense, Conv2D, Activation, Cropping2D, Lambda, Dropout


model = Sequential()
model.add(Cropping2D(cropping=((50,20),(0, 0)), input_shape=(160, 320, 3)))
model.add(Lambda(lambda x: x/127.5 - 1.))
model.add(Conv2D(5, (5, 5)))
model.add(Activation('relu'))
model.add(Conv2D(10, (5, 5)))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit_generator(train_generator,
                    samples_per_epoch=len(train_samples),
                    validation_data=valid_generator,
                    nb_val_samples=len(valid_samples),
                    nb_epoch=5)

model.save('model.h5')
          