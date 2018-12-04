from __future__ import print_function
from PIL import Image, ImageFilter
import numpy as np

# TODO add more augmentation functions
# TODO allow user to choose random augmentation or user specified augmentations

def blur_img(img):
    """Adds blur to image.
    """

    # TODO pass radius parameter through function parameters
    img = Image.fromarray(img.astype('uint8'))
    return np.array(img.filter(ImageFilter.GaussianBlur(radius=1.2))).astype('float64')
