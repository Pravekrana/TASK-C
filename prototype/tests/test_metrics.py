import unittest
from pathlib import Path
from prototype.src.validation import load_inputs
from prototype.src.models import Stock, Demand
from prototype.src.optimizer import allocate
from prototype.src.baseline import baseline
from prototype.src.metrics import metrics

class MetricsTests(unittest.TestCase):
    def test_demo_accounting_and_tradeoff(self):
        d = Path(__file__).resolve().parents[1]/'data'
        stock, demand = load_inputs(d/'synthetic_stock.csv', d/'synthetic_demand.csv', d/'synthetic_offcuts.csv')
        b, a = [metrics(stock, f(stock, demand)) for f in (baseline, allocate)]
        self.assertAlmostEqual(b['virgin_issued_kg'],120)
        self.assertAlmostEqual(a['virgin_issued_kg'],60)
        self.assertAlmostEqual(b['recoverable_remnant_kg'],60.08)
        self.assertAlmostEqual(a['recoverable_remnant_kg'],0)
        self.assertAlmostEqual(b['unrecoverable_scrap_kg'],0.12)
        self.assertAlmostEqual(a['unrecoverable_scrap_kg'],0.20)
        self.assertGreater(a['scrap_rate'],b['scrap_rate'])
        for m in (b,a):
            self.assertAlmostEqual(m['input_stock_kg'],m['good_parts_kg']+m['unrecoverable_scrap_kg']+m['recoverable_remnant_kg'])
    def test_incomplete_plan_not_comparable(self):
        s = Stock('S','P','G','X',100,10,'virgin')
        p = allocate([s],[Demand('D','P','G','X',101,1)])
        with self.assertRaises(ValueError): metrics([s],p)
    def test_tampered_mass_balance_rejected(self):
        s = Stock('S','P','G','X',100,10,'virgin')
        p = allocate([s],[Demand('D','P','G','X',50,1)])
        p['remaining_mm']['S'] = -1
        with self.assertRaises(ValueError): metrics([s],p)
    def test_reuse_threshold_boundary(self):
        s = Stock('S','P','G','X',1000,10,'virgin')
        p = allocate([s],[Demand('D','P','G','X',497,1)])
        self.assertAlmostEqual(metrics([s],p,500)['recoverable_remnant_kg'],5)
        self.assertEqual(metrics([s],p,501)['recoverable_remnant_kg'],0)
