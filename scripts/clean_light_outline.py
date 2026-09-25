#!/usr/bin/env python3
"""Remove exterior white-matte contamination, preserving enclosed white artwork.
Run once on the v1.0.0 source frames. No resizing or frame reordering.
"""
from pathlib import Path
from collections import deque
import json
import numpy as np
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]

def clean(image):
 a=np.array(image.convert('RGBA'));rgb=a[:,:,:3].astype(float);alpha=a[:,:,3]
 light=(rgb.min(axis=2)>150)&((rgb.max(axis=2)-rgb.min(axis=2))<40)
 traversable=(alpha==0)|light;outside=np.zeros(alpha.shape,bool);q=deque()
 h,w=alpha.shape
 for y,x in [(y,x) for y in range(h) for x in (0,w-1)]+[(y,x) for x in range(w) for y in (0,h-1)]:
  if traversable[y,x]:outside[y,x]=True;q.append((y,x))
 while q:
  y,x=q.popleft()
  for yy,xx in ((y-1,x),(y+1,x),(y,x-1),(y,x+1)):
   if 0<=yy<h and 0<=xx<w and traversable[yy,xx] and not outside[yy,xx]:outside[yy,xx]=True;q.append((yy,xx))
 # Only remove light exterior pixels beside the original dark brown outline.
 brown=(alpha>240)&(rgb[:,:,0]>rgb[:,:,1]*1.15)&(rgb[:,:,1]>rgb[:,:,2]*1.05)&(rgb.max(axis=2)<170)
 dist=np.full(alpha.shape,999.);idx=np.indices(alpha.shape)
 for dy in range(-3,4):
  for dx in range(-3,4):
   d=(dy*dy+dx*dx)**.5
   yy,xx=np.indices(alpha.shape);ny=np.clip(yy+dy,0,h-1);nx=np.clip(xx+dx,0,w-1)
   take=brown[ny,nx]&(d<dist);dist[take]=d;idx[0][take]=ny[take];idx[1][take]=nx[take]
 near_clear=np.zeros(alpha.shape,bool)
 yy,xx=np.indices(alpha.shape)
 for dy in range(-2,3):
  for dx in range(-2,3):
   if dx*dx+dy*dy<=4:near_clear|=alpha[np.clip(yy+dy,0,h-1),np.clip(xx+dx,0,w-1)]==0
 mask=outside&near_clear&light&(alpha>0)&(dist<=3)
 base=rgb[idx[0],idx[1]];v=255-base
 coverage=np.clip(((255-rgb)*v).sum(axis=2)/np.maximum((v*v).sum(axis=2),1),0,1)
 a[mask,:3]=base[mask].astype('uint8');a[mask,3]=np.rint(alpha[mask]*coverage[mask]).astype('uint8')
 a[a[:,:,3]==0]=0
 return Image.fromarray(a),int(mask.sum())

def main():
 counts={}
 for state in ('idle','waving'):
  for p in sorted((ROOT/'source/frames'/state).glob('*.png')):
   im=Image.open(p);out,n=clean(im);out.save(p);counts[str(p.relative_to(ROOT))]=n
 (ROOT/'qa/outline-cleanup.json').write_text(json.dumps({'method':'exterior white-matte alpha decontamination adjacent to brown outline','changed_pixels':counts,'geometry_and_timing':'unchanged','scope':['idle','waving']},indent=2)+'\n')
if __name__=='__main__':main()
