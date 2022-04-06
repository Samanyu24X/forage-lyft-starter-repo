import unittest
from ...tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        sensors = [0.5, 0.3, 0.4, 0.9]
        tires = CarriganTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        sensors = [0, 0, 0.5, 0]
        tires = CarriganTires(sensors)
        self.assertFalse(tires.needs_service())