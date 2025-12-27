from paradox_conservation_engine.engine_stub import ParadoxState
from conserved_contradiction_metrics.metrics_stub import paradox_density

state = ParadoxState(density=1.0, coherence=1.0)
print('Paradox density:', paradox_density(state))
