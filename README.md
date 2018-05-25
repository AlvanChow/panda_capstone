# Panda Image Classifier

The objective of this project was to create a convolutional neural network in Keras that could identify if an image depicts a panda. 

### Motivation

Pandas are monochromatic animals with features extremely similar to other animals (ursidae). I wanted to explore the difficulty of identifying this type of animal against a multiclass dataset (as opposed to 2000 images of cats and 2000 images of dogs).

### Dataset

The dataset used was curated in part from the LHI Animal Faces Dataset (http://www.stat.ucla.edu/~zzsi/HiT/exp5.html) and part from scraping Google Images. The ratio of pandas to not pandas in the LHI Dataset was around 20:1, so a Chrome extension was used to download Panda images to create better class balance. 

There were many unclean pictures of pandas from Google Images (including but not limited to Panda Express, Red Pandas, panda costumes). These were selected and deleted manually. In order to maintain the class balance, pictures from the LHI dataset were deleted at random.

The final split was: 1356 Panda Images, 1468 Not Panda Images. This yields a class balance of around 48:52.

### Process

The first attempt at creating a neural network included one layer of convolution with 32 feature extractors, ReLU activation, and 2x2 Max Pooling, followed by flattening and connecting two fully dense layers of 128 and 1 with a sigmoid function in the final layer. No dropout. 

Although the accuracy metric given by Keras was up in the 99th percentile for training and validation, when I manually tested images, it incorrectly identified over 95% non-panda images as 'Panda'. I combed through the dataset, and realized that there were many bad pictures in the panda folder (Panda Express, Red Pandas, etc). I deleted all of these manually.

A second attempt was made by creating a neural network with three convolutional layers. 32 feature extractors, 32 feature extractors, and 64 feature extractors with Max Pooling of 2x2 after each layer. 25 Epochs with 3000 steps each.

Although it was an improvement, it was still grossly overfit. The training/testing accuracy metric given by Keras was again upwards of 99%, but when I manually tested it, it had only classified 50% of non-panda images correctly. When tested against panda images, the model yielded a 100% accuracy.

The model had too many false positives.

I explored a separated method by calculating the RGB value of each pixel after sizing all images to 64x64 pixels. I wanted to explore the possibility of classifying a panda based on a majority white and black pixel count in the image. However, there were many images with shadows and poor resolution photographs that made this attempt useless.

I went back to convolutional neural networks to troubleshoot the overfitting problem. After many attempts, I found that lowering the batch size, lowering the epoch count, and lowering the steps worked in avoiding overfitting. Using a batch size of 10, with 25 epochs, and 100 steps, and running the neural network with random initializing weights a few times, I was able to get a model with my self-tested accuracy of 88%.


### Results

The final convolutional neural network has an accuracy of 88%, a precision of 84%, and a recall of 96%. This model is saved in the classifier_863.json and classifier_863.h5 files. 

### Conclusion

1. Data cleanliness and breadth is important, having a good dataset is extremely important. The neural net does not have any prior knowledge of pandas. 

2. Neural networks can overfit easily and are hard to troubleshoot. Since the weights and calculations are all hidden under Keras, it is hard to find where the model went wrong. I need to develop a stronger understanding of tensorflow and neural networks.

3. Softmax output might be better because of multiclass classification in this dataset. The CNN may detect classes easier if the other 19 classes in the LHI dataset were not put together. More exploration is needed. 

4. Image recognition is a problem far from being solved. It is not as easy as creating a 3 layer CNN and sending data through it. Even a simple image classification problem needs curating for overfitting and class imbalance. This field has a bright future for research and development!

