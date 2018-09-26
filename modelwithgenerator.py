import csv

lines = []
folder_names = ['center1', 
                'center2', 
                'reverse',
                'curve', 
                'dirt_curve',
                'dirt_curve2',
                'dirt_curve3',
                'dirt_curve4',
                'before_bridge',
                'flipped_center1',
                'flipped_center2',
                'flipped_reverse',
                'flipped_curve',
                'flipped_dirt_curve',
                'flipped_dirt_curve2',
                'flipped_dirt_curve3',
                'flipped_dirt_curve4',
                'flipped_before_bridge']
folder_names = ['center1', 
                'center2', 
                'reverse',
                'curve', 
                'recovery',
                'flipped_center1',
                'flipped_center2',
                'flipped_reverse',
                'flipped_curve',
                'flipped_recovery']
division_factor = 6
parent_dir = "/home/carnd/"
for f_name in folder_names:
# for f_name in folder_names[]:
    with open(parent_dir+'data/{}/driving_log.csv'.format(f_name)) as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for line in reader:
            if i%division_factor == 0:
                lines.append(line)
                # add left and right image
                adjust_const = 1.9
                left_line = [line[1], *line[1:3], str(float(line[3])+adjust_const), *line[4:]]
                right_line = [line[2], *line[1:3], str(float(line[3])-adjust_const), *line[4:]]
                #lines.append(left_line)
                #lines.append(right_line)
            i += 1
        print(f_name, ":", i)

from sklearn.model_selection import train_test_split
from random import shuffle
print("number of data:", len(lines))

import cv2
import numpy as np
import sklearn



images = []
angles = []
for line in lines:
    current_path = parent_dir+"data/{}".format("/".join(line[0].split("/")[-3:]))
    image = cv2.imread(current_path)
    images.append(image)
    angle = float(line[3])
    angles.append(angle)
    
X_train = np.array(images)
y_train = np.array(angles)


from keras.models import Sequential
from keras.layers import Flatten, Dense, Conv2D, Activation, Cropping2D, Lambda, Dropout, MaxPooling2D
import subprocess

model = Sequential()
model.add(Cropping2D(cropping=((40,20),(0, 0)), input_shape=(160, 320, 3)))
model.add(Lambda(lambda x: x/127.5-1.))
model.add(Conv2D(5, (5, 5)))
model.add(Activation('relu'))
model.add(Conv2D(10, (5, 5)))
model.add(Activation('relu'))
model.add(Conv2D(20, (5, 5)))
model.add(Activation('relu'))
model.add(Conv2D(30, (5, 5)))
model.add(Activation('relu'))
model.add(Flatten())
model.add(Dense(100))
model.add(Dropout(0.5))
model.add(Activation('relu'))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')

epochs = 10
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, epochs=epochs)
model_file_name = './model/model_f'+str(len(folder_names))+'_adj'+str(adjust_const)+'_DF'+str(division_factor)+'_e'+str(epochs)+'_.h5'
model.save(model_file_name)

subprocess.call(['echo', '-en', '\007'])
subprocess.call(['echo', '-en', '\007'])
subprocess.call(['echo', '-en', '\007'])
print(model_file_name)
