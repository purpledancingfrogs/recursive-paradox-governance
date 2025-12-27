def couple(state, field_strength=1.0):
    # Planetary-scale modulation of coherence without collapsing paradox
    state.coherence = min(1.0, state.coherence * field_strength)
    return state
