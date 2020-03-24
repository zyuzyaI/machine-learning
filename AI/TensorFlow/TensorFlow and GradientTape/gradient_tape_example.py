# import the necessary packages
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import BatchNormalization
# from tensorflow.keras.layers import Conv2D
# from tensorflow.keras.layers import MaxPooling2D
# from tensorflow.keras.layers import Activation
# from tensorflow.keras.layers import Flatten
# from tensorflow.keras.layers import Dropout
# from tensorflow.keras.layers import Dense
# from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.losses import categorical_crossentropy
# from tensorflow.keras.utils import to_categorical   
# from tensorflow.keras.datasets import mnist
# import tensorflow as tf 
# import numpy as np 
# import time 
# import sys 

# import the necessary packages
from keras.models import Sequential
from keras.layers import BatchNormalization
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import Dense
from keras.optimizers import Adam
from keras.losses import categorical_crossentropy
from keras.utils import to_categorical   
from keras.datasets import mnist
import tensorflow as tf 
import numpy as np 
import time 
import sys 

def build_model(width, height, depth, classes):
    # initialize the input shape and channels dimension to be "channels last" ordering
    inputShape = (height, width, depth)
    chanDim = -1

    # build the model using Keras' Sequential API
    model = Sequential([
        # CONV => RELU => BN => POOL layer set
        Conv2D(16, (3,3), padding="same", input_shape=inputShape),
        Activation("relu"),
        BatchNormalization(axis=chanDim),
        MaxPooling2D(pool_size=(2,2)),

        # (CONV => RELU => BN) * 2 => POOL layer set
        Conv2D(32, (3,3), padding="same"),
        Activation("relu"),
        BatchNormalization(axis=chanDim),
        Conv2D(32, (3,3), padding="same"),
        Activation("relu"),
        BatchNormalization(axis=chanDim),
        MaxPooling2D(pool_size=(2,2)),

        # (CONV => RELU => BN) * 3 => POOL layer set
        Conv2D(64, (3,3), padding="same"),
        Activation("relu"),
        BatchNormalization(axis=chanDim),
        Conv2D(64, (3, 3), padding="same"),
        Activation("relu"),
        BatchNormalization(axis=chanDim),
        Conv2D(64, (3, 3), padding="same"),
        Activation("relu"),
        BatchNormalization(axis=chanDim),
        MaxPooling2D(pool_size=(2,2)),

        # first (and only) set of FC => RELU layers
        Flatten(),
        Dense(256),
        Activation("relu"),
        BatchNormalization(),
        Dropout(0.5),

        # softmax classifier
        Dense(classes),
        Activation("softmax")
    ])

    # return the built model to the calling function
    return model 

def step(X, y):
    # keep track of our gradients
    with tf.GradientTape() as tape:
        # make a prediction using the model and then calculate the loss
        pred = model(X)
        loss = categorical_crossentropy(y, pred)

    # calculate the gradients using our tape and then update the model weights
    grads = tape.gradient(loss, model.trainable_variables)
    opt.apply_gradients(zip(grads, model.trainable_variables))

# initialize the number of epochs to train for, batch size, and initial learning rate
EPOCHS = 25
BS = 64
INIT_LR = 1e-3

# load the MNIST dataset
print("[INFO] loading MNIST dataset...")
((train_x, train_y), (test_x, test_y)) = mnist.load_data()

# add a channel dimension to every image in the dataset, then scale
# the pixel intensities to the range [0, 1]
train_x = np.expand_dims(train_x, axis=-1)
test_x = np.expand_dims(test_x, axis=-1)
train_x = train_x.astype("float32") / 255.0
test_x = test_x.astype("float32") / 255.0

# one-hot encode the labels
train_y = to_categorical(train_y, 10)
test_y = to_categorical(test_y, 10)

# build our model and initialize our optimizer
print("[INFO] creating model...")
model = build_model(28, 28, 1, 10)
opt = Adam(lr=INIT_LR, decay=INIT_LR/EPOCHS)

# compute the number of batch updates per epoch
numUpdates = int(train_x.shape[0]/BS)

# loop over the number of epochs
for epoch in range(0, EPOCHS):
    # show the current epoch number
    print("[INFO] starting epoch {}/{}...".format(epoch + 1, EPOCHS), end="")
    sys.stdout.flush()
    epochStart = time.time()

    # loop over the data in batch size increments
    for i in range(0, numUpdates):
        # determine starting and ending slice indexes for the current batch
        start = i * BS
        end = start + BS 

        # take a step
        step(train_x[start:end], train_y[start:end])

    # show timing information for the epoch
    epochEnd = time.time()
    elapsed = (epochEnd - epochStart) / 60.0
    print("took {:.4} minutes".format(elapsed))

# in order to calculate accuracy using Keras' functions we first need to compile the model
model.compile(optimazer=opt, loss=categorical_crossentropy, metrics=["acc"])

# now that the model is compiled we can compute the accuracy
(loss, acc) = model.evaluate(test_x, test_y)
print("[INFO] test accuracy: {:.4f}".format(acc))