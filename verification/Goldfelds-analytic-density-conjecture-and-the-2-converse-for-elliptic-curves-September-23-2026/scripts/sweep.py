# Congruent-number sweep: y^2 = x^3 - n^2 x, n in [2,59] with odd root number, k in a fixed list, p <= 2000.
# Writes one CSV row per (n,k): n,k,tested,fails
import cypari2,sys
pari=cypari2.Pari(); pari.allocatemem(10**9)
for src in [
 "S0of(n,k)={Set(concat([2],concat(factor(ellglobalred(ellinit([0,0,0,-n^2,0]))[1])[,1]~,factor(abs(k))[,1]~)))};",
 "fails(n,k,B)={my(E=ellinit([0,0,0,-n^2,0]),Ek=ellinit(elltwist(E,k)),S0=S0of(n,k),t=0,f=0);forprime(p=3,B,if(setsearch(S0,p)||kronecker(k,p)!=1,next);t++;if((ellap(Ek,p)-(p+1))%8,f++));[t,f]};",
]: pari(src)
print("n,k,tested,fails",flush=True)
tot=[0,0,0]
for n in range(2,60):
    if int(pari(f"ellrootno(ellinit([0,0,0,-{n}^2,0]))"))!=-1: continue
    for k in [-7,-15,-23,-31,-47,-71,-79,-103]:
        if int(pari(f"gcd({n}*2,{k})"))!=1: continue
        t,f=[int(x) for x in pari(f"fails({n},{k},2000)")]
        print(f"{n},{k},{t},{f}",flush=True); tot[0]+=1;tot[1]+=t;tot[2]+=f
print(f"# pairs={tot[0]} tested={tot[1]} fails={tot[2]} rate={tot[2]/tot[1]:.4f}",flush=True)
