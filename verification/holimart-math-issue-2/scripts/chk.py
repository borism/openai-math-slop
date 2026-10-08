def primerange(a,b):
    return [n for n in range(max(a,2),b) if all(n%d for d in range(2,int(n**.5)+1))]
def ap(p,k):
    A=(-25*k*k)%p
    sq={}
    for y in range(p): sq[y*y%p]=sq.get(y*y%p,0)+1
    s=0
    for x in range(p):
        s+=sq.get((x**3+A*x)%p,0)
    return p-s   # a_p = p+1-#E = p - affine count
k=-31;t=f=0;w=[]
for p in primerange(3,3001):
    if p in(5,31) : continue
    if pow(k%p,(p-1)//2,p)!=1: continue
    a=ap(p,k);t+=1
    if (a-(p+1))%8: f+=1; w.append((p,a))
print(t,f,w[:8])
