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

def scatter_params(line : int = 0, marker: list = [], M : int = 0):
    error       = None 
    m           = ["o", "^", "+", "*", ".", "v", "<", ">", "1", "2", "3", "4", "s", "p", "h", "H", "x", "D"]
    
    if not marker:
        for i in range(M):
            marker.append(m[0])
    else:
        for i, mark in enumerate( marker ):
            if 0 <= mark < len(m): 
                mark  = m[mark]
                marker[i] = mark
            else: 
                error = er.ERRORS(line=line).ERROR10(index=len(m), string=f"marker[{i}]")
                break 
    
    if error is None:
        if len(marker) == M: pass 
        elif len(marker) < M:
            idd = len(marker)
            while idd < M:
                marker.append(m[0])
                idd += 1 
        else: error = er.ERRORS(line).ERROR20(string = "marker", N=M)
    else: pass

    return marker, error 

def scatter_Size(line: int, size : list = [], M : int = 0):
    chaine, error = None, None 
    
    if size is not  None:
        for i, S in enumerate(size):
            if type(S) in [type(tuple()), type(list())]:
                if len(S) == 2:
                    size = list(S)
                    for i, s in enumerate(S):
                        if type(s) in [type(int()), type(float())]: S[i] = float(s)
                        else:
                            error = er.ERRORS(line).ERROR9(size, s)
                            break
                    if error is None:
                        if S[0] < S[1] : 
                            chaine = 'all' 
                            size[i] = S
                        else: 
                            error = er.ERRORS(line).ERROR12(data=tuple(S))
                            break
                    else: break
                else: error = er.ERRORS(line).ERROR8(string='lim')
            else:
                error = er.ERRORS(line).ERROR21(string=f'lim[{i}]') 
                break

        if len(size) == M: pass 
        elif len(size) < M:
            idd = len(size)
            while idd < M:
                size.append(None)
                idd += 1
        else: error = er.ERRORS(line).ERROR20(string = "lim", N=M)
    else: 
        size = []
        for i in range(M):
            size.append(None)

    return size,  chaine, error