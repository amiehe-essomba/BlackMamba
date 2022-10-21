from CythonModules.Windows.LEXER.arr                import arrError as AE
from script                                         import control_string as CS

cdef class SCANNER:
    cdef public:
        unsigned long long int line 
        dict data_base
        str master 
    cdef:
        str error, op, string_init
        list store_op, store_value
        dict _return_ 
        unsigned long long int length

    def __cinit__(self, master, data_base, line):
        self.master             = master
        self.data_base          = data_base
        self.line               = line 
        self.error              = ""
        self.store_value        = []
        self.store_op           = []
        self._return_           = {
            'values'            : None,
                'operators'     : None,
                'names'         : None,
                'type'          : 'numeric'
            }
        self.op                 = ""
        self.string_init        = ""
        self.length             = 0

    cdef DOUBLE_SCAN(self, str main_string, str String):

        self.string , self.error   = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( String, name="cython" )
        
        if not self.error:
            self.op  = self.string[ -1 ]
            
            if self.op == '+': self.length = len( self.string ) - 1
            else: self.length = len( self.string ) - 1

            self.string_init                    = self.master[ self.length : ]
            self.string_init, self.error        = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( 
                                        self.string_init, name="cython" )

            if not self.error:
                self.store_value.append( self.master[ : self.len ] )
                self.data , self.opeators, self.error = ARITHMETIC_OPERATORS( self.string_init, self.data_base,
                                                                            self.line).ARITHMETIC_OPAERATORS()#####
                if not self.error :
                    if self.opeators:
                        self.store_value.append( self.data )
                        self._return_[  'operators' ]   = self.opeators
                        self._return_[ 'values' ] = self.store_value
                    else:
                        self.store_value.append( self.data )
                        self._return_[ 'values' ] = self.store_value
                else: pass
            else: pass
        else: pass

        return self._return_, self.store_op,  self.error