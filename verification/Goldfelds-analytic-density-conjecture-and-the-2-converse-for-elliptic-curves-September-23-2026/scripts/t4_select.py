import json
from cypari import pari
pari.allocatemem(10**9)
pari('mk(a,b)=ellinit(ellminimalmodel(ellinit([0,-(a+b),0,a*b,0])))')
seen={}
for a in range(-80,81):
  for b in range(a+1,81):
    if a==0 or b==0: continue
    E=pari(f"mk({a},{b})")
    N=int(pari.ellglobalred(E)[0])
    if N>6000: continue
    c=[int(x) for x in pari.elltors(E)[1]]
    if not (len(c)==2 and c[0]%4==0): continue
    if int(pari.ellrootno(E))!=-1: continue
    j=str(E[12]) if False else str(pari(f"mk({a},{b}).j"))
    if (j,N) in seen: continue
    seen[(j,N)]=(a,b,c)
items=sorted(seen.items(),key=lambda kv:kv[0][1])
print(len(items))
for (j,N),(a,b,c) in items[:40]: print(a,b,N,c)
json.dump([(a,b,N,c) for (j,N),(a,b,c) in items],open("curves.json","w"))
