"""Check the shipped Work variant against approved desktop pixels and checksums."""
import hashlib
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
checks = {}
desktop = Image.open(ROOT / 'dist/yuexinmiao-selected/spritesheet.webp').convert('RGBA')
source = Image.open(ROOT / 'dist/yuexinmiao-work-fanning/spritesheet.webp')
work = source.convert('RGBA')
checks['format'] = source.format == 'WEBP' and source.mode == 'RGBA' and source.size == (1536, 1872)
checks['unchanged_other_rows'] = desktop.crop((0, 0, 1536, 1664)).tobytes() == work.crop((0, 0, 1536, 1664)).tobytes()
for col, original in enumerate([0, 1, 2, 2, 3, 4]):
    expected = desktop.crop((original * 192, 832, (original + 1) * 192, 1040))
    actual = work.crop((col * 192, 1664, (col + 1) * 192, 1872))
    checks[f'pixel_exact_slot_{col}'] = actual.tobytes() == expected.tobytes()
checks['unused_slots_transparent'] = work.crop((1152, 1664, 1536, 1872)).getchannel('A').getbbox() is None
manifest = json.loads((ROOT / 'dist/yuexinmiao-work-fanning/pet.json').read_text())
checks['manifest'] = manifest['spriteVersionNumber'] == 1 and manifest['spritesheetPath'] == 'spritesheet.webp' and manifest['id'] == 'yuexinmiao-work-fanning'
for line in (ROOT / 'CHECKSUMS.sha256').read_text().splitlines():
    digest, name = line.split(None, 1)
    checks[f'checksum:{name}'] = hashlib.sha256((ROOT / name.strip()).read_bytes()).hexdigest() == digest
report = {'ok': all(checks.values()), 'checks': checks, 'note': 'Frame repetition is deliberate; real-device evidence and untested states are documented in docs/MOBILE_WORK.md.'}
(ROOT / 'qa/work-package-check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'ok': report['ok'], 'checks': len(checks), 'failed': [k for k, v in checks.items() if not v]}))
raise SystemExit(0 if report['ok'] else 1)
