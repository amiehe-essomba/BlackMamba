from CythonModules.Linux.DEEP_PARSER          import logical_operator as LO

cdef class FINAL_VALUE:
    cdef public:
        list master, logical
        dict data_base 
        unsigned long int line 
    
    cdef:
        str error 
        list _return_
    
    def __cinit__(self, master, data_base, line, logical ):
        self.master             = master
        self.data_base          = data_base
        self.line               = line
        self.logical            = logical
        self.error              = ""
        self._return_           = []

    cdef FINAL_VALUE(self, bint _key_= False):
        cdef:
            signed long int i , k
            bint check 
            str string, _op_
            list _val_, _value_

        string = ""

        for i in range(len(self.master)):
            if self.logical[ i ] is None: 
                if type(self.master[i]) == type(list()):
                    self._return_ = self.master[i]
                else:
                    string = self.master[i]
            else:
                if   len( self.logical[ i ] ) == 1:
                    if self.logical[ i ][ 0 ] is not None:
                        if self.logical[ i ][ 0 ] not in [ '?', 'not' ]: pass
                        else: self.master[ i ] = self.master[ i ][0]

                        self._return_, self.error, check = LO.LOGICAL(self.master[i], self.logical, self.data_base, 
                                self.line).OPERATIONS(self.logical[ i ][ 0 ],  _key_=_key_)
                        
                        if not self.error: 
                            if check is True: pass 
                            else:  string = self._return_[ 0 ]
                        else:  break
                    else: self._return_ = self.master[ i ][0]
                
                elif len( self.logical[ i ])  == 2:
                    _op_   = ""
                    for k in range(len(self.logical[ i ])):
                        if self.logical[i][k] == '?':
                            _value_, self.error, check = LO.LOGICAL(self.master[i][k], self.logical, self.data_base, 
                                self.line).OPERATIONS(self.logical[ i ][ k ],  _key_=_key_)

                            if not self.error:  
                                if check is True : self.master[i][k] = _value_
                                else: self.master[i][k] = _value_[ 0 ]
                            else:  break
                        else:  _op_ = self.logical[ i ][k]

                    if not self.error :
                        self._return_, self.error, check = LO.LOGICAL(self.master[i], self.logical, self.data_base, 
                                self.line).OPERATIONS(_op_,  _key_=_key_)
                        if not self.error:
                            if check is True : pass 
                            else: string = self._return_[ 0 ]
                        else: break
                    else:  break
                
                elif len( self.logical [ i ]) == 3:
                    _op_       = '?'
                    _value_    = [ self.master[ i ][ 0 ], self.master[ i ][ -1 ]]
                    for k in range(len(_value_ )):
                        _val_, self.error, check = LO.LOGICAL(_value_[k] , self.logical, self.data_base, 
                                self.line).OPERATIONS(_op_,  _key_=_key_)
                        if self.error is None:  
                            if check is True:  _value_[ k ] = _val_ 
                            else: _value_[ k ] = _val_[ 0 ]
                        else: break
                    if not self.error:
                        self._op_ = '=='
                        self._return_, self.error, check = LO.LOGICAL(_value_ , self.logical, self.data_base, 
                                self.line).OPERATIONS(_op_,  _key_=_key_)
                        if not self.error :
                            if check is True: pass 
                            else: string = self._return_[ 0 ]
                        else: break
                    else:  break

        if string: return string, self.error 
        else:  return self._return_, self.error
                