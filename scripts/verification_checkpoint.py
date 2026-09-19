"""Local acceleration of a successful audit; never a publication approval.

Every reuse hashes all inputs, generated outputs and verifier code. Missing,
changed or malformed checkpoints fall back to the complete verifier. A full run
only records success when its inputs stayed unchanged while it was running.
"""
from hashlib import sha256
import json
from pathlib import Path
import platform
import sys


def fingerprint(paths):
    return {str(p.resolve()): sha256(p.read_bytes()).hexdigest()
            for p in sorted(set(map(Path, paths))) if p.is_file()}


def run(checkpoint, paths, action, outputs, *, full=False, runtime=''):
    checkpoint = Path(checkpoint)
    environment = [sys.version, platform.platform(), sys.flags.optimize, runtime]
    before = fingerprint(paths())
    if not full and checkpoint.is_file():
        try:
            saved = json.loads(checkpoint.read_text(encoding='utf-8'))
            if (saved['format'] == 1 and saved['environment'] == environment
                    and saved['fingerprint'] == before and saved['result']['status'] == 'passed'):
                return saved['result'], True
        except (OSError, ValueError, KeyError, TypeError):
            pass
    checkpoint.unlink(missing_ok=True)
    result = action()  # Failures propagate; no success checkpoint is retained.
    if result.get('status') != 'passed':
        raise ValueError('Verifier did not report success')
    after = fingerprint(paths())
    allowed = {str(Path(p).resolve()) for p in outputs}
    changed = {p for p in before.keys() | after.keys() if before.get(p) != after.get(p)}
    if changed - allowed:
        raise ValueError('Audit inputs changed during verification; rerun before caching')
    checkpoint.parent.mkdir(parents=True, exist_ok=True)
    # An interrupted write is harmless: a malformed cache forces revalidation.
    checkpoint.write_text(json.dumps({'format': 1, 'environment': environment,
        'fingerprint': after, 'result': result}, ensure_ascii=False), encoding='utf-8')
    return result, False
