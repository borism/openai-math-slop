import cypari2,time,sys
pari=cypari2.Pari(); pari.allocatemem(3*10**9)
pari('default(realprecision,25)')
for src in ['S0of(n,k)={Set(concat([2],concat(factor(ellglobalred(ellinit([0,0,0,-n^2,0]))[1])[,1]~,factor(abs(k))[,1]~)))};', 'fails(n,k,B)={my(E=ellinit([0,0,0,-n^2,0]),Ek=ellinit(elltwist(E,k)),S0=S0of(n,k),t=0,f=0);\n forprime(p=3,B, if(setsearch(S0,p)||kronecker(k,p)!=1,next); t++; if((ellap(Ek,p)-(p+1))%8,f++)); [ellrootno(E),t,f]};', 'adm(n,k,D)={my(S0=S0of(n,k),f=factor(D)[,1]);\n if(D%8!=1,return(0)); for(i=1,#f,if(setsearch(S0,f[i])||kronecker(k,f[i])!=1,return(0)));\n for(i=1,#S0,my(q=S0[i]);if(q>2&&kronecker(D,q)!=1,return(0))); 1};', 'wit(n,k,Dmax)={my(L0=lfun(lfuncreate(ellinit(elltwist(ellinit([0,0,0,-n^2,0]),k))),1),res=List());\n for(D=2,Dmax, if(!issquarefree(D)||omega(D)>2||!adm(n,k,D),next);\n   my(r=sqrt(D)*lfun(lfuncreate(ellinit(elltwist(ellinit([0,0,0,-n^2,0]),k*D))),1)/L0, q=round(r)); \n   if(abs(r-q)<1e-8 && q!=0 && valuation(q,2)==2*omega(D), listput(res,[D,q])));\n Vec(res)};']:
    pari(src)

import sys
if sys.argv[2]=="sweep":
    tot=[0,0,0]
    for n in range(2,60):
        if int(pari(f"ellrootno(ellinit([0,0,0,-{n}^2,0]))"))!=-1: continue
        for k in [-7,-15,-23,-31,-47,-71,-79,-103]:
            if int(pari(f"gcd({n}*2,{k})"))!=1: continue
            r=pari(f"fails({n},{k},2000)"); t,f=int(r[1]),int(r[2])
            tot[0]+=1;tot[1]+=t;tot[2]+=f
            if f==0: print("ZERO FAILS",n,k,t)
    print("pairs,tested,fails",tot, tot[2]/tot[1])
else:
    for n,k in [(6,-47),(7,-31),(13,-79),(31,-79)]:
        t=time.time(); print('witness',n,k,pari(f'wit({n},{k},{int(sys.argv[1])})'),round(time.time()-t),'s',flush=True)
