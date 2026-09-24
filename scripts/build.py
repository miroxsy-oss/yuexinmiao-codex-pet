#!/usr/bin/env python3
"""Build the v1 atlas from the approved, normalized source frames."""
import argparse
from pathlib import Path
from PIL import Image

STATES = [('idle',6),('running-right',8),('running-left',8),('waving',4),('jumping',5),('failed',8),('waiting',6),('running',6),('review',6)]
ROOT = Path(__file__).resolve().parents[1]

def clean(frame):
    frame=frame.convert('RGBA')
    frame.putdata([p if p[3] else (0,0,0,0) for p in frame.getdata()])
    return frame

def compose():
    atlas=Image.new('RGBA',(1536,1872))
    for row,(state,count) in enumerate(STATES):
        files=sorted((ROOT/'source/frames'/state).glob('*.png'))
        if len(files)!=count: raise ValueError(f'{state}: expected {count} frames, found {len(files)}')
        for col,path in enumerate(files):
            with Image.open(path) as source:
                if source.size!=(192,208):raise ValueError(f'{path.name}: invalid cell size')
                atlas.alpha_composite(source.convert('RGBA'),(col*192,row*208))
    return clean(atlas)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=ROOT/'dist/yuexinmiao-selected/spritesheet.webp');args=parser.parse_args()
    image=compose();args.output.parent.mkdir(parents=True,exist_ok=True)
    image.save(args.output,format='WEBP',lossless=True,quality=100,method=6,exact=True)
    print(f'Built {args.output}')

if __name__=='__main__':main()
