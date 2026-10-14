import unittest
from dataclasses import replace
from itertools import product
from prototype.src.models import Stock, Demand
from prototype.src.optimizer import allocate
from prototype.src.baseline import baseline

S = Stock('S', 'P', 'G', 'X', 6000, 10., 'virgin')
D = Demand('D', 'P', 'G', 'X', 1000, 1)

class OptimizerTests(unittest.TestCase):
    def test_project_grade_section_blocked(self):
        for field, reason in [('project','PROJECT_OWNERSHIP'), ('grade','GRADE'), ('section','SECTION')]:
            p = allocate([replace(S, **{field:'OTHER'})], [D])
            self.assertFalse(p['complete'])
            self.assertIn(reason, p['audit'][0]['reasons'])
    def test_kerf_boundary(self):
        self.assertTrue(allocate([S], [replace(D, length_mm=5997)])['complete'])
        self.assertFalse(allocate([S], [replace(D, length_mm=5998)])['complete'])
    def test_quantity_exhausts_inventory(self):
        p = allocate([S], [replace(D, length_mm=3000, quantity=2)])
        self.assertEqual(len(p['allocations']), 1)
        self.assertEqual(len(p['rejected']), 1)
    def test_determinism(self):
        self.assertEqual(allocate([S], [D]), allocate([S], [D]))
    def test_negative_kerf(self):
        with self.assertRaises(ValueError): allocate([S], [D], -1)
    def test_both_strategies_consider_offcuts_first(self):
        for strategy in [baseline, allocate]:
            p = strategy([S, replace(S, id='O', kind='offcut')], [D])
            self.assertEqual(p['allocations'][0]['stock'], 'O')
    def test_small_exhaustive_conservation(self):
        for lengths in product([1, 3, 5], repeat=3):
            stock = [replace(S, id=str(i), length_mm=10) for i in range(3)]
            demand = [replace(D, id=str(i), length_mm=v) for i,v in enumerate(lengths)]
            for strategy in [baseline, allocate]:
                p = strategy(stock, demand, kerf_mm=1)
                self.assertTrue(p['complete'])
                self.assertEqual(len({(a['part'],a['piece']) for a in p['allocations']}), 3)
                for s in stock:
                    used = sum(a['length_mm']+a['kerf_mm'] for a in p['allocations'] if a['stock']==s.id)
                    self.assertEqual(used + p['remaining_mm'][s.id], s.length_mm)
                    self.assertGreaterEqual(p['remaining_mm'][s.id], 0)
