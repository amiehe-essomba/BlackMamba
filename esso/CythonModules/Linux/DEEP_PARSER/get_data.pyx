from CythonModules.Linux.DEEP_PARSER          import error as err
from CythonModules.Linux.DEEP_PARSER          import conversion
from CythonModules.Linux.DEEP_PARSER          import error

cdef class GET:
    cdef public:
        unsigned long int line 
        str logical
        list master
    cdef:
        list number, partial_type, _return_
        str error

    def __cinit__(self, master, logical, line):
        self.master         = master
        self.line           = line 
        self.logical        = logical
        self.number         = []
        self.partial_type   = [ type(list()), type(dict()), type(str()), type(tuple())]
        self.error          = ""
        self._return_       = []
    
    cdef GET_DATA(self, object, bint out_side = True):
        cdef : 
            unsigned long int i
            bint result
            str ob1, ob2

        if self.master:
            for i in range(len(self.master)):
                result = False
                try:
                    if   self.logical == '=='   : result = self.master[i] ==  object
                    elif self.logical == '>='   : result = self.master[i] >=  object
                    elif self.logical == '<='   : result = self.master[i] <=  object
                    elif self.logical == '!='   : result = self.master[i] !=  object
                    elif self.logical == '<'    : result = self.master[i] <   object
                    elif self.logical == '>'    : result = self.master[i] >   object

                    if result is True:
                        self.number.append( i )
                        if out_side is False: self._return_.append( True )
                        else:  self._return_.append( self.master[i] )
                    else:
                        if out_side is False:  self._return_.append( False )
                        else:  pass
                except TypeError:
                    ob1 = conversion.CONVERSION( line = self.line  ).CONVERSION( master=self.master[i] )
                    ob2 = conversion.CONVERSION( line = self.line  ).CONVERSION( master=object )
                    self.error = error.ERRORS( self.line ).ERROR7( self.logical, ob1, ob2)
                    break
        else:  self.error = error.ERRORS( self.line ).ERROR8( self.master )

        if type( self.master ) == type(list()):   return self._return_, self.number, self.error
        else:   return list( self._return_ ), self.number, self.error
