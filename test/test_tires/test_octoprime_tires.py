import unittest
from ...tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        sensors = [1, 1, 1, 0]
        tires = OctoprimeTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        sensors = [0, 0, 0, 0]
        tires = OctoprimeTires(sensors)
        self.assertFalse(tires.needs_service())