cdef class FRAME:
    cdef public:
        dict master 
        unsigned long int line
    cdef:
        dict error 
    def __cinit__(self, master, line):
        self.master = master
        self.line   = line
        self.error  = {"s":None}
    
    cdef FRAME(self):
        cdef:
            list keys, values, typ
            unsigned long length, i, j
            list store = []
            unsigned long l

        typ=[type(None), type(int()), type(float()), type(bool()), type(str())]

        if type(self.master['data']) == type(dict()) :
            keys = list(self.master['data'].keys())
            values = list(self.master['data'].values())
            length = len(keys)
            if len(keys) <= 10:
                if values:
                    for i in range(length):
                        if type(values[i]) == type(list()):
                            if len(values[i]) == length(values[0]):
                                if values[i]:
                                    l = len(keys[i])
                                    for j in range(len(values[i])):
                                        if type(values[i][j]) in typ: 
                                            if len(str(str(values[i][j]))) > l: l = len(str(str(values[i][j])))
                                            else: pass 
                                            values[i][j] = str(values[i][j])
                                        else: break
                                    store.append(l)
                                else: break 
                            else: break
                        else: break
                    if self.error['s'] is None:
                        if len(values[0]) <=10:
                            
                            
            else: pass

