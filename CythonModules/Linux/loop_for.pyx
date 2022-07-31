#from script.PARXER.LEXER_CONFIGURE.lexer_and_parxer import NEXT_ANALYZE
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_statement

cdef dict UPDATING(dict base, str name, value):
    cdef :
        long idd 
        list var

    var = base[ 'variables' ][ 'vars' ]
    idd = var.index( name )
    base[ 'variables' ][ 'values' ][ idd ] = value
    


cdef class LOOP:
    cdef:
        public dict    data_base
        public int     line
        list    variables
        list    _values_

    def __init__( self, data_base, line ):
            self.data_base      = data_base
            self.line           = line
            self.variables      = self.data_base[ 'variables' ][ 'vars' ]
            self._values_       = self.data_base[ 'variables' ][ 'values' ]

    def LOOP( self, list for_values, str var_name ):
        cdef:
            str     error, normal_string, err
            dict    before
            dict    loop
            list    print_values
            list    finally_values
            list    any_values
            list    keys
            dict    lexer, lr
            long    counting
            long    index
            int     i, j
            long    for_line
            int     tabulation
            list    master
            bint    active_tab
        
        error       = ''
        counting    = 0

        if var_name in self.variables:
            index   = self.variables.index( var_name )
            self._values_[ index ] = for_values[ index ]
            self.data_base[ 'variables' ][ 'values' ] = self._values_

        else:
            self.variables.append( var_name )
            self._values_.append( for_values[ 0 ] )
            self.data_base[ 'variables' ][ 'values' ] = self._values_
            self.data_base[ 'variables' ][ 'vars' ] = self.variables 
        
        
        for i, _value_ in enumerate( for_values ):
            for_line    = 0
            counting    += 1

            UPDATING( self.data_base, var_name, _value_ )

            if error in ['', None]:
                if i == 0   :
                    loop, tabulation, error = for_statement.EXTERNAL_FOR_STATEMENT( None,
                                            self.data_base, self.line).FOR_STATEMENT( 1 )
                else :  loop = loop

                master = loop[ 'for' ] 

                for j, _string_ in enumerate( master[ : ] ):
                    for_line    += 1 
                    self.line   += 1

                    if type( _string_ ) == type( dict() ):
                        keys = list( _string_.keys() )
                        
                        if 'any' in keys:
                            any_values      = list( _string_[ 'any' ] )
                            normal_string   = any_values[ 0 ]
                            active_tab      = any_values[ 1 ]
                            lexer           = _string_[ 'lex' ]
                            error    = for_statement.NEXT_ANALYZE( normal_string, self.data_base,
                                       self.line ).SUB_ANALYZE( _type_ = 'loop', _lexer_ = lexer )

                            if error in ['', None] : pass 
                            else : break

                        else: pass
                    else: pass

                if error in ['', None]: pass
                else: break

            else : break
        
        return error