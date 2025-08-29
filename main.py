#!/usr/bin/env python3
import json, sys, time, hashlib, random, statistics, pathlib

STATE = {"version": "1.0.0", "runs": 0, "zdm": {"base": {}, "cache": {}}, "rollbacks": 0}
METRICS = {"reward": [], "coherence": [], "stability": []}

def simulate_step(seed=None):
    r = random.Random(seed)
    reward = r.uniform(0.4, 0.9)
    coherence = r.uniform(0.5, 0.95)
    stability = r.uniform(0.5, 0.95)
    return reward, coherence, stability

def guard_delta_m_11_3(stability, threshold=0.6):
    return stability >= threshold

def run_pipeline(steps=10):
    global STATE, METRICS
    for i in range(steps):
        reward, coherence, stability = simulate_step(seed=STATE["runs"]*steps + i)
        if not guard_delta_m_11_3(stability):
            STATE["rollbacks"] += 1
            # simple rollback: ignore this step
            continue
        METRICS["reward"].append(reward)
        METRICS["coherence"].append(coherence)
        METRICS["stability"].append(stability)
        STATE["runs"] += 1

def report():
    global STATE, METRICS
    rep = {
        "reward_avg": statistics.fmean(METRICS["reward"]) if METRICS["reward"] else 0.0,
        "coherence_avg": statistics.fmean(METRICS["coherence"]) if METRICS["coherence"] else 0.0,
        "stability_avg": statistics.fmean(METRICS["stability"]) if METRICS["stability"] else 0.0,
        "rollbacks": STATE["rollbacks"],
        "runs": STATE["runs"],
    }
    with open("metrics.json","w",encoding="utf-8") as f:
        json.dump(rep, f, indent=2)
    with open("state.json","w",encoding="utf-8") as f:
        json.dump(STATE, f, indent=2)
    print(json.dumps(rep, indent=2))

def main():
    if len(sys.argv) < 2:
        print("Usage: main.py [run|report]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "run":
        run_pipeline(steps=24)
        print("OK: pipeline executed.")
    elif cmd == "report":
        report()
    else:
        print("Unknown command.")
        sys.exit(2)

if __name__ == "__main__":
    main()
