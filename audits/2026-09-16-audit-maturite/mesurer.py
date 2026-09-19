"""Mesures de l'audit U249 : lecture seule du modèle, résultats dans l'audit."""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from structured_io import read

OUT = Path(__file__).resolve().parent
MODEL = ROOT / "modeles/release/2026-09-16.2/model.yaml"
model = read(MODEL)
backlog = read(ROOT / "modeles/backlog/model.yaml")
nodes = {n["id"]: n for n in model["nodes"]}
caps = [n for n in nodes.values() if n["kind"] == "capability"]
transverse = [r for r in model["relations"] if r["type"] not in ("contains", "presents")]
ends = {i for r in transverse for i in (r["source_id"], r["target_id"])}
backlog_nodes = {n["id"]: n for n in backlog["nodes"]}
backlog_rels = {r["id"]: r for r in backlog["relations"]}
metrics = {
    "publication": model["version"],
    "model_sha256": sha256(MODEL.read_bytes()).hexdigest(),
    "nodes_by_kind": dict(Counter(n["kind"] for n in nodes.values())),
    "relations_by_type": dict(Counter(r["type"] for r in model["relations"])),
    "transverse_relations": len(transverse),
    "transverse_capability_to_capability": sum(
        nodes[r["source_id"]]["kind"] == nodes[r["target_id"]]["kind"] == "capability"
        for r in transverse
    ),
    "capabilities_without_transverse_relation": [n["id"] for n in caps if n["id"] not in ends],
    "capability_natures": dict(Counter(n["fields"].get("nature", "absente") for n in caps)),
    "capabilities_without_nature": [n["id"] for n in caps if not n["fields"].get("nature")],
    "capabilities_without_scope": [n["id"] for n in caps if not n["fields"].get("scope")],
    "capabilities_with_definition": sum(bool(n["fields"].get("definition")) for n in caps),
    "capabilities_with_finality": sum(bool(n["fields"].get("finality")) for n in caps),
    "old_D07_domain_mentions_in_scope": [
        n["id"] for n in caps if any(
            text in n["fields"].get("scope", "") for text in ("dans D07", "par D07")
        )
    ],
    "published_node_fields_different_from_backlog": [
        n["id"] for n in nodes.values() if n["fields"] != backlog_nodes[n["id"]]["fields"]
    ],
    "published_relation_content_different_from_backlog": [
        r["id"] for r in model["relations"]
        if any(r.get(k) != backlog_rels[r["id"]].get(k)
               for k in ("source_id", "target_id", "type", "qualification"))
    ],
    "backlog_only_nodes": [
        {"id": n["id"], "kind": n["kind"], "name": n["fields"]["name"]}
        for n in backlog["nodes"] if n["id"] not in nodes
    ],
    "example_count_note": "Comptage qualitatif manuel dans qualite-granularite.md ; non déduit d'un mot-clé.",
}
(OUT / "metriques.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
before = json.loads((OUT / "empreintes-avant.json").read_text(encoding="utf-8"))
changes = [p for p, digest in before["files"].items()
           if not (ROOT / p).is_file() or sha256((ROOT / p).read_bytes()).hexdigest() != digest]
verification = {"protected_file_count": len(before["files"]), "changed_protected_files": changes}
(OUT / "verification.json").write_text(json.dumps(verification, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"capabilities": len(caps), "transverse_relations": len(transverse), **verification}))
if changes:
    raise SystemExit("Des fichiers protégés ont changé pendant l'audit.")
