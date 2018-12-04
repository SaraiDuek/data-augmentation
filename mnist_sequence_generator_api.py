from __future__ import print_function
from mnist_sequence_generator import MNIST_Sequence_Generator
import numpy as np
from PIL import Image

# TODO improve documentation

class MNIST_Sequence_Generator_API(object):

    def __init__(self):
        self.sequence = MNIST_Sequence_Generator()


    def generate_mnist_sequence(self, digits, spacing_range, image_width, augment=False):
        """Receives a sequence and measurements and returns an image of the sequence by the specified measurements.
           The images for the digit in the sequense are chosen randomly from the mnist dataset and stacked horizontally.
        """

        return (255 - self.sequence.generate_image_sequence(digits, spacing_range[0],
                                                      spacing_range[1], image_width, augment)).astype(np.uint8)


    def save_image(self, img, sequence):
        """Saves a given image in the current directory, named according to the sequence provided.
        """
        # TODO add incrementation to avoid overide existing images in current directory

        img = Image.fromarray(img)
        img_name = '-'.join(list(map(str, sequence)))
        img.save(img_name + '.png')
        print('Image was generated and saved as ' + img_name + '.png.')
