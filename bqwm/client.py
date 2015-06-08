from argparse import ArgumentParser
from yaml import load as yload

import requests


def main(argv=None):

    parser = ArgumentParser(description="batch queue workload manager client")
    parser.add_argument('-s', '--server', default='127.0.0.1', 
                        help='bqwmd server')
    parser.add_argument('-p', '--port', default='5000', help='bqwmd port')
    parser.add_argument('-i', '--input', help='input file')

    args = parser.parse_args()

    configs = yload(open(args.input, 'r'))

    service_url = "http://{}:{}/v2.0/createReservation".format(args.server,
                                                               args.port)
    response = requests.post(service_url, json=configs)

    print response.text

if __name__ == "__main__":
    main()
