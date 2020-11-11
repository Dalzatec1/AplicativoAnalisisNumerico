from Matrix import Matrix
import cmath
import numpy as np
class CHOL():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.solve()

    def solve(self):
        self.checkIfFirstZero()    
        n=self.matrix.size
        L=np.eye(n,dtype=np.complex)
        U=np.eye(n,dtype=np.complex)
        M=self.matrix.A

        for i in range(0,n):
            aux=(M[i,i]-np.dot(L[i,0:i],np.transpose(U[0:i,i])))
            f=float(aux)
            L[i,i]=cmath.sqrt(f)
        
            U[i,i]=L[i,i]
            for j in range(i+1,n):
               U[i,j]=(M[i,j]-np.dot(L[i,0:i],np.transpose(U[0:i,j])))/L[i,i]

            for j in range(i+1,n):
                L[j,i]=(M[j,i]-np.dot(L[j,0:i],np.transpose(U[0:i,i])))/U[i,i]

            print("\nStage #",i + 1)

            print("\nL: ")
            self.matrix.showMatrix(L)
            print("\nU: ")
            self.matrix.showMatrix(U)

        L[n-1,n-1]=cmath.sqrt(M[n-1,n-1]-np.dot(L[n-1,0:n-1],np.transpose(U[0:n-1,n-1])))
        U[n-1,n-1]=L[n-1,n-1]

        z=self.matrix.solvepro(L,self.matrix.B)
        x=self.matrix.solvereg(U,z)
       
        
    def checkIfFirstZero(self):
    
        if (self.matrix.getIndexOf(0,0) == 0):
            _index = 0
            for _row in self.matrix.ext:
                if (_row[0] != 0):
                    self.matrix.switchRows(_index,0)
                    return
                _index += 1