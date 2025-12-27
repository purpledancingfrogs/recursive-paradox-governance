from paradox_conservation_engine.engine import ParadoxEngine, ParadoxState
from conserved_contradiction_metrics.metrics import Pi

engine = ParadoxEngine()
state = ParadoxState(density=1.0, coherence=0.4)
for _ in range(5):
    state = engine.step(state)
    print('Π:', Pi(state))
