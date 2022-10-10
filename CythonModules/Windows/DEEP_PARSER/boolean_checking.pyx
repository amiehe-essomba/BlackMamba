from CythonModules.Windows.DEEP_PARSER import logical_checking as LO_C
from CythonModules.Windows.DEEP_PARSER import boolean_operation as BO

cdef class NUMERICAL:
    cdef public:
        unsigned long int line 
        dict master, data_base
    
    def:
        list value, arithmetic_operator, logical_operator, get_values
        list ar_op, num, numeric, _get_values_, boolean_operator, l_op
        str error
    
    def __cinit__(self, master, data_base, line ):
        self.line               = line 
        self.master             = master
        self.data_base          = data_base
        self.value              = []
        self.arithmetic_operator= []
        self.logical_operator   = []
        self.calculations       = []
        self.get_values         = []
        self.ar_op              = []
        self.num                = []
        self.numeric            = []
        self._return_           = []
        self._get_values_       = []
        self.boolean_operator   = []
        self.l_op               = []
        self.error              = ''

    cdef BOOLEAN_CHECKING(self, list values, lost arithmetic, list logical, list boolean ):
        cdef:
            unsigned long int i, j
            unsigned long long int len_val 
            list _num_, _ar_op_, _l_op_
            bint bool_value

        self.arithmetic_operator        = arithmetic
        self.logical_operator           = logical
        self.bool_operator              = boolean
        self.values                     = values

        for i in range(len(self.bool_operator)):
            if self.bool_operator[i] is None:
                self.get_values         = [ self.values[ i ] ]
                self.l_op               = [ self.logical_operator[ i ] ]
                self.ar_op              = [ self.arithmetic_operator[ i ] ]
                
                self.num, self.error    = LO_C.NUMERICAL( self.master, self.data_base,
                                                  self.line ).LOGICAL_CHECKING(self.get_values, self.ar_op, self.l_op )
                if self.error is None:  self.numeric.append( self.num )
                else:  break
            
            else:
                if self.data_base['irene'] is None: pass
                else: self.data_base['irene'] = None
                
                self.get_values     = self.values[ i ]
                self.l_op           = self.logical_operator[ i ]
                self.ar_op          = self.arithmetic_operator[ i ]
                len_val             = len( self.values[ i ])
                _num_               = []

                for j in range( len_val ):
                   
                    if self.ar_op[ j ] is None: _ar_op_    = [[ self._ar_op_ ]]
                    else: _ar_op_    = [ self._ar_op_ ]
                    
                    if self.l_op[ j ] is None: _l_op_     = [[ self._l_op_ ]]
                    else:  _l_op_     = [ self._l_op_ ]
              
                    if type( self.get_values[ j ] ) == type( dict() ):  self._get_values_   = [ [ self.get_values[ j ] ] ]
                    else:  self._get_values_   = [ self.get_values[ j ] ]

                    self.num, self.error = LO_C.NUMERICAL( self.master, self.data_base,
                                            self.line).LOGICAL_CHECKING( self._get_values_, self._ar_op_, self._l_op_)
                    if not self.error :  _num_.append( self.num )
                    else: break
                    
                if not self.error:
                    bool_value = BO.BOOLEAN(_num_, self.line ).BOOLEAN_OPERATION( self.bool_operator[i] )
                    self.numeric.append( bool_value )
                else: break

        return self.numeric, self.error
