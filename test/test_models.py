import unittest
from grantometer import models
from grantometer import db
from grantometer import app


class ModelTests(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        app.config['TESTING'] = True
        with app.app_context():
            db.create_all()

    def test_write_grumpy_DB(self):
        num_entries = models.Grumpyness.query.count()
        gd = models.Grumpyness(10)
        g1d = models.Grumpyness(80)
        db.session.add(g1d)
        db.session.add(gd)
        db.session.commit()
        gd2 = models.Grumpyness.query.all()
        assert len(gd2) == 2 + num_entries

    def test_read_last_in_bulk(self):
        objects =  [models.Grumpyness(2),
                    models.Grumpyness(3),
                    models.Grumpyness(50)]
        db.session.bulk_save_objects(objects)
        gd = db.session.query(models.Grumpyness).order_by(
                            models.Grumpyness.id.desc()).first()
        assert gd.grumpyness == 50

