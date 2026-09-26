"""Publication isolation, provenance and integrity checks for methodology guides.

Run: python -m unittest discover -s app -p test_modeling_guide.py
"""

import contextlib
import hashlib
import http.client
import io
import json
from pathlib import Path
import shutil
import threading
import unittest
from unittest.mock import patch
import uuid

from modeling_guide import ModelingGuideError, REPOSITORY_ROOT, load_modeling_guide
from server import create_server
from scripts.structured_io import dumps, read


from scripts.git_history import read_bytes as artifact_bytes

CURRENT = "2026-09-16.2"
HISTORICAL = "2026-09-15.1"
FUTURE = "2026-09-19.1"


class GuideFixture(unittest.TestCase):
    def setUp(self):
        self.root = REPOSITORY_ROOT / "app" / ("guide-test-" + uuid.uuid4().hex)
        self.root.mkdir()
        self.addCleanup(self.cleanup_fixture)
        self.release = self.root / "modeles/release"
        self.release.mkdir(parents=True)
        self.folder = self.root / "modeles/modeling-guides"
        shutil.copytree(REPOSITORY_ROOT / "modeles/modeling-guides", self.folder)
        self.index_path = self.folder / "index.yaml"
        self.guide_path = self.folder / "versions/2026-09-18.1.yaml"
        self.add_publication(CURRENT, artifact_bytes(REPOSITORY_ROOT / "modeles/release" / CURRENT / "model.yaml"))
        self.add_publication(HISTORICAL)

    def cleanup_fixture(self):
        path = self.root.resolve()
        if path.parent != (REPOSITORY_ROOT / "app").resolve() or not path.name.startswith("guide-test-"):
            raise RuntimeError("Répertoire de test hors du projet.")
        shutil.rmtree(path)

    def write(self, path, value):
        path.write_text(dumps(value, path.suffix), encoding="utf-8")

    def add_publication(self, version, model_bytes=None, current=False):
        directory = self.release / version
        directory.mkdir()
        model_path = directory / "model.yaml"
        model_path.write_bytes(model_bytes or dumps({"version": version, "nodes": []}).encode("utf-8"))
        descriptor_path = self.release / ("publication-" + version + ".yaml")
        self.write(descriptor_path, {"version": version, "path": version + "/model.yaml",
                                     "sha256": hashlib.sha256(model_path.read_bytes()).hexdigest()})
        index_path = self.release / "index.json"
        index = read(index_path) if index_path.exists() else {"schema_version": "1.0.0", "current": descriptor_path.name, "publications": []}
        index["publications"].append({"descriptor": descriptor_path.name, "sha256": hashlib.sha256(descriptor_path.read_bytes()).hexdigest()})
        if current:
            index["current"] = descriptor_path.name
        self.write(index_path, index)

    def rewrite_guide(self, guide):
        self.write(self.guide_path, guide)
        index = read(self.index_path)
        index["guides"][0]["sha256"] = hashlib.sha256(self.guide_path.read_bytes()).hexdigest()
        self.write(self.index_path, index)


