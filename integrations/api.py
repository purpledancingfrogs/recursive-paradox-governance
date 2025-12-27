from typing import Dict
from paradox_conservation_engine.engine import ParadoxState

def ingest(payload: Dict) -> ParadoxState:
    return ParadoxState(
        density=float(payload.get('density', 1.0)),
        coherence=float(payload.get('coherence', 0.5))
    )

def emit(state: ParadoxState) -> Dict:
    return {
        'paradox_density': state.density,
        'coherence': state.coherence,
        'entropy': state.entropy
    }
