import random, yaml
from datetime import datetime

class EvidenceV31:
    def __init__(self, idea:str, weights:dict):
        self.idea = idea
        self.weights = weights
        self.timestamp = datetime.utcnow().isoformat()
        self.metrics = {}
        self.rollback_flag = False

    def score(self):
        base = {
            "clarity_score": min(1.0, 0.3 + len(self.idea.split())/20),
            "coverage_score": random.uniform(0.5,0.9),
            "value_alignment": random.uniform(0.6,0.9),
            "cultural_acceptance": random.uniform(0.5,0.85),
            "social_cohesion": random.uniform(0.5,0.8),
            "carbon_footprint": random.uniform(0.1,0.5),
            "family_wellbeing": random.uniform(0.6,0.9),
            "historical_consistency": random.uniform(0.5,0.9),
            "accessibility_index": random.uniform(0.4,0.9),
            "legal_compliance": 1.0,
            "uncertainty_index": random.uniform(0.2,0.5)
        }
        self.metrics = {k: v*self.weights.get(k,1) for k,v in base.items()}
        stability = (self.metrics["clarity_score"]+self.metrics["coverage_score"])/2
        if stability < 0.7: self.rollback_flag = True

    def export_yaml(self, filename="evidence_v31.yaml"):
        record = {"idea": self.idea,"timestamp": self.timestamp,
                  "metrics": self.metrics,"rollback": self.rollback_flag}
        with open(filename,"w") as f: yaml.dump(record,f)
        return record

if __name__ == "__main__":
    weights = {"value_alignment":0.8,"culture":0.7,"society":0.9}
    ev = EvidenceV31("Les micro-réseaux solaires urbains sont une évidence.", weights)
    ev.score()
    print(ev.export_yaml())
