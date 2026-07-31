import argparse
import os
import sys
import logging
from regression import Regression


def main():
    parser = argparse.ArgumentParser(prog='regression_learning_rate',
                                     description='')
    parser.add_argument('file',
                        help='Path to the file containing the data to analyse')
    parser.add_argument('-l', "--learning_rate", type=float, help="learning_rate",
                        default=0.01, required=False)
    parser.add_argument('-i', "--iteration", type=int, help="learning_rate",
                        default=1000, required=False)
    args = parser.parse_args()
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                        level=logging.CRITICAL)
    if not os.path.exists(args.file):
        logging.critical('No file: %s', args.file)
        sys.exit(1)
    logging.info('%s exist', args.file)
    a = Regression(args.file, args.learning_rate, args.iteration)
    print("----")
    a.gradient_descent_norm()
    print("----")
    a.print_result()

    return


main()
