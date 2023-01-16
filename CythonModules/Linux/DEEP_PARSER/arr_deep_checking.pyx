from CythonModules.Linux.DEEP_PARSER        import arr_deep_checking_init as arr
from script.MATHS                           import mathematics
from script.PARSER                          import numerical_value as NV

cdef class AR_DEEP_CHECKING:
    cdef public:
        dict data_base
        unsigned long int line 
        dict master 
        list operators, values
    cdef :
        str error 
        list  index, numeric
        list _get_values_, calculations
    
    def __cinit__(self, master, values, operators, data_base, line):
        self.master         = master 
        self.data_base      = data_base 
        self.line           = line 
        self.operators      = operators
        self.values         = values
        self.error          = ""
        self.index          = []
        self.numeric        = []
        self.calculations   = []
        self._get_values_   = values

    cdef INIT_INIT(self, str main__main ):
        cdef:
            unsigned long int k, idd, s
            unsigned long int sub_len_val = len( self._get_values_ )
            unsigned long int sub_len_op  = len( self.operators )
            dict sub_values
            str typ , sign, string
            bint key = False
            str history_of_op = ""
            str main_string = main__main 

        if sub_len_val > sub_len_op     :
            for k in range( len(self._get_values_ )):
                if type( self._get_values_[ k ] ) == type( dict() ):
                    sub_values     = self._get_values_[ k ]
                    typ = sub_values[ 'type' ]

                    self.num, self.error = NV.TYPE( self.master, sub_values, self.data_base, 
                                        self.line, typ ).TYPE( main__main, name='cython' )
                    if not self.error:
                        if k != (sub_len_val - 1):
                            self.calculations.append( [ self.num[ 0 ] ] )
                            self.calculations.append( self.operators[ k ] )
                        else: self.calculations.append( [ self.num[ 0 ] ] )
                    else: break
                else:
                    self.num, self.error = arr.AR_DEEP_CHECKING(self.master, self.data_base,self._get_values_[ k ], 
                                    self.operators[ 0 ][ k ], self.line).INIT( main__main)
                                        
                    if not self.error:
                        if k != (sub_len_val - 1):
                            self.calculations.append( [ self.num[ 0 ] ] )
                            self.calculations.append(self.operators[ k ] )
                        else: self.calculations.append( [ self.num[ 0 ] ] )
                    else: break

            if not self.error:
                history_of_op = ""
                for k in range(len(self.calculations)):
                    if type( self.calculations[ k ] ) == type( str() ):
                        history_of_op += self.calculations[ k ]
                    else: pass

                self.num, self.error = mathematics.MAGIC_MATH_BASE(self.calculations, self.data_base,
                                                            history_of_op, self.line).MATHS_OPERATIONS(name = "cython")
                if self.error is None:
                    self.numeric.append( self.num[ 0 ] )
                else: pass
            else: pass

        elif sub_len_val == sub_len_op  :
            if type(  self.operators[ 0 ] ) == type( list() ): sign = ''
            else:
                sign            = self.operators[ 0 ]
                self.operators  = self.operators[ 1 : ]

                if sign in [ '-' ]: self.calculations.append( sign )
                else: pass

            for k in range(len(self._get_values_)):
                if type( self._get_values_[ k ]) == type( dict() ):
                    typ       = self._get_values_[ k ][ 'type' ]
                    self.num, self.error = NV.TYPE( self.master, self._get_values_[ k ], self.data_base, self.line,
                                                                                typ ).TYPE( main_string, name="cython" )
                    if not self.error:
                        if k != (sub_len_val - 1):
                            self.calculations.append( [ self.num[ 0 ]] )
                            self.calculations.append( self.operators[ k ] )
                        else: self.calculations.append( [ self.num[ 0 ] ] )
                    else: break
                else:
                    self.num, self.error = arr.AR_DEEP_CHECKING(self.master, self._get_values_[ k ],
                                    self.operators[ k ], self.data_base, self.line).INIT( main_string )

                    if not self.error:
                        if k != (sub_len_val - 1):
                            self.calculations.append( [ self.num[ 0 ] ] )
                            self.calculations.append( self.operators[ k ] )
                        else: self.calculations.append( [ self.num[ 0 ] ] )
                    else: break
            if not self.error:
                history_of_op = ""
                for k in range(len(self.calculations)):
                    if type(self.calculations[ k ]) == type(str()):  history_of_op += self.calculations[ k ]
                    else: pass

                self.num, self.error = mathematics.MAGIC_MATH_BASE(self.calculations, self.data_base,
                                                        history_of_op, self.line).MATHS_OPERATIONS(name="cython")

                if self.error is None:
                    self.numeric.append(self.num[ 0 ])
                else: pass
            else: pass

        else:
            if type( self.operators[ 0 ] ) == type( list() ):  sign = '+'
            else:
                sign            = self.operators[ 0 ]
                self.operators  = self.operators[ 1 : ]

                if sign in [ '-' ]: self.calculations.append( self.sign )
                else: pass

            for k in range(len(self._get_values_)):
                if type( self._get_values_[ k ] ) == type( dict() ):
                    typ               = self._get_values_[ k ] [ 'type' ]
                    self.num, self.error    = NV.TYPE( self.master, self._get_values_[ k ], self.data_base, self.line,
                                                                                typ ).TYPE( main_string , name='cython')

                    if not self.error:
                        if k != ( sub_len_val - 1):
                            try:
                                self.calculations.append( [ self.num[0]] )
                                self.calculations.append( self.operators[ k + 2 ] )
                            except TypeError:
                                self.calculations.append( [ self.num[0]] )
                                self.calculations.append( self.operators[k + 1] )
                            except IndexError:
                                self.calculations.append( [ self.num[0] ] )
                                self.calculations.append( self.operators[ k ] )
                        else:  self.calculations.append( [ self.num[0] ] )
                    else: break
                else:
                    self.num, self.error = arr.AR_DEEP_CHECKING(self.master, self._get_values_[k],
                                                self.operators[ k ], self.data_base, self.line).INIT( main_string )

                    if not self.error:
                        if k != (sub_len_val-1):
                            try:
                                self.calculations.append( [ self.num[ 0 ] ] )
                                self.calculations.append( self.operators[ k + 1 ] )
                            except TypeError:
                                self.calculations.append( [ self.num[ 0 ] ] )
                                self.calculations.append( self.operators[ k + 2 ] )
                        else:  self.calculations.append( [ self.num[ 0 ] ] )
                    else: break
            if not self.error :
                history_of_op = ""
                for k in range(len(self.calculations)):
                    if type( self.calculations[k] ) == type( str() ):  history_of_op += self.calculations[k]
                    else: pass

                self.num , self.error = mathematics.MAGIC_MATH_BASE( self.calculations, self.data_base,
                                                        history_of_op, self.line).MATHS_OPERATIONS(name="cython")
                if self.error is None:
                    self.numeric.append( self.num[0] )
                else: pass
            else: pass

        return self.numeric, self.error