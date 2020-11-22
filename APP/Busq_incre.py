from tkinter import *
import numpy as np
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class B_I(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entradaF  = StringVar()
        self.entradaX  = StringVar()
        self.entradaD  = StringVar()
        self.entradaN  = StringVar()


        label = tk.Label(self, text="BUSQUEDA INCREMENTAL", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="2")
        label.pack()

        #FUNCION:
        label =tk.Label(self,text="f(x) : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=200)
        fdx=tk.Entry(self, textvariable=self.entradaF)
        fdx.place(x=200,y=215)

        #X0:
        label =tk.Label(self,text="X0 : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80, y=250)
        Xcero=tk.Entry(self, textvariable=self.entradaX)
        Xcero.place(x=200,y=265)

        #DX:
        label =tk.Label(self,text="DX : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=300)
        dx=tk.Entry(self, textvariable=self.entradaD)
        dx.place(x=200,y=315)

        #N:
        label =tk.Label(self,text="N : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=350)
        Vn=tk.Entry(self, textvariable=self.entradaN)
        Vn.place(x=200,y=365)

        button1 = tk.Button(self, text="SOLUCIONAR",
                            command=self.calcular,width="30",height="2",bg="gray25",fg="cyan2")

        button1.place(x=150,y=500)

    def calcular(self):
        var1=str(self.entradaF.get())
        var2=float(self.entradaX.get())
        var3=float(self.entradaD.get())
        var4=int(self.entradaN.get())
        busqueda(var1,var2,var3,var4)


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



    

