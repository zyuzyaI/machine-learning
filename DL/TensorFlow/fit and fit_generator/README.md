## How to use Keras fit and fit_generator (a hands-on tutorial)
[sourse](https://www.pyimagesearch.com/2018/12/24/how-to-use-keras-fit-and-fit_generator-a-hands-on-tutorial/)

The Keras deep learning library includes three separate functions that can be used to train your own models:
* .fit
* .fit_generator
* .train_on_batch

### The Keras .fit function
The call to .fit  is making two primary assumptions here:
* Our entire training set can fit into RAM
* There is no data augmentation going on (i.e., there is no need for Keras generators)

Instead, our network will be trained on the raw data.

The raw data itself will fit into memory — we have no need to move old batches of data out of RAM and move new batches of data into RAM.

Furthermore, we will not be manipulating the training data on the fly using data augmentation.

### The Keras fit_generator function

Internally, Keras is using the following process when training a model with .fit_generator :

* Keras calls the generator function supplied to .fit_generator  (in this case, aug.flow ).
* The generator function yields a batch of size BS  to the .fit_generator  function.
* The .fit_generator  function accepts the batch of data, performs backpropagation, and updates the weights in our model.
* This process is repeated until we have reached the desired number of epochs.

You’ll notice we now need to supply a steps_per_epoch  parameter when calling .fit_generator  (the .fit  method had no such parameter).

Why do we need steps_per_epoch ?

Keep in mind that a Keras data generator is meant to loop infinitely — it should never return or exit.

Since the function is intended to loop infinitely, Keras has no ability to determine when one epoch starts and a new epoch begins.

Therefore, we compute the steps_per_epoch  value as the total number of training data points divided by the batch size. Once Keras hits this step count it knows that it’s a new epoch.

### The Keras train_on_batch function

The train_on_batch  function accepts a single batch of data, performs backpropagation, and then updates the model parameters.

The batch of data can be of arbitrary size (i.e., it does not require an explicit batch size to be provided).

The data itself can be generated however you like as well. This data could be raw images on disk or data that has been modified or augmented in some manner.

You’ll typically use the .train_on_batch  function when you have very explicit reasons for wanting to maintain your own training data iterator, such as the data iteration process being extremely complex and requiring custom code.

If you find yourself asking if you need the .train_on_batch  function then in all likelihood you probably don’t.

In 99% of the situations you will not need such fine-grained control over training your deep learning models. Instead, a custom Keras .fit_generator  function is likely all you need it.


The dataset we will be using [here](http://www.robots.ox.ac.uk/~vgg/data/flowers/17/) today is the Flowers-17 dataset, a collection of 17 different flower species with 80 images per class.

Our goal will be to train a Keras Convolutional Neural Network to correctly classify each species of flowers.
