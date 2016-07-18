import unittest
from grantometer import controllers
import dateutil.parser


class ControllerTests(unittest.TestCase):
    def test_increase_grumpyness_from_zero(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 0
        gt.increase_grumpyness()
        self.assertEqual(1, gt.grumpyness, 'Grumpyness from zero')

    def test_increase_grumpyness_from_255(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 73
        gt.increase_grumpyness()
        self.assertEqual(110, gt.grumpyness, 'Grumpyness from 73')

    def test_increase_grumpyness_to_max(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 50
        gt.increase_grumpyness()
        self.assertEqual(100, gt.grumpyness, 'Grumpyness to 100')

    def test_decrease_grumpyness(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 800
        gt.decrease_grumpyness()
        self.assertEqual(100, gt.grumpyness)

    def test_decrease_grumpyness_regular(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 73
        gt.decrease_grumpyness()
        self.assertEqual(66.75, gt.grumpyness)

    def test_cool_down_3h(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 51
        gt.timestamp = dateutil.parser.parse("2016-07-16T13:00:00Z")
        gt.cool_down_grumpyness("2016-07-16T16:00:00Z")
        self.assertEqual(44.25, gt.grumpyness)

    def test_cool_down_12h00m(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 110
        gt.timestamp = dateutil.parser.parse("2016-07-16T04:00:00Z")
        gt.cool_down_grumpyness("2016-07-16T16:00:00Z")
        self.assertEqual(2, gt.grumpyness)

    def test_cool_down_24h00(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 100
        gt.timestamp = dateutil.parser.parse("2016-07-15T16:00:00Z")
        gt.cool_down_grumpyness("2016-07-16T16:00:00Z")
        self.assertEqual(0, gt.grumpyness)

    def test_cool_down_7h00(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 100
        gt.timestamp = dateutil.parser.parse("2016-07-15T06:00:00Z")
        gt.cool_down_grumpyness("2016-07-15T16:00:00Z")
        self.assertEqual(25, gt.grumpyness)
