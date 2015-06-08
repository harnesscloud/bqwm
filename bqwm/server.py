from argparse import ArgumentParser
from daemon import DaemonContext

from bqwm.app import create_app


def main(argv=None):

    parser = ArgumentParser(description="batch queue workload manager daemon")
    parser.add_argument('-b', '--bind', default='127.0.0.1',
                        help='tcp bind address')
    parser.add_argument('-p', '--port', default='5000',
                        help='tcp listen port')
    parser.add_argument('-n', '--nofork', action='store_true',
                        help='do not fork to background')
    parser.add_argument('-c', '--config', help='override config file')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='debug mode')

    args = parser.parse_args()

    app = create_app(cfg=args.config)

    detach_process = not args.nofork

    if args.debug:
        app.run(debug=True)
    else:
        with DaemonContext(detach_process=detach_process):
            app.run(host=args.bind, port=args.port)


if __name__ == "__main__":
    main()
