from paradox_conservation_engine.engine import ParadoxEngine, ParadoxState
from higher_dimensional_horizons.multi import multi_horizon
from planetary_field_engine.coupling import couple

engine = ParadoxEngine()
state = ParadoxState(1.0, 0.5)

state = engine.step(state)
state = multi_horizon(state, depth=4)
state = couple(state, field_strength=0.95)

print(state)
