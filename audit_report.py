# Script d'audit simple
import json, sys
from collections import Counter

def audit_text(text):
    words = text.split()
    report = {
        "mots": len(words),
        "caracteres": len(text),
        "taux_repetition": sum(v>1 for v in Counter(words).values())/len(words)
    }
    return report

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audit_report.py <file.txt>")
        sys.exit(1)
    fname = sys.argv[1]
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    report = audit_text(content)
    print(json.dumps(report, indent=2, ensure_ascii=False))
