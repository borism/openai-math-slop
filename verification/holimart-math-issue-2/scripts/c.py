import cypari2
pari=cypari2.Pari(); pari.allocatemem(2*10**9)
pari('default(realprecision,30)')
pari(r'''
Lv(n,k)={my(E=ellinit(elltwist(ellinit([0,0,0,-n^2,0]),k)));lfun(lfuncreate(E),1)};
''')
# D=329 witness
print(pari('Lv(5,-31)'), pari('sqrt(329)*Lv(5,-31*329)/Lv(5,-31)'))
print(pari('sqrt(329)*Lv(5,-31*329)/Lv(5,-31)-16'))
