def rmultiples(f,fp,fpp,x0,tol,n):
    x=x0
    f1=float(f(x))
    f2=float(fp(x))
    f3=float(fpp(x))
    p=x-((f1*f2)/((f2**2)-(f1*f3)))
    error=1
    g2=0
    cont=0
    while error>tol and cont<n:
        x=p
        f1=f(x)
        f2=fp(x)
        f3=fpp(x)
        g2=p
        p=g2-((f1*f2)/((f2**2)-(f1*f3)))
        error=abs(p-g2)
        cont+=1
        print(cont,p,f1,error)
print("Iter"," | ","X"," | ","f(X)"," | ","E")

import numpy as np
def f(x):
    return (np.exp(x))-x-1
def fp(x):
    return (np.exp(x))-1
def fpp(x):
    return  np.exp(x)
x0=1
tol=1e-7
n=100
rmultiples(f,fp,fpp,x0,tol,n)


