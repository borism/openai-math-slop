# usage: g.py select | g.py work <worker 0..3> <stack GB> <Dmax>
import sys,cypari2,time,json
pari=cypari2.Pari(); pari.allocatemem(int(sys.argv[3])*10**9 if sys.argv[1]=="work" else 10**9)
pari('default(realprecision,25)')
for src in [
 "mk(a,b)=ellinit(ellminimalmodel(ellinit([0,-(a+b),0,a*b,0])))",
 "S0of(E,k)=Set(concat([2],concat(factor(E.disc*0+ellglobalred(E)[1])[,1]~,factor(abs(k))[,1]~)))",
 "Lv(E,k)=lfun(lfuncreate(ellinit(elltwist(E,k))),1)",
 "adm(E,k,D)={my(S0=S0of(E,k),f=factor(D)[,1]);if(D%8!=1,return(0));for(i=1,#f,if(setsearch(S0,f[i])||kronecker(k,f[i])!=1,return(0)));for(i=1,#S0,my(q=S0[i]);if(q>2&&kronecker(D,q)!=1,return(0)));1}",
 "fails(E,k,B)={my(Ek=ellinit(elltwist(E,k)),S0=S0of(E,k),t=0,f=0);forprime(p=3,B,if(setsearch(S0,p)||kronecker(k,p)!=1,next);t++;if((ellap(Ek,p)-(p+1))%8,f++));[t,f]}",
]: pari(src)

def select():
    seen={};out=[]
    for a in range(-30,31):
        for b in range(a+1,31):
            if a==0 or b==0: continue
            E=pari(f"mk({a},{b})")
            N=int(pari.ellglobalred(E)[0])
            if N>3000 or int(pari.ellrootno(E))!=-1: continue
            j=str(pari(f'mk({a},{b}).j'))
            if (j,N) in seen: continue
            seen[(j,N)]=(a,b)
    items=sorted(seen.items(),key=lambda kv:kv[0][1])
    step=max(1,len(items)//12)
    chosen=items[::step][:12]
    pairs=[]
    for (j,N),(a,b) in chosen:
        E=pari(f"mk({a},{b})"); cnt=0
        for m in range(1,201):
            k=-m
            if m%8!=7 or not pari.issquarefree(m) or int(pari.gcd(m,2*N))!=1: continue   # k = 1 mod 8
            if any(int(pari.kronecker(k,q))!=1 for q in pari.factor(N)[0] if q>2): continue
            if int(pari.ellrootno(pari.ellinit(pari.elltwist(E,k))))!=1: continue
            if abs(pari('Lv')(E,k))<1e-8: continue
            pairs.append((a,b,N,k)); cnt+=1
            if cnt==2: break
    return pairs

if sys.argv[1]=="select":
    P=select(); json.dump(P,open("pairs.json","w")); print(len(P),P)
else:
    w=int(sys.argv[2]); Dmax=int(sys.argv[4]); P=json.load(open("pairs.json"))
    for idx,(a,b,N,k) in enumerate(P):
        if idx%4!=w: continue
        E=pari(f"mk({a},{b})")
        t,f=map(int,pari(f"fails(mk({a},{b}),{k},3000)"))
        L0=pari(f"Lv(mk({a},{b}),{k})"); wits=[];errs=0;nD=0
        for D in range(2,Dmax+1):
            if int(pari(f"issquarefree({D})&&omega({D})<=2&&adm(mk({a},{b}),{k},{D})"))==0: continue
            nD+=1
            try:
                r=float(pari(f"sqrt({D})*Lv(mk({a},{b}),{k}*{D})/{L0}"))
                q=pari.bestappr(r,10**6); qf=float(q)
                if abs(qf-r)<1e-8 and qf!=0 and int(pari.valuation(q,2))==2*int(pari.omega(D)): wits.append((D,str(q)))
            except Exception as e:
                errs+=1
        print(json.dumps(dict(a=a,b=b,N=N,k=k,tested=t,fails=f,admD=nD,errs=errs,witnesses=wits)),flush=True)
