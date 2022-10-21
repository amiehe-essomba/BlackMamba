from CythonModules.Windows.DEEP_PARSER          import error as err
from CythonModules.Windows.DEEP_PARSER          import conversion
from CythonModules.Windows.DEEP_PARSER          import get_data

cdef class LOGICAL:
    cdef public:
        list master
        dict data_base
        unsigned long int line
        str logical 
    
    cdef:
        bint _return_
        str error
        list all_type, number

    def __cinit__(self, master,logical ,data_base, line):
        self.master         = master 
        self.logical        = logical
        self.data_base      = data_base 
        self.line           = line 
        self._return_       = False
        self.error          = ""
        self.all_type       = [ type(int()), type(bool()), type(float()) ]
        self.number         = []

    
    cdef bint OPERATIONS(self, str operation, bint _key_ = False):
        cdef:
            str ob1, ob2
            str string = ""

        try:
            if   operator == '==':  self._return_ = self.master[ 0 ] == self.master[ 1 ]
            elif operator == '>=':  self._return_ = self.master[ 0 ] >= self.master[ 1 ]
            elif operator == '<=':  self._return_ = self.master[ 0 ] <= self.master[ 1 ]
            elif operator == '!=':  self._return_ = self.master[ 0 ] != self.master[ 1 ]
            elif operator == '>' :  self._return_ = self.master[ 0 ] >  self.master[ 1 ]
            elif operator == '<' :  self._return_ = self.master[ 0 ] <  self.master[ 1 ]
            elif operator == 'in':
                if type(self.master[ 1 ] ) in [ type( list() ), type( str( ) ), type( tuple() ) ]:
                    self._return_ = self.master[ 0 ] in self.master[ 1 ]
                else: self.error = err.ERRORS( self.line ).ERROR6( self.master[ 1 ] )
            elif operator == 'not in':
                if type(self.master[ 1 ] ) in [ type( list() ), type( str( ) ), type( tuple() ) ]:
                    self._return_ = self.master[ 0 ] not in self.master[ 1 ]
                else:  self.error = err.ERRORS( self.line ).ERROR6( self.master[ 1 ] )

            elif operator == 'is'       :  self._return_ = self.master[ 0 ] is self.master[ 1 ]
            elif operator == 'is not'   :  self._return_ = self.master[ 0 ] is not self.master[ 1 ]
            elif operator == 'not'      :  self._return_ = not self.master
            elif operator == '?':
                string = conversion.CONVERSION( line = self.line  ).CONVERSION( master=self.master )
                self.data_base['irene'] = True
        except TypeError:
            ob1 = conversion.CONVERSION( line = self.line  ).CONVERSION( master=self.master[ 0 ])
            ob2 = conversion.CONVERSION( line = self.line  ).CONVERSION( master=self.master[ 1 ])

            if _key_ is False:
                if operator in [ '==', '!=', '<=', '>=', '<', '>']:
                    if type( self.master[ 0 ] ) in [ type( tuple() ), type( list()) ]:
                            if type( self.master[ 1 ] ) in self.all_type:
                                self._return_, self.number, self.error = get_data.GET(master=list(self.master[ 0 ]), logical=self.logical,
                                        line=self.line).GET_DATA(object=self.master[ 1 ])
                            else:  self.error = err.ERRORS(self.line).ERROR7(operator, ob1, ob2)
                    else: self.error = err.ERRORS( self.line ).ERROR7( operator, ob1, ob2 )
                else: self.error = err.ERRORS( self.line ).ERROR7( operator, ob1, ob2 )
            else:
                if self.master[ 0 ] in self.all_type:
                    if self.master[ 1 ] in self.all_type: pass
                    else: self.error = err.ERRORS( self.line ).ERROR7( operator, ob1, ob2 )
                else:  self.error = err.ERRORS( self.line ).ERROR7( operator, ob1, ob2 )

        if string:  return [string], self.error, False
        else:  return self._return_, self.error, True

