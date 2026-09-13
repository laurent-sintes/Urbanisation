"""Refresh the current source index without importing or publishing a model."""
from datetime import date
from pathlib import Path

try:
    from .migrate_urbanism import source_records
    from .publish_release import activate_pointer
    from .validate_models import validate_sources
except ImportError:
    from migrate_urbanism import source_records
    from publish_release import activate_pointer
    from validate_models import validate_sources


def main():
    document = {'schema_version':'1.0.0', 'captured_at':date.today().isoformat(), 'records':source_records()}
    errors = validate_sources(document)
    if errors:
        raise ValueError('\n'.join(errors))
    path = Path(__file__).resolve().parents[1] / 'modeles/provenance/source-records.json'
    activate_pointer(path, document)
    print(f'Current source index refreshed: {len(document["records"])} records; frozen files unchanged.')


if __name__ == '__main__':
    main()
