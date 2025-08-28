"""
Z5 Compression - Sobriété Cognitive
-----------------------------------
Compression fractale pour réduire les tokens (simulé par zlib).
"""

import zlib
import base64

def z5_compress(data: str) -> str:
    compressed = zlib.compress(data.encode())
    return "Z5::" + base64.b64encode(compressed).decode()

def z5_decompress(data: str) -> str:
    if not data.startswith("Z5::"):
        return data
    compressed = base64.b64decode(data[4:])
    return zlib.decompress(compressed).decode()

if __name__ == "__main__":
    msg = "Mémoire fractale ΔM11.3 et EthicChain."
    c = z5_compress(msg)
    print("Compressed:", c[:60] + "…")
    print("Decompressed:", z5_decompress(c))
