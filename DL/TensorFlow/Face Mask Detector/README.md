[COVID-19: Face Mask Detector with OpenCV, Keras/TensorFlow, and Deep Learning](https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/)

In this tutorial, you will learn how to train a COVID-19 face mask detector with OpenCV, Keras/TensorFlow, and Deep Learning.

Given the trained COVID-19 face mask detector, we’ll proceed to implement two more additional Python scripts used to:

1. Detect COVID-19 face masks in images
2. Detect face masks in real-time video streams

The dataset we’ll be using here today was created by PyImageSearch reader [Prajna Bhandary](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A6655711815361761280/).

This dataset consists of 1,376 images belonging to two classes:

- with_mask: 690 images
- without_mask: 686 images

We’ll be reviewing three Python scripts in this tutorial:

- train_mask_detector.py: Accepts our input dataset and fine-tunes MobileNetV2 upon it to create our mask_detector.model. A training history plot.png containing accuracy/loss curves is also produced
- detect_mask_image.py: Performs face mask detection in static images
- detect_mask_video.py: Using your webcam, this script applies face mask detection to every frame in the stream