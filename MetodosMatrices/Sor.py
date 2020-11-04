from Matrix import Matrix
import numpy as np

class Sor():
    def __init__(self, _matrix:Matrix, _x0, _w, _tol, _nMax):
        self.matrix = _matrix
        self.x0 = _x0
        self.w = _w
        self.tol = _tol
        self.nMax = _nMax

        self.solve()

    def solve(self):
        _D = np.diag(np.diag(self.matrix.A))
        _L = (np.tril(self.matrix.A) * -1) + _D
        _U = (np.triu(self.matrix.A) * -1) + _D
        _T = np.linalg.inv(_D - (self.w * _L)).dot((1-self.w) * _D + (self.w * _U))
        _C = self.w * np.linalg.inv(_D - (self.w * _L)).dot(self.matrix.B)

        print("\nT:\n", _T)
        print("\nC:\n", _C)

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
            