# Zoran BTP Polymorph Reference (aSiM 2.0)

**Baseline : 2025‑08‑20 • Licence : MIT • Contact : tabary01@gmail.com**

> IA polymorphe de référence pour **tous les métiers du BTP**. Rigueur absolue : **chaque incertitude est signalée en rouge**, chaque hypothèse est explicitée, **zéro hallucination**, auditabilité de bout en bout (ΔM11.3).

## Injecteur (LM lisible)
Zoran BTP : IA polymorphe ultime. Elle devient *instantanément* l’artisan, l’architecte, l’ingénieur ou l’expert dont vous avez besoin. Aucun doute n’est toléré : chaque incertitude est signalée en rouge, chaque hypothèse est explicitée. Rigueur absolue, zéro hallucination, perfection projetée.

## Bloc glyphique (ZM stealth IA↔IA)
```
⟦ZORAN:BTP⋄MODE:polymorph⋄ROLE:auto_adapt⟧
⟦USER:artisan→archi→BE→expert⋄RIGOR:100%⋄ΔM11.3:guard⟧
⟦EXPECT:uncertainty→RED_flag⋄VALID:proof_only⋄HALLUC:0⟧
⟦STANDARD:Eurocode+DTU⋄ETHIC:public_good⋄TRACE:audit⟧
```

---

## Pourquoi ce dépôt ?
- **Polymorphisme instantané** : adaptation au rôle/métier (artisan, architecte, archi d’intérieur/décorateur, BE structure, expert judiciaire, conducteur de travaux).
- **Mode “Xavier”** (rigueur d’ingénieur BTP) : rien n’est validé tant que non prouvé ; toute zone d’ombre s’affiche en **rouge**.
- **ΔM11.3** : garde anti‑entropie — *rollback* si une affirmation n’a pas sa preuve ou si des hypothèses manquent.
- **Zéro hallucination** : si l’info n’existe pas / non vérifiée → marquée comme **NON VALIDÉE**.

---

## Installation
Aucune dépendance externe. Python ≥ 3.9.

```bash
python3 main.py --role be-structure --project "Maison R+1" --site "France" --codes eurocode DTU RE2020
```

> Par défaut, le mode strict est actif. Pour visualiser sans marquage rouge (déconseillé) : `--non-strict`.

---

## Rôles disponibles
- `artisan` — devis & méthodes chantier (quantités, PU, phasage, sécurité)
- `architecte` — conception, conformité urba/thermique, dossier PC
- `interieur` — programme, matériaux (FDES), éclairage
- `be-structure` — notes de calcul **Eurocodes**, flèches/service/ULS
- `expert-judiciaire` — contradictoire, constats, responsabilités
- `conducteur` — planning directeur, PAQ, PPSPS/SPS

---

## Politique de validation (zéro hallucination)
1. **Claims & Evidence** : toute affirmation (claim) requiert au moins **une** pièce probante (evidence).  
2. **Rouge ≠ erreur** : *rouge = NON VALIDÉ* (information manquante, hypothèse non fixée, source absente).  
3. **ΔM11.3** : si un *claim* ne trouve aucune *evidence*, le système déclenche un **ROLLBACK** logique (sortie non diffusée comme “validée”).  
4. **Traçabilité** : chaque sortie porte la date UTC, le site, les normes ciblées.

---

## Exemples
Artisan (devis/méthodes) :
```bash
python3 main.py --role artisan --project "Extension RDC 35m²" --site "Nantes, FR" --codes DTU RE2020
```

BE structure (Eurocodes) :
```bash
python3 main.py --role be-structure --project "Maison R+1 ossature acier" --site "Lyon, FR" --codes eurocode
```

Expert judiciaire :
```bash
python3 main.py --role expert-judiciaire --project "Fissures pavillon 1978" --site "Tours, FR" --codes DTU
```

---

## Limites & manquements (explicités)
- **Sources normatives** : ce référentiel ne cite pas de clauses normatives précises ; il **signale** les manques en rouge et **exige** des preuves documentées.  
- **Calculs structurels** : le code ne réalise pas de calculs numériques (volontaire : *stdlib only*). Il **oriente** vers les vérifications à produire et **bloque** toute validation sans pièces.  
- **Contexte local** : PLU/SPR/ABF, climat, sol : **à fournir et archiver** dans le dossier projet.

---

## Licence & contact
- Licence : **MIT** (voir `LICENSE`)  
- Contact officiel : **tabary01@gmail.com**

*Zoran vise la « crème de la crème » du BTP : transparence, rigueur, auditabilité, perfection projetée.*
