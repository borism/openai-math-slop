# usage: run2.py a b k Dmax  -- ratio test only for admissible squarefree D with omega>=2
import sys,time
from cypari import pari
pari.allocatemem(3*10**9); pari('default(realprecision,25)')
for s in [
 "mk(a,b)=ellinit(ellminimalmodel(ellinit([0,-(a+b),0,a*b,0])))",
 "S0of(E,k)=Set(concat([2],concat(factor(E.disc*0+ellglobalred(E)[1])[,1]~,factor(abs(k))[,1]~)))",
 "Lv(E,k)=lfun(lfuncreate(ellinit(elltwist(E,k))),1)",
 "adm(E,k,D)={my(S0=S0of(E,k),f=factor(D)[,1]);if(D%8!=1,return(0));for(i=1,#f,if(setsearch(S0,f[i])||kronecker(k,f[i])!=1,return(0)));for(i=1,#S0,my(q=S0[i]);if(q>2&&kronecker(D,q)!=1,return(0)));1}",
]: pari(s)
a,b,k,Dmax=map(int,sys.argv[1:5])
L0=pari(f"Lv(mk({a},{b}),{k})")
for D in range(2,Dmax+1):
    if not int(pari(f"issquarefree({D})&&omega({D})>=2&&adm(mk({a},{b}),{k},{D})")): continue
    t0=time.time()
    try:
        r=pari(f"sqrt({D})*Lv(mk({a},{b}),{k}*{D})/{L0}")
        rf=float(r); q=pari.bestappr(r,10**6); ok=abs(float(q)-rf)<1e-8
        v=int(pari.valuation(q,2)) if ok and float(q)!=0 else None
        print(json.dumps(dict(a=a,b=b,k=k,D=D,omega=int(pari.omega(D)),ratio=rf,rational=bool(ok),v2=v,secs=int(time.time()-t0))) if (json:=__import__("json")) else "",flush=True)
    except Exception as e:
        print("ERR",D,repr(e)[:200],flush=True)
