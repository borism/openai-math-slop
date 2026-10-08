# usage: g4.py <worker 0..3> <stackGB> <Dmax> ; reads pairs14.json; logs one line per admissible D
import sys,json,time,cypari2
w,stack,Dmax=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
pari=cypari2.Pari(); pari.allocatemem(stack*10**9); pari('default(realprecision,25)')
for src in [
 "mk(a,b)=ellinit(ellminimalmodel(ellinit([0,-(a+b),0,a*b,0])))",
 "S0of(E,k)=Set(concat([2],concat(factor(ellglobalred(E)[1])[,1]~,factor(abs(k))[,1]~)))",
 "Lv(E,k)=lfun(lfuncreate(ellinit(elltwist(E,k))),1)",
 "adm(E,k,D)={my(S0=S0of(E,k),f=factor(D)[,1]);if(D%8!=1,return(0));for(i=1,#f,if(setsearch(S0,f[i])||kronecker(k,f[i])!=1,return(0)));for(i=1,#S0,my(q=S0[i]);if(q>2&&kronecker(D,q)!=1,return(0)));1}",
]: pari(src)
P=json.load(open("pairs_todo.json"))
for idx,(a,b,N,k) in enumerate(P):
    pass
    t0=time.time(); pari(f"E=mk({a},{b}); L0=Lv(E,{k});")
    Ds=[D for D in range(2,Dmax+1) if int(pari(f"issquarefree({D})&&omega({D})<=3&&adm(E,{k},{D})"))]
    print(f"PAIR N={N} k={k} a={a} b={b} admissible_D={len(Ds)}",flush=True)
    found=[]
    for D in Ds:
        try:
            r=float(pari(f"sqrt({D})*Lv(E,{k}*{D})/L0")); q=pari.bestappr(r,10**6); qf=float(q)
            ok=abs(qf-r)<1e-7 and qf!=0
            v=int(pari.valuation(q,2)) if ok else 99
            om=int(pari.omega(D)); wit=(v==2*om)
            if wit: found.append(D)
            print(f"  N={N} k={k} D={D} omega={om} ratio={r:.6g} v2={v} {'WITNESS' if wit else ''} t={round(time.time()-t0)}",flush=True)
        except Exception as e:
            print(f"  N={N} k={k} D={D} ERR {str(e)[:50]}",flush=True)
    print(f"DONE N={N} k={k} witnesses={found} t={round(time.time()-t0)}",flush=True)
