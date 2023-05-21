import numpy as np
from numba import jit
from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from CythonModules.Windows                      import fileError    as fe

def theta( params : int = 3):
    return np.random.random( params ).reshape((params, 1))
   
@jit(nopython=True, parallel=True)
def evaluation(X, y, theta):
    upper = ( (model(X=X, theta=theta) - y) ** 2 ).sum()
    lower = ( (y - np.mean(y)) ** 2 ).sum()
    R = 1 - (upper / lower)

    return R

def model(X, theta):
    return X.dot(theta)

def predict(X : np.ndarray, theta : np.ndarray, line : int = 0):
    try:
        y_pred = model(X, theta=theta)
        return y_pred, None
    except ValueError: 
        error = ERRORS(line).ERROR6()
        return None, error
    except Exception: 
        error = ERRORS(line).ERROR5()
        return None, error
    
def MSE(X, y, theta):
    return  ( (model(X=X, theta=theta) - y) ** 2 ).mean() / 2.0

def grad(X, y, theta):
    return (X.T.dot( model(X=X, theta=theta) - y )) / X.shape[0]

@jit(nopython=True, parallel=True)
def SGD(X : np.ndarray, y : np.ndarray, theta : np.ndarray, 
        learning_rate : float = 1e-4, tot = 1e-3, line : int = 1
        ):
    
    error = None

    try:
        if X.shape[0] == y.shape[0]:
            if X.shape[1] > 1:
                if y.shape[1] == 1:
                    if theta.shape[0] == X.shape[1] : 
                        if theta.shape[0] == 1:
                            cost_history, eval, iter = [], [], 0
                            while True:
                                theta = theta - learning_rate * grad(X=X, y=y, theta=theta)
                                cost_history.append( MSE(X, y, theta) )
                                eval.append( evaluation(X=X, y=y, theta=theta) )

                                if iter < 2 : pass 
                                else:
                                    if np.abs( cost_history[iter] - cost_history[iter-1] ) <= tot : break
                                    else: pass

                                iter += 1

                            cost_history = np.array(cost_history)
                            eval = np.array(eval)
                            data = {
                                'theta'         : theta, 
                                "cost_history"  : cost_history.reshape((-1, 1))[ : iter, : ], 
                                "evaluation"    : eval.reshape((-1, 1))[ : iter, : ], 
                                "coef"          : eval[-1],
                                "max_iter"      : iter
                                }
                        else:
                            error = ERRORS(line).ERROR0("theta", theta.shape[0])
                            data = {}
                    else:
                        error = ERRORS(line).ERROR0("theta", X.shape[1])
                        data = {}
                else:
                    error = ERRORS(line).ERROR0("y", y.shape[0])
                    data = {}
            else: 
                error = ERRORS(line).ERROR0("X", X.shape[0])
                data = {}
        else:
            error = ERRORS(line).ERROR2()
            data = {}
    except IndexError : 
        error = ERRORS(line).ERROR3()
        data = {}
    except Exception:
        data = {}
        error = ERRORS(line).ERROR5()
    
    return data.copy(), error

class ERRORS:
    def __init__(self, line):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    def ERROR0(self, string: str, m):
        error = '{}should be {}({}, 1) {}ndarray. {}line: {}{}'.format(self.white, self.red, m, self.blue, 
                                                    self.white,self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}{}'.format( self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str, m):
        error = '{}should be {}({}, n) {}ndarray {}with {}n >= 2. {}line: {}{}'.format(self.white, self.red, m,
                 self.blue, self.white, self.green, self.white,self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}{}'.format( self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR2(self):
        error = '{}y.ndim()[0]. {}line: {}{}'.format(self.green, self.white,self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}X.ndim()[0] {} != '.format( self.cyan, self.red) + error

        return self.error+self.reset
    
    def ERROR3(self):
        error = '{}y.ndim()[0] {}or {}X.ndim()[1] {}== {}theta.ndim()[0]. {}line: {}{}'.format(self.green, self.white, 
                        self.cyan, self.red, self.yellow, self.white,self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}check if {}X.ndim()[0] {} == '.format( self.white, 
                                    self.cyan, self.red) + error

        return self.error+self.reset
    
    def ERROR4(self, string: str):
        error = '{}cannot be negative. {}line: {}{}'.format(self.green, self.white,self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}{} '.format( self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR5(self):
        error = '{}or matrix y. {}line: {}{}'.format(self.green, self.white,self.yellow, self.line)     
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}bad values in {}maxtrix X '.format( self.cyan, self.red) + error

        return self.error+self.reset
    
    def ERROR6(self):
        error = '{}X.ndim()[1] {}== {}theta.ndim()[0]. {}line: {}{}'.format(self.green, self.white, self.red,
                                                 self.white,self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}check if  '.format( self.white) + error
    