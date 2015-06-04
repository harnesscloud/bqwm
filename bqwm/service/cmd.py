from argparse import ArgumentParser
from daemon import DaemonContext

from bqwm.service import create_app


def main(argv=None):

    parser = ArgumentParser(description="BQWM api daemon")
    parser.add_argument('-b', '--bind', help='bind to ip address',
                        default='127.0.0.1')
    parser.add_argument('-p', '--port', help='listen port',
                        default='5000')
    parser.add_argument('-n', '--nofork', help='tell daemon not to fork',
                        action='store_true')
    parser.add_argument('-c', '--config', help='override config file')

    args = parser.parse_args()

    app = create_app(cfg=args.config)

    detach_process = not args.nofork

    with DaemonContext(detach_process=detach_process):
        app.run(host=args.bind, port=args.port)


if __name__ == "__main__":
    main()
