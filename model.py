import csv

lines = []
# TODO: add data augmentation
# folder_names = ['center1', 'center2', 'center3', 'reverse', 'recovery', 'curve']
folder_names = ['center1', 'center2', 'reverse', 'curve', 'dirt_curve', 'flipped_dirt_curve',]
division_factor = 3
for f_name in folder_names:
# for f_name in folder_names[]:
    with open('/opt/data/{}/driving_log.csv'.format(f_name)) as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for line in reader:
            if i%division_factor == 0 or f_name == "dirt_curve" or f_name == "flipped_dirt_curve":
                lines.append(line)
                # add left and right image
                adjast_const = 2.
                left_line = [line[1], *line[1:3], str(float(line[3])+adjast_const), *line[4:]]
                right_line = [line[2], *line[1:3], str(float(line[3])-adjast_const), *line[4:]]
                lines.append(left_line)
                lines.append(right_line)
            i += 1
        print(f_name, ":", i)

from sklearn.model_selection import train_test_split
from random import shuffle
print("number of data:", len(lines))
train_samples, valid_samples = train_test_split(lines, test_size=0.2)

import cv2
import numpy as np
import sklearn


def generator(samples, batch_size):
    num_samples = len(samples)
    while 1:
        shuffle(samples)
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]
            
            images = []
            angles = []
            for line in batch_samples:
                current_path = "/opt/data/{}".format("/".join(line[0].split("/")[-3:]))
                image = cv2.imread(current_path)
                images.append(image)
                angle = float(line[3])
                angles.append(angle)
                
            X_train = np.array(images)
            y_train = np.array(angles)
            yield sklearn.utils.shuffle(X_train, y_train)

batch_size = 32
train_generator = generator(train_samples, batch_size=batch_size)
valid_generator = generator(valid_samples, batch_size=batch_size)

from keras.models import Sequential
from keras.layers import Flatten, Dense, Conv2D, Activation, Cropping2D, Lambda, Dropout


model = Sequential()
model.add(Cropping2D(cropping=((50,20),(0, 0)), input_shape=(160, 320, 3)))
model.add(Lambda(lambda x: x/127.5-1.))
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
                    epochs=3)

model.save('model.h5')
          