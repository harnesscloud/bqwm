import os
from flask import Flask

from bqwm.api.views import api_v2_0


def create_app(cfg=None):
    app = Flask(__name__)

    load_config(app, cfg)

    app.register_blueprint(api_v2_0, url_prefix='/v2.0')

    return app


def load_config(app, cfg):
    app.config.from_pyfile('config/default.cfg', silent=True)

    if cfg is None and 'BQWM_CFG' in os.environ:
        cfg = os.environ['BQWM_CFG']

    if cfg is not None:
        app.config.from_pytfile(cfg)
