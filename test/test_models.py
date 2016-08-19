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
        num_entries = models.Grumpiness.query.count()
        gd = models.Grumpiness(10)
        g1d = models.Grumpiness(80)
        db.session.add(g1d)
        db.session.add(gd)
        db.session.commit()
        gd2 = models.Grumpiness.query.all()
        assert len(gd2) == 2 + num_entries

    def test_read_last_in_bulk(self):
        objects =  [models.Grumpiness(2),
                    models.Grumpiness(3),
                    models.Grumpiness(50, "myId")]
        db.session.bulk_save_objects(objects)
        gd = db.session.query(models.Grumpiness).order_by(
                            models.Grumpiness.id.desc()).first()
        assert gd.grumpiness == 50
        assert gd.guid == "myId"
