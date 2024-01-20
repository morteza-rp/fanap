import argparse
import numpy as np
import sys
import os
from game import check_number


def main():
    parser = argparse.ArgumentParser(description="Generate an array and check for win/fail conditions.")
    parser.add_argument("-n", "--array_size", type=int, default=5, help="Size of the array to generate.")
    args = parser.parse_args()

    g = check_number()
    array = g.array_generator(args.array_size)
    print("array:", array)
    print("maximum number:", max(array))
    print("result:", g.win_fail(array))


if __name__ == "__main__":
    main()

