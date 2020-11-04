import numpy as np

class Lagrange():
    def __init__(self, _x, _y):
        self.X = _x
        self.Y = _y

        self.solve()

    def solve(self):
        _n = len(self.X)
        _L = np.zeros([_n,_n])
    
        for _i in range(0, _n):
            _aux0 = np.setdiff1d(self.X, self.X[_i])
            _aux1 = [1, (_aux0[0]*-1)]
            
            for _j in range(1,_n-1):
                _aux1 = np.convolve(_aux1, [1, (_aux0[_j]*-1)])

            _L[_i,:] = (_aux1)/(np.polyval(_aux1,self.X[_i]))
            
        _pols = []
        

        for _poli in _L:
            _exp = _n - 1
            _pol = ""
            for _val in _poli:
                _pol = _pol + str(_val) + "x^" + str(_exp) + " + "
                _exp -= 1
            _pol = _pol[:-2]
            _pols.append(_pol)
                

        


        print ("\nPolinomios interpolantes de Lagrange:\n")
        for _x in _pols:
            print(_x)

        
