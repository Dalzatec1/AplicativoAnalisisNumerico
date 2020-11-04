import numpy as np

class Vandermonde():
    def __init__(self, _x, _y):
        self.X = _x
        self.Y = _y

        self.solve()

    def solve(self):
        _n = len(self.X)
        _A = np.zeros([_n,_n])
    
        for _i in range(_n):
            _A[:,_i] = np.conjugate(np.power(self.X,(_n - _i-1 )))
        
        _res = np.linalg.solve(_A,np.transpose(self.Y))

        _exp = _n - 1
        _pol = ""
        for _coe in _res:
            _pol = _pol + str(_coe) + "x^"+str(_exp) + " + "
            _exp -= 1
        _pol = _pol[:-2]
        
        print ("\nMatriz de Vandermonde:\n",_A)
        print ("\nCoeficientes del polinomio:\n",_res)
        print ("\nPolinomio:\n",_pol)
