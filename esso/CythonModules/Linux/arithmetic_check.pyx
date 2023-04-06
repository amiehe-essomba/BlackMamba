cdef class ARR:
    cdef public :
        int line 
        dict master 
        dict DataBase
    def __init__(self, master, DataBase, line ):
        self.master     = master 
        self.DataBase   = DataBase
        self.line       = line 

    def ARR(self, list value, list arithmetic):
        pass