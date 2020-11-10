import numpy as np

class DifDiv():
    def __init__(self, _x, _y):
        self.X = _x
        self.Y = _y

        self.solve()

    def solve(self):
        _n = len(self.X) 
        _D = np.zeros([_n, _n])
    
        
        _D[:,0] = np.conjugate(self.Y)

        for _i in range (1,_n):
            _aux0 = _D[_i-1:_n, _i-1]
            _aux1 = np.diff(_aux0)
            _aux2 = np.subtract(self.X[_i:_n],self.X[0:_n-1-_i+1])
            _D[_i:_n,_i] = np.divide(_aux1,np.transpose(_aux2))

        _res = np.diag(_D)
    
        print ("\nTabla de diferencias divididas:\n",_D)        
        print ("\nCoeficientes del polinomio de Newton:\n",_res) 
        print ("\nPolinomio:\n",)
        
        _pol=""
        b=""
        cont=0
        for f in _res:
            n=str(self.X[cont])
            _pol=_pol+" + ("+str(f)+")"+b
            b=b+"(x - ("+n+"))"        
            cont+=1
        print(_pol[2:])

            

            

        