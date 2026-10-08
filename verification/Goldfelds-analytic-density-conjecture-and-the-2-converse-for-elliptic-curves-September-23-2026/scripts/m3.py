# Stricter matching: p' must have the same Frobenius data as p in Gal(Q(E[8])/Q)-visible invariants:
# p mod 8, a_p mod 8, 2-primary structure of E(F_p) truncated at 8 (E_k ~ E over F_p since k is a QR), Legendre symbols at odd S0 primes.
import sys,cypari2,time
n,k,pstart,Pmax,Dmax,stack,nmatch=[int(x) for x in sys.argv[1:8]]
pari=cypari2.Pari(); pari.allocatemem(stack*10**9); pari('default(realprecision,25)')
pari(f"E=ellinit([0,0,0,-{n}^2,0]); Ek=ellinit(elltwist(E,{k})); L0=lfun(lfuncreate(Ek),1);")
S0=[int(x) for x in pari("Set(concat([2],concat(factor(ellglobalred(E)[1])[,1]~,factor(abs(%d))[,1]~)))"%k)]
odd=[q for q in S0 if q>2]
def grp(p):
    g=[int(x) for x in pari(f"ellgroup(Ek,{p})")]
    return tuple(sorted(min(int(pari.valuation(x,2)),3) for x in g)+[0,0])[:2] if len(g)==2 else (min(int(pari.valuation(g[0],2)),3),0)
def cls(p): return (p%8,int(pari(f'ellap(Ek,{p})'))%8,grp(p))+tuple(int(pari.kronecker(p,q)) for q in odd)
def ok(p): return p not in S0 and p>2 and int(pari.kronecker(k,p))==1
P=[int(p) for p in pari(f"primes([3,{Pmax}])") if ok(int(p))]
t0=time.time()
for p in [int(x) for x in sys.argv[8:]]:
    c=cls(p); ap=int(pari(f"ellap(Ek,{p})")); fail=(ap-(p+1))%8!=0; m=0
    for q in P:
        if q==p or p*q>Dmax or cls(q)!=c: continue
        D=p*q
        r=float(pari(f"sqrt({D})*lfun(lfuncreate(ellinit(elltwist(E,{k*D}))),1)/L0"))
        qq=pari.bestappr(r,10**6); good=abs(float(qq)-r)<1e-7
        v=int(pari.valuation(qq,2)) if good and float(qq)!=0 else 99
        print(f"n={n} k={k} p={p} class={c} q={q} D={D} a_p={ap} fail_mod8={fail} v2={v} {'EQUAL' if v==4 else 'strict'} {'consistent' if (v==4) or not fail else 'VIOLATES'} t={round(time.time()-t0)}",flush=True)
        m+=1
        if m>=nmatch: break
    if m==0: print(f"p={p} class={c}: no matched p' with p*p'<={Dmax}",flush=True)
print("done")
