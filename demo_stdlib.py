# stdlib only demo — no external calls
import json, time, random
metrics = {"stability": round(0.8 + random.random()*0.15, 3),
           "latency_ms": random.randint(50, 200),
           "rollback_triggered": random.choice([False, False, False, True])}
time.sleep(0.1)
print("ΔM11.3 metrics:", json.dumps(metrics))
open("metrics.json","w").write(json.dumps(metrics, indent=2))
