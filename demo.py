#!/usr/bin/env python3
import sys, json

def sanitize_payload(s: str) -> str:
    # very small, explicit allowlist
    allowed = "".join(ch for ch in s if ch.isalnum() or ch in " .,;:!?-_()[]{}+/\@#")
    return allowed.strip()

def main():
    print(">> Zoran Injecteur (demo) — entrez une phrase, Ctrl-D pour finir:", file=sys.stderr)
    acc = []
    for line in sys.stdin:
        clean = sanitize_payload(line)
        if not clean:
            continue
        acc.append(clean)
    payload = " ".join(acc)[:5000]
    glyph = "⟦PAYLOAD:{}⟧".format(payload[:64])
    out = {"ok": True, "size": len(payload), "glyph": glyph}
    print(json.dumps(out, ensure_ascii=False))
if __name__ == "__main__":
    main()
