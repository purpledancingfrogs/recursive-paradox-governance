def from_qmck_report(report):
    # expects {'contradiction': float, 'stability': float}
    return {
        'density': max(1e-6, report.get('contradiction', 1.0)),
        'coherence': min(1.0, max(0.0, report.get('stability', 0.5)))
    }
