import os, json, hashlib, datetime
def embed(text): return [hash(text)%997/997.0]*1536
def normalize(t): return " ".join(t.split())
def iso_now(): return datetime.datetime.utcnow().isoformat()+"Z"
def sh256(s): return hashlib.sha256(s.encode()).hexdigest()
def build_fragment(text,layer="long",entropy=0.12,ttl_hours=168,zgs=""):
    text=normalize(text); frag_id=sh256(text)[:16]
    ttl=(datetime.datetime.utcnow()+datetime.timedelta(hours=ttl_hours)).isoformat()+"Z"
    return {"id":frag_id,"text":text,"layer":layer,"entropy":entropy,"ttl":ttl,"zgs":zgs,"hash":sh256(text),"timestamp":iso_now()}
def upsert_local(fragment):
    vec=embed(fragment["text"])
    with open("local_vectors.ndjson","a",encoding="utf-8") as f:
        f.write(json.dumps({"id":fragment["id"],"vec":vec,"meta":fragment})+"\n")
if __name__=="__main__":
    frag=build_fragment("Exemple fragment ΔM11.3 long terme."); upsert_local(frag); print("✓ upsert",frag["id"])
