import os


class default_settings(object):
    SCHEDULER_STRATEGY = 'dummy'


def create_app(cfg=None):
    from flask import Flask
    app = Flask(__name__, instance_relative_config=True)

    load_config(app, cfg)

    from bqwm.database import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    from bqwm import models

    from bqwm.views import api_v2_0
    app.register_blueprint(api_v2_0, url_prefix='/v2.0')

    return app


def load_config(app, cfg):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
        os.path.join(app.instance_path, 'bqwm.db'))
    app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(app.instance_path,
                                                         'db_repository')
    app.config.from_object('bqwm.app.default_settings')
    app.config.from_pyfile('/etc/bqwm/default.cfg', silent=True)
    app.config.from_pyfile('default.cfg', silent=True)

    if cfg is None and 'BQWM_CFG' in os.environ:
        cfg = os.environ['BQWM_CFG']

    if cfg is not None:
        app.config.from_pyfile(cfg, silent=False)
