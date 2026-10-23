# usage: t4_run.py <idx into curves.json> <Dmax>  -- congruence check (p<=3000) and witness search, omega(D)<=3; reads curves.json from cwd
import sys,json,time
from cypari import pari
pari.allocatemem(2*10**9); pari('default(realprecision,25)')
for s in [
 "mk(a,b)=ellinit(ellminimalmodel(ellinit([0,-(a+b),0,a*b,0])))",
 "S0of(E,k)=Set(concat([2],concat(factor(E.disc*0+ellglobalred(E)[1])[,1]~,factor(abs(k))[,1]~)))",
 "Lv(E,k)=lfun(lfuncreate(ellinit(elltwist(E,k))),1)",
 "adm(E,k,D)={my(S0=S0of(E,k),f=factor(D)[,1]);if(D%8!=1,return(0));for(i=1,#f,if(setsearch(S0,f[i])||kronecker(k,f[i])!=1,return(0)));for(i=1,#S0,my(q=S0[i]);if(q>2&&kronecker(D,q)!=1,return(0)));1}",
 "fails(E,k,B)={my(Ek=ellinit(elltwist(E,k)),S0=S0of(E,k),t=0,f=0);forprime(p=3,B,if(setsearch(S0,p)||kronecker(k,p)!=1,next);t++;if((ellap(Ek,p)-(p+1))%8,f++));[t,f]}",
]: pari(s)
a,b,N,c=json.load(open("curves.json"))[int(sys.argv[1])]; Dmax=int(sys.argv[2])
E=pari(f"mk({a},{b})"); ks=[]
for m in range(1,400):
    k=-m
    if m%8!=7 or not pari.issquarefree(m) or int(pari.gcd(m,2*N))!=1: continue
    if any(int(pari.kronecker(k,q))!=1 for q in pari.factor(N)[0] if q>2): continue
    if int(pari.ellrootno(pari.ellinit(pari.elltwist(E,k))))!=1: continue
    if abs(pari('Lv')(E,k))<1e-8: continue
    ks.append(k)
    if len(ks)==2: break
for k in ks:
    t,f=map(int,pari(f"fails(mk({a},{b}),{k},3000)"))
    L0=pari(f"Lv(mk({a},{b}),{k})"); wits=[];errs=0;nD=0;t0=time.time()
    for D in range(2,Dmax+1):
        if int(pari(f"issquarefree({D})&&omega({D})<=3&&adm(mk({a},{b}),{k},{D})"))==0: continue
        nD+=1; print("D",a,b,k,D,flush=True)
        try:
            r=float(pari(f"sqrt({D})*Lv(mk({a},{b}),{k}*{D})/{L0}"))
            q=pari.bestappr(r,10**6); qf=float(q)
            print("  ratio",D,r,flush=True)
            if abs(qf-r)<1e-8 and qf!=0 and int(pari.valuation(q,2))==2*int(pari.omega(D)): wits.append((D,str(q)))
        except Exception as e: errs+=1
    print(json.dumps(dict(a=a,b=b,N=N,tors=c,k=k,tested=t,fails=f,admD=nD,errs=errs,witnesses=wits,secs=int(time.time()-t0))),flush=True)
