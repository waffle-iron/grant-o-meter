import unittest
from grantometer import controllers


class ControllerTests(unittest.TestCase):
    def test_increase_grumpyness_from_zero(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 0
        gt.increase_grumpyness()
        self.assertEqual(1, gt.grumpyness, 'Grumpyness from zero')

    def test_increase_grumpyness_from_255(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 255
        gt.increase_grumpyness()
        self.assertEqual(510, gt.grumpyness, 'Grumpyness from 510')

    def test_increase_grumpyness_to_max(self):
        gt = controllers.GrumpyControl()
        gt.grumpyness = 501
        gt.increase_grumpyness()
        self.assertEqual(1000, gt.grumpyness, 'Grumpyness from 510')
