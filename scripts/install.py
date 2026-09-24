#!/usr/bin/env python3
"""Install the included pet without changing the user's active pet selection."""
import argparse,hashlib,json,os,shutil,tempfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def install(home):
    source=ROOT/'dist/yuexinmiao-selected'
    expected={}
    for line in (ROOT/'CHECKSUMS.sha256').read_text().splitlines():
        digest,name=line.split(None,1);expected[name.strip()]=digest
    for name in ['pet.json','spritesheet.webp']:
        rel=f'dist/yuexinmiao-selected/{name}';actual=hashlib.sha256((source/name).read_bytes()).hexdigest()
        if actual!=expected[rel]:raise ValueError(f'Checksum mismatch: {name}')
    manifest=json.loads((source/'pet.json').read_text())
    if manifest['id']!='yuexinmiao-selected' or manifest['spritesheetPath']!='spritesheet.webp':raise ValueError('Invalid package manifest')
    pets=home/'pets';pets.mkdir(parents=True,exist_ok=True);target=pets/'yuexinmiao-selected'
    if target.is_symlink():raise ValueError('Refusing to replace a symlink')
    if target.exists() and all((target/n).is_file() and (target/n).read_bytes()==(source/n).read_bytes() for n in ['pet.json','spritesheet.webp']):
        print(f'Already installed: {target}');return
    staged=Path(tempfile.mkdtemp(prefix='.yuexinmiao-',dir=pets));backup=None
    try:
        for name in ['pet.json','spritesheet.webp']:shutil.copy2(source/name,staged/name)
        if target.exists():
            parent=home/'pet-backups';parent.mkdir(exist_ok=True);backup=parent/f'yuexinmiao-selected-{time.time_ns()}';target.rename(backup)
        try:staged.rename(target)
        except Exception:
            if backup:backup.rename(target)
            raise
    finally:
        if staged.exists():shutil.rmtree(staged)
    print(f'Installed: {target}')
    if backup:print(f'Previous version backed up: {backup}')
    print('Select 月薪喵 · 自选组合 in the Codex pet picker. Existing selection is unchanged.')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--codex-home',type=Path,default=Path(os.environ.get('CODEX_HOME',Path.home()/'.codex')));a=p.parse_args();install(a.codex_home.expanduser().resolve())
