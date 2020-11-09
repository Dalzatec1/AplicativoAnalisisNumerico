from Matrix import Matrix
from GaussSimple import EGS
from GaussPivoteoParcial import EGPP
from GaussPivoteoTotal import EGPT
from Jacobi import Jacobi
from GSeidel import GSeidel
from Sor import Sor
from Vandermonde import Vandermonde
from DifDiv import DifDiv
from Lagrange import Lagrange
from TLineal import TLineal
from TCuad import TCuad
from TCubic import TCubic


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

_x = [-1, 0, 3, 4]
_y = [15.5, 3, 8, 1]

_matrix = Matrix(4,_a,_b)


_x0 = np.zeros(4).reshape(4,1)

#_egs = EGS(_matrix)                            #Gauss Simple
#_egpp = EGPP(_matrix)                          #Gauss Pivoteo Parcial
#_egpt = EGPT(_matrix)                          #Gauss Pivoteo Total

#_jac = Jacobi(_matrix,_x0,1E-7,100)
#_gse = GSeidel(_matrix,_x0,1E-7,100)
#_sor = Sor(_matrix,_x0,1.5,1E-7,100)
#_van = Vandermonde(_x, _y)
#_new = DifDiv(_x, _y)
#_lag = Lagrange(_x, _y)
#_tli = TLineal(_x, _y)
#_tcu = TCuad(_x, _y)
#_tcb = TCubic(_x, _y)