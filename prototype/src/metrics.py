import math


def metrics(stock, plan, min_reusable_mm=500):
    if type(min_reusable_mm) is not int or min_reusable_mm < 0:
        raise ValueError('Invalid remnant threshold')
    if not plan['complete'] or plan['rejected']:
        raise ValueError('Incomplete plans cannot be compared as complete demand')
    by_id = {s.id: s for s in stock}
    used = {a['stock'] for a in plan['allocations']}
    kg = lambda s, mm: mm / 1000 * s.kg_per_m
    input_kg = sum(kg(by_id[i], by_id[i].length_mm) for i in used)
    virgin = sum(kg(by_id[i], by_id[i].length_mm) for i in used if by_id[i].kind == 'virgin')
    good = sum(kg(by_id[a['stock']], a['length_mm']) for a in plan['allocations'])
    kerf = sum(kg(by_id[a['stock']], a['kerf_mm']) for a in plan['allocations'])
    recoverable, tail = 0., 0.
    for i in used:
        allocated = sum(a['length_mm'] + a['kerf_mm'] for a in plan['allocations'] if a['stock'] == i)
        rest = plan['remaining_mm'][i]
        if rest < 0 or allocated + rest != by_id[i].length_mm:
            raise ValueError('Length conservation failed')
        if rest >= min_reusable_mm:
            recoverable += kg(by_id[i], rest)
        else:
            tail += kg(by_id[i], rest)
    if not math.isclose(input_kg, good + kerf + tail + recoverable, abs_tol=1e-8):
        raise ValueError('Mass conservation failed')
    return dict(input_stock_kg=input_kg, virgin_issued_kg=virgin,
                existing_offcut_input_kg=input_kg-virgin, good_parts_kg=good,
                kerf_kg=kerf, unrecoverable_scrap_kg=kerf+tail,
                recoverable_remnant_kg=recoverable,
                scrap_rate=(kerf+tail)/input_kg if input_kg else 0,
                virgin_kg_per_good_kg=virgin/good if good else None,
                used_stock_count=len(used))
