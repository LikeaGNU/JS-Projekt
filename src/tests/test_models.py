#!/usr/bin/python3

import unittest
import sys
from memory_profiler import profile
sys.path.insert(0, '..')

import utils.models as models

class test_model(unittest.TestCase):
    def setUp(self):
        self.record = models.Record(list())
        self.record.set_station_name('Stacja')
        self.record.set_station_city('Kielce')
        self.record.set_station_quantity('Temperatura')
    def test_get_station_name(self):
        self.assertEqual(self.record.get_station_name(), 'Stacja')
    def test_get_station_city(self):
        self.assertEqual(self.record.get_station_city(), 'Kielce')
    def test_get_station_quantity(self):
        self.assertEqual(self.record.get_station_quantity(), 'Temperatura')

if __name__ == '__main__':
    unittest.main()
