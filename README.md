# Coding Project: MNIST digits sequence generator

## Problem
In the field of deep learning the volume of available data (labeled and unlabelled) is very important. 
Generating more data can make a difference in final results and improve regression and classification.
When working with visual data, generation of such data can be done by augmenting existing images (rescaling, warping, tilting and more..), 
or construction of random compositions of existing images, and adding them to the dataset to increase volume.
The [MNIST database](http://yann.lecun.com/exdb/mnist/) contains handwritten digits that are often used for training classifiers and generative deep learning
models.
By composing different sequences of digits from this dataset a deep neural network can learn to recognise a larger set of real world handwritten numbers in images.

## Implementation Details

 - The solution is designed in an object oriented approach that separates each functioning unit to an independent module. This allows for easy scaling and implementation improvements/replacements to be done locally without affecting other modules.
 - Loading the MNIST dataset from Keras as 28x28 numpy arrays using the ```mnist_dataset_loader.py``` file. Using the Keras library was implemented considering that most of the python deep learning community is familiar with Keras and most likely are already using it for their networks.
 - To chose random digits each time, a dictionary of digits was created. The dictionary has a key for each digit (0-9) and each key holds a list of indices corresponding to the digit index in the dataset.
 - The spacing between digits is calculated according the user input and the following formula: ```spacing = (final_width - sequence_length * 28) / float(sequence_length - 1)```. If ```spacing``` is an integer and is within the min and max spacing specified by the user, an image of the sequence is generated by joining the randomly chosen digits with the spacing between them.
 - In the corner case where there is only one digit in the sequence, if ```spacing = float(final_width - sequence_length * 28)``` is within the specified spacing, an image with the desired image width will be generated by adding spacing to the right side of the single digit. 
 - Blurring can be applied (and other augmentation functions in the future) to the image by using the ```mnist_data_augmentation.py``` file.
 - An API is provided in ```mnist_sequence_generator_api.py```. Instantiating the api loads the dataset and saves it for efficiency proposes, no need to reload the dataset with every use. The api contains two methods:
    - ```generate_mnist_sequence``` accepts the user input and generates a sequence image.
    - ```save_image``` saves the generated image as < sequence >.png.
 - A CLI script is provided for quick use (man is listed in the cli section). The script uses python's ```optparse``` library to construct a unix-like interface to the user. The CLI allows the user three options of input:
    - ```-s``` for generating a single sequence.
    - ```-f``` for supplying a filename and thus generate multiple sequences. Each line in the file should be in a format of the single sequence.
    - ```-a``` for applying blur augmentation to the final sequence image. 
 - Exceptions can be found in ```mnist_sequence_generator_exceptions.py```. These exceptions were added for ease of use and conveying a clear messages to the user on what went wrong.
 - Unit tests (using python's ```uniteset``` library) can be found in ```test.py```.
 - A Jupyter Notebook displaying running examples, augmentation and error messages in [```mnist_sequence_generator.ipynb```](https://gitlab.com/Shedvarod/mnist_sequence_generator/blob/master/mnist_sequence_generator.ipynb).
 

## Examples and Jupyter notebook

Example for running the ```mnist_sequence_generator_api``` can be viewed in the jupyter notebook [```mnist_sequence_generator.ipynb```](https://gitlab.com/Shedvarod/mnist_sequence_generator/blob/master/mnist_sequence_generator.ipynb)

It is also advised to run the cli locally with the following examples (the file ```sequences.txt``` is provided in the current directory):

```
python mnist_sequence_generator_cli.py -s 450 0 10 94
python mnist_sequence_generator_cli.py -s 650 0 10 94 -a
python mnist_sequence_generator_cli.py -f sequences.txt
python mnist_sequence_generator_cli.py -f sequences.txt -a
```
The file ```sequences.txt``` deliberately contains input errors to demonstrate the error-messages display to the user. 

## API

```
from mnist_sequence_generator_api import MNIST_Sequence_Generator_API

api = MNIST_Sequence_API()
img = api.generate_mnist_sequence(digits, spacing_range, image_width)
api.save_image(img, digits)
```

Parameters:

- ```digits``` is a list-like containing the numerical values of the digits from which the sequence will be generated (for example ```[3, 5, 0]```) 
- ```spacing_range``` a (minimum, maximum) pair (tuple), representing the min and max spacing between digits. Unit should be pixel. 
- ```image_width``` specifies the width of the image in pixels.

Returns:

The image containing the sequence of numbers (28 x image_width). Images are represented
    as floating point 32bits numpy arrays with a scale ranging from 0 (black) to
    1 (white), the first dimension corresponding to the height and the second
    dimension to the width.
    The generated image is saved in the current directory as a < sequence >.png, for example, 3-5-0.png.

## Cli (script)

The CLI man: 

Usage: ```mnist_sequence_generator_cli.py -s <sequence> <min_spacing> <max_spacing> <image_width>``` or usage: ```mnist_sequence_generator_cli.py -f <filename>```

Options:

  ```--version```             show program's version number and 
  
  ```-h, --help```            show this help message and exit
  
  ```-f FILENAME, --filename=FILENAME```
                        Read sequences from file with path filename. Allows
                        creation of multiple sequences at once. File format:
                        each line will contain a valid input to the function
                        generate_mnist_sequence. <sequence> <min_spacing>
                        <max_spacing> <image_width> Example: 350 0 10 94
                        
  ```-s SEQUENCE, --sequence=SEQUENCE```
                        Single sequence generation: <sequence> <min_spacing>
                        <max_spacing> <image_width> Example: 350 0 10 94
                        
  ```-a, --augment```         Augment result sequence.




## Dependencies

The library is supported for Python >= 2.7 (not well tested yet) and Python >= 3.5 (recommended).

Dependencies:
```
Pillow: 3.3.1
Keras: 2.0.4
Tensorflow: 1.1.0
numpy: 1.12.0
```

## Tests

currently there are 6 tests with several test-cases. Use the following command to run unit tests:

```
python test.py -v
```

## TODO (or, call it out)
- Improve documentation
- Test thoroughly 
- Add more augmentation options
- Allow user to choose augmentation and its parameters
- Allow augmentation per digit
- Add incrementation to filname while saving to avoid overwriting existing files
- Improve input checks in cli
- Add local upload of the dataset (to remove dependency in Keras)
- Use Tox for testing and support for all envs (like python 2.7)