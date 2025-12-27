from math import isfinite

def assert_invariants(prev, curr):
    if not isfinite(curr.density) or not isfinite(curr.coherence):
        raise ValueError('Non-finite state')
    if curr.density <= 0:
        raise ValueError('Paradox density collapsed')
    if curr.coherence < 0 or curr.coherence > 1:
        raise ValueError('Coherence out of bounds')
