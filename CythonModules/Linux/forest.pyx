import numpy as np
import pandas as pd
from script.STDIN.LinuxSTDIN import ascii 
from IDE.EDITOR              import test

cdef class forest:
    cdef public:
        dict master
        unsigned long int line
    cdef:
        dict error 
        dict acs
        str red, blue, green, white, reset
        unsigned long long int max_x, max_y 

    def __cinit__(master, line):
        self.master = master
        self.line   = line 
        self.acs['s'] = ascii.frame(True)
        self.red = bm.fg.rgb(255, 0, 0)
        self.green = bm.fg.rgb(0, 255, 0)
        self.white = bm.fg.rgb(255, 255, 255)
        self.reset = bm.init.reset 
        self.blue  = bm.fg.blue_L
        self.max_x, self.max_y      = test.get_linux_ter()

    cdef forest(self, dict key = {"key":None}):
        cdef:
            list keys, values
            tuple I, F, C, S = (type(int())), (type(float())), (type(complex())), (type(str()))
            tuple L, T, D, A = (type(list())), (type(tuple())), (type(dict())), (type(np.array([1]))) 
            tuple R = (type(range(1)))
            list names = ['Integer', 'Float', 'String', 'Complex', 'List', 'Tuple', 'Range', 'None', 'Dictionary', 'Ndarray', 'Table']
            unsigned long int i, j, length, n
            str string = ""
            bint  sub_k =False
            L_X = max_x // 2
        
        if self.master:
            if key['key'] is None:
                keys, values = list( self.master.keys() ), list( self.master.values()) 
                length = len( values )
                for i in range(length):
                    pass

                if length < 10:
                    if length % 2 == 0:
                        n = length // 2
                        string += " " * n + '|' + " " * n + "\n"
                        string += " " * n + '|' + " " * n + "\n"
                        string += "-" * length + '\n'

                              
                else: pass
            else: pass

            for i in range(length):
                if type( values[i] ) == D[0]:
                    pass 
                elif type(values[i]) == I[0]:

                
        else: pass





