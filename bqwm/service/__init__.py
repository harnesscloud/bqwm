class default_settings(object):
    SCHEDULER_STRATEGY = 'dummy'


def create_app(cfg=None):
    from flask import Flask
    app = Flask(__name__, instance_relative_config=True)

    load_config(app, cfg)

    from bqwm.service.models import db
    db.init_app(app)
    db.create_all(app=app)
    from bqwm.service import models

    from bqwm.service.views import api_v2_0
    app.register_blueprint(api_v2_0, url_prefix='/v2.0')

    return app


def load_config(app, cfg):
    import os

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                                     'app.db')
    app.config.SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

    app.config.from_object('bqwm.service.default_settings')
    app.config.from_pyfile('/etc/bqwm/default.cfg', silent=True)
    app.config.from_pyfile('default.cfg', silent=True)

    if cfg is None and 'BQWM_CFG' in os.environ:
        cfg = os.environ['BQWM_CFG']

    if cfg is not None:
        app.config.from_pyfile(cfg, silent=False)
