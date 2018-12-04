from __future__ import print_function
from keras.datasets import mnist


class MNIST(object):

    def __init__(self):
        pass


    def load(self):
        """Loads the MNIST dataset from Keras (Tensorflow) and returns the image data and corresponding labels.
        """

        (data, labels), (_, _) = mnist.load_data()
        return data, labels
