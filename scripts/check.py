#!/usr/bin/env python3
"""Validate the package and compare decoded pixels with its source build."""
import hashlib,json,sys
from pathlib import Path
from PIL import Image,ImageChops,ImageStat
from build import ROOT,STATES,compose

errors=[];rows=[];checks={}
def check(name,ok):
    checks[name]=bool(ok)
    if not ok:errors.append(name)

pet=ROOT/'dist/yuexinmiao-selected';manifest=json.loads((pet/'pet.json').read_text())
check('manifest',all(isinstance(manifest.get(k),str) and manifest[k] for k in ['id','displayName','description','spritesheetPath']))
check('sprite_version',manifest.get('spriteVersionNumber',1)==1)
check('sprite_path',manifest.get('spritesheetPath')=='spritesheet.webp')
with Image.open(pet/'spritesheet.webp') as source:
    check('WEBP',source.format=='WEBP');check('RGBA',source.mode=='RGBA');check('1536x1872',source.size==(1536,1872));atlas=source.convert('RGBA')
check('transparent_RGB_zero',all(not any(p[:3]) for p in atlas.getdata() if p[3]==0))
check('rebuild_pixel_equal',atlas.tobytes()==compose().tobytes())
for row,(state,count) in enumerate(STATES):
    fs=[atlas.crop((c*192,row*208,(c+1)*192,(row+1)*208)) for c in range(8)]
    boxes=[f.getbbox() for f in fs[:count]]
    check(f'{state}: valid frames',all(boxes))
    check(f'{state}: unused cells transparent',all(f.getbbox() is None for f in fs[count:]))
    check(f'{state}: no cell edge clipping',all(b and b[0]>0 and b[1]>0 and b[2]<192 and b[3]<208 for b in boxes))
    hashes=[hashlib.sha256(f.tobytes()).hexdigest() for f in fs[:count]]
    check(f'{state}: animation changes',len(set(hashes))>1)
    diffs=[]
    for a,b in zip(fs[:count],fs[1:count]+fs[:1]):
        # Premultiplied appearance on black; numbers are evidence, not a perceptual pass/fail claim.
        aa=Image.new('RGB',a.size);aa.paste(a,mask=a.getchannel('A'));bb=Image.new('RGB',b.size);bb.paste(b,mask=b.getchannel('A'))
        diffs.append(round(sum(ImageStat.Stat(ImageChops.difference(aa,bb)).mean)/3,5))
    rows.append({'state':state,'frames':count,'unique_images':len(set(hashes)),'alpha_boxes':boxes,'successive_MAE_including_loop':diffs})
checksums={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(pet.glob('*')) if p.is_file()}
report={'ok':not errors,'automated_checks':checks,'errors':errors,'rows':rows,'checksums':checksums,'visual_findings':'视觉范围见 docs/SELF_CHECK.md；自动检查不等于视觉完美或再分发授权。 / See docs/SELF_CHECK.md for visual scope; automated success is not visual perfection or a redistribution license.'}
(ROOT/'qa/package-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ok':not errors,'checks':len(checks),'errors':errors},ensure_ascii=False));sys.exit(bool(errors))
