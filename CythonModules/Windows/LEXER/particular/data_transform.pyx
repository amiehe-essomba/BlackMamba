from script.LEXER.error.CythonWIN           import affectationError as AE

cdef class DATA:
    cdef public:
        dict master 
        str long_chaine
     
    def __cinit__(self, master, long_chaine):
        self.master         = master 
        self.long_chaine    = long_chaine
     
    cdef dict TRANSFORM(self):
        cdef:
            unsigned long int i
        
        try:
            if 'operator' in list( self.master.keys() ):
                if   self.master[ 'operator' ] in [ '=' ]: pass
                elif self.master[ 'operator' ] in [ '+=' ]:
                    self.master[ 'operator' ] = '='
                    for i in range(len(self.master[ 'value' ])):
                        self.master[ 'value' ][ i ] += self.master[ 'variable' ][ i ] + ' ' + '+' + ' ' + self.master[ 'value' ][ i ]
                    
                elif self.master[ 'operator' ] in [ '-=' ]:
                    self.master[ 'operator' ] = '='
                    for i in range(len(self.master[ 'value' ])):
                        self.master[ 'value' ][ i ] += self.master[ 'variable' ][ i ] + ' ' + '-' + ' ' + self.master[ 'value' ][ i ]
                    
                elif self.master[ 'operator' ] in [ '*=' ]:
                    self.master[ 'operator' ] = '='
                    for i in range(len(self.master[ 'value' ])):
                        self.master[ 'value' ][ i ] += self.master[ 'variable' ][ i ] + ' ' + '*' + ' ' + self.master[ 'value' ][ i ]
                
                elif self.master[ 'operator' ] in [ '/=' ]:
                    self.master[ 'operator' ] = '='
                    for i in range(len(self.master[ 'value' ])):
                        self.master[ 'value' ][ i ] += self.master[ 'variable' ][ i ] + ' ' + '/' + ' ' + self.master[ 'value' ][ i ]
                
                elif self.master[ 'operator' ] in [ '%=' ]:
                    self.master[ 'operator' ] = '='
                    for i in range(len(self.master[ 'value' ])):
                        self.master[ 'value' ][ i ] += self.master[ 'variable' ][ i ] + ' ' + '%' + ' ' + self.master[ 'value' ][ i ]
                
                elif self.master[ 'operator' ] in [ '^=' ]:
                    self.master[ 'operator' ] = '='
                    for i in range(len(self.master[ 'value' ])):
                        self.master[ 'value' ][ i ] += self.master[ 'variable' ][ i ] + ' ' + '^' + ' ' + self.master[ 'value' ][ i ]
                    
            else: pass 
        except KeyError: self.error = AE.ERRORS(self.line).ERROR0( self.long_chaine )

        return self.master, self.error 