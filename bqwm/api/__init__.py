import os
from daemon import DaemonContext
from flask import Flask

from bqwm.api.views import api_v2_0


class default_settings(object):
    SCHEDULER_STRATEGY = 'dummy'


def create_app(cfg=None):
    app = Flask(__name__, instance_relative_config=True)

    load_config(app, cfg)

    app.register_blueprint(api_v2_0, url_prefix='/v2.0')

    return app


def load_config(app, cfg):

    app.config.from_object('bqwm.api.default_settings')
    app.config.from_pyfile('default.cfg', silent=True)

    if cfg is None and 'BQWM_CFG' in os.environ:
        cfg = os.environ['BQWM_CFG']

    if cfg is not None:
        app.config.from_pyfile(cfg, silent=False)

    print app.config


def main(argv=None):
    from argparse import ArgumentParser

    parser = ArgumentParser(description="BQWM api daemon")
    parser.add_argument('-b', '--bind', help='bind to ip address',
                        default='127.0.0.1')
    parser.add_argument('-p', '--port', help='listen port',
                        default='5000')
    parser.add_argument('-n', '--nofork', help='tell daemon not to fork',
                        action='store_true')
    args = parser.parse_args()

    detach_process = not args.nofork

    app = create_app()
    with DaemonContext(detach_process=detach_process):
        app.run(host=args.bind, port=args.port)


if __name__ == "__main__":
    main()
