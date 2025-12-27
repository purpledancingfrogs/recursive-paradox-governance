def Pi(state): return state.density
def Xi(state): return state.coherence
def Omega(prev, curr): return max(0.0, curr.entropy - prev.entropy)
def DeltaPi(prev, curr): return curr.density - prev.density
