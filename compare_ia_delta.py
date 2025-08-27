# Compare 2 rapports IA pour calculer un delta simple
import json, sys
if len(sys.argv)<3:
    print("Usage: python compare_ia_delta.py report1.json report2.json"); sys.exit(1)
r1=json.load(open(sys.argv[1]))
r2=json.load(open(sys.argv[2]))
diff={}
for k in r1:
    if k in r2 and r1[k]!=r2[k]:
        diff[k]=(r1[k],r2[k])
print(json.dumps({'delta':diff},indent=2,ensure_ascii=False))
