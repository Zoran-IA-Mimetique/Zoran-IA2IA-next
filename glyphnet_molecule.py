import time
import logging

logging.basicConfig(filename="glyphnet.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

GLYPH_DICT = {
    "H": "𐤇", "C": "𐤂", "O": "𐤏", "N": "𐤍",
    "=": "⋄", "#": "⧖", "c1ccccc1": "⦿"
}
REVERSE_DICT = {v: k for k, v in GLYPH_DICT.items()}

def smiles_to_glyphnet(smiles: str, level:int=1) -> str:
    res = smiles
    for k, v in GLYPH_DICT.items():
        res = res.replace(k, v)
    if level > 1:
        res = res.replace("𐤂𐤂", "¤")
    return res

def glyphnet_to_smiles(glyphs: str) -> str:
    res = glyphs
    for v, k in REVERSE_DICT.items():
        res = res.replace(v, k)
    res = res.replace("¤", "CC")
    return res

def benchmark(smiles: str, level:int=1):
    t0 = time.time(); g = smiles_to_glyphnet(smiles, level); t1 = time.time()
    t2 = time.time(); r = glyphnet_to_smiles(g); t3 = time.time()
    comp = 100 * (1 - len(g)/len(smiles)); ok = (smiles == r)
    logging.info(f"SMILES={smiles} Glyphs={g} Comp={comp:.1f}% Enc={(t1-t0)*1000:.2f}ms Dec={(t3-t2)*1000:.2f}ms RT={ok}")
    return {"smiles":smiles,"glyphs":g,"compression_%":comp,"encode_ms":(t1-t0)*1000,"decode_ms":(t3-t2)*1000,"roundtrip_ok":ok}

if __name__ == "__main__":
    for s in ["O", "c1ccccc1", "CCO"]:
        print(benchmark(s, level=2))
