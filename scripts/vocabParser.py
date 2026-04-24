import json
from typing import List, Dict


def load_vocab(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def flatten_vocab(data: List[Dict]) -> List[Dict]:
    rows = []

    for entry in data:
        word = entry.get("word")
        meanings = entry.get("meanings", [])

        for meaning in meanings:
            translation = meaning.get("translation")
            examples = meaning.get("examples", [])

            # If no examples exist, still keep the meaning
            if not examples:
                rows.append({
                    "word": word,
                    "translation": translation,
                    "sentence": None,
                    "sentence_translation": None
                })
                continue

            for ex in examples:
                rows.append({
                    "word": word,
                    "translation": translation,
                    "sentence": ex.get("sentence"),
                    "sentence_translation": ex.get("translation")
                })

    return rows


def print_sample(rows: List[Dict], n: int = 10):
    for r in rows[:n]:
        print(r)


if __name__ == "__main__":
    path = "../data/fi/finnish-1000-words.json"

    data = load_vocab(path)
    rows = flatten_vocab(data)

    print(f"Total rows: {len(rows)}\n")
    print_sample(rows)
