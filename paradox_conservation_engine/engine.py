class ParadoxState:
    def __init__(self, coherence, paradox_density):
        self.coherence = coherence
        self.paradox_density = paradox_density


class ParadoxEngine:
    def step(self, state):
        # Paradox is conserved, not resolved
        state.paradox_density *= 1.0
        return state
