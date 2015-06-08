from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class JobConfiguration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    utility_function = db.Column(db.String(64))
    estimated_time = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __init__(self, utility_function, estimated_time, price):
        self.utility_function = utility_function
        self.estimated_time = estimated_time
        self.price = price

    def __repr__(self):
        return 'JobConfiguration: {} {} {}'.format(self.utility_function,
                                                   self.estimated_time,
                                                   self.price)
