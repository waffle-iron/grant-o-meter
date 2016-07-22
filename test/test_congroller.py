import unittest
from grantometer import controllers
import dateutil.parser


class GrumpyControllerTests(unittest.TestCase):
    def test_increase_grumpiness_from_zero(self):
        self.assertEqual(1, controllers.increase_grumpiness(0),
                         'Grumpyness from zero')

    def test_increase_grumpiness_from_73(self):
        self.assertEqual(110, controllers.increase_grumpiness(73),
                         'Grumpyness from 73')

    def test_increase_grumpiness_to_max(self):
        self.assertEqual(100, controllers.increase_grumpiness(50),
                         'Grumpyness to 100')

    def test_decrease_grumpiness(self):
        self.assertEqual(100, controllers.decrease_grumpiness(800))

    def test_decrease_grumpiness_regular(self):
        self.assertEqual(66.75, controllers.decrease_grumpiness(73))

    def test_cool_down_3h(self):
        test = controllers.cool_down_grumpiness(51,  dateutil.parser.parse(
                                                    "2016-07-16T16:00:00Z"),
                                                     dateutil.parser.parse(
                                                     "2016-07-16T13:00:00Z"))
        self.assertEqual(44.25, test)

    def test_cool_down_12h00m(self):
        test = controllers.cool_down_grumpiness(110,  dateutil.parser.parse(
                                                        "2016-07-16T16:00:00Z"),
            dateutil.parser.parse("2016-07-16T04:00:00Z"))
        self.assertEqual(2, test)

    def test_cool_down_24h00(self):
        test = controllers.cool_down_grumpiness(100,  dateutil.parser.parse(
                                                        "2016-07-16T16:00:00Z"),
                                                      dateutil.parser.parse(
                                                      "2016-07-15T16:00:00Z"))
        self.assertEqual(0, test)

    def test_cool_down_7h00(self):
        test = controllers.cool_down_grumpiness(100,  dateutil.parser.parse(
                                                        "2016-07-15T16:00:00Z"),
                                                      dateutil.parser.parse(
                                                      "2016-07-15T06:00:00Z"))
        self.assertEqual(25, test)
