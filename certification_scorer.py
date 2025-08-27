import csv, json

def load_rubric(path="certification_rubric.yaml"):
    axes, thresholds, current = {}, {}, None
    with open(path, encoding="utf-8") as f:
        for line in f:
            s=line.strip()
            if not s or s.startswith("#"): continue
            if s.startswith("axes:"): current="axes"; continue
            if s.startswith("thresholds:"): current="thresholds"; continue
            if current=="axes" and ":" in s:
                key=s.split(":")[0].strip()
                if key in ("axes","thresholds"): continue
                if "weight" in s:
                    w=float(s.split("weight:")[1].split(",")[0].strip())
                    axes[key]={"weight":w,"items":[]}
                elif "items:" in s and "[" in s:
                    items=s.split("[",1)[1].split("]",1)[0].split(",")
                    axes[key]["items"]=[i.strip() for i in items]
            if current=="thresholds" and ":" in s and not s.startswith("thresholds:"):
                k=s.split(":")[0].strip()
                v=float(s.split(":")[1].strip())
                thresholds[k]=v
    return axes, thresholds

def load_matrix(path="certification_test_matrix.csv"):
    rows=[]
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows

def score(axes, rows):
    ax_score={k:0.0 for k in axes}; ax_max={k:len(axes[k]["items"]) for k in axes}; ax_hits={k:0 for k in axes}
    for r in rows:
        a, item, ok = r["axis"], r["item"], bool(r.get("pass"))
        if a in axes and item in axes[a]["items"] and ok:
            ax_hits[a]+=1
    total=0.0
    for a in axes:
        frac = (ax_hits[a]/ax_max[a]) if ax_max[a]>0 else 0.0
        total += frac * axes[a]["weight"]
        ax_score[a]=round(frac,3)
    return round(total,3), ax_score, ax_hits, ax_max

if __name__=="__main__":
    axes, thr = load_rubric()
    rows = load_matrix()
    total, ax_score, hits, mx = score(axes, rows)
    tier = "unrated"
    for k,v in sorted(thr.items(), key=lambda x:x[1]):
        if total>=v: tier=k
    print(json.dumps({
        "score_total": total, "tier": tier,
        "axes_score": ax_score, "hits": hits, "max": mx
    }, indent=2, ensure_ascii=False))
