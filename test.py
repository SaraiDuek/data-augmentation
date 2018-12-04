from __future__ import print_function
import unittest
import os
from mnist_dataset_loader import MNIST
from mnist_sequence_generator import MNIST_Sequence_Generator
from mnist_sequence_generator_api import MNIST_Sequence_Generator_API
from mnist_sequence_generator_exceptions import BadMeasurementsException, BadArgumentsException


#TODO use tox and test for other python envs (like python 2.7)

class Tests(unittest.TestCase):
    def setUp(self):
        self.dataset = MNIST()
        self.mnist_sequence = MNIST_Sequence_Generator()
        self.mnist_sequence_api = MNIST_Sequence_Generator_API()

    # TODO add more tests

    ########### Test loader ###########

    def test_load_dataset_from_keras(self):
        data, labels = self.dataset.load()
        size, rows, cols = data.shape
        self.assertEqual(rows, cols)
        self.assertEqual(rows, 28)
        self.assertEqual(size, len(labels))
        self.assertTrue(size > 0)


    ########### Test data augmentation ###########

    def test_data_augmentation(self):
        img = self.mnist_sequence_api.generate_mnist_sequence([3, 5, 0], (0, 10), 94, augment=True)
        rows, cols = img.shape
        self.assertEqual(rows, 28)
        self.assertEqual(cols, 94)


    ########### Test API ###########

    def test_generate_mnist_sequence(self):
        img = self.mnist_sequence_api.generate_mnist_sequence([3, 5, 0], (0, 10), 94)
        rows, cols = img.shape
        self.assertEqual(rows, 28)
        self.assertEqual(cols, 94)


    def test_save(self):
        img = self.mnist_sequence_api.generate_mnist_sequence([3, 5, 0], (0, 10), 94)
        self.mnist_sequence_api.save_image(img, [3, 5, 0])
        self.assertTrue(os.path.isfile('3-5-0.png'))


    ########### Test mnist sequence generator ###########

    def test_generate_mnist_sequence_success(self):
        img = self.mnist_sequence_api.generate_mnist_sequence([3, 5, 0], (0, 10), 94)
        rows, cols = img.shape
        self.assertEqual(rows, 28)
        self.assertEqual(cols, 94)

        img = self.mnist_sequence_api.generate_mnist_sequence([3, 5, 0, 6, 8, 3], (0, 10), 178)
        rows, cols = img.shape
        self.assertEqual(rows, 28)
        self.assertEqual(cols, 178)

        img = self.mnist_sequence_api.generate_mnist_sequence([3, 5, 0, 6, 8, 3], (0, 10), 178, True)
        rows, cols = img.shape
        self.assertEqual(rows, 28)
        self.assertEqual(cols, 178)

    def test_generate_mnist_sequence_fail(self):
        self.assertRaises(BadArgumentsException,
                          self.mnist_sequence_api.generate_mnist_sequence, [], (0, 10), 178, True)
        self.assertRaises(BadMeasurementsException,
                          self.mnist_sequence_api.generate_mnist_sequence, [3, 5, 0], (0, 10), 178, True)
        self.assertRaises(BadMeasurementsException,
                          self.mnist_sequence_api.generate_mnist_sequence, [3, 5, 0], (0, 10), 30, True)
        self.assertRaises(BadMeasurementsException,
                          self.mnist_sequence_api.generate_mnist_sequence, [3, 5, 0], (2, 10), 84, True)



if __name__ == '__main__':
    unittest.main()
