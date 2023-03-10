import numpy as np

cdef class ndarray:
    cdef :
        public int line 
        public list listOfValue
    cdef:
        type typ1 
        type typ2 

    def __init__(self, listOfValue, line):
        self.listOfValue        = listOfValue
        self.line               = line 
        self.typ1               = type(np.array([]))
        self.typ2               = type(list())
    
    cpdef list List(self):
        cdef :
            int x 
            list my_list = []
            bint key = False

        for x in range(len(self.listOfValue)):
            if type(self.listOfValue[ x ]) == self.typ1: 
                if self.listOfValue[ x ].any() is False: self.listOfValue[ x ] = []
                else: self.listOfValue[ x ] = ndarray(list(self.listOfValue[ x ]), self.line).L1()
            elif type(self.listOfValue[ x ]) == self.typ2:
                if self.listOfValue[ x ]: self.listOfValue[ x ] = ndarray(self.listOfValue[ x ], self.line).L1()
                else: self.listOfValue[ x ] = []
            else:  
                key = True
                my_list.append(self.listOfValue[ x ])
        if key is True: return my_list
        else: return self.listOfValue
    
    cdef list L1(self):
        cdef :
            int x 
            list my_list = []
            bint key = False

        for x in range(len(self.listOfValue)):
            if type(self.listOfValue[ x ]) == self.typ1: 
                if self.listOfValue[ x ].any() is False: self.listOfValue[ x ] = []
                else: self.listOfValue[ x ] = ndarray(list(self.listOfValue[ x ]), self.line).L2()
            elif type(self.listOfValue[ x ]) == self.typ2:
                if self.listOfValue[ x ]: self.listOfValue[ x ] = ndarray(self.listOfValue[ x ], self.line).L2()
                else: self.listOfValue[ x ] = []
            else:  
                key = True
                my_list.append(self.listOfValue[ x ])
        if key is True: return my_list
        else: return self.listOfValue

    cdef list L2(self):
        cdef :
            int x
            list my_list = []
            bint key = False

        for x in range(len(self.listOfValue)):
            if type(self.listOfValue[ x ]) == self.typ1: 
                if self.listOfValue[ x ].any() is False: self.listOfValue[ x ] = []
                else: self.listOfValue[ x ] = ndarray(list(self.listOfValue[ x ]), self.line).L1()
            elif type(self.listOfValue[ x ]) == self.typ2:
                if self.listOfValue[ x ]: self.listOfValue[ x ] = ndarray(self.listOfValue[ x ], self.line).L1()
                else: self.listOfValue[ x ] = []
            else:  
                key = True
                my_list.append(self.listOfValue[ x ])
        if key is True: return my_list
        else: return self.listOfValue

        return self.listOfValue