"""Extract the described SI landscape, preserving source fields and uncertainties.

This is a deterministic migration of knowledge, never a deployment discovery.
Run from any directory: python scripts/extract_panorama.py [--check]
The application and all Markdown registers are left unchanged.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VERSION = "2026-09-13.1"
AS_OF = "2026-09-13"
BASE = "modeles/panorama-as-is"
SHARED_PATH = f"{BASE}/shared-{VERSION}.json"
CANDIDATES_PATH = "modeles/backlog/panorama-candidates.json"
FILES = {
    "objects": "connaissance/07-composants.md",
    "flows": "connaissance/08-flux.md",
    "information_authorities": "connaissance/10-autorites-information.md",
    "decision_responsibilities": "connaissance/11-responsabilites-decision.md",
}
CORRECTIONS = "connaissance/04-corrections.md"
SOURCE_COUNTS = {"objects": 20, "flows": 21, "information_authorities": 22, "decision_responsibilities": 22}
SECTION = re.compile(r"^## ([A-Z]+(?:-[A-Z]+|\d+))\s*$", re.MULTILINE)
FIELD = re.compile(r"^\*\*([a-z_]+)\*\*\s*$", re.MULTILINE)
REFERENCE = re.compile(r"\b(?:INF|DEC|CAP|CMP|ELM|[UFACPQ])\d{1,4}\b")
RANGE = re.compile(r"\b(INF|DEC|CAP|CMP|ELM|[UFACPQ])(\d{1,4})\s*[-–—]\s*(?:\1)?(\d{1,4})\b")

KINDS = {
    "ORG-GBM": "organisation", "ORG-CLOG": "organisation",
    "APP-STR": "application_family", "APP-POS": "application_collection",
    "APP-WEB": "application_collection", "APP-TAL": "integration_platform",
    "ALIAS-ACH": "unresolved_application_mention", "SI-SAR": "system_landscape_mention",
    "APP-AFS": "solution_and_feature_mention",
}
SHARED_IDS = {"ORG-CLOG", "APP-XRD", "FL12", "FL13", "FL14", "INF09", "INF13", "DEC16", "DEC17", "DEC18", "DEC19"}
BOARDRIDERS_IDS = {"APP-ECC", "APP-AFS", "APP-NEW"}
SARENZA_IDS = {"SI-SAR", "FL21", "INF17"}
TARGET_IDS = {"INF18", "INF19", "INF20", "INF21", "INF22"}
NEED_IDS = {"DEC21", "DEC22"}
CANDIDATE_IDS = SARENZA_IDS | TARGET_IDS | NEED_IDS | {"DEC20"}
UNKNOWN_AUTHORITIES = {"INF02", "INF03", "INF08", "INF09", "INF10", "INF11", "INF12"}
UNKNOWN_DECISIONS = {"DEC09", "DEC10", "DEC11", "DEC12", "DEC20"}
CORRECTION_LINKS = {
    "ORG-CLOG": ["C06", "C44"], "APP-UR": ["C02", "C03"],
    "APP-STR": ["C04"], "APP-TAL": ["C05"], "SI-SAR": ["C01"],
    "DEC20": ["C32"], "DEC21": ["C32"], "DEC22": ["C32"],
}


def canonical(value: str) -> str:
    value = value.replace("GBM — marques historiques", "Périmètre historique de Beaumanoir")
    value = re.sub(r"\bGBM\b", "périmètre historique de Beaumanoir", value)
    return re.sub(r"\bBRD\b", "Boardriders", value)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encoded(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def source_refs(text: str) -> list[str]:
    refs = set(REFERENCE.findall(text))
    for match in RANGE.finditer(text):
        prefix, first, last = match.groups()
        start, end = int(first), int(last)
        if start > end or end - start > 1000:
            raise ValueError(f"Plage de sources invalide : {match.group()}")
        width = max(len(first), len(last))
        refs.update(prefix + str(i).zfill(width) for i in range(start, end + 1))
    return sorted(refs, key=lambda value: (re.sub(r"\d+$", "", value), int(re.search(r"\d+$", value).group())))


def parse_records(path: str) -> list[dict]:
    text = (ROOT / path).read_text(encoding="utf-8-sig")
    headings = list(re.finditer(r"^## (.+)$", text, re.MULTILINE))
    records = []
    for index, heading in enumerate(headings):
        identifier = heading.group(1).strip()
        if not re.fullmatch(r"[A-Z]+(?:-[A-Z]+|\d+)", identifier):
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        block = text[heading.end():end].strip()
        fields = list(FIELD.finditer(block))
        values = {}
        for field_index, field in enumerate(fields):
            field_end = fields[field_index + 1].start() if field_index + 1 < len(fields) else len(block)
            key = field.group(1)
            if key in values:
                raise ValueError(f"Champ dupliqué {identifier}.{key}")
            values[key] = block[field.end():field_end].strip()
        if values.get("id") != identifier:
            raise ValueError(f"Identifiant non concordant dans {path} : {identifier}")
        records.append({
            "id": identifier,
            "source_fields": values,
            "source_record_text": text[heading.start():end].strip(),
            "source_locator": {"path": path, "anchor": identifier.lower()},
            "source_refs": source_refs(values.get("source", "")),
        })
    return records


def endpoint(label: str, object_ids: set[str]) -> dict:
    # Only an exact existing identifier resolves. 'SI C-Log' is not ORG-CLOG.
    if label in object_ids:
        return {"id": label, "unresolved_label": None}
    return {"id": None, "unresolved_label": canonical(label)}


def classification(identifier: str, category: str) -> tuple[str, str]:
    if identifier in TARGET_IDS:
        return "declared", "target"
    if identifier in NEED_IDS:
        return "declared", "need"
    if identifier == "DEC20":
        return "unknown", "unknown"
    if identifier in UNKNOWN_AUTHORITIES or identifier in UNKNOWN_DECISIONS:
        return "unknown", "as_is"
    if identifier == "FL19":
        return "inferred", "as_is"
    return "declared", "as_is"


def normalize(record: dict, category: str, object_ids: set[str], corrections: dict) -> dict:
    item = dict(record)
    fields = item["source_fields"]
    identifier = item["id"]
    item["name"] = canonical(next((fields[key] for key in ("nom", "contenu", "objet", "decision") if key in fields), identifier))
    item["scope"] = canonical(fields.get("perimetre", fields.get("contexte", "Périmètre non renseigné dans la fiche source.")))
    item["evidence_status"], item["architecture_intent"] = classification(identifier, category)
    item["observed_at"] = None
    item["limitations"] = [canonical(fields["reserve"])] if fields.get("reserve") else []
    item["source_category"] = category
    item["classification_basis"] = "Qualification de migration à partir du registre et de ses réserves ; aucune observation de déploiement. Les champs source sont conservés intégralement."
    item["correction_refs"] = CORRECTION_LINKS.get(identifier, [])
    item["correction_context"] = [
        {"id": cid, "text": canonical(corrections[cid]["source_fields"]["formulation_retenue"]), "source_locator": corrections[cid]["source_locator"]}
        for cid in item["correction_refs"]
    ]
    if category == "objects":
        item["kind"] = KINDS.get(identifier, "application")
        item["described_role"] = canonical(fields["role"])
        item["deployment_status"] = {
            "APP-IRM": "deployment_in_progress_declared", "APP-SCO": "retirement_in_progress_declared",
            "ALIAS-ACH": "unresolved_identity", "APP-AFS": "scope_not_established",
            "APP-POS": "not_inventoried", "APP-WEB": "not_inventoried",
        }.get(identifier, "not_independently_verified")
    elif category == "flows":
        item["kind"] = {
            "FL01": "data_exchange", "FL02": "data_exchange", "FL03": "functional_dependency",
            "FL05": "document_exchange", "FL10": "human_interaction", "FL19": "flow_to_reconcile",
        }.get(identifier, "business_flow")
        item["endpoints"] = {
            "source": endpoint(fields["origine"], object_ids),
            "target": endpoint(fields["destination"], object_ids),
        }
        item["content"] = canonical(fields["contenu"])
        item["modality"] = canonical(fields["modalite"])
        item["technical_interface_status"] = "declared" if identifier in {"FL01", "FL02", "FL05"} else "not_established"
        item["described_status"] = canonical(fields["statut"])
    elif category == "information_authorities":
        item["kind"] = "information_authority_or_producer"
        item["information"] = canonical(fields["objet"])
        item["authority_or_producer"] = canonical(fields["autorite_ou_producteur"])
        item["other_contributions"] = canonical(fields["autres_contributions"])
        item["authority_qualification"] = "unknown" if identifier in UNKNOWN_AUTHORITIES else "source_reservations_apply"
    else:
        item["kind"] = "decision_responsibility"
        item["decision"] = canonical(fields["decision"])
        item["described_realization"] = canonical(fields["realisation"])
        item["exercise_status"] = "not_exercised_in_described_scope" if identifier == "DEC08" else "subject_to_source_reservations"
    return item


def envelope(model_id: str, source_files: list[dict], assessment_status: str) -> dict:
    return {
        "schema_version": "1.0.0", "model_id": model_id, "space": "panorama-as-is",
        "version": VERSION, "as_of": AS_OF, "observed_at": None,
        "assessment_status": assessment_status,
        "source_files": source_files,
        "objects": [], "flows": [], "information_authorities": [], "decision_responsibilities": [],
        "exclusions": [],
        "limitations": [
            "as_of est la date de publication de cet état de connaissance, pas une attestation de fraîcheur des SI ; aucune date d’observation opérationnelle vérifiée n’est disponible.",
            "Les descriptions sont issues de récits et registres. declared ne signifie pas observed ; inconnues, réserves et périmètres source sont conservés.",
            "source_fields et source_record_text sont des transcriptions de provenance : leurs abréviations et formulations historiques restent intactes ; les champs de lecture utilisent les libellés canoniques.",
            "Une source ou destination textuelle non résolue ne crée pas un nouveau composant ni une interface directe. Une organisation n’est pas un système.",
            "Les catégories et statuts de migration qualifient la preuve disponible ; ils n’adoptent aucune architecture cible.",
        ],
    }


def build() -> dict[str, bytes]:
    inputs = {category: parse_records(path) for category, path in FILES.items()}
    if {key: len(value) for key, value in inputs.items()} != SOURCE_COUNTS:
        raise ValueError("Le contenu des registres a changé : relire la qualification et la répartition avant d’extraire.")
    corrections = {r["id"]: r for r in parse_records(CORRECTIONS)}
    object_ids = {r["id"] for r in inputs["objects"]}
    # A frozen extraction keeps its original source-file fingerprints. Appending
    # unrelated analysis to a register must not change a historical snapshot.
    # Relevant source fields and linked corrections are still parsed afresh:
    # a material change produces a different payload and is rejected below.
    frozen_context = ROOT / SHARED_PATH
    if frozen_context.is_file():
        baseline = json.loads(frozen_context.read_text(encoding="utf-8"))
        if baseline.get("version") != VERSION:
            raise ValueError("Version incohérente dans le contexte partagé gelé.")
        source_files = baseline["source_files"]
    else:
        source_files = [{"path": path, "sha256": sha256((ROOT / path).read_bytes())} for path in [*FILES.values(), CORRECTIONS]]
    outputs = {
        "beaumanoir-historique": envelope("beaumanoir-historique-si", source_files, "partially_documented"),
        "boardriders": envelope("boardriders-si", source_files, "partially_documented"),
        "sarenza": envelope("sarenza-si", source_files, "not_assessed"),
        "shared": envelope("beaumanoir-shared-context", source_files, "partially_documented"),
    }
    outputs["sarenza"]["assessment_reason"] = "Panorama Sarenza non traité. Les trois mentions initiales SI-SAR, FL21 et INF17 restent à instruire dans le backlog ; aucune cartographie As Is n’est déduite de ces mentions."
    outputs["shared"]["context_role"] = "Frontière C-Log et éléments partagés ; ce fichier n’est pas un quatrième SI."
    candidates = {
        "schema_version": "1.0.0", "model_id": "panorama-candidates", "space": "backlog",
        "version": VERSION, "date": AS_OF, "source_files": source_files, "records": [],
        "limitations": [
            "Ces entrées ne sont pas des réalisations As Is. Elles préservent des orientations cible, besoins, responsabilités inconnues ou mentions Sarenza à instruire.",
            "DEC20 ne localise pas une responsabilité exercée ; C32/U30 confirme séparément le principe de réservation à la commande dans le périmètre historique de Beaumanoir, sans en prouver le réalisateur.",
        ],
    }
    destinations = {}
    for category, records in inputs.items():
        for record in records:
            item = normalize(record, category, object_ids, corrections)
            identifier = item["id"]
            if identifier in CANDIDATE_IDS:
                item["review_status"] = "pending_review"
                reason = (
                    "Sarenza n’est pas encore traité ; mention source conservée à instruire."
                    if identifier in SARENZA_IDS else
                    "Orientation de maîtrise externe et de plateforme, sans preuve de déploiement."
                    if identifier in TARGET_IDS else
                    "Besoin Boardriders déclaré, réalisation installée et responsable non établis."
                    if identifier in NEED_IDS else
                    "Responsabilité issue de propositions et questions ; réalisateur non établi."
                )
                item["exclusion_from_as_is_reason"] = reason
                candidates["records"].append(item)
                destinations[identifier] = "backlog"
                if identifier in SARENZA_IDS:
                    outputs["sarenza"]["exclusions"].append({"record_id": identifier, "reason": reason, "preserved_in": CANDIDATES_PATH})
                elif identifier in NEED_IDS:
                    outputs["boardriders"]["exclusions"].append({"record_id": identifier, "reason": reason, "preserved_in": CANDIDATES_PATH})
                continue
            destination = "shared" if identifier in SHARED_IDS else "boardriders" if identifier in BOARDRIDERS_IDS else "beaumanoir-historique"
            outputs[destination][category].append(item)
            destinations[identifier] = destination
    all_source_ids = [r["id"] for records in inputs.values() for r in records]
    all_output_ids = [r["id"] for output in outputs.values() for key in FILES for r in output[key]] + [r["id"] for r in candidates["records"]]
    if Counter(all_source_ids) != Counter(all_output_ids) or len(set(all_output_ids)) != len(all_output_ids):
        raise ValueError("Perte ou duplication d’un repère lors de la répartition.")
    source_by_id = {r["id"]: r for records in inputs.values() for r in records}
    for output in [*outputs.values(), {"records": candidates["records"]}]:
        for key in [*FILES, "records"]:
            for item in output.get(key, []):
                if item["source_fields"] != source_by_id[item["id"]]["source_fields"]:
                    raise ValueError(f"Champs source modifiés pour {item['id']}")
                if item["evidence_status"] == "observed" or item["observed_at"] is not None:
                    raise ValueError("Observation opérationnelle inventée")
    written = {CANDIDATES_PATH: encoded(candidates)}
    shared_path = SHARED_PATH
    written[shared_path] = encoded(outputs["shared"])
    shared_ref = {"path": shared_path, "sha256": sha256(written[shared_path]), "relationship_status": "context_only", "note": "Référence de contexte ; aucune relation de déploiement ou interface avec chaque SI n’est déduite de ce partage."}
    index = {
        "schema_version": "1.0.0", "model_id": "beaumanoir-si", "space": "panorama-as-is",
        "version": VERSION, "as_of": AS_OF, "observed_at": None,
        "shared": shared_ref, "panoramas": [],
        "candidates": {"path": CANDIDATES_PATH, "sha256": sha256(written[CANDIDATES_PATH])},
        "source_record_counts": SOURCE_COUNTS,
        "record_assignment": destinations,
        "limitations": ["Les trois panoramas décrivent l’état de connaissance courant ; les traces datées ne constituent pas un audit des déploiements au 13 septembre 2026."],
    }
    for slug in ("beaumanoir-historique", "boardriders", "sarenza"):
        output = outputs[slug]
        output["shared_context"] = shared_ref
        path = f"{BASE}/{slug}/versions/{VERSION}/panorama.json"
        written[path] = encoded(output)
        index["panoramas"].append({"model_id": output["model_id"], "name": {"beaumanoir-historique": "Périmètre historique de Beaumanoir", "boardriders": "Boardriders", "sarenza": "Sarenza"}[slug], "version": VERSION, "path": path, "sha256": sha256(written[path]), "assessment_status": output["assessment_status"], "record_counts": {key: len(output[key]) for key in FILES}})
    written[BASE + "/current.json"] = encoded(index)
    return written


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Vérifier les sorties sans écrire.")
    args = parser.parse_args()
    results = build()
    # Preflight every immutable output before any write: a failed migration must
    # not leave the current pointer or mutable backlog partially refreshed.
    if not args.check:
        assert_immutable_outputs(results)
    for name, data in results.items():
        path = ROOT / name
        if args.check:
            if not path.is_file() or path.read_bytes() != data:
                raise SystemExit(f"Sortie absente ou non conforme : {name}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(json.dumps({"mode": "check" if args.check else "write", "files": len(results), "source_records_preserved": sum(SOURCE_COUNTS.values()), "source_fields_preserved": True}, ensure_ascii=False))


def assert_immutable_outputs(results: dict[str, bytes]) -> None:
    for name, data in results.items():
        if "/versions/" not in name and name != SHARED_PATH:
            continue
        path = ROOT / name
        if path.is_file() and path.read_bytes() != data:
            raise SystemExit(f"Version immuable déjà présente et différente : {name}. Créer et qualifier une nouvelle version ; aucun fichier n’a été écrit.")


if __name__ == "__main__":
    main()
