import unittest
from dataclasses import replace
from prototype.src.models import Stock, Demand
from prototype.src.validation import validate

S = Stock('S', 'P', 'G', 'X', 6000, 10., 'virgin')
D = Demand('D', 'P', 'G', 'X', 1000, 1)

class ValidationTests(unittest.TestCase):
    def test_duplicate_physical_identity(self):
        with self.assertRaises(ValueError): validate([S, replace(S, kind='offcut')], [D])
    def test_missing_project(self):
        with self.assertRaises(ValueError): validate([replace(S, project='')], [D])
    def test_invalid_quantities_and_lengths(self):
        for d in [replace(D, quantity=0), replace(D, quantity=1.5), replace(D, length_mm=-1)]:
            with self.assertRaises(ValueError): validate([S], [d])
    def test_nonfinite_mass(self):
        for v in [float('nan'), float('inf'), -1]:
            with self.assertRaises(ValueError): validate([replace(S, kg_per_m=v)], [D])
    def test_inconsistent_density(self):
        with self.assertRaises(ValueError): validate([S, replace(S, id='S2', kg_per_m=11)], [D])
    def test_duplicate_demand(self):
        with self.assertRaises(ValueError): validate([S], [D, D])