class ModelingGuideTests(GuideFixture):
    def test_methodology_glossary_is_frozen_and_validated(self):
        guide = read(self.guide_path)
        guide['glossary'] = {'terms': [{'id': 'MOD001', 'name': 'Capability', 'definition': 'Aptitude durable.', 'examples': ['Exemple métier.']}], 'model_term_ids': ['TER001']}
        self.rewrite_guide(guide)
        self.assertEqual(load_modeling_guide(self.root)['guide']['glossary'], guide['glossary'])
        guide['glossary']['terms'].append(guide['glossary']['terms'][0])
        self.rewrite_guide(guide)
        with self.assertRaises(ModelingGuideError):
            load_modeling_guide(self.root)

    def test_invalid_lexical_partition_is_rejected(self):
        for ids in (['TER001', 'TER001'], ['BHV001'], [None]):
            with self.subTest(ids=ids):
                guide = read(self.guide_path)
                guide['glossary'] = {'terms': [], 'model_term_ids': ids}
                self.rewrite_guide(guide)
                with self.assertRaises(ModelingGuideError):
                    load_modeling_guide(self.root)

    def test_explicit_and_current_publication_use_the_same_association(self):
        result = load_modeling_guide(self.root)
        self.assertEqual(result, load_modeling_guide(self.root, CURRENT))
        self.assertEqual(result["status"], "available")
        self.assertEqual(result["association"]["scope"], "retrospective_methodology")
        self.assertEqual(len(result["guide"]["lessons"]), 6)
        self.assertEqual(result["guide"]["editorial_status"], "proposed_wording")

    def test_known_history_and_new_current_have_no_implicit_guide(self):
        historical = load_modeling_guide(self.root, HISTORICAL)
        self.assertEqual(historical["status"], "unavailable")
        self.assertNotIn("guide", historical)
        self.add_publication(FUTURE, current=True)
        self.assertEqual(load_modeling_guide(self.root)["publication_version"], FUTURE)
        self.assertEqual(load_modeling_guide(self.root)["status"], "unavailable")
        self.assertEqual(load_modeling_guide(self.root, CURRENT)["status"], "available")

    def test_unknown_or_invalid_publication_does_not_fall_back(self):
        with self.assertRaises(ModelingGuideError):
            load_modeling_guide(self.root, FUTURE)
        for version in ("", "../backlog/model.yaml", "v007", "2026-09-16.2/", "2026-09-16.0"):
            with self.subTest(version=version), self.assertRaises(ValueError):
                load_modeling_guide(self.root, version)

    def test_no_backlog_or_live_source_reads(self):
        original = Path.open
        opened = []

        def confined(path, *args, **kwargs):
            opened.append(path)
            relative = path.relative_to(self.root).as_posix()
            self.assertTrue(relative.startswith(("modeles/release/", "modeles/modeling-guides/")), relative)
            return original(path, *args, **kwargs)

        with patch.object(Path, "open", confined):
            result = load_modeling_guide(self.root)
        self.assertTrue(opened)
        source = next(item for item in result["guide"]["sources"] if item["id"] == "U322")
        self.assertIn("complètement décorrélé", source["excerpt"])
        self.assertFalse((self.root / "modeles/backlog").exists())
        self.assertFalse((self.root / "connaissance").exists())

    def test_missing_index_is_unavailable_but_missing_associated_guide_fails(self):
        self.guide_path.unlink()
        with self.assertRaises(ModelingGuideError):
            load_modeling_guide(self.root)
        self.index_path.unlink()
        self.assertEqual(load_modeling_guide(self.root)["status"], "unavailable")

    def test_tampering_with_frozen_guide_is_detected(self):
        self.guide_path.write_bytes(self.guide_path.read_bytes() + b"\n# changed\n")
        with self.assertRaisesRegex(ModelingGuideError, "empreinte"):
            load_modeling_guide(self.root)

    def test_publication_integrity_is_checked_before_reading_guide(self):
        snapshot = self.release / CURRENT / "model.yaml"
        snapshot.write_bytes(snapshot.read_bytes() + b"\n# changed\n")
        with self.assertRaisesRegex(ModelingGuideError, "Publication"):
            load_modeling_guide(self.root)

    def test_paths_cannot_escape_or_read_backlog(self):
        for invalid in ("../backlog/model.yaml", "/private.yaml", "versions/../../backlog/model.yaml", "versions\\2026-09-18.1.yaml", "versions/other.yaml"):
            with self.subTest(path=invalid):
                index = read(self.index_path)
                index["guides"][0]["path"] = invalid
                self.write(self.index_path, index)
                with self.assertRaisesRegex(ModelingGuideError, "Chemin"):
                    load_modeling_guide(self.root)

    def test_symlinked_guide_cannot_be_read_even_with_a_matching_hash(self):
        target = self.folder / "copy.yaml"
        target.write_bytes(self.guide_path.read_bytes())
        self.guide_path.unlink()
        try:
            self.guide_path.symlink_to(target)
        except OSError:
            self.skipTest("Création de liens symboliques non autorisée par Windows.")
        with self.assertRaisesRegex(ModelingGuideError, "Chemin"):
            load_modeling_guide(self.root)

    def test_resolved_guide_path_must_equal_its_declared_path(self):
        original = Path.resolve

        def redirected(path, *args, **kwargs):
            if path == self.guide_path:
                return self.root / "outside.yaml"
            return original(path, *args, **kwargs)

        # Also exercises junction/symlink rejection on hosts where creating a
        # real filesystem link requires a Windows privilege unavailable in CI.
        with patch.object(Path, "resolve", redirected):
            with self.assertRaisesRegex(ModelingGuideError, "Chemin"):
                load_modeling_guide(self.root)

    def test_duplicate_associations_are_rejected(self):
        index = read(self.index_path)
        index["associations"].append(dict(index["associations"][0]))
        self.write(self.index_path, index)
        with self.assertRaises(ModelingGuideError):
            load_modeling_guide(self.root)

    def test_verified_hash_does_not_allow_wrong_version_or_unresolved_sources(self):
        baseline = read(self.guide_path)
        for field in ("version", "source_refs"):
            with self.subTest(field=field):
                guide = dict(baseline)
                guide[field] = "2099-01-01.1" if field == "version" else ["MISSING"]
                self.rewrite_guide(guide)
                with self.assertRaises(ModelingGuideError):
                    load_modeling_guide(self.root)

    def test_solution_examples_support_shared_and_distributed_realization(self):
        scene = load_modeling_guide(self.root)["guide"]["lessons"][0]["scene"]
        self.assertEqual(len(scene["items"]), 2)
        variants = {item["id"]: item for item in scene["variants"]}
        self.assertEqual(variants["shared"]["realizations"][0]["capability_indexes"], [0, 1])
        for capability in (0, 1):
            self.assertGreater(sum(capability in item["capability_indexes"] for item in variants["distributed"]["realizations"]), 1)
        guide = read(self.guide_path)
        guide["lessons"][0]["scene"]["variants"][0]["realizations"][0]["capability_indexes"] = [999]
        self.rewrite_guide(guide)
        with self.assertRaises(ModelingGuideError):
            load_modeling_guide(self.root)


