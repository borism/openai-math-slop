# Test the lemma's internal prediction: for allowed K-split p and a matched p' (same classes at S0, K-split),
# the proof's identity forces  a_p != p+1 (mod 8)  <=>  v(a(pp')) = omega = 2  (ratio valuation exactly 4).
import sys,cypari2,time
n,k,Pmax,Dmax,stack=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])
pari=cypari2.Pari(); pari.allocatemem(stack*10**9); pari('default(realprecision,25)')
pari(f"E=ellinit([0,0,0,-{n}^2,0]); Ek=ellinit(elltwist(E,{k})); L0=lfun(lfuncreate(Ek),1);")
S0=[int(x) for x in pari("Set(concat([2],concat(factor(ellglobalred(E)[1])[,1]~,factor(abs(%d))[,1]~)))"%k)]
odd=[q for q in S0 if q>2]
P=[int(p) for p in pari(f"select(p->kronecker({k},p)==1&&p>2,primes([2,{Pmax}]))") if int(p) not in S0]
def cls(p): return (p%8,int(pari(f'ellap(Ek,{p})'))%8)+tuple(int(pari.kronecker(p,q)) for q in odd)
t0=time.time()
for i,p in enumerate(P):
    ap=int(pari(f"ellap(Ek,{p})")); fail=(ap-(p+1))%8!=0
    for q in P[i+1:]:
        if cls(q)!=cls(p) or p*q>Dmax: continue
        D=p*q
        r=float(pari(f"sqrt({D})*lfun(lfuncreate(ellinit(elltwist(E,{k*D}))),1)/L0"))
        qq=pari.bestappr(r,10**6)
        ok=abs(float(qq)-r)<1e-7
        v=int(pari.valuation(qq,2)) if ok and float(qq)!=0 else 99
        print(f"p={p} q={q} D={D} a_p={ap} fail_mod8={fail} ratio={r:.6g} v2={v} {'EQUAL' if v==4 else 'strict'} {'CONSISTENT' if (v==4)==fail else 'VIOLATES-PREDICTION'} t={round(time.time()-t0)}",flush=True)
print("done")
