#from script.PARXER.LEXER_CONFIGURE.lexer_and_parxer import NEXT_ANALYZE
from script.PARXER.PARXER_FUNCTIONS._IF_                import loop_if_statement
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import loop_unless_statement
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
        public dict    DataBase
        public int     line

    cdef:
        list    variables
        list    _values_

    def __init__( self, DataBase, line ):
            self.DataBase       = DataBase
            self.line           = line
            self.variables      = self.DataBase[ 'variables' ][ 'vars' ]
            self._values_       = self.DataBase[ 'variables' ][ 'values' ]

    cpdef LOOP( self, list for_values, str var_name, bint interpreter = False, tuple loop_list = () ):
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
            bint    boolean_value
            list    if_values
            bint    doubleKey
            bint    broke
            bint    locked
            list    unless_values
            dict    subfor_value
            list    subfor_values

        error       = ''
        counting    = 0
        doubleKey   = False
        broke       = False

        if var_name in self.variables:
            index   = self.variables.index( var_name )
            self._values_[ index ] = for_values[ -1 ]
            self.DataBase[ 'variables' ][ 'values' ] = self._values_

        else:
            self.variables.append( var_name )
            self._values_.append( for_values[ 0 ] )
            self.DataBase[ 'variables' ][ 'values' ] = self._values_
            self.DataBase[ 'variables' ][ 'vars' ] = self.variables 
        
        
        for i in range( len( for_values ) ):
            for_line    = 0
            counting    += 1
            locked      = False

            UPDATING( self.DataBase, var_name, for_values[ i ] )

            if not error :
                if i == 0   :
                    if interpreter is False:
                        loop, tabulation, error = for_statement.EXTERNAL_FOR_STATEMENT( None,
                                            self.DataBase, (self.line+for_line) ).FOR_STATEMENT( 1 )
                        if not error: master = loop['for']
                        else: break
                    else:  
                        loop, tabulation, error = loop_list
                        if not error: master = loop['for']
                        else: break
                else :  pass 

                for j, _string_ in enumerate( master[ : ] ):
                    if locked is False:
                        for_line    += 1 

                        if type( _string_ ) == type( dict() ):
                            keys = list( _string_.keys() )
                            if   'any'    in keys           :
                                any_values      = list( _string_[ 'any' ] )
                                normal_string   = any_values[ 0 ]
                                active_tab      = any_values[ 1 ]
                                lexer           = _string_[ 'lex' ]
                                
                                error    = for_statement.NEXT_ANALYZE( normal_string, self.DataBase,
                                        ( self.line+for_line ) ).SUB_SUB_ANALYZE( _lexer_ = lexer )

                                #error    = for_statement.NEXT_ANALYZE( normal_string, self.DataBase,
                                #        ( self.line+for_line ) ).SUB_ANALYZE( _type_ = 'loop', _lexer_ = lexer )
                                
                                if not error: 
                                    if   self.DataBase[ 'break' ] is None: pass 
                                    else:
                                        self.DataBase[ 'break' ] = None 
                                        doubleKey = True
                                        break

                                    if self.DataBase[ 'exit' ] is None: pass
                                    else:
                                        self.DataBase['exit'] = None 
                                        doubleKey = True
                                        broke     = True
                                        break
                                        
                                    if self.DataBase[ 'pass' ] is None: pass
                                    else: locked      = True

                                    if self.DataBase[ 'continue' ] is None: pass
                                    else: locked      = True

                                    if self.DataBase[ 'next' ] is None: pass
                                    else: locked      = True

                                else : break
                            
                            elif 'if'     in keys           :
                                    if_values      = _string_[ 'if' ]
                                    #tabulation     = _string_[ 'tabulation' ]
                                    boolean_value  = _string_[ 'value' ]
                                    
                                    error = loop_if_statement.INTERNAL_IF_LOOP_STATEMENT( None , self.DataBase,
                                            (self.line+for_line) ).IF_STATEMENT( boolean_value, tabulation , if_values, 'loop' )
                                    if error is None: 
                                        if   self.DataBase[ 'break' ] is None: pass 
                                        else:
                                            self.DataBase[ 'break' ] = None 
                                            doubleKey = True
                                            break

                                        if self.DataBase[ 'exit' ] is None: pass
                                        else:
                                            self.DataBase['exit'] = None 
                                            doubleKey = True
                                            broke     = True
                                            break 
                                    else: break
                            elif 'unless' in keys           :
                                unless_values  = _string_[ 'unless' ]
                                #tabulation     = _string_[ 'tabulation' ]
                                boolean_value  = _string_[ 'value' ]
                                error = loop_unless_statement.INTERNAL_UNLESS_FOR_STATEMENT( None , self.DataBase,
                                        (self.line+for_line) ).UNLESS_STATEMENT( boolean_value, tabulation, unless_values, 'loop' )
                                                                                        
                                if error is None:
                                    if   self.DataBase[ 'break' ] is None: pass 
                                    else:
                                        self.DataBase[ 'break' ] = None 
                                        doubleKey = True
                                        break

                                    if self.DataBase[ 'exit' ] is None: pass
                                    else:
                                        self.DataBase['exit'] = None 
                                        doubleKey = True
                                        broke     = True
                                        break 
                                else: break
                            elif 'for'    in keys           :
                                subfor_values  = _string_[ 'for' ]
                                #tabulation     = _string_[ 'tabulation' ]
                                subfor_value   = _string_[ 'value' ]
                                self.DataBase[ subfor_value[ 'variable' ] ] = subfor_value[ 'value' ]

                                error = LOOP( self.DataBase, (self.line+for_line) ).SubLOOP( list(subfor_value[ 'value' ]), 
                                                subfor_value[ 'variable' ], True, (subfor_values[1], tabulation, None))    
                                                
                                if error is None:
                                    if   self.DataBase[ 'break' ] is None: pass 
                                    else:
                                        self.DataBase[ 'break' ] = None 
                                        doubleKey = True
                                        break

                                    if self.DataBase[ 'exit' ] is None: pass
                                    else:
                                        self.DataBase['exit'] = None 
                                        doubleKey = True
                                        broke     = True
                                        break 
                                else: break
                            else: pass
                        else: pass
                    else: pass
                if not error: 
                    if doubleKey is False: 
                        if broke is True:  exit()
                        else: pass 
                    else: break

                else: break
            else : break
        return error

    cdef SubLOOP( self, list for_values, str var_name, bint interpreter = False, tuple loop_list = () ):
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
            bint    boolean_value
            list    if_values
            bint    doubleKey
            bint    broke
            bint    locked
            list    unless_values
            dict    subfor_value
            list    subfor_values

        error       = ''
        counting    = 0
        doubleKey   = False
        broke       = False

        if var_name in self.variables:
            
            index   = self.variables.index( var_name )
            self._values_[ index ] = for_values[ -1 ] 
            self.DataBase[ 'variables' ][ 'values' ] = self._values_

        else:
            self.variables.append( var_name )
            self._values_.append( for_values[ 0 ] )
            self.DataBase[ 'variables' ][ 'values' ] = self._values_
            self.DataBase[ 'variables' ][ 'vars' ] = self.variables 
        
        
        for i in range( len( for_values ) ):
            for_line    = 0
            counting    += 1
            locked      = False

            UPDATING( self.DataBase, var_name, for_values[ i ] )

            if not error :
                if i == 0   :
                    if interpreter is False:
                        loop, tabulation, error = for_statement.EXTERNAL_FOR_STATEMENT( None,
                                            self.DataBase, (self.line+for_line) ).FOR_STATEMENT( 1 )
                    else:  loop, tabulation, error = loop_list
                else :  loop = loop

                master = loop[ 'for' ] 

                for j, _string_ in enumerate( master[ : ] ):
                    if locked is False:
                        for_line    += 1 

                        if type( _string_ ) == type( dict() ):
                            keys = list( _string_.keys() )
                            if  'any'     in keys           :
                                any_values      = list( _string_[ 'any' ] )
                                normal_string   = any_values[ 0 ]
                                active_tab      = any_values[ 1 ]
                                lexer           = _string_[ 'lex' ]
                    
                                error    = for_statement.NEXT_ANALYZE( normal_string, self.DataBase,
                                        ( self.line+for_line ) ).SUB_ANALYZE( _type_ = 'loop', _lexer_ = lexer )
                                
                                if not error: 
                                    if   self.DataBase[ 'break' ] is None: pass 
                                    else:
                                        self.DataBase[ 'break' ] = None 
                                        doubleKey = True
                                        break

                                    if self.DataBase[ 'exit' ] is None: pass
                                    else:
                                        self.DataBase['exit'] = None 
                                        doubleKey = True
                                        broke     = True
                                        break
                                        
                                    if self.DataBase[ 'pass' ] is None: pass
                                    else: locked      = True

                                    if self.DataBase[ 'continue' ] is None: pass
                                    else: locked      = True

                                    if self.DataBase[ 'next' ] is None: pass
                                    else: locked      = True

                                else : break
                            
                            elif 'if'     in keys           :
                                    if_values      = _string_[ 'if' ]
                                    tabulation     = _string_[ 'tabulation' ]
                                    boolean_value  = _string_[ 'value' ]
                                    
                                    error = loop_if_statement.INTERNAL_IF_LOOP_STATEMENT( None , self.DataBase,
                                            (self.line+for_line) ).IF_STATEMENT( boolean_value, tabulation , if_values, 'loop' )
                                    if error is None: 
                                        if   self.DataBase[ 'break' ] is None: pass 
                                        else:
                                            self.DataBase[ 'break' ] = None 
                                            doubleKey = True
                                            break

                                        if self.DataBase[ 'exit' ] is None: pass
                                        else:
                                            self.DataBase['exit'] = None 
                                            doubleKey = True
                                            broke     = True
                                            break 
                                    else: break
                            elif 'unless' in keys           :
                                unless_values  = _string_[ 'unless' ]
                                tabulation     = _string_[ 'tabulation' ]
                                boolean_value  = _string_[ 'value' ]
                                error = loop_unless_statement.INTERNAL_UNLESS_FOR_STATEMENT( None , self.DataBase,
                                        (self.line+for_line) ).UNLESS_STATEMENT( boolean_value, tabulation, unless_values, 'loop' )
                                                                                        
                                if error is None:
                                    if   self.DataBase[ 'break' ] is None: pass 
                                    else:
                                        self.DataBase[ 'break' ] = None 
                                        doubleKey = True
                                        break

                                    if self.DataBase[ 'exit' ] is None: pass
                                    else:
                                        self.DataBase['exit'] = None 
                                        doubleKey = True
                                        broke     = True
                                        break 
                                else: break
                            elif 'for'    in keys           :
                                subfor_values  = _string_[ 'for' ]
                                tabulation     = _string_[ 'tabulation' ]
                                subfor_value   = _string_[ 'value' ]
                                self.DataBase[ subfor_value[ 'variable' ] ] = subfor_value[ 'value' ]
                                
                                error = LOOP( self.DataBase, (self.line+for_line) ).SubLOOP( list(subfor_value[ 'value' ]), 
                                                subfor_value[ 'variable' ], interpreter, loop_list )                     
                                if error is None:
                                    if   self.DataBase[ 'break' ] is None: pass 
                                    else:
                                        self.DataBase[ 'break' ] = None 
                                        doubleKey = True
                                        break

                                    if self.DataBase[ 'exit' ] is None: pass
                                    else:
                                        self.DataBase['exit'] = None 
                                        doubleKey = True
                                        broke     = True
                                        break 
                                else: break
                            else: pass
                        else: pass
                    else: pass
                if not error: 
                    if doubleKey is False: 
                        if broke is True:  exit()
                        else: pass 
                    else: break

                else: break
            else : break
        return error