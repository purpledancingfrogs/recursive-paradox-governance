from paradox_conservation_engine.engine import ParadoxEngine, ParadoxState
from conserved_contradiction_metrics.metrics import Pi

engine = ParadoxEngine()
s0 = ParadoxState(density=1.0, coherence=0.5)
s1 = engine.step(s0)
assert Pi(s1) > 0
