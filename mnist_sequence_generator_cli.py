from __future__ import print_function
from optparse import OptionParser
from mnist_sequence_generator_api import MNIST_Sequence_Generator_API
import sys

def parse_sequences_file(filename):
    with open(filename) as f:
        sequences = []
        for line in f.readlines():
            sequences.append(tuple(line.strip().split(' ')))
    return sequences

def sequence_str_to_list(sequence):
    return [int(sequence[i]) for i in range(len(sequence))]

def is_sequence_valid(sequence):
    for val in sequence:
        if not val.isdigit():
            return False
    return True

def main():
    """Runs the minst_sequence_generator_api through the command line.
       Accepts a single sequence or a file contining many sequences, generates and saves them to the local directory.
    """

    # TODO check input thoroughly

    parser = OptionParser(usage='usage: %prog -s <sequence> <min_spacing> <max_spacing> <image_width> ' +
                                'or usage: %prog -f <filename>',
                          version='%prog 1.0')
    parser.add_option('-f', '--filename',
                      dest='filename',
                      help='Read sequences from file with path filename. ' +
                           'Allows creation of multiple sequences at once. ' +
                           'File format: each line will contain a valid input to ' +
                           'the function generate_mnist_sequence. ' +
                           '<sequence> <min_spacing> <max_spacing> <image_width> ' +
                           'Example: 350 0 10 94')
    parser.add_option('-s', '--sequence',
                      dest='sequence',
                      nargs=4,
                      help='Single sequence generation: <sequence> <min_spacing> <max_spacing> <image_width> ' +
                           'Example: 350 0 10 94')
    parser.add_option('-a', '--augment',
                      dest='augment',
                      action='store_true',
                      default=False,
                      help='Augment result sequence.')
    (options, args) = parser.parse_args()

    if options.filename and options.sequence:
        parser.error('Wrong number of arguments. Please use either -f or -s.')

    if len(args) != 0:
        parser.error('Wrong number of arguments. Please use either -f or -s, with no further arguments.')



    sequences = []
    if options.filename:
        sequences = parse_sequences_file(options.filename)
    elif options.sequence:
        sequences.append(options.sequence)

    mnist_sequence_generator_api = MNIST_Sequence_Generator_API()
    line_counter = 1
    for seq in sequences:
        sys.stdout.write(str(line_counter) + ': ')
        line_counter += 1

        if len(seq) < 4:
            print('Bad Arguments: Sequence must contain 4 arguments.')
            continue
        if not is_sequence_valid(seq):
            print('Bad Arguments: Please make sure all arguments are numeric.')
            continue

        sequence = sequence_str_to_list(seq[0])
        try:
            img = mnist_sequence_generator_api.generate_mnist_sequence(sequence, (int(seq[1]), int(seq[2])),
                                                                       int(seq[3]), options.augment)
            mnist_sequence_generator_api.save_image(img, sequence)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
