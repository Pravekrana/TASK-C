from .optimizer import allocate


def baseline(stock, demand, kerf_mm=3):
    return allocate(stock, demand, kerf_mm=kerf_mm, assisted=False)
