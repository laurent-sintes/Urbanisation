"""Shared, process-safe publication/export/build lock; nested calls are allowed."""
from contextlib import contextmanager
from pathlib import Path
import os
import threading

_guard = threading.RLock()
_owners = {}


@contextmanager
def atlas_lock(root):
    key = str(Path(root).resolve())
    owner = threading.get_ident()
    with _guard:
        if key in _owners:
            if _owners[key][0] != owner:
                raise ValueError('Atlas is being published, exported or built; retry after completion.')
            _owners[key][1] += 1
        else:
            path = Path(key) / '.runtime/atlas.lock'
            path.parent.mkdir(parents=True, exist_ok=True)
            stream = path.open('a+b')
            if stream.seek(0, os.SEEK_END) == 0:
                stream.write(b'\0'); stream.flush()
            stream.seek(0)
            try:
                if os.name == 'nt':
                    import msvcrt
                    msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError as exc:
                stream.close()
                raise ValueError('Atlas is being published, exported or built; retry after completion.') from exc
            _owners[key] = [owner, 1, stream]
    try:
        yield
    finally:
        with _guard:
            _owners[key][1] -= 1
            if not _owners[key][1]:
                _owners.pop(key)[2].close()  # OS releases the lock, also on process exit.
