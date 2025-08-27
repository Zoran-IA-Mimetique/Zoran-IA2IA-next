# Zoran-IA2IA-Review-Chain v2

**Licence**: MIT • **Contact**: tabary01@gmail.com • **Date**: 2025-08-27T21:36:12Z

## TL;DR
Zoran-IA2IA-Review-Chain v2 — dépôt opérationnel pour la revue mimétique distribuée : hub FastAPI-ready, EthicChain (garde éthique) minimal, glyphes JSON (schemas + samples), 100 scénarios YAML, OpenAPI, docker-compose, tests & métriques (latence P95, % acceptation, coûts).

## Objectif
Rendre **concret, mesurable et auditable** le processus de revue mimétique distribuée (IA↔IA), via un **hub API minimal**, un **garde éthique** (EthicChain), des **glyphes JSON standardisés** et **100 scénarios** de tests.

## Architecture
```
[Agents IA] ⇄ [Hub FastAPI] ⇄ [EthicChain Guard] ⇄ [Logs/Append-only]
           ⇅
        [Glyphs JSON ↔ Validator]     [Scénarios YAML]
```
- **hub/** : API (health, /glyphs/validate, /messages).
- **ethicchain/** : filtrage heuristique + veto.
- **glyphs/** : schémas + exemples (100).
- **scenarios/** : 100 scénarios (id, seed, KPI).
- **openapi/** : spécification 3.0 minimaliste.
- **tests/** : validation de schémas.
- **tools/** : utilitaires (Z5, validator CLI).

## Sécurité & Conformité
- *Security & Privacy by design* : filtrage, journalisation, redaction, TTL.
- *ΔM11.3* : rollback conceptuel si instabilité détectée (à implémenter).

## Déploiement local
```bash
docker compose up --build
```
Services : `hub` (FastAPI), `ethicchain` (guard).
OpenAPI (minimal) : voir `openapi/openapi.yaml` (exposé par hub).

## KPIs à instrumenter
- Latence P95 < 100 ms ; ≥ 1000 req/s.
- ≥ 75 % de suggestions acceptées ; TTR -30 %.
- < 5 % sur-blocage ; détection < 60 s.

## Roadmap
1. Renforcer EthicChain (Bandit/Semgrep + modèles de modération).
2. Versionner les glyphes et validation stricte.
3. Statelessorcher le hub (LB + cache).
4. Export métriques (Prometheus) + dashboard Grafana.
5. Audit externe + SSRN/DOI.

---

### ZM (bloc glyphique)
Voir `./.zgs/fragments.zgs`.
