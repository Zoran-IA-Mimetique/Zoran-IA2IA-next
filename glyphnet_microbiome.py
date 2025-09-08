import time, logging
logging.basicConfig(filename="glyphnet_microbiome.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

GLYPH_DICT = {"Bacteroides":"𐤁","Firmicutes":"𐤅","Actinobacteria":"𐤀","Proteobacteria":"𐤐",";":"⋄"}
REVERSE_DICT = {v:k for k,v in GLYPH_DICT.items()}

def taxa_to_glyphnet(t): 
    r=t
    for k,v in GLYPH_DICT.items(): r=r.replace(k,v)
    return r

def glyphnet_to_taxa(g):
    r=g
    for v,k in REVERSE_DICT.items(): r=r.replace(v,k)
    return r

def benchmark(taxa):
    a=time.time(); g=taxa_to_glyphnet(taxa); b=time.time()
    c=time.time(); r=glyphnet_to_taxa(g); d=time.time()
    comp=100*(1-len(g)/len(taxa)); ok=(taxa==r)
    logging.info(f"Taxa={taxa} Glyphs={g} Comp={comp:.1f}% Enc={(b-a)*1000:.2f}ms Dec={(d-c)*1000:.2f}ms RT={ok}")
    return {"taxa":taxa,"glyphs":g,"compression_%":comp,"encode_ms":(b-a)*1000,"decode_ms":(d-c)*1000,"roundtrip_ok":ok}

if __name__=="__main__":
    for t in ["Bacteroides;Firmicutes;Actinobacteria","Bacteroides;Proteobacteria"]:
        print(benchmark(t))
