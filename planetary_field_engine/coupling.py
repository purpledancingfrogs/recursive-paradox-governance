def couple(state, field_strength=1.0):
    state.coherence = min(1.0, state.coherence * field_strength)
    return state
