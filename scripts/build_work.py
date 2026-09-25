"""Rebuild the optional Work atlas without changing desktop art."""
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
source=Image.open(ROOT/'dist/yuexinmiao-selected/spritesheet.webp').convert('RGBA')
atlas=source.copy()
for col,src in enumerate([0,1,2,2,3,4]):
    atlas.paste(source.crop((src*192,4*208,(src+1)*192,5*208)),(col*192,8*208))
out=ROOT/'dist/yuexinmiao-work-fanning/spritesheet.webp'
atlas.save(out,lossless=True,quality=100,method=6,exact=True)
print(out)
