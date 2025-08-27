# README — Intégrations Avancées V2 (Guide 15 minutes)
_Date: 2025-08-27_

Ce guide relie, en un seul document, toutes les briques **V2** livrées dans `IA2IA_AdvancedIntegration_FLAT.zip` :
- **ΔM11.3 × Vector Stores** (Milvus/Pinecone) — *mémoire requêtable & prouvable*
- **OPA/EthicChain** — *politiques éthiques exécutables*
- **Kubernetes/ArgoCD** — *industrialisation de `serve`*
- **Certification Tiers** — *score interop + auditabilité opposable*
- **Human Reading Paradox** — *la preuve qu’un audit humain exhaustif est irréaliste*

---

## 0) Pré-requis (démo locale stdlib)
- Python 3.11+ (stdlib seulement)
- Fichiers présents à la **racine** de V2 (copie du zip à plat)
- Accès facultatif à un cluster K8s + ArgoCD pour la partie déploiement

---

## 1) ΔM11.3 × Vector Stores (démo locale)
1. Lisez `memory_vector_README.md` (conception).  
2. Exécutez :
```
python memory_vector_upsert_fragment.py
```
3. Résultat : création (ou append) de `local_vectors.ndjson` avec `{id, vec, meta}`.  
4. Schéma de fragment : `memory_vector_fragment.schema.json`.  
5. Configs (remplaçables si vous branchez un vrai store) :  
   - `memory_vector_milvus.config.yaml`  
   - `memory_vector_pinecone.config.yaml`

**But** : démontrer que ΔM11.3 peut être **indexée, requêtée, purgée** (TTL/redaction), et **tracée** (hash, timestamp).

---

## 2) OPA x EthicChain (politiques exécutables)
1. Lisez `policy_OPA_README.md`.  
2. Lancez OPA avec la politique `policy_ethicchain.rego` (en local ou via le manifeste K8s dédié).  
3. Testez le client stdlib :
```
python serve_policy_gate.py
```
4. Entrée d’exemple : `policy_example_input.json`  
5. Sortie attendue : `allow = true|false`

**But** : faire du texte éthique un **garde-fou exécutable** (gate IA↔IA en temps réel).

---

## 3) Kubernetes / ArgoCD (industrialisation)
**Manifeste K8s** :  
- `k8s_deployment.yaml` (serve)  
- `k8s_service.yaml` (service)  
- `k8s_opa.yaml` (OPA)  

**ArgoCD** :  
- `argocd_app.yaml` → sync auto (`prune`, `selfHeal`, `CreateNamespace`)  
- Pointez `repoURL` vers votre V2 public.  
- Pushez, Argo synchronise.

**But** : un **serve** minimal, **déclaratif**, observable (probes), prêt à scaler.

---

## 4) Certification Tiers (interop + auditabilité)
1. Lisez `certification_interop_audit_spec.md` (axes et procédure).  
2. Ouvrez `certification_test_matrix.csv` et **cochez** la colonne `pass` pour chaque test réussi.  
3. Calculez le score :
```
python certification_scorer.py
```
4. Sortie : JSON `{ score_total, tier, axes_score, hits, max }`  
   - **Tiers** : `silver ≥ 0.65`, `gold ≥ 0.80`, `platinum ≥ 0.90`.

**But** : produire un **score opposable et réplicable** par un auditeur tiers.

---

## 5) Human Reading Paradox
Lisez `HUMAN_READING_PARADOX.md`. Fait essentiel :  
- **+155 dépôts** : https://github.com/Zoran-IA-Mimetique?tab=repositories  
- Lecture humaine exhaustive = **irréaliste**.  
- Solution honnête : **IA = parser/auditeur radical**, Humain = **contrôle externe**.

---

## 6) Fil d’Ariane (V1 ↔ V2)
- **V1** = masse brute, injecteur pour IA (illisible humainement, par design)  
- **V2** = interprétation structurée (pont IA ↔ humain)  
- Le duo V1+V2 = **double-couche de transparence** : *preuve brute + preuve lisible*

---

## 7) Foire aux questions (FAQ express)
- *Pourquoi “code minimal” ?* → pour **maximiser la lisibilité et l’auditabilité**.  
- *Peut-on brancher un “vrai” vector store ?* → oui, utilisez les configs incluses.  
- *Qui attribue le “tier” de certification ?* → le **script calcule**, un tiers **publie le rapport**.  
- *OPA est-il obligatoire ?* → non, mais recommandé pour **EthicChain exécutable**.

---

## 8) Prochaines étapes
- Publier les premiers **rapports de certification** (JSON + PDF) dans `/certification/reports/`.  
- Brancher un **vecteur store managé** (Milvus/Pinecone/pgvector) et publier les **benchmarks**.  
- Étendre la politique OPA avec de nouvelles règles (biais, logging, licences).  
- Ajouter un **/healthz** & **/metrics** standards à `serve` pour l’observabilité.

---

**Contact** : tabary01@gmail.com — Licence MIT — © Zoran IA Mimétique

