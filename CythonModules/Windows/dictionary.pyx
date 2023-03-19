from src.transform                  import error as er
from script.STDIN.LinuxSTDIN        import bm_configure as bm


cdef class dic:
    cdef public:
        unsigned long long int line 
    cdef :
        str func
        dict data, error
    
    def __cinit__(self, line):
        self.line       = line  
        self.error      = {"s":None}
        self.data       = {}
        self.func       = bm.init.bold+bm.fg.rbg(0, 255, 0   )+' in dictionary( ).' + bm.init.reset 

    cpdef dic(self, dict val, list list_of_values):
        cdef:
            signed long int i
            list keys = list(val['s'][0])
            list values = list(val['s'][1])
            list double_keys = []

        if len( keys ) == len( values ):
            if type( keys ) == type(list()):
                if type( values ) == type(list()):
                    if len( keys ) == 1 :
                        if keys[ 0 ] is None:
                            if values[ 0 ] is None: pass
                            else: self.error['s'] = er.ERRORS( self.line ).ERROR5( list_of_values[ 0 ], func = self.func )
                        else:
                            if type( keys[ 0 ] ) == type( str() ): self.data[ keys[ 0 ] ] = values[ 0 ]
                            else: self.error['s'] = er.ERRORS( self.line ).ERROR5( list_of_values[ 0 ], func = self.func )
                    else:
                        for i in range(len(keys)):
                            if type( keys[i] ) == type( str() ):
                                if not double_keys:
                                    self.data[ keys[i] ] = values[ i ]
                                    double_keys.append( keys[i] )
                                else:
                                    if keys[i] not in double_keys: 
                                        self.data[ keys[i] ] = values[ i ]
                                        double_keys.append( keys[i] )
                                    else: 
                                        self.error['s'] = er.ERRORS(self.line).ERROR36(keys[i], func = self.func)
                                        break
                            else:
                                self.error['s'] = er.ERRORS( self.line ).ERROR5( keys[i], func = self.func )
                                break
                else: self.error['s'] = er.ERRORS(self.line).ERROR5('values', 'a list', func = self.func)
            else: self.error['s'] = er.ERRORS(self.line).ERROR5('keys', 'a list', func = self.func)
        else: self.error['s'] = er.ERRORS(self.line).ERROR6('keys', 'values', func = self.func)

        return self.data, self.error['s'] 