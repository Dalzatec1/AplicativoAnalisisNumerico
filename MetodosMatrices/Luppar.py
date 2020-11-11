from Matrix import Matrix
import numpy as np
import copy
class LUPP():
    def __init__(self, _matrix:Matrix):
        self.matrix = _matrix
        self.solve()

    def solve(self):
        self.checkIfFirstZero()   
        n=self.matrix.size
        L=np.eye(n)
        U=np.zeros([n,n])
        P=np.eye(n)
        M=self.matrix.A
     
        for i in range(self.matrix.size-1 ):
          

            aux0=max(abs(M[i+1:n,i]))
            aux=len(M[i+1:n,i])
       
            if (aux0>abs(M[i,i])):
                aux2=M[i+aux,i:n].copy()
                aux3=P[i+aux,:].copy()
                
                M[aux+i,i:n]=M[i,i:n]
                
                P[aux+i,0:n]=P[i,:]
                
                M[i,i:n]=aux2
                P[i,:]=aux3

                
                if i>0:
                    aux4=L[i+aux,1:i-1].copy()
                    L[i+aux,1:i-1]=L[i,1:i-1]
                    L[i,1:i-1]=aux4
            
            for j in range(i+1,self.matrix.size):
                if (M[j,i]!=0):
                    L[j,i]=M[j,i]/M[i,i]
                    M[j,i:n]=(M[j,i:n]-(M[j,i]/M[i,i])*(M[i,i:n]))          
            U[i,i:n]=M[i,i:n]
            U[i+1,i+1:n]=M[i+1,i+1:n]

            
            print("\nStage #",i + 1)
            self.matrix.showMatrix(M)
            print("\nL: ")
            self.matrix.showMatrix(L)
            print("\nU: ")
            self.matrix.showMatrix(U)
        U[n-1,n-1]=M[n-1,n-1]
        z=self.matrix.solvepro(L,np.dot(P,self.matrix.B))

        x=self.matrix.solvereg(U,z)
        
        
    def checkIfFirstZero(self):
    
        if (self.matrix.getIndexOf(0,0) == 0):
            _index = 0
            for _row in self.matrix.ext:
                if (_row[0] != 0):
                    self.matrix.switchRows(_index,0)
                    return
                _index += 1