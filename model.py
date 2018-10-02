import csv

lines = []

folder_names = ['center2', 
                'center3', 
                'reverse',
                'curve2', 
                'recovery',
                'flipped_center2',
                'flipped_center3',
                'flipped_reverse',
                'flipped_curve2',
                'flipped_recovery' ]
division_factor = 1
parent_dir = "/Users/Kazutaka/Downloads/"

# extract each line from csv file
for f_name in folder_names:
    with open(parent_dir+'data/{}/driving_log.csv'.format(f_name)) as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for line in reader:
            if i%division_factor == 0:
                lines.append(line)

            i += 1
        print(f_name, ":", i)

from sklearn.model_selection import train_test_split
from random import shuffle
print("number of data:", len(lines))

import cv2
import numpy as np
import sklearn
import scipy

# extract angle and image from each line of csv
images = []
angles = []
for line in lines:
    current_path = parent_dir+"data/{}".format("/".join(line[0].split("/")[-3:]))
    image = scipy.misc.imread(current_path)
    images.append(image)
    angle = float(line[3])
    angles.append(angle)
    
X_train = np.array(images)
y_train = np.array(angles)


from keras.models import Sequential
from keras.layers import Flatten, Dense, Conv2D, Activation, Cropping2D, Lambda, Dropout, MaxPooling2D
import subprocess

model = Sequential()
model.add(Cropping2D(cropping=((50,20),(0, 0)), input_shape=(160, 320, 3)))
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

## since I have enough memory on aws machine, I did not use fit_generator
#model.fit(X_train, y_train, validation_split=0.2, shuffle=True, epochs=epochs)
#model_file_name = './model/model_f'+str(len(folder_names))+'_DF'+str(division_factor)+'_e'+str(epochs)+'_.h5'
#model.save(model_file_name)
#
#import datetime
#date = datetime.datetime.now()
#
## make log about the model just trained
#with open('log.txt', 'a') as logfile:
#    logfile.write(str(date)[:-10] + " " + model_file_name + '\n')
#    logfile.write("data: " + str(folder_names) + '\n')
#    logfile.write("division factor: " + str(division_factor) + '\n')
#    logfile.write("cpochs: " + str(epochs) + '\n')
#    model.summary(print_fn=lambda x: logfile.write(x + '\n'))
#    logfile.write('\n')
#    logfile.write('\n')
#
## beep when the training ends
#subprocess.call(['echo', '-en', '\007'])
#subprocess.call(['echo', '-en', '\007'])
#subprocess.call(['echo', '-en', '\007'])
#print(model_file_name)
#
