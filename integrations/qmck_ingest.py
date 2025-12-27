import json
from integrations.qmck_adapter import from_qmck_report

def ingest_report(path):
    with open(path) as f:
        report = json.load(f)
    return from_qmck_report(report)
