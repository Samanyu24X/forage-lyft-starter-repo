import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2003-1-1")
        last_service_date = date.isoformat("2000-1-1")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2001-1-1")
        last_service_date = date.isoformat("2000-1-1")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())