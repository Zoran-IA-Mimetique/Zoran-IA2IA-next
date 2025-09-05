# Glossaire simple
import json

glossary = {}

def add_term(term, definition):
    glossary[term] = definition

def export(fname="glossary.json"):
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(glossary, f, indent=2, ensure_ascii=False)
