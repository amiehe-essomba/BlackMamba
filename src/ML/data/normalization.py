import numpy as np 
from numba import jit
from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from CythonModules.Windows                      import fileError    as fe


def Scaler(X : np.ndarray, axis : any = None, line : int = 0, cal : str = 'standardscaler'):
    # x_normalized = (x - min(x)) / (max(x) - min(x))
    # x_normalized = (x - median(x)) / median_absolute_deviation(x)
    error = None

    try:
        if len( X.shape ) == 2:
            if X.size != 0:
                if axis is None: 
                    if  cal == 'StandardScaler'     :
                        X = (X - X.min()) / X.std() 
                    elif cal == 'MinMaxScaler'      :
                        X = (X - X.min()) / (X.max() - X.min())
                    elif cal == 'LogarithmicScaler' :
                        X = np.log(X)
                    elif cal == "SoftmaxScaler"     :
                        X = np.exp(X) / ( np.exp(X) ).sum()
                    elif cal == "MinAbsScaler"      :
                        X = (X - np.median(X)) / np.std(X)
                else:
                    if axis < X.shape[1]:
                        if cal == 'StandardScaler'      : 
                            if X[:, axis].std() != 0:
                                X[:, axis] = (X[:, axis] - X[:, axis].min()) / X[:, axis].std()
                            else: error = ERRORS(line).ERROR4( "std(X)")
                        elif cal == 'MinMaxScaler'      :
                            if  (X[:, axis].max() - X[:, axis].min()) != 0:
                                X[:, axis] = (X[:, axis] - X[:, axis].min()) / (X[:, axis].max() - X[:, axis].min())
                            else: error = ERRORS(line).ERROR4('max(X) - min(X)')
                        elif cal == 'LogarithmicScaler' :
                            X[:, axis] = np.log(X[:, axis])
                        elif cal == "SoftmaxScaler"     :
                            if ( np.exp(X[:, axis]) ).sum() != 0 :
                                X[:, axis] = np.exp(X[:, axis]) / ( np.exp(X[:, axis]) ).sum()
                            else: error = ERRORS(line).ERROR4("sum( exp(X) )")
                        elif cal == "MinAbsScaler"      :
                            if np.std(X[:, axis]) != 0:
                                X[:, axis] = (X[:, axis] - np.median(X[:, axis])) / np.std(X[:, axis])
                            else: error = ERRORS(line).ERROR4( "std(X)")
                        else: error =ERRORS(line).ERROR1('axis', X.shape[1])
            else: error = ERRORS(line).ERROR2()
        else: error = ERRORS(line).ERROR0()
    except ValueError: error = ERRORS(line).ERROR3()
    except RuntimeWarning : 
        if   cal == 'StandardScaler'    : error = ERRORS(line).ERROR4( "std(X)")
        elif cal == 'MinMaxScaler'      : error = ERRORS(line).ERROR4('max(X) - min(X)')
        elif cal == 'MinAbsScaler'      : error = ERRORS(line).ERROR4("std(X")
        else : pass 

    return X, error


class ERRORS:
    def __init__(self, line):
        self.line       = line
        self.cyan       = bm.init.bold + bm.fg.rbg(0,255,255)
        self.red        = bm.init.bold + bm.fg.rbg(255,0,0)
        self.green      = bm.init.bold + bm.fg.rbg(0,255,0)
        self.yellow     = bm.init.bold + bm.fg.rbg(255,255,0)
        self.magenta    = bm.init.bold + bm.fg.rbg(255,0,255)
        self.white      = bm.init.bold + bm.fg.rbg(255,255,255)
        self.blue       = bm.init.bold + bm.fg.rbg(0,0,255)
        self.reset      = bm.init.reset

    def ERROR0(self):
        error = '{}should be a {}[n, m] {}ndarray, {}with m and n not null. {}line: {}{}'.format(self.white, self.red, self.blue, 
                                                   self.green, self.white,self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}the X matrix '.format( self.cyan) + error

        return self.error+self.reset

    def ERROR1(self, string: str = "axis", n : int = 0):
        error = '{}> {}{}. {}line: {}{}'.format(self.red, self.green, n, self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}{} '.format( self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR2(self):
        error = '{}EMPTY. {}line: {}{}'.format(self.green, self.white,self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}the X matrix{}caannot be '.format( self.cyan, self.white) + error
        return self.error+self.reset
    
    def ERROR3(self):
        error = '{}are not {}numeric {}types. {}line: {}{}'.format(self.white, self.green, self.yellow,
                                                 self.white,self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}all elements in the {}X matrix '.format(self.white, self.cyan) + error
        return self.error+self.reset
    
    def ERROR4(self, string : str = "standard deviation"):
        error = '{}when dividing by the {}{}. {}line: {}{}'.format(self.white, self.green, string, self.white,self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}invalide value encountered '.format(self.white ) + error
        return self.error+self.reset
