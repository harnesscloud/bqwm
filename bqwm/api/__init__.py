from flask import Flask
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('api.cfg', silent=True)

import bqwm.api.views
