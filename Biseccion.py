def bisec(f,a,b,tol,n):
    cont = 1
    error=-1
    while cont<n:
        if (error < tol and error != -1):
            break
        p1=(a+b)/2
        fa=f(a)
        fp1=f(p1)
        if fp1==0:
            p1=raiz
            break
        elif fa*fp1<0:
            b=p1
        else:
            a=p1
        raiz=p1
        error=abs(fp1)
        print(cont," | ",a," | ",p1," | ",b," | ",fp1," | ",error," | ")
        cont += 1
    print("Se encontró una raiz en: ",p1)
print("iter"," | ","a"," | ","Xm"," | ","b"," | ","f(Xm)"," | ","E")
import numpy as np
def f(x):
    return np.log((np.sin(x))**2+1)-1/2
a=0
b=1
tol=1e-7
n=100
bisec(f,a,b,tol,n)
