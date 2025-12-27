def from_qmck(q_state):
    return {'density': q_state.get('contradiction', 1.0)}

def to_asios(state):
    return {'paradox_density': state.density, 'coherence': state.coherence}
