from Matrix import Matrix
from GaussSimple import EGS
from GaussPivoteoParcial import EGPP
from GaussPivoteoTotal import EGPT
"""
_a = [2, -1, 0, 3, 
        1, 0.5, 3, 8, 
        0, 13, -2, 11, 
        14, 5, -2, 3]
_b = [1, 1, 1, 1]

_a = [0, 0, 1, 
        4, 2, 1, 
        0.64, 0.8, 1]
_b = [0.5, 1, 0]
"""


_a = [1, 2, 3, 
        4, 5, 6, 
        7, 8, 9]
_b = [1, 1, 1]

_matrix = Matrix(3,_a,_b)
_matrix.getD()
_matrix.getL()
_matrix.getU()
_matrix.getT()
_matrix.getC()
#_egs = EGS(_matrix)                            #Gauss Simple
#_egpp = EGPP(_matrix)                          #Gauss Pivoteo Parcial
#_egpt = EGPT(_matrix)                          #Gauss Pivoteo Total
