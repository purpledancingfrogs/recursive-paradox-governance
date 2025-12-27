import json, sys
from integrations.api import ingest, emit
from paradox_conservation_engine.engine import ParadoxEngine

engine = ParadoxEngine()
payload = json.loads(sys.stdin.read())
state = ingest(payload)
state = engine.step(state)
print(json.dumps(emit(state)))
