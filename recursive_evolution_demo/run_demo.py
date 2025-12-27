from paradox_conservation_engine.engine import ParadoxEngine, ParadoxState
from higher_dimensional_horizons.multi import multi_horizon
from planetary_field_engine.coupling import couple

def main():
    engine = ParadoxEngine()
    state = ParadoxState(coherence=1.0, paradox_density=0.5)

    state = engine.step(state)
    state = multi_horizon(state, depth=3)
    state = couple(state, field_strength=0.9)

    print(state.coherence, state.paradox_density)

if __name__ == "__main__":
    main()