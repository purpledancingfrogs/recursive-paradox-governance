from paradox_conservation_engine.engine import ParadoxEngine, ParadoxState
from conserved_contradiction_metrics.checks import assert_invariants
from higher_dimensional_horizons.horizons import refract
from higher_dimensional_horizons.nesting import nest

engine = ParadoxEngine()
state = ParadoxState(density=1.0, coherence=0.4)
horizons = [refract, refract]

for _ in range(10):
    prev = state
    state = engine.step(state)
    state = nest(horizons, state)
    assert_invariants(prev, state)
    print('Π:', state.density, 'Ξ:', state.coherence)
