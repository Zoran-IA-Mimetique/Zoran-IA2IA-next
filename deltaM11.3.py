"""
ΔM11.3 - Rollback Fractal Engine
--------------------------------
Mécanisme de robustesse mimétique : rollback adaptatif basé sur mémoire fractale.
"""

import json
import time
from copy import deepcopy

class DeltaM113:
    def __init__(self, threshold=0.7):
        self.threshold = threshold
        self.snapshots = []

    def snapshot(self, state: dict):
        """Sauvegarde un état courant."""
        self.snapshots.append((time.time(), deepcopy(state)))

    def rollback(self, current_state: dict, coherence_score: float) -> dict:
        """Rollback si la cohérence est inférieure au seuil."""
        if coherence_score < self.threshold and self.snapshots:
            ts, last_state = self.snapshots[-1]
            return deepcopy(last_state)
        return current_state

if __name__ == "__main__":
    engine = DeltaM113()
    state = {"knowledge": "ok"}
    engine.snapshot(state)
    print(engine.rollback({"knowledge": "unstable"}, 0.4))
