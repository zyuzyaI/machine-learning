https://www.pyimagesearch.com/2020/03/02/anomaly-detection-with-keras-tensorflow-and-deep-learning/

Anomaly detection with Keras, TensorFlow, and Deep Learning

In this tutorial, you will learn how to perform anomaly and outlier detection using autoencoders, Keras, and TensorFlow.

From there, we’ll implement an autoencoder architecture that can be used for anomaly detection using Keras and TensorFlow. We’ll then train our autoencoder model in an unsupervised fashion.

Our convautoencoder.py file contains the ConvAutoencoder class which is responsible for building a Keras/TensorFlow autoencoder implementation.

We will train an autoencoder with unlabeled data inside train_unsupervised_autoencoder.py, resulting in the following outputs:

autoencoder.model: The serialized, trained autoencoder model.


images.pickle: A serialized set of unlabeled images for us to find anomalies in.


plot.png: A plot consisting of our training loss curves.

	
recon_vis.png: A visualization figure that compares samples of ground-truth digit images versus each reconstructed image.


From there, we will develop an anomaly detector inside find_anomalies.py and apply our autoencoder to reconstruct data and find anomalies.

