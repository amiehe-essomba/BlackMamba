from sklearn.datasets import  make_regression
import numpy as np 

def R(
        samples     : int, 
        features    : int, 
        noise       : int, 
        target      : int = 1, 
        seed        : int = None, 
        shuffle     : bool = True, 
        polynomial  : int = None  
        ):
    
    X, Y = make_regression(
        n_samples=samples, 
        n_features=features, 
        noise=noise, 
        n_targets=target, 
        random_state=seed,
        shuffle=shuffle, 
        )
    
    error = None
    if polynomial is None: pass 
    else:
        my_list = sorted(range(1, polynomial+1), reverse=True)
        XX = [X ** i for i in my_list]
        X = np.column_stack((XX)).reshape((-1, len(my_list)))

    bias = np.ones((X.shape[0], 1))
    MATRIX = np.column_stack((X, bias)).reshape((-1, X.shape[1]+1))

    data = {"X" : X , "matrix" : MATRIX, "target" : Y.reshape((-1, 1)), "bias" : bias}

    return data, error


