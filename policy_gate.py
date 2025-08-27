import json,urllib.request
def policy_allow(payload,opa_url="http://opa:8181/v1/data/ethicchain/allow"):
    req=urllib.request.Request(opa_url,data=json.dumps(payload).encode(),headers={"Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=3) as r: return json.loads(r.read()).get("result",False)
