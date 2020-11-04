from Matrix import Matrix
from GaussSimple import EGS
from GaussPivoteoParcial import EGPP
from GaussPivoteoTotal import EGPT
from Jacobi import Jacobi
from GSeidel import GSeidel
from Sor import Sor
import numpy as np
"""
_a = [2, -1, 0, 3, 
        1, 0.5, 3, 8, 
        0, 13, -2, 11, 
        14, 5, -2, 3]
_b = [1, 1, 1, 1]
"""
_a = [4, -1, 0, 3, 
        1, 15.5, 3, 8,
        0, -1.3, -4, 1.1,
        14, 5, -2, 30]
_b = [1, 1, 1, 1]




_matrix = Matrix(4,_a,_b)

_x0 = np.zeros(4).reshape(4,1)

#_jac = Jacobi(_matrix,_x0,1E-7,100)
#_gse = GSeidel(_matrix,_x0,1E-7,100)
#_sor = Sor(_matrix,_x0,1.5,1E-7,100)
#_egs = EGS(_matrix)                            #Gauss Simple
#_egpp = EGPP(_matrix)                          #Gauss Pivoteo Parcial
#_egpt = EGPT(_matrix)                          #Gauss Pivoteo Total
