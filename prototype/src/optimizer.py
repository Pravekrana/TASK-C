from .validation import validate, rejection_reasons


def allocate(stock, demand, kerf_mm=3, assisted=True):
    """Deterministic offcut-first greedy allocation; no optimality claim.

    One kerf per produced piece, even exact-end cuts. Integer mm. No transfers.
    Baseline uses input demand order and first-fit. Assisted uses decreasing
    lengths and best-fit within offcut/virgin priority. Both check offcuts first.
    """
    validate(stock, demand)
    if type(kerf_mm) is not int or kerf_mm < 0:
        raise ValueError('Kerf must be non-negative integer mm')
    pieces = [(d, n + 1) for d in demand for n in range(d.quantity)]
    if assisted:
        pieces.sort(key=lambda x: (-x[0].length_mm, x[0].id, x[1]))
    remaining = {s.id: s.length_mm for s in stock}
    allocations, rejected, trail = [], [], []
    for d, n in pieces:
        candidates = []
        for order, s in enumerate(stock):
            reasons = rejection_reasons(s, d, remaining[s.id], kerf_mm)
            if reasons:
                trail.append(dict(part=d.id, piece=n, stock=s.id, event='INELIGIBLE', reasons=reasons))
            else:
                rank = (s.kind != 'offcut', remaining[s.id] - d.length_mm - kerf_mm if assisted else order, s.id)
                candidates.append((rank, s))
        if not candidates:
            rejected.append(dict(part=d.id, piece=n, reason='NO_FEASIBLE_STOCK'))
            continue
        _, s = min(candidates, key=lambda x: x[0])
        remaining[s.id] -= d.length_mm + kerf_mm
        row = dict(part=d.id, piece=n, stock=s.id, length_mm=d.length_mm, kerf_mm=kerf_mm)
        allocations.append(row)
        trail.append(dict(**row, event='SELECTED', remaining_mm=remaining[s.id]))
    return dict(strategy='assisted' if assisted else 'baseline', complete=not rejected,
                allocations=allocations, rejected=rejected, remaining_mm=remaining, audit=trail)
