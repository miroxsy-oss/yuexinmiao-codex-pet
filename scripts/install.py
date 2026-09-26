#!/usr/bin/env python3
"""Install the included pet; explicitly choose replace or keep-both on updates."""
import argparse,hashlib,json,os,shutil,sys,tempfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def require_real_directory(path):
    if path.is_symlink():
        raise ValueError('拒绝通过符号链接目录安装 / Refusing a symlink directory')
    if path.exists() and not path.is_dir():
        raise ValueError('安装路径不是目录 / Installation path is not a directory')

def install(home,existing=None):
    source=ROOT/'dist/yuexinmiao-selected'
    expected={}
    for line in (ROOT/'CHECKSUMS.sha256').read_text().splitlines():
        digest,name=line.split(None,1);expected[name.strip()]=digest
    payload={name:(source/name).read_bytes() for name in ['pet.json','spritesheet.webp']}
    for name,data in payload.items():
        if hashlib.sha256(data).hexdigest()!=expected[f'dist/yuexinmiao-selected/{name}']:
            raise ValueError(f'校验值不符 / Checksum mismatch: {name}')
    manifest=json.loads(payload['pet.json'])
    if manifest['id']!='yuexinmiao-selected' or manifest['spritesheetPath']!='spritesheet.webp':
        raise ValueError('安装配置无效 / Invalid package manifest')
    pets=home/'pets';target=pets/'yuexinmiao-selected'
    require_real_directory(pets)
    def same(path):
        return path.is_dir() and all((path/n).is_file() and (path/n).read_bytes()==data for n,data in payload.items())
    if target.is_symlink():raise ValueError('拒绝覆盖符号链接 / Refusing to replace a symlink')
    if same(target):
        print(f'Already installed / 已安装同一版本: {target}');return target
    if target.exists():
        if existing is None:
            if not sys.stdin.isatty():
                raise ValueError('检测到不同的旧版，尚未修改文件。请先确认：--existing replace 替换并备份；--existing keep-both 并存保留。 / Choose an existing-version policy before retrying.')
            print('发现不同的旧版月薪喵 / Existing version found:')
            print('  1. 替换旧版，自动保留回滚备份 / Replace with backup')
            print('  2. 保留旧版，新版另建条目 / Keep both')
            answer=input('请选择 1 或 2；其他输入取消 / Choose 1 or 2: ').strip()
            if answer not in ('1','2'):
                print('已取消，未修改文件 / Cancelled without changes');return None
            existing={'1':'replace','2':'keep-both'}[answer]
        if existing not in ('replace','keep-both'):raise ValueError('旧版处理选项无效 / Invalid existing-version policy')
        if existing=='keep-both':
            revision=hashlib.sha256(payload['spritesheet.webp']).hexdigest()[:8]
            manifest['id']=f'yuexinmiao-selected-{revision}'
            manifest['displayName']+=f'（独立副本 / Separate copy {revision}）'
            payload['pet.json']=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode()
            target=pets/manifest['id']
            if target.is_symlink():raise ValueError('拒绝覆盖符号链接 / Refusing to replace a symlink')
            if same(target):
                print(f'Already installed / 已有同一独立副本: {target}');return target
            if target.exists():raise ValueError(f'独立副本目录已存在且内容不同，未覆盖 / Conflicting copy: {target}')
    backup_parent=home/'pet-backups'
    if target.exists():require_real_directory(backup_parent)
    pets.mkdir(parents=True,exist_ok=True)
    staged=Path(tempfile.mkdtemp(prefix='.yuexinmiao-',dir=pets));backup=None
    try:
        for name,data in payload.items():(staged/name).write_bytes(data)
        if target.exists():
            parent=backup_parent;require_real_directory(parent);parent.mkdir(exist_ok=True)
            backup=parent/f'{target.name}-{time.time_ns()}';target.rename(backup)
        try:staged.rename(target)
        except Exception:
            if backup:backup.rename(target)
            raise
    finally:
        if staged.exists():shutil.rmtree(staged)
    print(f'Installed / 已安装: {target}')
    if backup:print(f'Previous version backed up / 旧版已移出宠物列表并备份: {backup}')
    print(f"在 Codex 中选择 / Select: {manifest['displayName']}；当前选中项未改变 / Existing selection is unchanged.")
    return target

if __name__=='__main__':
    p=argparse.ArgumentParser(description='安装月薪喵 Codex Pet / Install Yuexinmiao Codex Pet')
    p.add_argument('--codex-home',type=Path,default=Path(os.environ.get('CODEX_HOME',Path.home()/'.codex')),help='Codex 数据目录 / Codex data directory')
    p.add_argument('--existing',choices=['replace','keep-both'],help='用户确认旧版处理方式后使用 / Apply after the user chooses how to handle an existing version.')
    a=p.parse_args()
    try:install(a.codex_home.expanduser().resolve(),a.existing)
    except (ValueError,OSError) as error:p.exit(1,f'{error}\n')
