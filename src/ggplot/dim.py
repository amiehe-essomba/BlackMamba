import numpy as np 
from src.ggplot import error as er
import pandas as pd 
import matplotlib.colors as mcolors

def check_dim(X, Y, label, axis, line : int = 0):
    error = None 
    LABEL, data = None, None
    all_c = list(mcolors.CSS4_COLORS.keys())
    try:
        M = X[0]
        if type(X) == type(np.array([1])):
            if type(Y) == type(np.array([1])):
                if (X.shape in [(X.shape[0], 1),(X.shape[0], ) ]): 
                    if X.shape[0] == Y.shape[0]:
                        if len(Y.shape) == 2:
                            width = Y.shape[1]
                            if type(label) == type(str()):
                                if label: LABEL = [label] + [f'{x}' for x in range(width-1)]
                                else: LABEL = [f'{x}' for x in range(width)]
                            else:
                                if len(label) == width: LABEL = label
                                else:
                                    if len(label) < width: LABEL = label + [f"{x}" for x in range(width-len(label))]
                                    else: LABEL = label[ : width]
                            for i, s in enumerate(LABEL):
                                LABEL[i] = str(s)
                            LABEL = ['X'] + LABEL
                            if axis is None:
                                XX, YY = X.reshape((-1, 1)), Y.reshape((-1, width))
                                X_Y = np.column_stack((XX, YY)).reshape((-1, width+1))
                                data = pd.DataFrame(data=X_Y, columns=LABEL)
                                data.set_index(LABEL[0], inplace=True)
                            else:
                                if axis < width:
                                    XX, YY = X.reshape((-1, 1)), Y.reshape((-1, width))
                                    X_Y = np.column_stack((XX, YY[:, axis])).reshape((-1, 2))
                                    LABEL = [LABEL[0], LABEL[axis+1]]
                                    data = pd.DataFrame(data=X_Y, columns=LABEL)
                                    data.set_index(LABEL[0], inplace=True)
                                else: error  = er.ERRORS(line).ERROR10(axis, "col")
                        else: error  = er.ERRORS(line).ERROR13(string='Y')
                    else: error  = er.ERRORS(line).ERROR1(X.shape, Y.shape)
                else: error  = er.ERRORS(line).ERROR2('X')
            else:
                if (X.shape in [(X.shape[0], 1),(X.shape[0], ) ]): 
                    if X.shape[0] == len(Y): 
                        if label:
                            if type(label) == type(str()): LABEL = [label]
                            else: 
                                LABEL = [str(label[0])] 
                        else: LABEL = ['0']

                        if axis in [0, None]:
                            LABEL = ['X']+LABEL
                            XX, YY = X.reshape((-1, 1)), np.array(Y).reshape((-1, 1))
                            X_Y = np.column_stack((XX, YY)).reshape((-1, 2))
                            data = pd.DataFrame(data=X_Y, columns=LABEL)
                            data.set_index(LABEL[0], inplace=True)
                        else: error  = er.ERRORS(line).ERROR10(axis, "col")
                    else: error  = er.ERRORS(line).ERROR1(X.shape, len(Y))
                else: error  = er.ERRORS(line).ERROR2('X')
        else:
            if X:
                if type(Y) == type(np.array([1])):
                    if len(Y.shape) == 2:
                        if len(X) == Y.shape[0]: 
                            width = Y.shape[1]
                            if type(label) == type(str()):
                                if label: LABEL = [label] + [f'{x}' for x in range(width-1)]
                                else: LABEL = [f'{x}' for x in range(width)]
                            else:
                                if len(label) == width: LABEL = label
                                else:
                                    if len(label) < width: LABEL = label + [f"{x}" for x in range(width-len(label))]
                                    else: LABEL = label[ : width]
                            for i, s in enumerate(LABEL):
                                LABEL[i] = str(s)
                            LABEL = ['X'] + LABEL
                            
                            if axis is None:
                                XX, YY = np.array(X).reshape((-1, 1)), Y.reshape((-1, width))
                                X_Y = np.column_stack((XX, YY)).reshape((-1, width+1))
                                data = pd.DataFrame(data=X_Y, columns=LABEL)
                                data.set_index(LABEL[0], inplace=True)
                            else:
                                if axis < width:
                                    XX, YY = np.array(X).reshape((-1, 1)), Y.reshape((-1, width))
                                    X_Y = np.column_stack((XX, YY[:, axis])).reshape((-1, 2))
                                    LABEL = [LABEL[0], LABEL[axis+1]]
                                    data = pd.DataFrame(data=X_Y, columns=LABEL)
                                    data.set_index(LABEL[0], inplace=True)
                                else: error  = er.ERRORS(line).ERROR10(axis, "col")
                        else: error  = er.ERRORS(line).ERROR1(len(X), Y.shape)
                    else: error  = er.ERRORS(line).ERROR13(string='Y')
                else:
                    if len(X) == len(Y): 
                        if label:
                            if type(label) == type(str()): LABEL = [label]
                            else: 
                                LABEL = [str(label[0])] 
                        else: LABEL = ['0']

                        if axis in [0, None]:
                            LABEL = ['X']+LABEL
                            XX, YY = np.array(X).reshape((-1, 1)), np.array(Y).reshape((-1, 1))
                            X_Y = np.column_stack((XX, YY)).reshape((-1, 2))
                            data = pd.DataFrame(data=X_Y, columns=LABEL)
                            data.set_index(LABEL[0], inplace=True)
                        else: error  = er.ERRORS(line).ERROR10(axis, "col")
                    else: error  = er.ERRORS(line).ERROR1(len(X), len(Y))
            else: error  = er.ERRORS(line).ERROR7("X")
    except IndexError: error  = er.ERRORS(line).ERROR7("X")
    
    if error is None: return error, data, LABEL[1:] 
    else: return error, data, LABEL 

def scatter_params(line : int = 0, marker: str = 0):
    error       = None 
    m           = ["o", "^", "+", "*", ".", "v", "<", ">", "1", "2", "3", "4", "s", "p", "h", "H", "x", "D"]
    
    if 0 <= marker < len(m): marker = m[marker]
    else: error = er.ERRORS(line=line).ERROR10(len(m))

    return marker, error 

def scatter_Size(line, size):
    chaine, error = None, None 
   
    if size is not  None:
        if len(size) == 2:
            size = list(size)
            for i, s in enumerate(size):
                if type(s) in [type(int()), type(float())]: size[i] = float(s)
                else:
                    error = er.ERRORS(line).ERROR9(size, s)
                    break
            if error is None:
                if size[0] < size[1] : chaine = 'all' 
                else: error = er.ERRORS(line).ERROR12(data=tuple(size))
        else: error = er.ERRORS(line).ERROR8(string='lim')
    else: pass 

    return size,  chaine, error