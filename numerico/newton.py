import numpy as np
def newton(f,fp,p0,tol,n):
 error=10
 print("|",n,"      ||   ",p0,"                      ||",f(p0),"    ||                        |")
 while error>tol and n<100:
  a=f(p0)
  b=fp(p0)
  p=p0-(a/b)
  error=abs(p-p0)
  p0=p
  n=n+1
  print("|",n,"      ||   ",p,"       ||",a,"    ||  ",error,"|")


def f(x):
 return ((np.log(((np.sin(x))**2)+1))-1/2)
def fp(x):
 return 2*((((np.sin(x))**2)+1)**-1)*np.sin(x)*np.cos(x)
p0=0.5
tol=1e-7
n=0
print("|Iteración||     xi                       ||   f(xi)                 ||                 E     |")
newton(f,fp,p0,tol,n)