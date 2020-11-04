import numpy as np

class TCuad():
    def __init__(self, _x, _y):
        self.X = _x
        self.Y = _y


        self.solve()

    def solve(self):
        _n = len(self.X)
        _m = 3 * (_n - 1)
        _A = np.zeros([_m, _m])
        _B = np.zeros(_m).reshape(_m, 1)
        _coef = np.zeros([_n-1, 3])


        for _i in range(0, _n-1):
            _A[(_i+1), 3*(_i+1)-3:3*(_i+1)] = [self.X[_i+1]**2, self.X[_i+1], 1]
            _B[(_i+1)] = self.Y[_i+1]

        _A[0, 0:3] = [self.X[0]**2, self.X[0], 1]
        _B[0] = self.Y[0]
        
        for _i in range(1, len(self.X)-1):
            _A[_n-1 + _i, 3*(_i+1)-6:3*(_i+1)] = [self.X[_i]**2,self.X[_i], 1,(self.X[_i]**2)*-1, (self.X[_i]*-1), -1]
            _B[_n-1 + _i] = 0

        for _i in range(1, len(self.X)-1):
            _A[2*_n-4+(_i+1),3*(_i+1)-6:3*(_i+1)] = [2*self.X[_i], 1 , 0 , -2*self.X[_i], -1, 0]
            _B[2*_n-3+(_i+1)] = 0

        _A[_m-1,0] = 2
        _B[_m-1] = 0

        
        
        _res = np.linalg.solve(_A,_B)
  

        for _i in range(0,len(self.X)-1):
            _coef[_i,:] = _res[3*(_i+1) - 3: 3*(_i+1)].reshape(1,3)

        print ("\nCoeficientes de los trazadores:\n")
        for _co in _coef:
            print(_co[0],' ',_co[1],' ',_co[2])
        print ("\nTrazadores:\n")
        for _tra in _coef:
            print(str(_tra[0])+'x^2 + ', str(_tra[1])+ 'x + ',_tra[2])
