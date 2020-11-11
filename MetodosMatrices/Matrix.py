import numpy as np

class Matrix ():
        def __init__(self, _size, *args:list):

            self.size = _size
            self.sol = np.zeros(self.size)
            

            np.set_printoptions(suppress=True) #Scientific notation

            if (len(args) < 2):
                self.ext = np.zeros((self.size, self.size + 1))
                print(self.ext)
                return

            if (len(args[0]) != self.size**2 or len(args[1]) != self.size):
                return


            self.ext = self.createExtendedMatrix(args[0],args[1])
            
            self.A = self.createA(args[0])
            self.B = self.createB(args[1])


            #print("\n",self.ext)
            #print("\n",self.A)

        def createA(self, _a):
            _rows = []
            _tuple = []
            _i = 0
            for _val in _a:
                _tuple.append(_val)

                if (len(_tuple) == self.size):
                    #_tuple.append(_b[_i])
                    _rows.append(_tuple)

                    _tuple = []
                    _i += 1
            return np.array(_rows)

        def createB(self, _b):
            return np.array(_b).reshape(self.size,1)

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
            self.ext[[_a, _b]] = self.ext[[_b, _a]]
        
        def switchCols(self, _a, _b):
            self.ext[:,[_a, _b]] = self.ext[:,[_b, _a]]

        def susRows(self, _a, _b, _s):
            self.ext[_b] = self.ext[_b] - (self.ext[_a] * _s)

        def scalarRow(self, _a, _s):
            self.ext[_a] = self.ext[_a] * _s

        def getIndexOf(self, _val, _a):
            _index = 0
            for _value in self.ext[_a]:
                if(_value == _val):
                    return _index
                _index += 1
            return None

        def showMatrix(self, matrix):
            
            print("\n",matrix)

        def solveMatrix(self):
            _n = len(self.ext)
            _x = np.zeros(_n)

            for _i in reversed(range(_n)):
                _piv = self.ext[_i][_i]
                _sum = np.sum(self.ext[_i][_i+1:_n]*_x[_i+1:_n]) / _piv
                _x[_i] = self.ext[_i][_n] / _piv - _sum

            print("\n Solution: \n\n", _x)
       

        def solvepro(self,first,second):
            
            extend=np.column_stack([first,second])
         
            n = len(extend)
            x = np.zeros(n,dtype=np.complex_)
            x[0] =extend[0,n]/extend[0,0]
            for i in range(1,n):
                a=np.append([1],np.transpose(x[0:i]))           
                a1=np.append(extend[i,n],extend[i,0:i]*-1)                         
                x[i]=np.dot(a,a1)/extend[i,i]
            
            print("\n Solution: \n\n", x)
            return x
            
        def solvereg(self,first,second):
            
            extend=np.column_stack([first,second])
   
            n = len(extend)
            x = np.zeros(n,dtype=np.complex_)
            x[n-1] = extend[n-1,n]/extend[n-1,n-1]
            for i in reversed(range(n-1)):
                a=np.append([1],np.transpose(x[i+1:n])) 
                a1=np.append(extend[i,n],extend[i,i+1:n]*-1)            
                x[i]=np.dot(a,a1)/extend[i,i]

            print("\n Solution reg: \n\n", x.real)
            return x
        
