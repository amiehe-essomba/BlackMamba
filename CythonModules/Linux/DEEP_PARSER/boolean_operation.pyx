cdef class BOOLEAN:
    cdef public:
        list master 
        unsigned long int line
    cdef:
        signed int _return_ 

    def __cinit__(self, master, line):
        self.master         = master 
        self.line           = line  
        self._return_       = 0

    cdef bint BOOLEAN_OPERATION(self, list operator):
        cdef:
            unsigned long int i
            bint final = False
      
        for i in range(len(self.master)):
            if     self.master[i] == True   :  self.master[ i ] = 1
            elif   self.master[i] == False  :  self.master[ i ] = 0
            else                            :  self.master[ i ] = 1

        self._return_   = self.master[ 0 ]
        self.master     = self.master[ 1 : ]

        for i range(len(operator)):
            if   operator[i] == 'or'    : self._return_ += self.master[ i ]
            elif operator[i] == 'and'   : self._return_ *= self.master[ i ]

        if self._return_ != 0: final = True
        else:  final = False

        return final