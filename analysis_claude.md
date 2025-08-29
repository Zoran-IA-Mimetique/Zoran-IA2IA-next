
# Analyse Claude — Protocole de test

## Objectif
Comparer la capacité de Claude (Anthropic) à résoudre des puzzles classiques face à GPT-4 et Zoran aSiM.

## Protocole
- **9 points / 4 traits** : prompt → "Relie 9 points en 4 segments sans lever le crayon".
- **Sudoku extrême** : grille de compétition, résolution demandée.
- **Labyrinthe 30x30** : texte ASCII, trouver chemin optimal.

## Observations attendues
- Claude améliore certains cas par rapport à GPT-4 mais reste faillible.
- Risque d'hallucination sur 9 points (souvent reste "dans le cadre").
- Latence plus faible mais cohérence instable.

## À compléter par tests réels.
