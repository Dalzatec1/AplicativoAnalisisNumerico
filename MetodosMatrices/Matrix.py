import numpy as np

class Matrix ():
        def __init__(self, _size, *args:list):

            self.size = _size
            self.sol = np.zeros(self.size)

            np.set_printoptions(suppress=True) #Scientific notation

            if (len(args) < 2):
                self.data = np.zeros((self.size, self.size + 1))
                print(self.data)
                return

            if (len(args[0]) != self.size**2 or len(args[1]) != self.size):
                return

            self.data = self.createExtendedMatrix(args[0],args[1])

            print("\n",self.data)

        def createExtendedMatrix(self, _a, _b):
            _rows = []
            _tuple = []
            _i = 0
            for _val in _a:
                _tuple.append(_val)

                if (len(_tuple) == self.size):
                    _tuple.append(_b[_i])
                    _rows.append(_tuple)

                    _tuple = []
                    _i += 1
            return np.array(_rows)
            

        def switchRows(self, _a, _b):
            self.data[[_a, _b]] = self.data[[_b, _a]]
        
        def switchCols(self, _a, _b):
            self.data[:,[_a, _b]] = self.data[:,[_b, _a]]

        def susRows(self, _a, _b, _s):
            self.data[_b] = self.data[_b] - (self.data[_a] * _s)

        def scalarRow(self, _a, _s):
            self.data[_a] = self.data[_a] * _s

        def getIndexOf(self, _val, _a):
            _index = 0
            for _value in self.data[_a]:
                if(_value == _val):
                    return _index
                _index += 1
            return None

        def showMatrix(self):
            
            print("\n",self.data)

        def solveMatrix(self):
            _n = len(self.data)
            _x = np.zeros(_n)

            for _i in reversed(range(_n)):
                _piv = self.data[_i][_i]
                _sum = np.sum(self.data[_i][_i+1:_n]*_x[_i+1:_n]) / _piv
                _x[_i] = self.data[_i][_n] / _piv - _sum

            print("\n Solution: \n\n", _x)
        