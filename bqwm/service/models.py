from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class JobConfiguration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    utility_function = db.Column(db.String(64))
    estimated_time = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
