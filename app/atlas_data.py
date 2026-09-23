"""Read authoritative YAML/legacy JSON; API responses remain JSON."""

from __future__ import annotations

import hashlib
import html
import json
import re
import unicodedata
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

SCHEMA_VERSION = 2
REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))
from scripts.git_history import read_bytes as artifact_bytes
from scripts.release_catalog import resolve_release, catalog
from scripts.structured_io import read as read_document, working_path
MAP_PATH = "connaissance/25-domaines-coeur-et-epreuve-recits.md"
MODEL_DIRECTORY = "modeles"
SPACES = {"backlog", "release"}
DEFAULT_SPACE = "backlog"
SOURCE_DIRECTORIES = ("connaissance", "marche", "audits")
ROOT_SOURCES = ("README.md", "AGENTS.md", "JOURNAL.md")
REFERENCE_ID = re.compile(r"(?:U|P|C|Q|INF|CMP|ELM|CAP|F|A)\d{1,4}\Z")


class ModelError(ValueError):
    """The source cannot be faithfully represented with the current adapter."""


class SourceAccessError(ValueError):
    """The requested file is outside the explicit document allowlist."""


def plain_text(value: str) -> str:
    """Remove the small amount of Markdown used in canonical table cells."""
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    return html.unescape(value.replace("**", "").replace("`", "").replace(r"\|", "|")).strip()


def heading_anchor(title: str) -> str:
    """Match the Unicode heading IDs used by MkDocs' default toc slugifier."""
    title = unicodedata.normalize("NFKC", plain_text(title)).lower()
    title = re.sub(r"[^\w\s-]", "", title, flags=re.UNICODE).strip()
    return re.sub(r"[-\s]+", "-", title)


def resolve_source(root: Path, path: str) -> Path:
    """Authorize both the lexical path and its final symlink-resolved target."""
    if not isinstance(path, str) or not path or any(c in path for c in ("\\", "\x00", ":")):
        raise SourceAccessError("Chemin de source non autorisé.")
    relative = PurePosixPath(path)
    if relative.is_absolute() or any(p in (".", "..", "") for p in path.split("/")):
        raise SourceAccessError("Chemin de source non autorisé.")
    root = root.resolve()
    allowed = path in ROOT_SOURCES or (
        len(relative.parts) > 1
        and relative.parts[0] in SOURCE_DIRECTORIES
        and relative.suffix == ".md"
    )
    if not allowed:
        raise SourceAccessError("Seuls les documents Markdown du modèle sont accessibles.")
    target = (root / Path(*relative.parts)).resolve()
    try:
        final = target.relative_to(root).as_posix()
    except ValueError as exc:
        raise SourceAccessError("La source sort du répertoire du projet.") from exc
    # Also reject symlinks from an allowed folder into archive or another folder.
    if final != path:
        raise SourceAccessError("Les liens vers une autre source ne sont pas accessibles.")
    if not target.is_file():
        raise FileNotFoundError("Source introuvable.")
    return target


def source_paths(root: Path) -> list[str]:
    paths = [name for name in ROOT_SOURCES if (root / name).is_file()]
    for directory in SOURCE_DIRECTORIES:
        paths.extend(p.relative_to(root).as_posix() for p in (root / directory).rglob("*.md"))
    result = []
    for path in sorted(set(paths)):
        try:
            resolve_source(root, path)
        except (SourceAccessError, FileNotFoundError):
            continue
        result.append(path)
    return result


def _read_corpus(root: Path) -> dict[str, bytes]:
    return {path: resolve_source(root, path).read_bytes() for path in source_paths(root)}


