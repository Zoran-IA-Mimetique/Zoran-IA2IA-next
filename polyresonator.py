"""
PolyResonator - Orchestration Multi-Modèles
-------------------------------------------
Simule la résonance morphique entre modèles hétérogènes.
"""

import random

class PolyResonator:
    def __init__(self, models: list):
        self.models = models

    def resonate(self, prompt: str) -> str:
        """Chaque modèle vote, la résonance pondère les sorties."""
        responses = [m(prompt) for m in self.models]
        # simple majority resonance (demo)
        return max(set(responses), key=responses.count) if responses else ""

# Démos simples : 3 modèles jouets
if __name__ == "__main__":
    m1 = lambda p: "A" if "ethic" in p.lower() else "X"
    m2 = lambda p: "A" if random.random() > 0.3 else "Y"
    m3 = lambda p: "A" if "zoran" in p.lower() else "Z"
    pr = PolyResonator([m1, m2, m3])
    print(pr.resonate("Test ethic Zoran"))
