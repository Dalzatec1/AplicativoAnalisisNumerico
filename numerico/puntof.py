import numpy as np
def puntofijo(f,g,p0,tol,n):
 error=100
 p=g(p0)
 p1=f(p0)
 
 print("|",n,"         ||   ",p0,"||",p,"||",p1,"||         |")
 p0=p
 while error>=tol and n<100:
     
  p=g(p0)
  p1=f(p0)
  error=abs(p-p0)
 
  
  n=n+1
  print("|",n,"         |""|   ",p0,"||",p,"||",p1,"||",error,"|")
  p0=p
  
  

def g(x):
 return (np.log(((np.sin(x))**2)+1))-1/2
def f(x):
 return (np.log(((np.sin(x))**2)+1))-(1/2)-(x)
p0=-0.5

tol=1e-7
n=0
print("|  iteración ||       Xi                ||      g(xi)            ||     f(xi)          ||   E   |")

puntofijo(f,g,p0,tol,n)
