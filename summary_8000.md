# Zoran BTP Polymorphe — Description longue

**Ambition** — Faire de Zoran **la référence absolue** pour **tous les métiers du BTP**, du plus petit artisan à l’expert judiciaire, en passant par l’architecte, l’architecte d’intérieur, le bureau d’études et le conducteur de travaux.  
**Principe fondateur** — On ne construit pas avec du flou : **tant qu’une information n’est pas validée, elle est affichée en ROUGE** et n’entre pas en “état validé”. **Zéro hallucination** : tout ce qui n’est pas sourcé est marqué *NON VALIDÉ*.

---

## 1. Polymorphisme instantané par rôle
À partir d’un **même noyau**, Zoran se **reconfigure** selon le rôle :
- **Artisan** : devis détaillé, quantités × PU, méthodes, phasage, sécurité.
- **Architecte** : esquisse/APS/APD/PRO, insertion urbaine, RT/RE, dossier PC.
- **Archi d’intérieur/Déco** : programme, matériaux (FDES), éclairage, ergonomie.
- **BE Structure** : notes de calcul **Eurocodes**, flèches/service/ULS/SLS.
- **Expert judiciaire** : principe du contradictoire, constats, responsabilités.
- **Conducteur de travaux** : planning directeur, PAQ, PPSPS/SPS, jalons.

Chaque profil possède un **vocabulaire**, des **livrables** et des **preuves** attendues. Zoran n’invente pas : il **structure**, **drapeau‑rouge** ce qui manque, **bloque la validation** tant que les preuves ne sont pas attachées.

---

## 2. Politique de vérité & ΔM11.3 (rollback)
Zoran applique une règle simple et dure :
- **Claim ⇒ Evidence** : une affirmation n’existe pas sans **au moins une** preuve documentée.  
- **ΔM11.3** surveille les sorties : si un *claim* reste sans *evidence*, la sortie bascule en **ROLLBACK** (non‑diffusable comme “validée”).
- **Traçabilité** : timestamp UTC, contexte (site, climat, sol), normes visées (**Eurocodes, DTU, sécurité**), statut de validation.

---

## 3. Pipeline opérationnel (auditable)
1) **Contexte** (projet/site/codes) → 2) **Profil métier** (polymorphisme) →  
3) **Claims** (vérifications attendues) → 4) **Evidence** (pièces jointes/mesures/contrôles) →  
5) **ΔM11.3** (garde) → 6) **Rapport** (diffusable **uniquement** si claims couverts).

**Couleurs** :  
- **Rouge** = *NON VALIDÉ* (hypothèse, donnée manquante, source absente).  
- **Neutre** = information contextuelle.  
- **Vert** (optionnel, futur) = *VALIDÉ* (preuve contrôlée par un pair).

---

## 4. Exemples de “claims ↔ evidence”
- **Artisan**  
  - Claim : “Quantités matériaux réalistes.”  
    - Evidence : **Relevé de métrés signé** + **Devis fournisseurs**.  
- **Architecte**  
  - Claim : “Projet conforme PLU/SPR/ABF.”  
    - Evidence : **Note d’analyse PLU** + **Courriel ABF** (le cas échéant).  
- **BE Structure**  
  - Claim : “Poutre principale conforme EC3, flèche ≤ L/300.”  
    - Evidence : **Note de calcul EC3** + **Plan exé** + **Contrôle par pair**.  
- **Expert judiciaire**  
  - Claim : “Causalité des fissures établie.”  
    - Evidence : **Constats horodatés** + **Mesures** + **Scénarios alternatifs falsifiés**.  
- **Conducteur**  
  - Claim : “Planning exécutable.”  
    - Evidence : **Capacités ressources** + **Chemins critiques** + **Procédures réception**.

---

## 5. Sorties standardisées (lisibles & auditables)
Chaque rôle produit un **rapport structuré** : *Contexte*, *Livrables*, *Hypothèses/Points non validés (en ROUGE)*, *Claims*, *Evidence requise*, *Statut ΔM11.3*.  
Ces rapports sont **copiables** dans un DMS et diffusables **seulement** si le statut ΔM11.3 = OK.

---

## 6. Ce que Zoran **ne** fait pas ici (par design)
- **Pas de calculs structurels chiffrés** dans ce dépôt (stdlib only) : l’objectif est la **méthode** et la **rigueur**, pas une boîte noire.  
- **Pas de citation de clauses normatives** : Zoran exige la preuve, signale ce qui manque, mais **n’énonce pas** ici de textes juridiques (éviter la fausse précision).  
- **Pas d’approximations** : inconnue = ROUGE, hypothèse = ROUGE, source absente = ROUGE.

---

## 7. Avantages clés
- **Rigueur absolue** (mode “Xavier”) : on **bloque** tant que non prouvé.  
- **Polymorphisme** : un unique outillage pour tous les métiers.  
- **Transparence** : rouge visible, pas d’ambiguïté.  
- **Auditabilité** : ΔM11.3, claims↔evidence, horodatage, contexte.  
- **Interop** : sorties texte simples, intégrables dans n’importe quel SI.

---

## 8. Mode d’emploi rapide
```bash
# Artisan
python3 main.py --role artisan --project "Extension 35m²" --site "Nantes, FR" --codes DTU RE2020

# BE Structure
python3 main.py --role be-structure --project "Maison R+1 acier" --site "Lyon, FR" --codes eurocode

# Expert judiciaire
python3 main.py --role expert-judiciaire --project "Fissures pavillon 1978" --site "Tours, FR" --codes DTU
```
Par défaut, le **mode strict** est actif (ROUGE pour tout non validé). `--non-strict` neutralise l’affichage rouge (usage déconseillé).

---

## 9. Roadmap (évolutions sobres)
- **Vert “VALIDÉ”** après double contrôle pair.  
- **Journal d’audit** signé (hash/Merkle local).  
- **Connecteurs sources** (DMS, GED) pour lier les pièces probantes.  
- **Modules métiers** additionnels (CVC, CFO/CFA, photométrie).  
- **Exports** (PDF/JSON) et gabarits de rapports.

---

## 10. Licence & contact
Licence **MIT**. Contact : **tabary01@gmail.com**.  
Zoran BTP polymorphe vise la **crème de la crème** : *perfection projetée*, sans hallucination, avec preuves — ou rien.
