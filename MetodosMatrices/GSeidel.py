from Matrix import Matrix
import numpy as np

class GSeidel():
    def __init__(self, _matrix:Matrix, _x0, _tol, _nMax):
        self.matrix = _matrix
        self.x0 = _x0
        self.tol = _tol
        self.nMax = _nMax

        self.solve()

    def solve(self):
        _D = np.diag(np.diag(self.matrix.A))
        _L = (np.tril(self.matrix.A) * -1) + _D
        _U = (np.triu(self.matrix.A) * -1) + _D
        _T = np.linalg.inv(_D - _L).dot(_U)
        _C = np.linalg.inv(_D - _L).dot(self.matrix.B)
        [val,vec]=np.linalg.eig(_T)
        ro=max(abs(val))	
        
        if ro>=1:
            print("\nEl radio espectral > 1\n")

        print("\nT:\n", _T)
        print("\nC:\n", _C)
        print("\nradio espectral:\n",ro)

        _xant = self.x0
        _E = 1
        _i = 0

        print("\n| Iter |    E     | ")

        while ((_E > self.tol) and (_i < self.nMax)):
            _xact = _T.dot(_xant) + _C
            _E = np.linalg.norm(_xant - _xact)
            _xant = _xact
            _i += 1
            print("| ", _i , " | ", _E, " | ", _xact.reshape(1,self.matrix.size))
            