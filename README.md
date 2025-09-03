# Santé mentale des jeunes
**But** — Santé mentale des jeunes (module du pack X10).

## 🎯 Objectifs
- Impact concret et mesurable dans le domaine.
- Sécurité mineurs: contrôle parental (`policy.yaml`), langage adapté.
- ΔM11.3 pour rollback si dérive (métriques incluses).

## 🧪 Démo (stdlib)
- `demo_stdlib.py` : simulation simple, aucun accès externe.
- `metrics.json` : journal local (latence, stabilité, rollback).

## 🗣️ Injecteurs
- **Humain (prompt de départ)** : voir `injectors/injector_human.txt`.
- **IA↔IA (bloc ZGS)** : voir `injectors/injector_zgs.zgs`.

## ⚖️ Éthique & conformité
- RGPD: consentement, minimisation, droit d’effacement.
- AI Act: transparence, risques limités, documentation.
- ISO 42001 (en cours): management responsable.

## 🗂️ Fichiers
- `policy.yaml` — paramètres (horaires, sujets, filtres).
- `injectors/` — prompts lisibles + bloc .zgs.
- `demo_stdlib.py` — script de démonstration.
- `metrics.json` — sortie locale (debug).

---
Licence MIT — réutilisation encouragée (attribution).
