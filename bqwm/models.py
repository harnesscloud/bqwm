from bqwm.database import db


class ResourceManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manager = db.Column(db.String(255))
    host = db.Column(db.String(255))
    port = db.Column(db.Integer)
    name = db.Column(db.String(255))


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_ = db.Column(db.String(255))
    attributes = db.relationship("ResourceAttributes", backref="resource")
    reservations = db.relationship("ResourceReservation", backref="resource")


class ResourceAttributes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey("resource.id"))
    key = db.Column(db.String(255))
    value = db.Column(db.Integer)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    allocation = db.relationship("ResourceReservation", backref="reservation")
    constraints = db.relationship("Constraint", backref="reservation")


class ResourceReservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey("reservation.id"))
    type_ = db.Column(db.String(255))
    group = db.Column(db.String(255))
    resource_id = db.Column(db.Integer, db.ForeignKey("resource.id"))
    attributes = db.relationship("ResourceReservationAttributes",
                                 backref="resource_reservation")


class ResourceReservationAttributes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_reservation_id = db.Column(
        db.Integer, db.ForeignKey("resource_reservation.id"))
    key = db.Column(db.String(255))
    value = db.Column(db.Integer)


class Constraint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey("reservation.id"))
    source = db.Column(db.String(255))
    target = db.Column(db.String(255))
    constraint_type = db.Column(db.String(255))


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
        return 'JobConfiguration: {} {} {}'.format(
            self.utility_function, self.estimated_time, self.price)
