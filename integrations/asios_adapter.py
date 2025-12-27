def to_asios_mission(state):
    return {
        'type': 'PARADOX_GOVERNED',
        'paradox_density': state.density,
        'coherence': state.coherence
    }
