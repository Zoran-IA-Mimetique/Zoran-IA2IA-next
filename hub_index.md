# Hub Index — Zoran‑IA2IA‑next

## 1) Injecteurs IA↔IA
- `demo.py` — démo stdlib‑only (flux stdin/stdout, validation minimale).
- `zoran_ia2ia_next.zgs` — bloc glyphique pour IA‑to‑IA.

## 2) Mémoire ZDM (Dual‑Memory)
- `main.py run` → simule base persistante + cache résonant.
- `state.json` / `metrics.json` générés via `main.py report`.

## 3) Orchestrateur (PolyResonator)
- UCB1 mock, quorum self‑patch, mixer EMA‑like (placeholders).

## 4) Conformité (EthicChain)
- `EthicChain.md` — principes, checklist, RGPD/AI Act.

## 5) Résumés & Métadonnées
- `summary_150.txt`, `summary_350.txt`, `summary_8000.md`, `project.yaml`.

## 6) Liens (à compléter)
- Gamma, Zenodo (DOI), Medium/Substack.

## 7) Commandes
```
python demo.py
python main.py run
python main.py report
```