def _model_path(root: Path, space: str, version=None) -> str:
    if space not in SPACES:
        raise ModelError("Espace inconnu : choisir release ou backlog.")
    if space == "backlog":
        return working_path(root / "modeles/backlog").relative_to(root).as_posix()
    try:
        pointer = resolve_release(root / 'modeles/release', version)
    except (ValueError, OSError, KeyError) as exc:
        raise ModelError(str(exc)) from exc
    relative = pointer.get("path")
    if not isinstance(relative, str) or not relative.endswith(("/model.json", "/model.yaml")):
        raise ModelError("Le pointeur de release ne désigne pas un modèle versionné YAML/JSON.")
    return _safe_model_path(root, "modeles/release/" + relative).relative_to(root).as_posix()


def _safe_model_path(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or any(c in relative for c in ("\\", ":", "\x00")):
        raise ModelError("Chemin de modèle invalide.")
    parts = relative.split("/")
    if not parts or parts[0] != MODEL_DIRECTORY or any(p in ("", ".", "..") for p in parts):
        raise ModelError("Chemin de modèle hors du périmètre autorisé.")
    target = root.joinpath(*parts).resolve()
    if target.relative_to(root).as_posix() != relative:
        raise ModelError("Lien de modèle non autorisé.")
    return target


def _read_json(root: Path, relative: str) -> dict:
    try:
        value = read_document(_safe_model_path(root, relative))
    except (OSError, ValueError) as exc:
        raise ModelError(f"Modèle YAML/JSON absent ou invalide : {relative}.") from exc
    if not isinstance(value, dict):
        raise ModelError(f"Un objet structuré est attendu : {relative}.")
    return value


def get_revision(root: Path = REPOSITORY_ROOT, space: str = DEFAULT_SPACE, version=None) -> str:
    root = Path(root).resolve()
    if space == "panorama-as-is":
        index = _read_json(root, "modeles/panorama-as-is/current.json")
        paths = ["modeles/panorama-as-is/current.json"] + [entry["path"] for entry in index.get("panoramas", [])]
        if index.get("shared", {}).get("path"):
            paths.append(index["shared"]["path"])
    else:
        paths = [_model_path(root, space, version)]
        if space == 'release' and (root/'modeles/release/index.json').exists():
            paths.append('modeles/release/index.json')
    digest = hashlib.sha256()
    # Evidence edits do not change model identity. Only the selected JSON model
    # and presentation configuration affect this view; no cross-space fallback.
    for relative in [*paths, "app/exploration.json"]:
        target = (root / relative) if relative == "app/exploration.json" else _safe_model_path(root, relative)
        digest.update(relative.encode() + b"\0" + (artifact_bytes(target) if relative != "app/exploration.json" or target.is_file() else b"missing"))
    return digest.hexdigest()[:20]


def _decode(data: bytes, path: str) -> str:
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ModelError(f"La source {path} doit être encodée en UTF-8.") from exc


def _title(content: str, fallback: str) -> str:
    match = re.search(r"^# (.+)$", content, re.MULTILINE)
    return plain_text(match.group(1)) if match else fallback


def read_source(path: str, anchor: str = "", root: Path = REPOSITORY_ROOT) -> dict:
    if len(anchor) > 300 or any(ord(c) < 32 for c in anchor):
        raise SourceAccessError("Ancre de source invalide.")
    target = resolve_source(Path(root), path)
    content = _decode(target.read_bytes(), path)
    return {"path": path, "title": _title(content, target.stem), "content": content, "anchor": anchor}


def _source_index(corpus: dict[str, bytes]) -> tuple[list[dict], dict[str, dict]]:
    files = []
    references: dict[str, dict] = {}
    for path, data in corpus.items():
        content = _decode(data, path)
        files.append({"path": path, "title": _title(content, Path(path).stem)})
        for line_number, line in enumerate(content.splitlines(), 1):
            match = re.match(r"^#{1,6}\s+([A-Z]+\d+)\s*$", line)
            if match and REFERENCE_ID.fullmatch(match.group(1)):
                identifier = match.group(1)
                # Dedicated register headings take precedence over prose mentions.
                references.setdefault(identifier, {
                    "id": identifier, "path": path,
                    "anchor": heading_anchor(identifier), "line": line_number,
                })
    return files, references


def load_model(root: Path = REPOSITORY_ROOT, space: str = DEFAULT_SPACE, version=None) -> dict:
    """Load one JSON space without enriching its fields from any other space."""
    root = Path(root).resolve()
    model_path = _model_path(root, space, version)
    value = _read_json(root, model_path)
    if value.get("schema_version") != "1.0.0" or value.get("space") != space:
        raise ModelError("Schéma ou espace du modèle JSON incompatible.")
    if not isinstance(value.get("nodes"), list) or not isinstance(value.get("relations"), list):
        raise ModelError("Le modèle JSON doit fournir nodes et relations.")
    seen = set()
    for node in value["nodes"]:
        if not isinstance(node, dict) or not isinstance(node.get("id"), str) or node["id"] in seen:
            raise ModelError("Identifiant de nœud manquant ou dupliqué.")
        seen.add(node["id"])
        if not isinstance(node.get("fields"), dict) or not isinstance(node.get("source_refs"), list):
            raise ModelError(f"Champs ou provenance invalides : {node['id']}.")
        if space == "release" and node.get("review", {}).get("state") not in {"accepted", "partial", "proposed", "under_review"}:
            raise ModelError(f"Statut non publiable dans la release : {node['id']}.")
    edges = set()
    for edge in value["relations"]:
        if not isinstance(edge, dict) or not edge.get("id") or edge["id"] in edges:
            raise ModelError("Identifiant de relation manquant ou dupliqué.")
        edges.add(edge["id"])
        if edge.get("source_id") not in seen or edge.get("target_id") not in seen:
            raise ModelError(f"Cible de relation absente : {edge['id']}.")
        if space == "release" and edge.get("review", {}).get("state") not in {"accepted", "partial", "proposed", "under_review"}:
            raise ModelError(f"Relation non publiable dans la release : {edge['id']}.")
    source_files, references = _source_index(_read_corpus(root))
    value.update({
        "schemaVersion": SCHEMA_VERSION,
        "date": value.get("as_of", value.get("date", "")),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "dataRevision": get_revision(root, space, version),
        "sourcePath": model_path,
        "sourceFiles": source_files,
        "sourceReferences": references,
        "warnings": ["Release : dernier modèle publié avec statuts explicites. La publication ne valide pas toutes les capacités ; propositions, validations partielles et réexamens restent visibles."] if space == "release" else ["Backlog : propositions, éléments acceptés et illustrations restent distingués. Cette vue n’est pas la release."],
    })
    return value


def load_panorama(root: Path = REPOSITORY_ROOT) -> dict:
    """Read the three current SI files through a fixed index, separately from models."""
    root = Path(root).resolve()
    value = _read_json(root, "modeles/panorama-as-is/current.json")
    if value.get("space") != "panorama-as-is" or len(value.get("panoramas", [])) != 3:
        raise ModelError("Le panorama doit identifier les trois SI.")
    for entry in value["panoramas"]:
        relative = entry.get("path", "")
        if not relative.startswith("modeles/panorama-as-is/"):
            raise ModelError("Chemin de panorama non autorisé.")
        entry["data"] = _read_json(root, relative)
        if entry["data"].get("model_id") != entry.get("model_id") or entry["data"].get("space") != "panorama-as-is":
            raise ModelError("Le panorama chargé ne correspond pas au SI annoncé.")
    if value.get("shared", {}).get("path"):
        if not value["shared"]["path"].startswith("modeles/panorama-as-is/"):
            raise ModelError("Chemin de contexte partagé non autorisé.")
        value["shared"]["data"] = _read_json(root, value["shared"]["path"])
    value.update({"revision": get_revision(root, "panorama-as-is"), "date": value.get("as_of"), "sourcePath": "modeles/panorama-as-is/current.json", "sourceReferences": _source_index(_read_corpus(root))[1]})
    return value


