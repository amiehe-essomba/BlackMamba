import numpy as np
import pandas as pd

cdef class forest:
    cdef public:
        dict master
        unsigned long int line
    cdef:
        error 
    def __cinit__(master, line):
        self.master = master
        self.line   = line 
    cdef forest(self):
        cdef:
            list keys, values
            tuple I, F, C, S = (type(int())), (type(float())), (type(complex())), (type(str()))
            tuple L, T, D, A = (type(list())), (type(tuple())), (type(dict())), (type(np.array([1]))) 
            tuple R = (type(range(1)))
            list names = ['Integer', 'Float', 'String', 'Complex', 'List', 'Tuple', 'Range', 'None', 'Dictionary', 'Ndarray', 'Table']
            unsigned long int i, j, length, n
            str string = ""
            
        
        if self.master:
            keys, values = list( self.master.keys() ), list( self.master.values()) 
            length = len( values )
            if length < 10:
                if length % 2 == 0:
                    n = length // 2
                    string += " " * n + '|' + " " * n + "\n"
                    string += " " * n + '|' + " " * n + "\n"
                    string += "-" * length + '\n'

                              
            else: pass

            for i in range(length):
                if type( values[i] ) == D[0]:
                    pass 
                elif type(values[i]) == I[0]:

                
        else: pass





