https://www.pyimagesearch.com/2019/07/22/keras-learning-rate-schedules-and-decay/


The worker  module contains our ResNet CNN and our learning_rate_schedulers.py . The LearningRateDecay  parent class simply includes a method called plot  for plotting each of our types of learning rate decay. Also included are subclasses, StepDecay  and PolynomialDecay  which calculate the learning rate upon the completion of each epoch. Both of these classes contain the plot  method via inheritance (an object-oriented concept).

Our training script, train.py , will train ResNet on the CIFAR-10 dataset. We’ll run the script with the absence of learning rate decay as well as standard, linear, step-based, and polynomial learning rate decay.

