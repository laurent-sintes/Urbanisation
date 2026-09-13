"""Regression checks for current business boundaries and the read-only adapter.

Run from the repository root: python -m unittest discover -s app -p test_data.py
"""

import contextlib
import http.client
import io
import json
import shutil
import threading
import unittest
import uuid
from pathlib import Path
from urllib.parse import urlencode

from atlas_data import (
    MAP_PATH, REPOSITORY_ROOT, ModelError, SourceAccessError,
    get_revision, load_model, load_panorama, read_source, resolve_source,
)
from server import create_server
from scripts.release_catalog import resolve_release

def active_pointer(root):
    folder=root / "modeles/release"
    return folder / ("index.json" if (folder/"index.json").exists() else "current.json")



class SourceFixture(unittest.TestCase):
    def setUp(self):
        # Keep temporary copies inside the authorized workspace on Windows.
        # mkdir's inherited ACL works in a restricted Windows token; Python
        # 3.14 TemporaryDirectory's mode 0700 excludes that token on this host.
        self.root = REPOSITORY_ROOT / "app" / ("flow-atlas-test-" + uuid.uuid4().hex)
        self.root.mkdir()
        self.addCleanup(self.cleanup_fixture)
        for relative in (MAP_PATH, "app/exploration.json"):

            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY_ROOT / relative, target)
        shutil.copytree(REPOSITORY_ROOT / "modeles", self.root / "modeles")

    def cleanup_fixture(self):
        target = self.root.resolve()
        if target.parent != (REPOSITORY_ROOT / "app").resolve() or not target.name.startswith("flow-atlas-test-"):
            raise RuntimeError("Répertoire de test hors du projet.")
        shutil.rmtree(target)

    def change_map(self, before, after):
        target = self.root / MAP_PATH
        content = target.read_text(encoding="utf-8")
        self.assertIn(before, content)
        target.write_text(content.replace(before, after, 1), encoding="utf-8")


