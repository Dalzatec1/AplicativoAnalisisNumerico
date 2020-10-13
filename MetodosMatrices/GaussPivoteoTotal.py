from Matrix import Matrix

class EGPT():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.solve()
    
    def solve(self):

        _i = 0
        _j = 1
        for _i in range(self.matrix.size - 1):
            
            _index = _i + 1
            
            while (_index < self.matrix.size):
                if (self.matrix.data[_i][_i] < self.matrix.data[_index][_i]):
                    self.matrix.switchRows(_i, _index)
                _index += 1

            _index = _i + 1

            while (_index < self.matrix.size+1):
                if (self.matrix.data[_i][_i] < self.matrix.data[_i][_index]):
                    self.matrix.switchCols(_i, _index)
                _index += 1

            _j = _i + 1
            while (_j <= self.matrix.size - 1):
                if (self.matrix.data[_j][_i] != 0):
                    _s = self.matrix.data[_j][_i] / self.matrix.data[_i][_i]
                    self.matrix.susRows(_i, _j , _s)
                _j += 1
            print("\nStage #",_i + 1)
            self.matrix.showMatrix()

        self.matrix.solveMatrix()

    