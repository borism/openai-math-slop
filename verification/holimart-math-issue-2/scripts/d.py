import cypari2,time,sys
pari=cypari2.Pari(); pari.allocatemem(3*10**9)
pari('default(realprecision,25)')
pari(r'''
fails(n,k,B)={my(E=ellinit([0,0,0,-n^2,0]),Ek=ellinit(elltwist(E,k)),S=factor(2*E.disc\2^12)[,1]~,S0=concat(S,factor(abs(k))[,1]~),t=0,f=0);
 forprime(p=3,B, if(setsearch(Set(S0),p)||kronecker(k,p)!=1,next); t++; if((ellap(Ek,p)-(p+1))%8,f++)); [ellrootno(E),t,f]};
''')
for n,k in [(5,-31),(6,-47),(7,-31),(13,-79),(31,-79)]:
    print(n,k,pari(f'fails({n},{k},3000)'),flush=True)
