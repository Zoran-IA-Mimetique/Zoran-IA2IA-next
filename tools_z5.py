import sys, zlib, base64

def z5_encode(text: str) -> str:
    return "Z5::" + base64.b64encode(zlib.compress(text.encode("utf-8"))).decode("ascii")

if __name__ == "__main__":
    data = sys.stdin.read()
    print(z5_encode(data))