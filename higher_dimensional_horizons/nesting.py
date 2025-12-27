def nest(horizons, state):
    for h in horizons:
        state = h(state)
    return state
