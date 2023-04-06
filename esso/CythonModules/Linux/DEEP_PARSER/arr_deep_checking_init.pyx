from CythonModules.Linux.DEEP_PARSER        import arr_deep_checking as arr
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
        self.operators      = []
        self.values         = []
        self.index          = []
        self.numeric        = []
        self._get_values_   = values
        self.calculations   = []

    cdef INIT(self, str main__main ):
        cdef:
            unsigned long int k, idd, s
            unsigned long int sub_len_val = len( self._get_values_ )
            unsigned long int sub_len_op  = len( self.operators )
            dict sub_values
            str typ , sign, history_of_op, string
            bint key = False

        if sub_len_val > sub_len_op:
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
                                    self.operators[ 0 ][ k ], self.line).INIT_INIT( main__main)
                                        
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
                                                            history_of_op,self.line).MATHS_OPERATIONS(name = "cython")
                if self.error is None:
                    self.numeric.append( self.num[ 0 ])
                else: pass
            else: pass
        else:
            if type( self.operators[ 0 ]) == type( list() ):  sign       = '+'
            else:
                sign            = self.operators[ 0 ]
                self.operators  = self.operators[ 1 : ]
                self.calculations.append( sign )

            for k in range( len(self._get_values_ )):
                if type( self._get_values_[ k ] ) == type( dict() ):
                    typ               = self._get_values_[ k ][ 'type' ]
                    self.num, self.error    = NV.TYPE( self.master, self._get_values_[ k ], self.data_base, self.line,
                                                                        typ ).TYPE( main__main, name="cython" )
                    if not self.error:
                        if k != (sub_len_val - 1):
                            if not self.index:
                                try:
                                    self.calculations.append( [ self.num[ 0 ]] )
                                    self.calculations.append( self.operators[ k ])
                                except IndexError: self.calculations.append( self.operators[ k ] )
                            else:
                                self.calculations.append( [ self.num[ 0 ] ] )
                                self.calculations.append( self.operators[ k + self.index[ -1 ] + 1 ])
                        else:  self.calculations.append( [ self.num[ 0 ] ] )
                    else: break
                else:
                    if type( self.operators[ k ] ) == type( list()):
                        self.num, self.error = arr.AR_DEEP_CHECKING(self.master,  self._get_values_[ k ], self.operators[ k ], self.data_base,
                                        self.line).INIT_INIT( main__main )
                    else:
                        idd    = 0
                        for s in range(len(self.operators[k : ])):
                            if type( self.operators[k : ][s] ) == type( list() ):
                                idd = s
                                break
                            else: pass
                        
                        self.index.append( idd )
                        self.num, self.error = arr.AR_DEEP_CHECKING(self.master, self._get_values_[ k ], self.operators[k + idd ], self.data_base,
                                    self.line).INIT_INIT(main__main)
                        
                    if not self.error:
                        key = True
                        if k != (sub_len_val - 1):
                            try:
                                self.calculations.append( [ self.num[ 0 ] ] )
                                self.calculations.append( self.operators[ k + 1 ] )
                            except TypeError:
                                self.calculations.append( [ self.num[ 0 ] ] )
                                self.calculations.append( self.operators[ k + 2 ] )
                        else:  self.calculations.append( [ self.num[ 0 ] ] )
                    else: break

            if not self.error:
                history_of_op = ""
                for k in range(len(self.calculations)):
                    if type(self.calculations[ k ]) == type(str()):  
                        string = self.calculations[ k ]
                        history_of_op += string
                    else:  pass
                self.num, self.error = mathematics.MAGIC_MATH_BASE(self.calculations, self.data_base,
                                                            history_of_op, self.line).MATHS_OPERATIONS(name="cython")

                if not self.error:  self.numeric.append( self.num[ 0 ] )
                else:pass
            else: pass


        return self.numeric, self.error
