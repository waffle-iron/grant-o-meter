from grantometer import db
import datetime


class Grumpiness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String(36))
    grumpiness = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def __init__(self, grumpiness, guid='', timestamp=datetime.datetime.now()):
        self.guid = guid
        self.grumpiness = grumpiness
        self.timestamp = timestamp

    def __repr__(self):
        return 'Grumpiness of  %s is %s at %s' % (self.guid, self.grumpiness,
                                                  self.timestamp)


def save_new_grumpiness(guid, grumpiness, timestamp):
    new_entry = Grumpiness(guid, grumpiness, timestamp)
    db.session.add(new_entry)
    db.session.commit()
    print(new_entry)
