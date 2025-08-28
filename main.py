#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zoran BTP Polymorph Reference — stdlib-only CLI
- Strict "no hallucination" policy: unknowns are red-flagged.
- Roles: artisan, architecte, interieur, be-structure, expert-judiciaire, conducteur
"""
import argparse
import sys
from datetime import datetime

ANSI_RED = "\033[31m"
ANSI_BOLD = "\033[1m"
ANSI_RESET = "\033[0m"

def red(txt): return f"{ANSI_RED}{txt}{ANSI_RESET}"
def bold(txt): return f"{ANSI_BOLD}{txt}{ANSI_RESET}"

def header(title):
    return f"{bold('═'*60)}\n{bold(title)}\n{bold('═'*60)}"

def guard_dm113_checks(sections):
    """
    Simple ΔM11.3-like guard: verify that each 'Claim' has at least one 'Evidence'
    sections: dict of {'claims': [..], 'evidence': [..]}
    """
    claims = sections.get("claims", [])
    evidence = sections.get("evidence", [])
    ok = True
    missing = []
    for c in claims:
        # naive rule: a piece of evidence must mention at least one keyword of claim
        kwords = [w for w in c.replace(':', ' ').split() if len(w) > 3]
        matched = any(any(kw.lower() in e.lower() for kw in kwords) for e in evidence)
        if not matched:
            ok = False
            missing.append(c)
    return ok, missing

def red_if_unknown(value, label=None):
    if value is None or (isinstance(value, str) and (value.strip()=="" or value.strip()=="??")):
        msg = f"{label or 'Valeur'}: ??"
        return red(f"[NON VALIDÉ] {msg}")
    return value

def print_section(title, lines):
    print(f"\n{bold(title)}")
    for ln in lines:
        print(f" - {ln}")

def base_context(args):
    return {
        "Projet": red_if_unknown(args.project, "Projet"),
        "Site": red_if_unknown(args.site, "Site"),
        "Codes": ", ".join(args.codes) if args.codes else red("[NON VALIDÉ] Normes/codes non fournis"),
        "Date": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    }

def role_artisan(ctx):
    claims = [
        "Quantités matériaux estimées sont réalistes",
        "Prix unitaires compatibles marchés locaux",
        "Planning exécutable sans conflit de ressources"
    ]
    evidence = [
        red_if_unknown(None, "Relevé métrés signé"),
        red_if_unknown(None, "Devis fournisseurs"),
        red_if_unknown(None, "Planning validé MO/MOE")
    ]
    print(header("ARTISAN — Devis & Méthodes"))
    print_section("Contexte", [f"{k}: {v}" for k,v in ctx.items()])
    print_section("Livrables", [
        "Devis détaillé (quantités × prix unitaires)",
        "Méthodes et phasage (préparation, exécution, contrôle)",
        "Plan hygiène & sécurité (PPSPS si applicable)"
    ])
    print_section("Hypothèses", [
        red_if_unknown(None, "Hauteur sous plafond"),
        red_if_unknown(None, "Classe d’exposition béton"),
        red_if_unknown(None, "Accès chantier / emprise")
    ])
    print_section("Claims (à prouver)", claims)
    print_section("Evidence requise", evidence)
    ok, missing = guard_dm113_checks({"claims": claims, "evidence": evidence})
    print(f"\nΔM11.3: {'OK' if ok else red('ROLLBACK: Claims sans preuve → compléter avant validation')}")
    if missing:
        print_section("Claims sans preuve", [red(m) for m in missing])

def role_architecte(ctx):
    print(header("ARCHITECTE — Conception & Conformité"))
    print_section("Contexte", [f"{k}: {v}" for k,v in ctx.items()])
    print_section("Livrables", [
        "Esquisse / APS / APD / PRO",
        "Insertion site & gabarits, accessibilité, RT/RE",
        "Dossier PC (autorisation d’urbanisme) — si applicable"
    ])
    print_section("Points non validés", [
        red_if_unknown(None, "PLU/SPR/ABF (contraintes patrimoniales)"),
        red_if_unknown(None, "Étude thermique préliminaire"),
        red_if_unknown(None, "Étude sol G2 AVP")
    ])

def role_interieur(ctx):
    print(header("ARCHI INT./DÉCO — Programme & Matériaux"))
    print_section("Contexte", [f"{k}: {v}" for k,v in ctx.items()])
    print_section("Livrables", [
        "Programme détaillé (usages, flux, ergonomie)",
        "Palette matériaux & FDES/Fiches sanitaires",
        "Plans mobilier/éclairage, moodboards"
    ])
    print_section("Points non validés", [
        red_if_unknown(None, "Classement feu revêtements"),
        red_if_unknown(None, "COV & émissions intérieures"),
        red_if_unknown(None, "Coordination élec/éclairage")
    ])

def role_be_structure(ctx):
    claims = [
        "Dimensionnement poutre principale conforme EC3",
        "Flèche service ≤ L/300",
        "Taux utilisation ≤ 100 % en ULS"
    ]
    evidence = [
        red_if_unknown(None, "Note de calcul EC3 avec hypothèses"),
        red_if_unknown(None, "Plans d’exécution signés"),
        red_if_unknown(None, "Contrôle croisé par pair")
    ]
    print(header("BE STRUCTURE — Eurocodes"))
    print_section("Contexte", [f"{k}: {v}" for k,v in ctx.items()])
    print_section("Vérifications clés", claims)
    print_section("Evidence requise", evidence)
    ok, missing = guard_dm113_checks({"claims": claims, "evidence": evidence})
    print(f"\nΔM11.3: {'OK' if ok else red('ROLLBACK: compléter les preuves avant diffusion')}")
    if missing:
        print_section("Claims sans preuve", [red(m) for m in missing])

def role_expert_judiciaire(ctx):
    print(header("EXPERT JUDICIAIRE — Contradictoire & Traçabilité"))
    print_section("Contexte", [f"{k}: {v}" for k,v in ctx.items()])
    print_section("Cadre", [
        "Principe du contradictoire",
        "Chronologie des faits",
        "Constats, mesures, photos géolocalisées horodatées"
    ])
    print_section("Points non validés", [
        red_if_unknown(None, "Causalité fissures (retrait, fondations, eau)"),
        red_if_unknown(None, "Responsabilités contractuelles"),
        red_if_unknown(None, "Mise en sécurité immédiate")
    ])

def role_conducteur(ctx):
    print(header("CONDUCTEUR DE TRAVAUX — Phasage & Sécurité"))
    print_section("Contexte", [f"{k}: {v}" for k,v in ctx.items()])
    print_section("Livrables", [
        "Planning directeur & jalons d’acceptation",
        "Plan de contrôle qualité (auto-contrôles, fiches points d’arrêt)",
        "PPSPS / coordination SPS"
    ])
    print_section("Points non validés", [
        red_if_unknown(None, "Capacité grues/accès"),
        red_if_unknown(None, "Approvisionnement & stockage"),
        red_if_unknown(None, "Procédures réception/levée réserves")
    ])

ROLES = {
    "artisan": role_artisan,
    "architecte": role_architecte,
    "interieur": role_interieur,
    "be-structure": role_be_structure,
    "expert-judiciaire": role_expert_judiciaire,
    "conducteur": role_conducteur,
}

def main(argv=None):
    p = argparse.ArgumentParser(description="Zoran BTP Polymorph — Rigueur absolue, incertitudes en rouge.")
    p.add_argument("--role", required=True, choices=sorted(ROLES.keys()), help="Métier/role")
    p.add_argument("--project", help="Nom du projet (ex: Maison R+1)")
    p.add_argument("--site", help="Localisation/pays (impact normes, climat)")
    p.add_argument("--codes", nargs="*", default=[], help="Liste de normes/codes (ex: eurocode DTU RE2020)")
    p.add_argument("--non-strict", action="store_true", help="Désactiver les drapeaux rouges (déconseillé)")
    args = p.parse_args(argv)

    ctx = base_context(args)
    if args.non_strict:
        global ANSI_RED
        ANSI_RED = ""  # neutralise la couleur si non strict
    fn = ROLES[args.role]
    fn(ctx)

if __name__ == "__main__":
    main()
