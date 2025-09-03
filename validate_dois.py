
#!/usr/bin/env python3
import sys, json, time, requests

with open('dois/index.json') as f:
    items = json.load(f)['items']

ok = True
for it in items:
    doi = it['doi']
    url = f"https://doi.org/{doi}"
    try:
        r = requests.head(url, allow_redirects=True, timeout=10)
        code = r.status_code
        if code >= 400:
            print(f"[FAIL] {doi} -> HTTP {code}")
            ok = False
        else:
            print(f"[OK]   {doi} -> {r.url}")
    except Exception as e:
        print(f"[ERR]  {doi} -> {e}")
        ok = False
    time.sleep(0.2)

sys.exit(0 if ok else 1)
