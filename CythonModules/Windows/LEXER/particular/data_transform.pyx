cdef class DATA:
    cdef public:
        dict master 
     
    def __cinit__(self, master):
        self.master         = master 
     
    cdef dict TRANSFORM(self):
        cdef:
            unsigned long int i
    
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

        return self.master 