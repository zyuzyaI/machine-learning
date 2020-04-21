[Detect and remove duplicate images from a dataset for deep learning](https://www.pyimagesearch.com/2020/04/20/detect-and-remove-duplicate-images-from-a-dataset-for-deep-learning/)

In the first part of this tutorial, you’ll learn why detecting and removing duplicate images from your dataset is typically a requirement before you attempt to train a deep neural network on top of your data.

From there, we’ll review the example dataset I created so we can practice detecting duplicate images in a dataset.

We’ll then implement our image duplicate detector using a method called [image hashing](https://www.pyimagesearch.com/2017/11/27/image-hashing-opencv-python/).

1. Perform a dry run to validate that our image duplicate detector is working properly
2. Run our duplicate detector a second time, this time removing the actual duplicates from our dataset