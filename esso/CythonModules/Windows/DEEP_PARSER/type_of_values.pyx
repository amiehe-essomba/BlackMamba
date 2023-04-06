cdef class TYPE:
    cdef public :
        dict main_master, master, data_base
        unsigned long int line 
        str typ

    cdef:
        str error 

    def __init__(self, main_master, master, data_base, line, typ):
        self.type               = typ
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.main_master        = main_master
        self.error              = ""

    cdef TYPE(self, str main_string, str name = 'python'):

        self._return_           = None