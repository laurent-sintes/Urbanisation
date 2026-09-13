"""Assemble the dated inline preview from the fragment and derived model snapshot."""
import argparse
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent


def build(destination: Path) -> None:
    data = json.loads((BASE / "model-snapshot.json").read_text(encoding="utf-8-sig"))
    fragment = (BASE / "explorer.fragment.html").read_text(encoding="utf-8")
    assert fragment.count("__MODEL_SNAPSHOT__") == 1
    payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(fragment.replace("__MODEL_SNAPSHOT__", payload), encoding="utf-8")
    print(destination)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("destination", type=Path)
    build(parser.parse_args().destination)
