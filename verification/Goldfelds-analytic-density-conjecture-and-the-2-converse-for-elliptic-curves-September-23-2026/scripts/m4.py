# usage: m4.py <a> <b> <k> <Pmax> <Dmax> <stackGB>   general curve y^2=x(x-a)(x-b)... strict matching, tally v2 at D=pq by fail status
import sys,cypari2,time
a,b,k,Pmax,Dmax,stack=[int(x) for x in sys.argv[1:7]]
pari=cypari2.Pari(); pari.allocatemem(stack*10**9); pari('default(realprecision,25)')
pari(f"E=ellinit(ellminimalmodel(ellinit([0,-({a}+{b}),0,{a}*{b},0]))); Ek=ellinit(elltwist(E,{k})); L0=lfun(lfuncreate(Ek),1);")
S0=[int(x) for x in pari("Set(concat([2],concat(factor(ellglobalred(E)[1])[,1]~,factor(abs(%d))[,1]~)))"%k)]
odd=[q for q in S0 if q>2]
def grp(p):
    g=[int(x) for x in pari(f"ellgroup(Ek,{p})")]
    v=sorted(min(int(pari.valuation(x,2)),3) for x in g)
    while len(v)<2: v=[0]+v
    return tuple(v)
def cls(p): return (p%8,int(pari(f'ellap(Ek,{p})'))%8,grp(p))+tuple(int(pari.kronecker(p,q)) for q in odd)
P=[int(p) for p in pari(f"primes([3,{Pmax}])") if int(p) not in S0 and int(pari.kronecker(k,int(p)))==1]
C={p:cls(p) for p in P}
t0=time.time()
for i,p in enumerate(P):
    for q in P[i+1:]:
        if C[q]!=C[p] or p*q>Dmax: continue
        D=p*q; ap=int(pari(f"ellap(Ek,{p})")); fail=(ap-(p+1))%8!=0
        r=float(pari(f"sqrt({D})*lfun(lfuncreate(ellinit(elltwist(E,{k*D}))),1)/L0")); qq=pari.bestappr(r,10**6)
        ok=abs(float(qq)-r)<1e-7 and float(qq)!=0
        v=int(pari.valuation(qq,2)) if ok else 99
        print(f"curve=({a},{b}) k={k} N={int(pari.ellglobalred(pari('E'))[0])} p={p} q={q} D={D} fail={fail} v2={v} t={round(time.time()-t0)}",flush=True)
print("done",flush=True)
