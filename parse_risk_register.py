# Parse le registre des risques et génère un rapport JSON
import csv, json
with open('RISK_REGISTER.csv','r',encoding='utf-8',errors='ignore') as f:
    reader = csv.DictReader(f)
    risks = [r for r in reader]
report = {
    'total_risks': len(risks),
    'high_risks': [r for r in risks if r.get('probability')=='high'],
}
print(json.dumps(report, indent=2, ensure_ascii=False))
