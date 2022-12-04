from src.transform     import error as er

cdef class Open:
    cdef public:
        dict data_base
        unsigned long long int line  
    cdef :
        dict error

    def __cinit__(self, data_base, line):
        self.data_base      = data_base
        self.line           = line 
        self.error          = {"s":None}
    cpdef  Open(self, list keys):

        if not self.data_base[ 'open' ][ 'name' ]:
            self.data_base[ 'open' ][ 'name' ].append(keys[ 0 ])
            self.data_base[ 'open' ][ 'file' ].append(keys[ 1 ])   
            self.data_base[ 'open' ][ 'action' ].append(keys[ 2 ])   
            self.data_base[ 'open' ][ 'status' ].append(keys[ 3 ])  
            self.data_base[ 'open' ][ 'encoding' ].append(keys[ 4 ])
            self.data_base[ 'open'][ 'nonCloseKey' ].append(keys[ 0 ] )
        else:
            if keys[ 0 ] in self.data_base[ 'open' ][ 'name' ]: self.error['s'] = er.ERRORS( self.line ).ERROR18( keys[ 0 ] )
            else:
                self.data_base[ 'open' ][ 'name' ].append(keys[ 0 ])
                self.data_base[ 'open' ][ 'file' ].append(keys[ 1 ])   
                self.data_base[ 'open' ][ 'action' ].append(keys[ 2 ])   
                self.data_base[ 'open' ][ 'status' ].append(keys[ 3 ])  
                self.data_base[ 'open' ][ 'encoding' ].append(keys[ 4 ])
                self.data_base[ 'open'][ 'nonCloseKey' ].append( keys[ 0 ] )

        return self.error['s'], self.data_base[ 'open']