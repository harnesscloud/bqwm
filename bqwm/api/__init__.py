
def create_app():
    from flask import Flask
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('api.cfg', silent=True)
    from bqwm.api.views import api
    app.register_blueprint(api, url_prefix='/v2.0')
    return app
