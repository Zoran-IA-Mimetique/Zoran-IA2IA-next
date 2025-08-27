# ΔM11.3 × Vector Store (Milvus/Pinecone)
- Chaque fragment = {id, text, layer, entropy, ttl, zgs, hash, timestamp}
- Index: cosine / IP ; metadata filtrable (layer, entropy<=τ, ttl>now)
- Politique: purge TTL, redaction, rollback ΔM11.3 quand entropy↑

## Flux
1) Normalize → Hash → Embed → Upsert
2) Query → Filter(meta) → Rerank(light) → ΔM11.3 check → Trace

## Remarque
Ce design reste "code minimal = transparence". Les fichiers de config sont plats et les embeddings sont stubbés (remplacables).
