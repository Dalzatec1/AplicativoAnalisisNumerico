from fourFn import pyParsingEvaluate as pypEval
import re

def expEval(_function, *args):

    _function = str(_function)

    print("\nf( g ) = ", _function)
    
    if(len(args) > 0):       
        _parsedFunction = re.sub(r"\b[x]", str(args[0]), _function)
        print("f(", args[0] ,") = ", pypEval(_parsedFunction))
        return pypEval(_parsedFunction)
    else:
        print("\nf( g ) = ", pypEval(_function))
        return pypEval(_function)