class ModelTests(SourceFixture):
    def test_omitted_space_loads_backlog_and_its_revision(self):
        value = load_model(self.root)
        self.assertEqual(value["space"], "backlog")
        explicit = load_model(self.root, "backlog")
        for field in ("nodes", "relations", "sourcePath", "dataRevision"):
            self.assertEqual(value[field], explicit[field])
        self.assertEqual(get_revision(self.root), get_revision(self.root, "backlog"))

    def test_release_has_current_capabilities_with_explicit_statuses(self):
        release = load_model(self.root, "release")
        by_id = {n["id"]: n for n in release["nodes"]}
        capabilities = [n for n in release["nodes"] if n["kind"] == "capability"]
        self.assertEqual(len(capabilities), 36)
        self.assertEqual(sum(n["review"]["state"] == "accepted" for n in capabilities), 9)
        self.assertIn("definition", by_id["D01"]["fields"])
        self.assertNotIn("definition", by_id["D01"]["approved_fields"])
        self.assertIn("definition", by_id["D01"]["proposed_fields"])
        self.assertIn("D04", by_id)
        self.assertFalse(any(n["kind"] in {"object", "document", "event"} for n in release["nodes"]))
        reservation = next(r for r in release["relations"] if r["target_id"] == "D02.c")
        self.assertEqual(reservation["review"]["state"], "under_review")
        self.assertTrue(reservation["adoption_ids"])

    def test_backlog_retains_all_current_candidates_and_separate_alternative(self):
        value = load_model(self.root, "backlog")
        self.assertEqual(sum(n["kind"] == "capability" for n in value["nodes"]), 36)
        names = {n['id']: n['fields']['name'] for n in value['nodes']}
        self.assertEqual(names['D01.f'], 'Inventory Tracking')
        self.assertEqual(names['D01.g'], 'Record Inventory Movements')
        self.assertEqual(names['D01.c'], 'Inventory Visibility')
        self.assertNotIn('D01.a', names)
        self.assertNotIn('D01.b', names)
        self.assertEqual(sum(n["kind"] in {"object", "document", "event"} for n in value["nodes"]), 4)
        self.assertTrue(value["alternatives"])
        parents = {r["target_id"]: r["source_id"] for r in value["relations"] if r["type"] == "contains"}
        self.assertEqual(parents["D02.e"], "D03")
        self.assertEqual(parents["D02.b"], "D01")

    def test_markdown_and_old_metadata_cannot_change_model(self):
        before = load_model(self.root)
        self.change_map("Promise Proposal", "THIS IS NOT THE MODEL")
        (self.root / "app/model-metadata.json").write_text('{"invalid":"ignored"}', encoding="utf-8")
        after = load_model(self.root)
        self.assertEqual(before["nodes"], after["nodes"])
        self.assertEqual(before["relations"], after["relations"])
        self.assertEqual(before["dataRevision"], after["dataRevision"])

    def test_backlog_changes_do_not_change_release(self):
        before = get_revision(self.root, "release")
        backlog_before = get_revision(self.root)
        path = self.root / "modeles/backlog/model.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["nodes"][0]["fields"]["name"] = "BACKLOG MODIFIED"
        path.write_text(json.dumps(value), encoding="utf-8")
        self.assertEqual(before, get_revision(self.root, "release"))
        self.assertNotEqual(backlog_before, get_revision(self.root))
        self.assertEqual(load_model(self.root, "backlog")["nodes"][0]["fields"]["name"], "BACKLOG MODIFIED")

    def test_missing_release_never_falls_back_to_backlog_or_markdown(self):
        pointer = active_pointer(self.root)
        pointer.write_text('{"path":"missing/model.json"}', encoding="utf-8")
        with self.assertRaises(ModelError):
            load_model(self.root, "release")
        self.assertEqual(load_model(self.root, "backlog")["space"], "backlog")
        self.assertEqual(load_model(self.root)["space"], "backlog")

    def test_release_rejects_illustrations_without_falling_back(self):
        pointer = resolve_release(self.root / "modeles/release")
        path = self.root / "modeles/release" / pointer["path"]
        value = json.loads(path.read_text(encoding="utf-8"))
        value["nodes"][0]["review"]["state"] = "illustration"
        path.write_text(json.dumps(value), encoding="utf-8")
        with self.assertRaises(ModelError):
            load_model(self.root, "release")

    def test_model_path_cannot_escape_space(self):
        for path in ["../../backlog/model.json", "C:/private/model.json", "../model.json"]:
            (active_pointer(self.root)).write_text(json.dumps({"path": path}), encoding="utf-8")
            with self.subTest(path=path), self.assertRaises(ModelError):
                load_model(self.root, "release")

    def test_panorama_has_three_distinct_perimeters_and_sarenza_unassessed(self):
        value = load_panorama(self.root)
        self.assertEqual(len(value["panoramas"]), 3)
        entries = {p["model_id"]: p["data"] for p in value["panoramas"]}
        self.assertIn("beaumanoir-historique-si", entries)
        self.assertIn("boardriders-si", entries)
        self.assertEqual(entries["sarenza-si"]["assessment_status"], "not_assessed")
        for key in ["objects", "flows", "information_authorities", "decision_responsibilities"]:
            self.assertEqual(entries["sarenza-si"][key], [])
        self.assertEqual(value["shared"]["relationship_status"], "context_only")


class SourceAccessTests(SourceFixture):
    def test_traversal_and_private_paths_are_rejected(self):
        invalid = [
            "../README.md", "connaissance/../../README.md", "connaissance/../AGENTS.md",
            "/etc/passwd", "C:/Windows/win.ini", "connaissance\\file.md",
            "archive/conversation.md", "app/model-metadata.json", ".git/config",
            "connaissance/a.md:secret", "connaissance//a.md", "connaissance/./a.md",
        ]
        for path in invalid:
            with self.subTest(path=path), self.assertRaises(SourceAccessError):
                resolve_source(self.root, path)

    def test_allowlisted_file_returns_plain_markdown(self):
        source = read_source(MAP_PATH, "d01-stocks", self.root)
        self.assertEqual(source["path"], MAP_PATH)
        self.assertEqual(source["anchor"], "d01-stocks")
        self.assertTrue(source["content"].startswith("# Domaines cœur"))

    def test_symlink_cannot_bypass_allowlist(self):
        outside = self.root / "archive/private.md"
        outside.parent.mkdir()
        outside.write_text("private", encoding="utf-8")
        link = self.root / "connaissance/link.md"
        try:
            link.symlink_to(outside)
        except OSError:
            self.skipTest("Création de lien symbolique non autorisée sur cet hôte.")
        with self.assertRaises(SourceAccessError):
            resolve_source(self.root, "connaissance/link.md")


