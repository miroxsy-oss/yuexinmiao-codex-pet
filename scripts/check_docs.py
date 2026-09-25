"""Check local documentation links and bilingual user-facing metadata."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
links = 0
documents = list(ROOT.rglob('*.md'))
for path in documents:
    text = path.read_text(encoding='utf-8')
    destinations = re.findall(r'\]\(([^)]+)\)', text)
    destinations += re.findall(r'(?:src|href)="([^"]+)"', text)
    for target in destinations:
        target = target.split('#')[0]
        if not target or re.match(r'^[a-z]+:', target):
            continue
        links += 1
        if not (path.parent / target).exists():
            errors.append(f'{path.relative_to(ROOT)}: missing file / 缺少文件: {target}')
    paragraphs = re.split(r'\n\s*\n', re.sub(r'```.*?```', '', text, flags=re.S))
    for index, paragraph in enumerate(paragraphs):
        if not re.search('[\u4e00-\u9fff]', paragraph) or re.search('[A-Za-z]{3}', paragraph):
            continue
        following = paragraphs[index + 1] if index + 1 < len(paragraphs) else ''
        if not re.search('[A-Za-z]{3}', following):
            errors.append(f'{path.relative_to(ROOT)}: review translation / 请复核译文: {paragraph[:100]}')
for path in (ROOT / 'dist').glob('*/pet.json'):
    description = json.loads(path.read_text(encoding='utf-8')).get('description', '')
    if not (re.search('[\u4e00-\u9fff]', description) and re.search('[A-Za-z]{3}', description)):
        errors.append(f'{path.relative_to(ROOT)}: bilingual description required / 描述需要中英对应')
print(json.dumps({'ok': not errors, 'documents': len(documents), 'local_file_links': links,
                  'errors': errors, 'scope': 'Structural lint, not a full translation review / 结构检查，不代替完整译审'}, ensure_ascii=False))
raise SystemExit(bool(errors))
