#!/usr/bin/env python3
"""Remove exterior white-matte contamination, preserving enclosed white artwork.
Run once on the v1.0.0 source frames. No resizing or frame reordering.
"""
from pathlib import Path
from collections import deque
import json
import numpy as np
from PIL import Image, ImageFilter
ROOT=Path(__file__).resolve().parents[1]

def clean(image):
 a=np.array(image.convert('RGBA'));rgb=a[:,:,:3].astype(float);alpha=a[:,:,3]
 light=(rgb.min(axis=2)>85)&((rgb.max(axis=2)-rgb.min(axis=2))<70)
 traversable=(alpha==0)|light;outside=np.zeros(alpha.shape,bool);q=deque()
 h,w=alpha.shape
 for y,x in [(y,x) for y in range(h) for x in (0,w-1)]+[(y,x) for x in range(w) for y in (0,h-1)]:
  if traversable[y,x]:outside[y,x]=True;q.append((y,x))
 while q:
  y,x=q.popleft()
  for yy,xx in ((y-1,x),(y+1,x),(y,x-1),(y,x+1)):
   if 0<=yy<h and 0<=xx<w and traversable[yy,xx] and not outside[yy,xx]:outside[yy,xx]=True;q.append((yy,xx))
 # Only remove light exterior pixels beside the original dark brown outline.
 brown=(alpha>240)&(rgb[:,:,0]>rgb[:,:,1]*1.15)&(rgb[:,:,1]>rgb[:,:,2]*1.05)&(rgb[:,:,0]<125)&(rgb[:,:,1]<85)&(rgb[:,:,2]<70)
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
   if dx*dx+dy*dy<=4:near_clear|=alpha[np.clip(yy+dy,0,h-1),np.clip(xx+dx,0,w-1)]<16
 mask=near_clear&(alpha>0)&(dist<=3)
 base=rgb[idx[0],idx[1]];v=255-base
 coverage=np.clip(((255-rgb)*v).sum(axis=2)/np.maximum((v*v).sum(axis=2),1),0,1)
 mask &= (rgb.mean(axis=2)>base.mean(axis=2)+12)
 a[mask,:3]=base[mask].astype('uint8');a[mask,3]=np.rint(alpha[mask]*coverage[mask]).astype('uint8')
 a[a[:,:,3]<16]=0
 # Remove ringing within the exterior brown ink band; do not blur interiors.
 r=a[:,:,:3].astype(float);al=a[:,:,3].copy();ai=Image.fromarray(al)
 band=np.array(ai.filter(ImageFilter.MinFilter(7)))<16
 brownish=(r[:,:,0]>r[:,:,1]*1.18)&(r[:,:,1]>r[:,:,2]*1.05)&(r[:,:,0]<165)
 ink_mask=band&(al>0)&brownish
 # Reference ink sampled from the approved nose-covering/fanning outline.
 a[ink_mask,:3]=[98,55,42]
 # Correct isolated pale pinholes along the outer contour, not the white body.
 adjacent=np.array(Image.fromarray((ink_mask*255).astype('uint8')).filter(ImageFilter.MaxFilter(3)))>0
 outer=np.array(ai.filter(ImageFilter.MinFilter(3)))<16
 pale=outer&adjacent&(al>0)&(~brownish)&(r.max(axis=2)-r.min(axis=2)<80)
 # Preserve the intentionally open, straight white bottom of the greeting art.
 ys=np.nonzero(al>0)[0]
 if len(ys):pale[max(0,int(ys.max())-1):]=False
 a[pale,:3]=[98,55,42]
 smooth=np.array(ai.filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.GaussianBlur(.35)))
 boundary=np.array(ai.filter(ImageFilter.MinFilter(3)))<240
 a[boundary,3]=smooth[boundary]
 added=(a[:,:,3]>0)&(al==0)
 a[added,:3]=[98,55,42]
 a[a[:,:,3]<8]=0
 # Isolated pale flecks in the outer two-pixel band belong to the dirty matte.
 # Replace their contaminated RGB with existing outline ink, preserving alpha.
 aa=Image.fromarray(a[:,:,3]);rr=a[:,:,:3].astype(float)
 rim=np.array(aa.filter(ImageFilter.MinFilter(5)))<32
 ink=(rr[:,:,0]>rr[:,:,1]*1.18)&(rr[:,:,0]<155)&(a[:,:,3]>128)
 near_ink=np.array(Image.fromarray((ink*255).astype('uint8')).filter(ImageFilter.MaxFilter(5)))>0
 flecks=rim&near_ink&(a[:,:,3]>24)&(rr.mean(axis=2)>115)
 # Detect and protect the intentionally open white bottom of the waving frame.
 bottom=int(np.nonzero(a[:,:,3]>0)[0].max())
 bottom_white=(rr[bottom-2].min(axis=1)>220)&(a[bottom-2,:,3]>128)
 if bottom_white.sum()>20:flecks[bottom-6:]=False
 a[flecks,:3]=[98,55,42]
 # Remove tiny, disconnected warm/light islands trapped inside the edge ink.
 rr=a[:,:,:3].astype(float)
 bright=(rr.mean(axis=2)>140)&(a[:,:,3]>24)
 edge4=np.array(Image.fromarray(a[:,:,3]).filter(ImageFilter.MinFilter(9)))<32
 seen=np.zeros(bright.shape,bool)
 for sy,sx in zip(*np.nonzero(bright)):
  if seen[sy,sx]:continue
  q=deque([(int(sy),int(sx))]);seen[sy,sx]=True;component=[]
  while q:
   cy,cx=q.popleft();component.append((cy,cx))
   for ny,nx in ((cy-1,cx),(cy+1,cx),(cy,cx-1),(cy,cx+1)):
    if 0<=ny<h and 0<=nx<w and bright[ny,nx] and not seen[ny,nx]:seen[ny,nx]=True;q.append((ny,nx))
  if len(component)<=12 and all(edge4[cy,cx] and rr[cy,cx,0]>=rr[cy,cx,1]>=rr[cy,cx,2] for cy,cx in component):
   for cy,cx in component:a[cy,cx,:3]=[98,55,42]
 return Image.fromarray(a),int(np.any(a!=np.array(image.convert('RGBA')),axis=2).sum())

def main():
 counts={}
 for state in ('idle','waving'):
  for p in sorted((ROOT/'source/frames'/state).glob('*.png')):
   im=Image.open(p);out,n=clean(im);out.save(p);counts[str(p.relative_to(ROOT))]=n
 (ROOT/'qa/outline-cleanup.json').write_text(json.dumps({'method':'r3: white-matte decontamination; boundary-local ink de-ringing and alpha antialias; interior pixels preserved','changed_pixels':counts,'geometry_and_timing':'canvas, registration, frame order and timing unchanged; silhouette antialias locally refined','scope':['idle','waving']},indent=2)+'\n')
if __name__=='__main__':main()
