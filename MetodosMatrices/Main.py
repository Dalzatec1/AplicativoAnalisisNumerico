from Matrix import Matrix
from GaussSimple import EGS
from GaussPivoteoParcial import EGPP
from GaussPivoteoTotal import EGPT

_a = [2, -1, 0, 3, 
        1, 0.5, 3, 8, 
        0, 13, -2, 11, 
        14, 5, -2, 3]
_b = [1, 1, 1, 1]


_matrix = Matrix(4,_a,_b)

#_egs = EGS(_matrix)                            #Gauss Simple
#_egpp = EGPP(_matrix)                          #Gauss Pivoteo Parcial
#_egpt = EGPT(_matrix)                          #Gauss Pivoteo Total
