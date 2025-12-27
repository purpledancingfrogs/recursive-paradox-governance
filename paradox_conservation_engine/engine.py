from dataclasses import dataclass

@dataclass
class ParadoxState:
    density: float
    coherence: float
    entropy: float = 0.0

class ConservationViolation(Exception): pass

class ParadoxEngine:
    MIN_DENSITY = 1e-6

    def step(self, state: ParadoxState) -> ParadoxState:
        if state.density <= self.MIN_DENSITY:
            raise ConservationViolation("Paradox density collapsed")
        # evolve without annihilation
        return ParadoxState(
            density=state.density,
            coherence=min(1.0, state.coherence + 0.01),
            entropy=state.entropy + 0.01
        )
