def refract(state):
    # fragment without loss
    return state

def firewall(prev, curr):
    if curr.density < prev.density * 0.9:
        raise Exception("Illicit paradox leakage")
    return curr
