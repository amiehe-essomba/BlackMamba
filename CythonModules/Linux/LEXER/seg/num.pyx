cdef class NUMBER:
    cdef public :
        unsigned long long int number 
    cdef :
        str Open 

    def __cinit__(self):
        self.number     = int(1e10)
        self.Open       = ''

    cdef str OPENING(self,  str string ):
        self.open = ''

        if   string == ']'      : self.Open   = '['         # opening and closing brackets
        elif string == ')'      : self.Open   = '('         # opening ans closing parentheses
        elif string == '}'      : self.Open   = '{'         # ......
        elif string == '"'      : self.Open   = '"'         # ......
        elif string == "'"      : self.Open   = "'"         # ......

        return self.Open                                    # returning value