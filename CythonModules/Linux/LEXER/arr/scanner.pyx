from CythonModules.Windows.LEXER.arr                import arrError as AE

cdef class SCANNER:
    cdef public:
        unsigned long long int line 
        dict data_base
        str master 
    cdef:
        str error 
    def __cinit__(self, master, data_base, line):
        self.master             = master 
        self.data_base          = data_base
        self.line               = line 
        self.error              = ""

    cdef str SCANNER(self, str main_string):
    
        self.ll = looking_for_logical_operators.LOGICAL_OPERATORS( self.master, self.data_base, self.line ) #####
        self.lb = looking_for_bool_operators.BOOLEAN_OPERATORS( self.master, self.data_base, self.line) ####

        self.test_bool, self.bool_op_, self.error = self.lb.BOOLEAN_OPAERATORS() #####

        if self.error is None:
            if not self.bool_op_:
                self.test_logical, self.logical_op_, self.error = self.ll.LOGICAL_OPAERATORS_INIT() ###
                if not self.error:
                    if not self.logical_op_: pass
                    else: self.error = AE.ERRORS( self.line ).ERROR0( main_string )
                else: self.error = AE.ERRORS( self.line ).ERROR0( main_string )
            else: self.error = AE.ERRORS( self.line ).ERROR0( main_string )
        else: self.error = AE.ERRORS( self.line ).ERROR0( main_string )

        return self.error