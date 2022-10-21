from CythonModules.Windows.DEEP_PARSER import arithmetic_checking as AR_C
from CythonModules.Windows.DEEP_PARSER import final_result

cdef class NUMERICAL:
    cdef public:
        unsigned long int line 
        dict master, data_base
    
    def:
        list value, arithmetic_operator, logical_operator, get_values
        list ar_op, num, numeric, _get_values_
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
        self.error              = ''
        
    cdef LOGICAL_CHECKING(self, list values, list arithmetic, list logical):
  
        cdef:
            unsigned long int i
            list _num_

        self.arithmetic_operator    = arithmetic
        self.logical_operator       = logical
        self.values                 = values

        for i in range(len(self.logical_operator )):
            if self.logical_operator[i] is None:
                self.get_values = [ self.values[ i ] ]
                self.ar_op      = [ self.arithmetic_operator[ i ] ]
                self.num, self.error = AR_C.NUMERICAL( self.master, self.data_base,  self.line ).ARITHMETIC_CHECKING( self.get_values, self.ar_op )
                
                if not self.error:  self.numeric.append( self.num[ 0 ] )
                else:  break

            else:
                if self.data_base['irene'] is None: pass
                else: self.data_base['irene'] = None

                _num_  = []
                self.get_values = self.values[ i ]

                for j in range( len( self.get_values ) ):
                    
                    if type( self.get_values[ j ] ) == type( dict() ):  self._get_values_   = [[ self.get_values[ j ] ]]
                    else:  self._get_values_   = [ self.get_values[ j ] ]

                    self.ar_op              = [ self.arithmetic_operator[ i ][ j ] ]
                    self.num, self.error    = AR_C.NUMERICAL(self.master, self.data_base, self.line).ARITHMETIC_CHECK( self._get_values_, self.ar_op )

                    if not self.error :  _num_.append( self.num[ 0 ] )
                    else:  break

                if not self.error :  self.numeric.append( _num_ )
                else: break

        
        if not self.error :
            return final_result.FINAL_VALUE(self.numeric, self.data_base, self.line, self.logical_operator).FINAL_VALUE(), self.error
        else: return None, self.error 