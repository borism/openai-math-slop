import sys,cypari2,time
pari=cypari2.Pari(); pari.allocatemem(int(sys.argv[3])*10**9)
pari('default(realprecision,25)')
for src in ['S0of(n,k)={Set(concat([2],concat(factor(ellglobalred(ellinit([0,0,0,-n^2,0]))[1])[,1]~,factor(abs(k))[,1]~)))};', 'fails(n,k,B)={my(E=ellinit([0,0,0,-n^2,0]),Ek=ellinit(elltwist(E,k)),S0=S0of(n,k),t=0,f=0);\n forprime(p=3,B, if(setsearch(S0,p)||kronecker(k,p)!=1,next); t++; if((ellap(Ek,p)-(p+1))%8,f++)); [ellrootno(E),t,f]};', 'adm(n,k,D)={my(S0=S0of(n,k),f=factor(D)[,1]);\n if(D%8!=1,return(0)); for(i=1,#f,if(setsearch(S0,f[i])||kronecker(k,f[i])!=1,return(0)));\n for(i=1,#S0,my(q=S0[i]);if(q>2&&kronecker(D,q)!=1,return(0))); 1};', 'wit(n,k,Dmax)={my(L0=lfun(lfuncreate(ellinit(elltwist(ellinit([0,0,0,-n^2,0]),k))),1),res=List());\n for(D=2,Dmax, if(!issquarefree(D)||omega(D)>2||!adm(n,k,D),next);\n   my(r=sqrt(D)*lfun(lfuncreate(ellinit(elltwist(ellinit([0,0,0,-n^2,0]),k*D))),1)/L0, q=round(r)); \n   if(abs(r-q)<1e-8 && q!=0 && valuation(q,2)==2*omega(D), listput(res,[D,q])));\n Vec(res)};']:
    pari(src)

import sys
Dmax=int(sys.argv[1]); n,k=31,-79
pari(f"L0=lfun(lfuncreate(ellinit(elltwist(ellinit([0,0,0,-{n}^2,0]),{k}))),1)")
t0=time.time()
for D in range(2,Dmax+1):
    if int(pari(f"issquarefree({D})&&omega({D})<=2&&adm({n},{k},{D})"))==0: continue
    try:
        r=pari(f"sqrt({D})*lfun(lfuncreate(ellinit(elltwist(ellinit([0,0,0,-{n}^2,0]),{k}*{D}))),1)/L0")
        q=round(float(r))
        print(D,float(r),"WITNESS" if abs(float(r)-q)<1e-8 and q!=0 and pari(f"valuation({q},2)==2*omega({D})") else "",round(time.time()-t0),flush=True)
    except Exception as e:
        print(D,"ERR",str(e)[:60],flush=True)
print("done",flush=True)
