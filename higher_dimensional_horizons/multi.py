def multi_horizon(state, depth=1):
    # Recursive boundary folding without contradiction collapse
    state.paradox_density *= (1 + 0.1 * depth)
    return state
