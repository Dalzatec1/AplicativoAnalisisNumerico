from tkinter import *
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class NEW(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.entradaF  = StringVar()
        self.entradaF1  = StringVar()
        self.entradaX  = StringVar()
        self.entradaT  = StringVar()
        self.entradaN  = StringVar()

        label = tk.Label(self, text="NEWTON", font=("controller.title_font",30),width="60",height="0",fg="cyan2")
        label.pack()

        label =tk.Label(self,text=" ",fg="gray25", font=("Comic Seans MS",15),width="80",height="2")
        label.pack()

        #FUNCION:
        label =tk.Label(self,text="f(x) : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=200)
        fdx=tk.Entry(self, textvariable=self.entradaF)
        fdx.place(x=200,y=215)

        #FUNCION':
        label =tk.Label(self,text="f'(x) : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80, y=250)
        fpt=tk.Entry(self, textvariable=self.entradaF1)
        fpt.place(x=200,y=265)

        #X0:
        label =tk.Label(self,text="X0 : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=300)
        xcero=tk.Entry(self, textvariable=self.entradaX)
        xcero.place(x=200,y=315)

        #Tol:
        label =tk.Label(self,text="Tol : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=350)
        tt=tk.Entry(self, textvariable=self.entradaT)
        tt.place(x=200,y=365)

        #N:
        label =tk.Label(self,text="N : ",fg="gray25", font=("Comic Seans MS",15),width="10",height="2")
        label.place(x=80,y=400)
        nt=tk.Entry(self, textvariable=self.entradaN)
        nt.place(x=200,y=415)

        button1 = tk.Button(self, text="SOLUCIONAR",
                            command=self.calcular,width="30",height="2",bg="gray25",fg="cyan2")

        button1.place(x=150,y=500)
    
    def calcular(self):
        print(self.entradaF.get())
        print(self.entradaF1.get())
        print(self.entradaX.get())
        print(self.entradaT.get())
        print(self.entradaN.get())