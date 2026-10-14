import csv
import math
from .models import Stock, Demand


def load_inputs(stock_path, demand_path, offcut_path):
    def rows(path):
        with open(path, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    def stocks(path, kind):
        return [Stock(r['id'], r['project'], r['grade'], r['section'],
                      int(r['length_mm']), float(r['kg_per_m']), kind) for r in rows(path)]
    stock = stocks(stock_path, 'virgin') + stocks(offcut_path, 'offcut')
    demand = [Demand(r['id'], r['project'], r['grade'], r['section'],
                     int(r['length_mm']), int(r['quantity'])) for r in rows(demand_path)]
    validate(stock, demand)
    return stock, demand


def validate(stock, demand):
    for name, records in [('stock', stock), ('demand', demand)]:
        ids = [r.id for r in records]
        if len(set(ids)) != len(ids):
            raise ValueError(f'Duplicate {name} ID')
        for r in records:
            if any(not str(getattr(r, k)).strip() for k in ('id', 'project', 'grade', 'section')):
                raise ValueError('Missing identity or eligibility field')
            if type(r.length_mm) is not int or r.length_mm <= 0:
                raise ValueError('Length must be a positive integer in mm')
    densities = {}
    for s in stock:
        if s.kind not in ('virgin', 'offcut') or not math.isfinite(s.kg_per_m) or s.kg_per_m <= 0:
            raise ValueError('Invalid stock kind or mass per metre')
        key = s.grade, s.section
        if key in densities and not math.isclose(densities[key], s.kg_per_m):
            raise ValueError('Inconsistent mass per metre for material family')
        densities[key] = s.kg_per_m
    for d in demand:
        if type(d.quantity) is not int or d.quantity <= 0:
            raise ValueError('Quantity must be a positive integer')


def rejection_reasons(s, d, remaining, kerf):
    reasons = []
    if s.project != d.project:
        reasons.append('PROJECT_OWNERSHIP')
    if s.grade != d.grade:
        reasons.append('GRADE')
    if s.section != d.section:
        reasons.append('SECTION')
    if remaining < d.length_mm + kerf:
        reasons.append('LENGTH_PLUS_KERF')
    return reasons
