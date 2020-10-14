def falsaposicion(f,a,b,tol):
    error=10
    cont = 1
    while error>tol:
        fa=f(a)
        fb=f(b)
        p=b-((fb*(b-a))/(fb-fa))
        fp=f(p)
        if fp==0:
            p=raiz
            break
        elif fa*fp<0:
            b=p
        else:
            a=p
        raiz=p
        error=abs(fp)
        print(cont,"    |",a," | ",p," | ",b," | ",fp," | ",error)
        cont += 1
    print("Se encontró una raiz en: ",p)
print("iter"," | ","     a","            | ","         Xm","        | ","        b","          | ","         f(Xm)","        | ","         E")
import numpy as np
def f(x):
    return np.log((np.sin(x))**2+1)-1/2
a=0
b=1
tol=1e-7
falsaposicion(f,a,b,tol)

