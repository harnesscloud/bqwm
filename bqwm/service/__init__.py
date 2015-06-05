import os
from flask import Flask

from bqwm.service.api import api_v2_0


class default_settings(object):
    SCHEDULER_STRATEGY = 'dummy'


def create_app(cfg=None):
    app = Flask(__name__, instance_relative_config=True)

    load_config(app, cfg)

    app.register_blueprint(api_v2_0, url_prefix='/v2.0')

    return app


def load_config(app, cfg):

    app.config.from_object('bqwm.service.default_settings')
    app.config.from_pyfile('/etc/bqwm/default.cfg', silent=True)
    app.config.from_pyfile('default.cfg', silent=True)

    if cfg is None and 'BQWM_CFG' in os.environ:
        cfg = os.environ['BQWM_CFG']

    if cfg is not None:
        app.config.from_pyfile(cfg, silent=False)
