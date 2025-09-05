# Script de comptage simple
import sys

def count_words(text):
    words = text.split()
    return len(words), len(text), len(text.replace(" ", ""))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_counter.py <file.txt>")
        sys.exit(1)
    fname = sys.argv[1]
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    wc, chars, chars_ns = count_words(content)
    print(f"Mots: {wc}\nCaractères (espaces): {chars}\nCaractères (sans espaces): {chars_ns}")
