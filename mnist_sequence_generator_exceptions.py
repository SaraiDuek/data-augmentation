
class MissingImgException(Exception):
    """Raised when there are no images of a certain digit in the sequence in the dataset.

        Attributes:
            digit -- the digit from which there are no images in the dataset
    """

    def __init__(self, digit):
        self.digit = digit


    def __str__(self):
        return 'There are no images for the digit ' + str(self.digit) + ' in the dataset.'


class BadArgumentsException(Exception):
    """Raised when some arguments are bad.

        Attributes:
            msg  -- explanation of why the specific argument is bad
    """

    def __init__(self, msg):
        self.msg = msg


    def __str__(self):
        return self.msg


class BadMeasurementsException(Exception):
    """Raised when the specepied measurements do not fit, and it is impossible to generate sequence.
    """

    def __init__(self, sequence_length, min_space, max_space, final_width):
        self.sequence_length = sequence_length
        self.min_space = min_space
        self.max_space = max_space
        self.final_width = final_width


    def __str__(self):
        return 'Unable to generate the sequence with the specified measurements. \n' +\
               '    Sequence_length = ' + str(self.sequence_length) + '\n' + \
               '    Minimum_spacing = ' + str(self.min_space) + '\n' + \
               '    Maximum_spacing = ' + str(self.max_space) + '\n' + \
               '    Final_width = ' + str(self.final_width) + '\n' + \
               '    Try adjusting the measurements to fit the following formula: \n' + \
               '    Final_width = (sequence_length * ' + str(28) + \
               ') + (number_between[Minimum_spacing - Maximum_spacing] * (Sequence_length - 1))'
