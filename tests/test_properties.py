from paradox_conservation_engine.engine import ParadoxEngine, ParadoxState
from conserved_contradiction_metrics.checks import assert_invariants

engine = ParadoxEngine()
s = ParadoxState(density=1.0, coherence=0.5)
for _ in range(100):
    prev = s
    s = engine.step(s)
    assert_invariants(prev, s)
