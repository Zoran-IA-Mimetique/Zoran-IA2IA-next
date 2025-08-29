#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Demo d'analyse socio-thique (stdlib only)
Entrée: liste de signes (hashtags, slogans)
Sortie: JSON des rattachements à des familles de valeurs
'''
import argparse, json, sys

FAMILIES = {
    "justice": ["justice", "égalité", "droit", "pouvoir d'achat"],
    "rupture": ["bloquons tout", "démission", "grève générale", "boycott"],
    "cohesion": ["union", "ensemble", "paix", "médiation"],
    "dignite": ["respect", "dignité", "conditions de vie"],
    "autonomie": ["autonomie", "décentralisation", "VIe République"],
    "soin": ["santé", "éducation", "service public", "care"],
}

def classify(sign: str):
    s = sign.lower()
    hits = []
    for fam, terms in FAMILIES.items():
        for t in terms:
            if t in s:
                hits.append(fam)
                break
    return hits or ["indéterminé"]

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--signs", nargs="*", default=[],
                   help="Liste de signes (hashtags, slogans)")
    args = p.parse_args(argv)

    signs = args.signs or ["#Mobilisation10Septembre", "Bloquons tout", "Justice sociale"]
    result = {s: classify(s) for s in signs}
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
