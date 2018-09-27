# **Behavioral Cloning** 

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/placeholder.png "Model Visualization"
[image2]: ./examples/placeholder.png "Grayscaling"
[image3]: ./examples/placeholder_small.png "Recovery Image"
[image4]: ./examples/placeholder_small.png "Recovery Image"
[image5]: ./examples/placeholder_small.png "Recovery Image"
[image6]: ./examples/placeholder_small.png "Normal Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network (This file can be downloaded from [here](https://www.dropbox.com/s/49zqlgtoe5s7264/model.h5?dl=1) . I coudn't include in this repo because the file size was too big.)
* writeup.md summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

My model consists of 4 convolutional layers, two fully connected layer and dropout layer inbetween fully connected ones. (model.py line 60-72) I chose relu as activation function and use Lambda function to normalize iamge data. (model.py line 59)

#### 2. Attempts to reduce overfitting in the model

The model contains dropout layers in order to reduce overfitting (model.py lines 70). 

The model was trained and validated on different data sets to ensure that the model was not overfitting (code line 78). The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 74).

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used two different version of center lane driving, recovering from the left and right sides of the road, center lane driving to the opposite way, driving on each curve, and mirrored images of all kinds.

For details about how I created the training data, see the next section. 

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was to modify the architecture I used for traffict sign classifier as I need.

My first step was to use a convolution neural network model similar to the LeNet. I thought this model might be appropriate because the model has relatively less number of layer, which means faster training time and I wanted to build a model that works and to modify it layer. With a smaller model, a bug is easier to be spoted too.

As I increase the number of training data, model.fit() function started to yeild a resource exhaustion error, which required me to implement generator function and use fit_generator(). This slows down training too.
Since I have dropout layer initially, I did not see the huge gap between validation loss and training loss.

The final step was to run the simulator to see how well the car was driving around track one. There were a few spots where the vehicle fell off the track. To improve the model, I added new data of driving where the car drove off. This shows some improvement but other part started failing.
The final epochs I used was 10, as the loss did not go down after 10 epochs.
I've also tried more data, less data, different cropping, and etc ...
Finally, I've used up all the avilable hours on workspace. Even though I got 25 hours more, I imagined I could end up use it all again, since I wasn't really seeing consistent improvment on my model. Then I've tried Google Colab, which runs much faster due to the larger memory it has. However, it turns out that the model created on Colab causes an error with drive.py. Then I moved on to aws, which also had enough memory for me to use only model.fit(). I was able to train much faster pace and to try many different pattern of variables. However, my model drove very wiggly and can never make on the curve where there is dirt road connected. Then, I realized that I'm reading image as BGR not RGB. This was the source of my poor model. After fixiting it, my model turns out to drive very good.

Also, since there are so many variation of parameters and data, I wrote code to leave log after each training, (model.py line 86-93) so that I can reflect on what works and what not.

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

My model has the following structure.

| Layer          		|     Description	 | 
|:-----------------:|:------------------------------------------------------:| 
| Input          		| 160x320x3 RGB image | 
| Convolution 5x5 	| 1x1 stride, 5 depth, valid padding |
| RELU	            | |
| Convolution 5x5	  | 1x1 stride, 10 depth, valid padding	|
| RELU              | |
| Convolution 5x5	  | 1x1 stride, 20 depth, valid padding	|
| RELU              | |
| Convolution 5x5	  | 1x1 stride, 30 depth, valid padding	|
| Fully connected		| outputs 100 |
| Dropout           | 50% keep probability |
| RELU					    | |
| Fully connected		| outputs 1 |

The final model architecture (model.py lines 18-24) consisted of a convolution neural network with the following layers and layer sizes ...

Here is a visualization of the architecture (note: visualizing the architecture is optional according to the project rubric)

![alt text][image1]

#### 3. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one using center lane driving. Here is an example image of center lane driving:

![alt text][image2]

I then recorded the vehicle recovering from the left side and right sides of the road back to center so that the vehicle would learn to .... These images show what a recovery looks like starting from ... :

![alt text][image3]
![alt text][image4]
![alt text][image5]

Then I repeated this process on track two in order to get more data points.

To augment the data sat, I also flipped images and angles thinking that this would ... For example, here is an image that has then been flipped:

![alt text][image6]
![alt text][image7]

Etc ....

After the collection process, I had X number of data points. I then preprocessed this data by ...


I finally randomly shuffled the data set and put Y% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was Z as evidenced by ... I used an adam optimizer so that manually training the learning rate wasn't necessary.
