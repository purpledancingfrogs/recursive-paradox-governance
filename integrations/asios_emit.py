from integrations.asios_adapter import to_asios_mission

def emit_mission(state):
    return to_asios_mission(state)
