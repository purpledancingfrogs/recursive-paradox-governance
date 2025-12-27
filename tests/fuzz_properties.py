import random
from paradox_conservation_engine.engine import ParadoxEngine, ParadoxState
from conserved_contradiction_metrics.checks import assert_invariants

engine = ParadoxEngine()
s = ParadoxState(1.0, 0.5)
for _ in range(200):
    s = engine.step(s)
    s.coherence = min(1.0, max(0.0, s.coherence + random.uniform(-0.05, 0.05)))
    assert_invariants(s, s)
