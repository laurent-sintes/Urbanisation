"""Extract the two original PPTX images without editing their pixels."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('template', type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parent
assets = root / 'assets'
assets.mkdir(exist_ok=True)
source = args.template.read_bytes()
media = []
with ZipFile(args.template) as archive:
    for entry, filename, label in [
        ('ppt/media/image1.png', 'beaumanoir-original.png', 'Groupe Beaumanoir'),
        ('ppt/media/image2.png', 'flow-original.png', 'FLOW, avec sa signature'),
    ]:
        data = archive.read(entry)
        (assets / filename).write_bytes(data)
        media.append({'name': label, 'file': 'assets/' + filename, 'pptx_entry': entry,
                      'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                      'processing': 'Exact embedded PNG bytes; no image transformation.'})
manifest = {
    'source': {'name': args.template.name, 'bytes': len(source), 'sha256': hashlib.sha256(source).hexdigest()},
    'assets': media,
    'note': 'User-provided graphic reference U207. No business-model authority or design adoption.',
}
(root / 'assets-provenance.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(manifest, ensure_ascii=False, indent=2))
