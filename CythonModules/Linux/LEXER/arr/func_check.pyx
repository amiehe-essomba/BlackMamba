from script                                         import control_string as CS
from CythonModules.Windows.LEXER.arr                import arrError as AE

cdef class FUNC:
    cdef public:
        unsigned long long int line 
        dict data_base
        str master 
    cdef:
        str error, new_string, nextchar 

    def __cinit__(self, master, data_base, line):
        self.master             = master
        self.data_base          = data_base
        self.line               = line 
        self.error              = ""
        self.new_string         = ""
        self.nextchar           = ""

    cdef str FUNC_CHECK(self, str string, bint end = True):
        self.new_string         = string
 
        if self.new_string[ : 4 ] == 'func':
            try:
                self.nextchar = self.new_string[ 4 : ]
                self.nextchar, self.error = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( self.nextchar, name="cython" )
                if not self.error:
                    if self.nextchar[ 0 ] == '(':
                        self.error = AE.ERRORS( self.line ).ERROR6( self.master, 'func( ... )' )
                    elif self.nextchar[ 0 ] == '[':
                        self.error = AE.ERRORS( self.line ).ERROR6( self.master, 'func[ ... ]' )
                    elif self.nextchar[ 0 ] == '{':
                        self.error = AE.ERRORS( self.line ).ERROR6( self.master, 'func{ ... }' )
                    elif self.nextchar[ 0 ] == '"':
                        self.error = AE.ERRORS( self.line ).ERROR6( self.master, 'func" ... "' )
                    elif self.nextchar[ 0 ] == "'":
                        self.error = AE.ERRORS( self.line ).ERROR6( self.master, "func' ... '" )
                    else: pass
                else:
                    if end is True: self.error = AE.ERRORS( self.line ).ERROR6( self.master, 'func' )
                    else:
                        if self.new_string == 'func': self.error = AE.ERRORS( self.line ).ERROR6( self.master, 'func' )
                        else: self.error = None

            except IndexError:
                if end is True: self.error = AE.ERRORS( self.line).ERROR6( self.master, 'func' )
                else:
                    if self.new_string == 'func': self.error = AE.ERRORS( self.line ).ERROR6( self.master, 'func' )
                    else: self.error = ""
        else: self.error = ""

        return self.error