class HTTPTests(SourceFixture):
    def setUp(self):
        super().setUp()
        (self.root / "app/index.html").write_text("<!doctype html><title>Atlas</title>", encoding="utf-8")
        self.server = create_server(0, self.root)
        self.port = self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.stop_server)

    def stop_server(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)

    def request(self, path, method="GET", headers=None):
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        try:
            with contextlib.redirect_stderr(io.StringIO()):
                connection.request(method, path, headers=headers or {})
                response = connection.getresponse()
                body = response.read()
            return response.status, dict(response.getheaders()), body
        finally:
            connection.close()

    def test_api_identification_and_security_headers(self):
        status, headers, body = self.request("/api/status")
        self.assertEqual(status, 200)
        data = json.loads(body)
        self.assertEqual(data["appName"], "FLOW Atlas")
        self.assertEqual(data["repositoryRoot"], str(self.root.resolve()))
        self.assertEqual(data["schemaVersion"], 2)
        self.assertEqual(data["space"], "release")
        self.assertIsInstance(data["pid"], int)
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertEqual(headers["X-Content-Type-Options"], "nosniff")
        self.assertIn("script-src 'self'", headers["Content-Security-Policy"])

    def test_model_error_is_json_and_reading_refreshes(self):
        status, _, body = self.request("/api/model")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)["space"], "release")
        self.assertEqual(json.loads(self.request("/api/model?space=release")[2])["space"], "release")
        self.assertEqual(json.loads(self.request("/api/status?space=release")[2])["space"], "release")
        self.assertEqual(self.request("/api/model?space=backlog")[0], 422)
        self.assertEqual(self.request("/api/status?space=backlog")[0], 422)
        self.assertEqual(self.request("/api/panorama")[0], 404)
        self.assertEqual(self.request("/api/model?space=unknown")[0], 422)
        (active_pointer(self.root)).write_text("invalid JSON", encoding="utf-8")
        status, _, body = self.request("/api/model?space=release")
        self.assertEqual(status, 422)
        self.assertIn("error", json.loads(body))
        self.assertEqual(self.request("/api/model")[0], 422)

    def test_invalid_backlog_does_not_affect_published_urbanisation(self):
        (self.root / "modeles/backlog/model.json").write_text("invalid JSON", encoding="utf-8")
        self.assertEqual(self.request("/api/model")[0], 200)
        self.assertEqual(self.request("/api/model?space=release")[0], 200)

    def test_http_source_allowlist_and_static_allowlist(self):
        for path in ["../AGENTS.md", "connaissance/../../secret.md", "archive/source.md"]:
            with self.subTest(path=path):
                self.assertEqual(self.request("/api/source?" + urlencode({"path": path}))[0], 403)
        for path in ["/.git/config", "/model-metadata.json", "/../AGENTS.md", "/connaissance/25-domaines-coeur-et-epreuve-recits.md"]:
            with self.subTest(path=path):
                self.assertEqual(self.request(path)[0], 404)
        self.assertEqual(self.request("/api/source?" + urlencode({"path": MAP_PATH, "anchor": "d01-stocks"}))[0], 200)

    def test_foreign_hosts_and_cross_origin_reads_are_rejected(self):
        self.assertEqual(self.request("/api/model", headers={"Host": "evil.example"})[0], 403)
        self.assertEqual(self.request("/api/model", headers={"Origin": "https://evil.example"})[0], 403)
        self.assertEqual(self.request("/api/model", headers={"Sec-Fetch-Site": "cross-site"})[0], 403)
        self.assertEqual(self.request("/api/model", method="POST")[0], 405)


if __name__ == "__main__":
    unittest.main()
