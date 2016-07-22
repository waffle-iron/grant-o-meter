from grantometer import db
import datetime


class Grumpiness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grumpiness = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def __init__(self, grumpiness, timestamp=datetime.datetime.now()):
        self.grumpiness = grumpiness
        self.timestamp = timestamp

    def __repr__(self):
        return 'Grumpiness %s at %s' % (self.grumpiness, self.timestamp)
