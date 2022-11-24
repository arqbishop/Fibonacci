import argparse

if __name__ == '__main__':

    # Argument creation
    parser = argparse.ArgumentParser(
        description = 'Computes the Fibonacci sequence up to a given number.'
                      '\n Also returns the length of the sequence.'
    )

    parser.add_argument(
        'integer',
        metavar = 'integer',
        type = int,
        help = 'Enter the integer you wish to compute the sequence up to.'
    )
    args = vars(parser.parse_args())

    # Variable creation according to the argument
    n = args['integer']

    if n <= 0:
        raise ValueError('the integer must be greater than zero.')

    else:

        a, b = 0, 1
        sequence = []

        while a < n:
            sequence.append(a)
            a, b = b, a + b

        print("Sequence: ", sequence, "\n n = ", len(sequence), "\n")