class ModelingGuideHttpTests(GuideFixture):
    def setUp(self):
        super().setUp()
        from scripts.export_atlas import export_atlas
        export_atlas(self.root, [self.root / 'app/dist/data'])
        self.server = create_server(0, self.root)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.close_server)

    def close_server(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=5)

    def request(self, path, method="GET"):
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=10)
        try:
            with contextlib.redirect_stderr(io.StringIO()):
                connection.request(method, path)
                response = connection.getresponse()
                return response.status, dict(response.getheaders()), response.read()
        finally:
            connection.close()

    def test_get_head_and_unassociated_publication(self):
        status, headers, payload = self.request("/data/" + CURRENT + "/guide.json")
        self.assertEqual(status, 200)
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertEqual(json.loads(payload)["publication_version"], CURRENT)
        status, head_headers, body = self.request("/data/" + CURRENT + "/guide.json", "HEAD")
        self.assertEqual(status, 200)
        self.assertEqual(body, b"")
        self.assertEqual(head_headers["Content-Length"], str(len(payload)))
        status, _, payload = self.request("/data/" + HISTORICAL + "/guide.json")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(payload)["status"], "unavailable")
        self.assertEqual(self.request("/data/" + FUTURE + "/guide.json")[0], 404)

    def test_query_is_strictly_single_version(self):
        for query in ("version=", "version=" + CURRENT + "&version=" + CURRENT,
                      "space=backlog", "version=../backlog/model.yaml", "unused=1", "version=v007"):
            with self.subTest(query=query):
                self.assertEqual(self.request("/api/modeling-guide?" + query)[0], 404)

    def test_corrupt_source_blocks_export_without_damaging_served_snapshot(self):
        from scripts.export_atlas import export_atlas
        before = self.request('/data/' + CURRENT + '/guide.json')[2]
        self.guide_path.write_bytes(b'corrupt')
        with self.assertRaises(ValueError):
            export_atlas(self.root, [self.root / 'app/dist/data'])
        self.assertEqual(self.request('/data/' + CURRENT + '/guide.json')[2], before)
        self.assertEqual(self.request('/data/' + CURRENT + '/model.json')[0], 200)


if __name__ == "__main__":
    unittest.main()
