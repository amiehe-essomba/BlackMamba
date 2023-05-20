import numpy as np 
from src.ggplot import error as er

def check_dim(X, Y, line : int = 0):
    error = None 

    try:
        M = X[0]
        if type(X) == type(np.array([1])):
            if type(Y) == type(np.array([1])):
                if (X.shape in [(X.shape[0], 1),(X.shape[0], ) ]): 
                    if (X.shape == Y.shape) : pass
                    else: error  = er.ERRORS(line).ERROR1(X.shape, Y.shape)
                else: error  = er.ERRORS(line).ERROR2('X')
            else:
                if (X.shape in [(X.shape[0], 1),(X.shape[0], ) ]): 
                    if X.shape[0] == len(Y): pass 
                    else: error  = er.ERRORS(line).ERROR1(X.shape, len(Y))
                else: error  = er.ERRORS(line).ERROR2('X')
        else:
            if type(Y) == type(np.array([1])):
                if Y.shape in [(Y.shape[0], 1), (Y.shape[0], )]:
                    if len(X) == Y.shape[0]: pass 
                    else: pass 
                else: er.ERRORS(line).ERROR1(Y.shape, len(X))
            else:
                if len(X) == len(Y): pass 
                else: error  = er.ERRORS(line).ERROR1(len(X), len(Y))
    except IndexError: error  = er.ERRORS(line).ERROR7("X")

    return error 