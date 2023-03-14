from hashlib import new
from CythonModules.Linux            import array_to_list as atl  
from src.transform                  import matrix_modules as mm

def Array(master, line=1):
    try:
        if master.any(): final_value = atl.ndarray(list(master), line).List() 
        else: self.final_value =  []
    except DeprecationWarning: 
        final_value = atl.ndarray(list(master), line).List()
    except ValueError : raise ValueError
    except IndexError: raise IndexError
    except TypeError : raise TypeError
    
    
    try:
        ncol, nraw = len(final_value[0]), len(final_value)
    except IndexError:
        ncol, nraw = len(final_value), 1
    
    return final_value, nraw, ncol, final_value.copy()

def reverse(master, line=1):
    new_matrix = []
    error  =None
    
    if master:
        if master[3] is False: new_matrix = master[0].copy()
        else:
            for i in range(master[2]):
                ss = []
                for j in range(master[1]):
                    ss.append(master[0][j][i])
                new_matrix.append(ss)
    else: pass
        #final_value, error = mm.MATRIX(master[0], master[1],master[2],
        #                master[3], line).MATRIX(master[5], ctype=master[4])
    return new_matrix, error