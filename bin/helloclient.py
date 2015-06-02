#!/usr/bin/env python

from argparse import ArgumentParser
from yaml import load as yload

import requests


def main(argv=None):

    parser = ArgumentParser(description="Solve a vector packing problem.")
    parser.add_argument('-i', '--input', help='input file')

    args = parser.parse_args()

    configs = yload(open(args.input, 'r'))

    response = requests.post("http://127.0.0.1:5000/createReservation",
                             json=configs)

    print response.text

if __name__ == "__main__":
    main()
