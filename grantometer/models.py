from grantometer import db
import datetime

class Grumpyness(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    grumpyness = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def __init__(self, grumpyness):
        self.grumpyness = grumpyness
        self.timestamp = datetime.datetime.now()

    def __repr__(self):
        return 'Grumpyness %r at %r' % (self.grumpyness, self.timestamp)
