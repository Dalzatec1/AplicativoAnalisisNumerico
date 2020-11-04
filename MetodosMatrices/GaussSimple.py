from Matrix import Matrix
class EGS():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.solve()

    def solve(self):
        self.checkIfFirstZero()
        
        _i = 0
        _j = 1
        for _i in range(self.matrix.size - 1):
            _j = _i + 1
            while (_j <= self.matrix.size - 1):
                if (self.matrix.ext[_j][_i] != 0):
                    _s = self.matrix.ext[_j][_i] / self.matrix.ext[_i][_i]
                    self.matrix.susRows(_i, _j , _s)
                _j += 1
            print("\nStage #",_i + 1)
            self.matrix.showMatrix(self.matrix.ext)

        self.matrix.solveMatrix()

            
    def checkIfFirstZero(self):

        if (self.matrix.getIndexOf(0,0) == 0):
            _index = 0
            for _row in self.matrix.ext:
                if (_row[0] != 0):
                    self.matrix.switchRows(_index,0)
                    return
                _index += 1

    
        

