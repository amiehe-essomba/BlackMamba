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
        try:
            ncol, nraw = len(final_value), len(final_value[0])
            new_list = []
            for i in range(ncol):
                new_list += final_value[i]
        except TypeError:
            ncol, nraw = len(final_value), 1
            new_list = final_value.copy()
    except IndexError:
        new_list = final_value.copy()
        ncol, nraw = len(final_value), 1
        
    return final_value, nraw, ncol, new_list

def reverse(master, line=1):
    final_value, error = mm.MATRIX(master[0], master[1],master[2],
                        master[3], line).MATRIX(master[5], ctype=master[4])
    
    return final_value, error