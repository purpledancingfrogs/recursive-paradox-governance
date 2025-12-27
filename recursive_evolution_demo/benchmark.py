import time
from paradox_conservation_engine.engine import ParadoxEngine, ParadoxState

engine = ParadoxEngine()
s = ParadoxState(1.0, 0.5)
t0 = time.time()
for _ in range(1000):
    s = engine.step(s)
print('steps:', 1000, 'elapsed:', time.time() - t0)
