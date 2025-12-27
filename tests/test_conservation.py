from paradox_conservation_engine.engine import ParadoxEngine, ParadoxState

def test_paradox_conserved():
    engine = ParadoxEngine()
    state = ParadoxState(1.0, 0.7)
    new_state = engine.step(state)
    assert new_state.paradox_density == 0.7
