"""Local, read-only HTTP server for FLOW Atlas (Python standard library only)."""

from __future__ import annotations

import argparse
import json
import os
import sys
from functools import partial
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

from atlas_data import (
    DEFAULT_SPACE, ModelError, REPOSITORY_ROOT, SCHEMA_VERSION, SourceAccessError,
    get_revision, load_model, load_panorama, read_source, catalog,
)

STATIC_FILES = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/index.html": ("index.html", "text/html; charset=utf-8"),
    "/app.js": ("app.js", "text/javascript; charset=utf-8"),
    "/model.js": ("model.js", "text/javascript; charset=utf-8"),
    "/styles.css": ("styles.css", "text/css; charset=utf-8"),
    "/icon.svg": ("icon.svg", "image/svg+xml"),
    "/exploration.json": ("exploration.json", "application/json; charset=utf-8"),
    "/manifest.webmanifest": ("manifest.webmanifest", "application/manifest+json"),
    "/app.webmanifest": ("app.webmanifest", "application/manifest+json"),
}
CSP = (
    "default-src 'self'; script-src 'self'; style-src 'self'; "
    "img-src 'self' data:; connect-src 'self'; font-src 'self'; "
    "object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'"
)


class AtlasHandler(BaseHTTPRequestHandler):
    server_version = "FLOWAtlas/1"
    sys_version = ""

    def __init__(self, *args, root=REPOSITORY_ROOT, **kwargs):
        self.root = Path(root).resolve()
        super().__init__(*args, **kwargs)

    def _send(self, status: int, body: bytes, content_type: str, head: bool = False):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Security-Policy", CSP)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Frame-Options", "DENY")
        self.end_headers()
        if not head:
            self.wfile.write(body)

    def _json(self, status: int, value: dict, head: bool = False):
        self._send(status, json.dumps(value, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8", head)

    def _error(self, status: int, message: str, head: bool = False):
        self._json(status, {"error": message, "status": status}, head)

    def _local_request(self) -> bool:
        # No permissive CORS, and reject DNS-rebinding hostnames before exposing
        # source contents. The server itself binds exclusively to loopback.
        authority = self.headers.get("Host", "")
        expected_port = self.server.server_address[1]
        if authority.lower() not in {f"127.0.0.1:{expected_port}", f"localhost:{expected_port}"}:
            return False
        origin = self.headers.get("Origin")
        if origin and origin not in {f"http://127.0.0.1:{expected_port}", f"http://localhost:{expected_port}"}:
            return False
        return self.headers.get("Sec-Fetch-Site", "") != "cross-site"

    def do_GET(self):
        self._dispatch()

    def do_HEAD(self):
        self._dispatch(head=True)

    def do_POST(self):
        self._error(405, "Cette application propose uniquement la lecture du modèle.")

    do_PUT = do_POST
    do_PATCH = do_POST
    do_DELETE = do_POST

    def _dispatch(self, head: bool = False):
        if not self._local_request():
            self._error(403, "Accès réservé à l’application locale.", head)
            return
        try:
            request = urlsplit(self.path)
            route = unquote(request.path, errors="strict")
            if route in {"/api/model", "/api/status"}:
                query = parse_qs(request.query, keep_blank_values=True, max_num_fields=3)
                if set(query) - {"space", "version"} or len(query.get("space", ["release"])) != 1 or len(query.get('version', [''])) != 1:
                    raise ValueError("Espace unique attendu.")
                space = query.get("space", ["release"])[0]
                version = query.get('version', [''])[0] or None
                if space != "release":
                    raise ModelError("Atlas affiche uniquement l’urbanisation publiée.")
            if route == "/api/model":
                self._json(200, load_model(self.root, space, version), head)
            elif route == '/api/releases':
                self._json(200, catalog(self.root/'modeles/release'), head)
            elif route == "/api/status":
                self._json(200, {
                    "appName": "FLOW Atlas", "schemaVersion": SCHEMA_VERSION,
                    "pid": os.getpid(), "repositoryRoot": str(self.root),
                    "revision": get_revision(self.root, space, version), "space": space,
                }, head)
            elif route == "/api/source":
                args = parse_qs(request.query, keep_blank_values=True, max_num_fields=4)
                if set(args) - {"path", "anchor"} or len(args.get("path", [])) != 1 or len(args.get("anchor", [""])) != 1:
                    self._error(400, "Une source path unique et une ancre facultative sont attendues.", head)
                    return
                self._json(200, read_source(args["path"][0], args.get("anchor", [""])[0], self.root), head)
            elif route in STATIC_FILES:
                filename, content_type = STATIC_FILES[route]
                app_dir = (self.root / "app").resolve()
                path = (app_dir / filename).resolve()
                if path.parent != app_dir:
                    raise SourceAccessError("Fichier statique non autorisé.")
                self._send(200, path.read_bytes(), content_type, head)
            else:
                self._error(404, "Ressource introuvable.", head)
        except SourceAccessError as exc:
            self._error(403, str(exc), head)
        except FileNotFoundError:
            self._error(404, "Source ou fichier de l’application introuvable.", head)
        except ModelError as exc:
            self._error(422, str(exc), head)
        except (ValueError, UnicodeError):
            self._error(400, "Requête invalide.", head)
        except (ConnectionError, BrokenPipeError):
            pass
        except OSError:
            self._error(500, "Lecture impossible. Vérifie la disponibilité des fichiers du projet.", head)

    def log_message(self, format, *args):
        # Avoid copying source query strings or terminal control characters into
        # logs. Status codes are enough to diagnose this small local server.
        status = args[1] if len(args) > 1 else ""
        print(f"FLOW Atlas {self.command} {status}", file=sys.stderr)


def create_server(port=8765, root=REPOSITORY_ROOT):
    return ThreadingHTTPServer(("127.0.0.1", port), partial(AtlasHandler, root=root))


def main(argv=None):
    parser = argparse.ArgumentParser(description="FLOW Atlas — explorateur local du modèle métier")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--check", action="store_true", help="Vérifier la lecture du modèle et quitter")
    args = parser.parse_args(argv)
    if not 1 <= args.port <= 65535:
        parser.error("Le port doit être compris entre 1 et 65535.")
    try:
        backlog = load_model()
    except (ModelError, OSError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    if args.check:
        try:
            model = load_model(space="release")
            panorama = load_panorama()
        except (ModelError, OSError) as exc:
            print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
            return 1
        print(json.dumps({
            "release": {"version": model["version"], "nodes": len(model["nodes"]), "capabilities": sum(n["kind"] == "capability" for n in model["nodes"])},
            "backlog": {"version": backlog["version"], "nodes": len(backlog["nodes"]), "capabilities": sum(n["kind"] == "capability" for n in backlog["nodes"])},
            "panorama_as_is": {"version": panorama["version"], "systems": len(panorama["panoramas"])},
            "warnings": model["warnings"],
        }, ensure_ascii=False))
        return 0
    try:
        server = create_server(args.port)
    except OSError as exc:
        print(f"Démarrage impossible sur le port {args.port} : {exc}", file=sys.stderr)
        return 1
    print(f"FLOW Atlas : http://127.0.0.1:{args.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
