from __future__ import print_function
import numpy as np
from random import choice
from mnist_dataset_loader import MNIST
from mnist_data_augmentation import blur_img
from mnist_sequence_generator_exceptions import MissingImgException, BadMeasurementsException, BadArgumentsException

# TODO improve documentation

class MNIST_Sequence_Generator(object):

    def __init__(self):
        self.dataset = MNIST()
        self.data, self.labels = self.dataset.load()
        self.digits_map = self.__generate_digits_map()


    def __generate_digits_map(self):
        digits_map = [[] for i in range(10)]
        for i in range(len(self.labels)):
            digits_map[self.labels[i]].append(i)
        return digits_map


    def __select_random_digit_from_dataset(self, digit):
        if len(self.digits_map[digit]) > 0:
            return choice(self.digits_map[digit])
        else:
            raise MissingImgException(digit)


    def __calculate_spacing(self, sequence_length, min_space, max_space, final_width, image_width=28):
        if sequence_length <= 1:
            spacing = float(final_width - sequence_length * image_width)
        else:
            spacing = (final_width - sequence_length * image_width) / float(sequence_length - 1)

        if not spacing.is_integer() or spacing < min_space or spacing > max_space:
            raise BadMeasurementsException(sequence_length, min_space, max_space, final_width)
        return int(spacing)


    def generate_image_sequence(self, sequence, min_space, max_space, final_width, augment=False, img_height=28):
        """Generates sequence.
           Calculates spacing according to measurements and stacks randomly chosen digits horizontally.
        """
        #TODO allow augmentation per digit

        sequence_length = len(sequence)
        if sequence_length < 1:
            raise BadArgumentsException('Sequence can not be empty. Please enter at least one digit as a sequence.')
        spacing = self.__calculate_spacing(sequence_length, min_space, max_space, final_width)
        spacing = np.ones(img_height * spacing, dtype='float32').reshape(img_height, spacing)

        img = []
        for i in range(sequence_length):
            random_digit_index = self.__select_random_digit_from_dataset(sequence[i])
            if i == 0:
                img = self.data[random_digit_index]
                if sequence_length == 1:
                    img = np.hstack((img, spacing))
                continue
            if i < sequence_length:
                img = np.hstack((img, spacing))
            img = np.hstack((img, self.data[random_digit_index]))
        if augment:
            img = blur_img(img)
        return img
