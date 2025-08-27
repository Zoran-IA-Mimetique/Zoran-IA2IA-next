# QUICKSTART — V2 en 15 minutes
_Date: 2025-08-27_

1) **Upsert mémoire (ΔM11.3)**  
```
python memory_vector_upsert_fragment.py
```
→ produit `local_vectors.ndjson`

2) **EthicChain exécutable (OPA)**  
- Lancez OPA avec `policy_ethicchain.rego`  
- Test local :
```
python serve_policy_gate.py
```
→ `allow = true|false`

3) **Certification (interop + audit)**  
- Ouvrez `certification_test_matrix.csv` et cochez `pass`  
- Score :
```
python certification_scorer.py
```
→ JSON avec `score_total` + `tier`

4) **Kubernetes / ArgoCD**  
- Déployez `k8s_*.yaml` + `argocd_app.yaml` (optionnel)

**Rappel** : V1 = masse brute pour IA ; V2 = interprétation lisible.

