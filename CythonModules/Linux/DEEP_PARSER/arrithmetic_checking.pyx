from CythonModules.Windows.DEEP_PARSER  import arr_deep_checking_init as arr
from CythonModules.Linux.DEEP_PARSER    import error
from script.MATHS                       import mathematics
from script.PARSER                      import numerical_value as NV

cdef class NUMERICAL:
    cdef public:
        unsigned long int line 
        dict master, data_base
    cdef:
        list value, arithmetic_operator, numeric, calculations, _return_
        dict get_values, _get_values_
        str error, type
        
    def __cinit__(self, master, data_base, line ):
            self.line               = line 
            self.master             = master
            self.data_base          = data_base
            self.value              = []
            self.arithmetic_operator= []
            self.calculations       = []
            self.numeric            = []
            self.error              = ''
            self._return_           = []
            self.get_values         = {}
            self._get_values_       = {}
            self.type               = ''

    cdef ARITHMETIC_CHECKING(self, list values, list arithmetic, str main_string):
        self.values                     = values
        self.arithmetic_operator        = arithmetic

        cdef:
            unsigned int i , j, w
            unsigned long int len_val
            str history_of_op = "", string, sign
            list __values__, operators
            bint key
            unsigned long long int length_values = len(self.arithmetic_operator)
            str main__main = main_string

        for i in range(length_values):
            if self.arithmetic_operator[i] is None:
                try:
                    self.get_values             = self.values[ i ][ 0 ]
                    self.type                   = self.get_values[ 'type' ]

                    self._return_, self.error   = NV.TYPE( self.master, self.get_values, self.data_base, self.line, 
                                                self.type ).TYPE( main__main, name="cython" )
                    if not self.error : self.numeric.append( self._return_[ 0 ] )
                    else:  break
                except IndexError:
                    self.error = error.ERRORS( self.line ).ERROR0( main_string)
                    break
            else:
                if len( self.values[ i ] ) > len( self.arithmetic_operator[i] ):
                    len_val                             = len( self.values[ i ] )
                    for j in range( len_val ):
                        self.type                        = self.values[ i ][ j ][ 'type' ]

                        self._return_, self.error       = NV.TYPE( self.master, self.values[ i ][ j ], self.data_base,
                                                          self.line, self.type ).TYPE( main__main, name="cython" )
                        if  not self.error:
                            if j != len_val - 1:
                                self.calculations.append( [ self._return_[0] ] )
                                self.calculations.append( self.arithmetic_operator[i][ j ] )
                            else: self.calculations.append( [ self._return_ [0]] )
                        else:  break
                
                    if not  self.error:
                        history_of_op   = ''
                        for w in range(len(self.calculations)):
                            if type( self.calculations[w] ) == type( str() ):
                                history_of_op += self.calculations[w]
                            else:  pass

                        __values__, self.error       = mathematics.MAGIC_MATH_BASE( self.calculations, self.data_base,
                                                                history_of_op, self.line ).MATHS_OPERATIONS(name="cython")
                        if not self.error:
                            self.numeric.append( __values__[ 0 ] )
                            self.calculations = []
                        else:   break
                    else:  break
                elif len( self.values[ i ] ) == len( self.arithmetic_operator[i] ):
                    if type( self.arithmetic_operator[i][ 0 ] ) == type( list() ):  sign = '+'
                    else:
                        if len( self.arithmetic_operator[i] ) == 1:  sign = self.arithmetic_operator[i][ 0 ]
                        else:
                            key = False
                            for w in range(len(self.arithmetic_operator[i])):
                                if type( self.arithmetic_operator[i][w] ) == type( list( ) ):
                                    key = True
                                    break
                                else: pass

                            if key == False: sign = self.arithmetic_operator[i][ 0 ]
                            else:  sign = ''

                    if sign in [ '-' ]: self.calculations.append( sign )
                    else:  pass

                    len_val = len( self.values[ i ] )

                    if len( self.arithmetic_operator[i] ) == 1:
                        self._get_values_ = self.values[ i ][ 0 ]

                        try:
                            self.type                   = self._get_values_[ 'type' ]
                            self._return_, self.error   = NV.TYPE( self.master, self._get_values_, self.data_base, self.line,
                                                                              self.type ).TYPE( main__main, name='cython' )
                            if not self.error :
                                self.calculations.append( [ self._return_[ 0 ] ] )
                                history_of_op      = ''
                                for w in range(len(self.calculations)):
                                    if type( self.calculations[w] ) == type( str() ): history_of_op += self.calculations[w]
                                    else:  pass

                                __values__, self.error = mathematics.MAGIC_MATH_BASE( self.calculations,
                                                    self.data_base, history_of_op, self.line ).MATHS_OPERATIONS(name='cython')

                                if not self.error:
                                    self.numeric.append( __values__[ 0 ] )
                                    self.calculations = []
                                else:  break
                            else : break

                        except TypeError :
                            self._return_, self.error   = arr.AR_DEEP_CHECKING( self.master, self._get_values_,
                                        self.arithmetic_operator[i][ 0 ], self.data_base, self.line ).INIT( main__main )
                            if not self.error:
                                self.calculations.append( [ self._return_[ 0 ] ])
                                history_of_op      = ''
                                for w in range(len(self.calculations)):
                                    if type( self.calculations[w] ) == type( str() ):
                                        history_of_op += self.calculations[w]
                                    else:  pass
                            
                                __values__, self.error = mathematics.MAGIC_MATH_BASE( self.calculations,
                                                    self.data_base, history_of_op, self.line ).MATHS_OPERATIONS(name='cython')

                                if not self.error:
                                    self.numeric.append( __values__[ 0 ] )
                                    self.calculations = []
                                else:  break
                            else: break
                    else:
                        for j in range( len_val ):   
                            if type( self.values[ i ][ j ] ) == type( dict() ) :
                                self._get_values_ = self.values[ i ][ j ]
                                self.type = self._get_values_[ 'type' ]
                                self._return_, self.error = NV.TYPE( self.master, self._get_values_, self.data_base, self.line,
                                                            self.type ).TYPE( main__main, name='cython' )
                                if not self.error:
                                    if j != self.len_val - 1:
                                        try:
                                            self.calculations.append( [ self._return_[ 0 ] ] )
                                            if self.calculations[ 0 ] == '-':  
                                                self.calculations.append( self.arithmetic_operator[i][ j + 1 ] )
                                            else:  self.calculations.append(self.arithmetic_operator[i][ j ])
                                        except TypeError:
                                            self.calculations.append( [ self._return_[ 0 ] ] )
                                            self.calculations.append( self.arithmetic_operator[i][ j ] )
                                    else:  self.calculations.append( [ self._return_[ 0 ] ] )
                                else: break
                            else:
                                self._return_, self.error = arr.AR_DEEP_CHECKING(self.master, self.values[ i ][ j ],
                                                self.arithmetic_operator[i][ j ], self.data_base, self.line).INIT( main__main )

                                if not self.error:
                                    if j != len_val - 1:
                                        try:
                                            self.calculations.append( [ self._return_[ 0 ] ] )
                                            self.calculations.append( self.arithmetic_operator[i][ j + 1 ] )
                                        except TypeError:
                                            self.calculations.append( [ self._return_[ 0 ] ] )
                                            self.calculations.append( self.arithmetic_operator[i][ j ] )
                                    else:  self.calculations.append( [ self._return_[ 0 ]] )
                                else: break
                        if not self.error:
                            history_of_op  = ''
                            for w in range(len(self.calculations)):
                                if type( self.calculations[w] ) == type( str() ):  history_of_op += self.calculations[w]
                                else: pass

                            __values__, self.error = mathematics.MAGIC_MATH_BASE(self.calculations,
                                                self.data_base, history_of_op, self.line) .MATHS_OPERATIONS(name="cython")

                            if self.error is None:
                                self.numeric.append( __values__[ 0 ] )
                                self.calculations = []
                            else: break
                        else:  break
                
                else:
                    sign               = ''
             
                    self._return_, self.error = arr.AR_DEEP_CHECKING(self.master, self.values[ i ],
                                                       self.arithmetic_operator[i], self.data_base, self.line).INIT( main__main )

                    if not self.error:
                        history_of_op  =  ''
                        self.calculations.append( [ self._return_[ 0 ]] )
                        for w in range(len(self.calculations)):
                            if type( self.calculations[w] ) == type( str() ):  history_of_op += self.calculations[w]
                            else:  pass
                        
                        __values__, self.error = mathematics.MAGIC_MATH_BASE(self.calculations,
                                            self.data_base, history_of_op, self.line).MATHS_OPERATIONS(name = 'cython')

                        if not self.error:
                            self.numeric.append( __values__[ 0 ][ 0 ] )
                            self.calculations = []
                        else:  break
                    else:  break
        
        return  self.numeric, self.error