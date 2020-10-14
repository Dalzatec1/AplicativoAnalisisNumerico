import numpy as np

def secant(f,p0,p1,tol,n):
 error=10
 fp0=f(p0)
 fp1=f(p1)
 print("|",n,"      | "                  ,p0,"                        |"   ,fp0,   "    |                       |")
 n=n+1
 print("|",n,"      | "                  ,p1,"                          |"   ,fp1,   "    |                       |")
 while error>tol and n<100 :
  fp0=f(p0)
  fp1=f(p1)
  p=p1-(((fp1)*(p1-p0))/((fp1-fp0)))

  
  
  p0=p1
  p1=p
  error=abs((p0-p1))
  aux=f(p)
  n=n+1
  print("|",n,"      | "     ,p,"         |"   ,aux,   " |"     ,error,"     |")
 

def f(x):
 return np.log(((np.sin(x))**2)+1)-1/2
p0=0.5
p1=1
tol=1e-7
n=0
print("Iteración |     xi                       |   f(xi)                 |                 E     |")
secant(f,p0,p1,tol,n)
