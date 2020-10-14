def busqueda(f,x0,dx,n):
    xant=x0
    xact=xant+dx
    fant=f(xant)
    fact=f(xact)
    cont=1
    while cont<n:
        xant=xact
        xact=xant+dx
        fant=f(xant)
        fact=f(xact)
        
        if fant*fact<0:
            print("Hay una raiz de f en: ","[ ",xant," , ",xact," ]")
        cont+=1
import numpy as np
def f(x):
    return np.log((np.sin(x))**2+1)-1/2
x0=-3
dx=0.5
n=100
busqueda(f,x0,dx,n)