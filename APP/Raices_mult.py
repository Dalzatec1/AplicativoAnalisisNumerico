from tkinter import *
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class R_M(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entradaF  = StringVar()
        self.entradaF1  = StringVar()
        self.entradaF2 = StringVar()
        self.entradaX = StringVar()
        self.entradaT  = StringVar()
        self.entradaN  = StringVar()

        label = tk.Label(self, text="RAICES MULTIPLES", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="2")
        label.pack()

        #FUNCION:
        label =tk.Label(self,text="f(x) : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=200)
        fdx=tk.Entry(self, textvariable=self.entradaF)
        fdx.place(x=200,y=215)

        #F'(x):
        label =tk.Label(self,text=" f'(x) : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80, y=250)
        fpt=tk.Entry(self, textvariable=self.entradaF1)
        fpt.place(x=200,y=265)

        #F''(X):
        label =tk.Label(self,text="f''(x) : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=300)
        fppt=tk.Entry(self, textvariable=self.entradaF2)
        fppt.place(x=200,y=315)

        #X0:
        label =tk.Label(self,text="X0 : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=350)
        Xcero=tk.Entry(self, textvariable=self.entradaX)
        Xcero.place(x=200,y=365)

        #Tol:
        label =tk.Label(self,text="Tol : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=400)
        tt=tk.Entry(self, textvariable=self.entradaT)
        tt.place(x=200,y=415)

        #N:
        label =tk.Label(self,text="N : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=450)
        nt=tk.Entry(self, textvariable=self.entradaN)
        nt.place(x=200,y=465)

        button1 = tk.Button(self, text="SOLUCIONAR",
                            command=self.calcular,width="30",height="2",bg="gray25",fg="cyan2")

        button1.place(x=150,y=500)

    def calcular(self):
        print(self.entradaF.get())
        print(self.entradaF1.get())
        print(self.entradaF2.get())
        print(self.entradaX.get())
        print(self.entradaT.get())
        print(self.entradaN.get())