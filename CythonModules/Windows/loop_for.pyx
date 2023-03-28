#from script.PARXER.LEXER_CONFIGURE.lexer_and_parxer import NEXT_ANALYZE
#from script.PARXER.PARXER_FUNCTIONS._IF_                import loop_if_statement
#from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import loop_unless_statement
import sys
from loop.loop_constructor                              import loop_if_statement
from loop.loop_constructor                              import loop_unless_statement
from script.PARXER.PARXER_FUNCTIONS._FOR_.FOR.WIN       import for_analyze 
from loop                                               import mainFor



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

    def __cinit__( self, DataBase, line ):
            self.DataBase       = DataBase
            self.line           = line
            self.variables      = self.DataBase[ 'variables' ][ 'vars' ]
            self._values_       = self.DataBase[ 'variables' ][ 'values' ]
    cpdef LOOP( self, list for_values, str var_name, tuple loop_list = () ):
        cdef:
            str     error, normal_string, err
            dict    before, loop, lexer={}, lr, lex
            list    print_values, keys, finally_values, any_values, master
            long    counting, index, for_line
            int     i, j, tabulation
            bint    active_tab
            bint    boolean_value
            list    if_values
            bint    doubleKey
            bint    broke
            bint    locked
            list    unless_values
            dict    subfor_value, already = {}
            list    subfor_values
            tuple   all_for_values
            unsigned long long int m

        counting    = 0
        doubleKey   = False
        broke       = False

        loop, tabulation, error = loop_list

        if not error:
            master = loop['for']

            if var_name in self.variables:
                index   = self.variables.index( var_name )
                self._values_[ index ] = for_values[ -1 ]
                self.DataBase[ 'variables' ][ 'values' ] = self._values_

            else:
                self.variables.append( var_name )
                self._values_.append( for_values[ 0 ] )
                self.DataBase[ 'variables' ][ 'values' ] = self._values_
                self.DataBase[ 'variables' ][ 'vars' ] = self.variables 

            for i in range( len( for_values )):
                for_line    = 0
                counting   += 1
                locked      = False

                UPDATING( self.DataBase, var_name, for_values[ i ] )

                if not error :
                    for j, _string_ in enumerate( master[ : ] ):
                        if i == 0:
                            try: already["j"] = already["j"]
                            except KeyError: already["j"] = False 
                        else: pass

                        if locked is False:
                            for_line    += 1 

                            if type( _string_ ) == type( dict() ):
                                keys = list( _string_.keys() )
                                if   'any'    in keys           :
                                    if i == 0:
                                        any_values      = list( _string_[ 'any' ] )
                                        normal_string   = any_values[ 0 ]
                                        active_tab      = any_values[ 1 ]
                                        #lexer           = _string_[ 'lex' ]
                                        lexer[f'{j}'], error    = for_analyze.NEXT_ANALYZE( normal_string, self.DataBase,
                                                    ( self.line+for_line ) ).SUB_ANALYZE( _type_ = 'loop' )

                                        #error    = for_analyze.NEXT_ANALYZE( normal_string, self.DataBase,
                                        #        ( self.line+for_line ) ).SUB_SUB_ANALYZE( _lexer_ = lexer )
                                        #if already['j'] is False:
                                        #    lexer['j'], error    = for_analyze.NEXT_ANALYZE( normal_string, self.DataBase,
                                        #            ( self.line+for_line ) ).SUB_ANALYZE( _type_ = 'loop' )
                                    else:
                                        error    = for_analyze.NEXT_ANALYZE( normal_string, self.DataBase,
                                            ( self.line+for_line ) ).SUB_SUB_ANALYZE( _lexer_ = lexer[f'{j}'] )
                                       
                                    
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

                                        already['j']      = True

                                    else : break
                                
                                elif 'if'     in keys           :
                                        if_values      = _string_[ 'if' ]
                                        #tabulation     = _string_[ 'tabulation' ]
                                        boolean_value  = _string_[ 'value' ]
                            
                                        error = loop_if_statement.INTERNAL_IF_LOOP_STATEMENT( None , self.DataBase,
                                                (self.line+for_line) ).IF_STATEMENT( True, tabulation , if_values, 'loop' )
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
                                            (self.line+for_line) ).UNLESS_STATEMENT( True, tabulation, unless_values, 'loop' )
                                                                                            
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
                                    #subfor_value   = _string_[ 'value' ]
                                    #self.DataBase[ subfor_value[ 'variable' ] ] = subfor_value[ 'value' ]
                                    
                                    all_for_values = mainFor.FOR_BLOCK(normal_string = subfor_values[0][0][tabulation : ], 
                                            data_base=self.DataBase, line=(self.line+for_line)).FOR( function = 'loop', interpreter = False, locked=False)
                                    
                                    if not all_for_values[ 2 ]:
                                        subfor_value = all_for_values[ 1 ]
                                
                                        error = LOOP( DataBase=self.DataBase, line=(self.line+for_line) ).SubLOOP( for_values=list(subfor_value[ 'value' ]), 
                                                        var_name=subfor_value[ 'variable' ], loop_list=(subfor_values[1], tabulation, ''))    
                                                        
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
                                    else: 
                                        error = all_for_values[ 2 ]
                                        break
                                else: pass
                            else: pass
                        else: pass
                    if not error: 
                        if doubleKey is False: 
                            if broke is True: sys.exit()
                            else: pass 
                        else: break

                    else: break
                else : break
            return [None if not error else error ][0]
        else: return [None if not error else error ][0]

    cdef SubLOOP( self, list for_values, str var_name, tuple loop_list = () ):
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

        counting    = 0
        doubleKey   = False
        broke       = False
        
        loop, tabulation, error = loop_list

        if not error :
            master = loop['for']

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
                        
                                    error    = for_analyze.NEXT_ANALYZE( normal_string, self.DataBase,
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
                                        #tabulation     = _string_[ 'tabulation' ]
                                        boolean_value  = _string_[ 'value' ]
                                        
                                        error = loop_if_statement.INTERNAL_IF_LOOP_STATEMENT( None , self.DataBase,
                                                (self.line+for_line) ).IF_STATEMENT( boolean_value, tabulation+1 , if_values, 'loop' )
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
                                    #tabulation     = _string_[ 'tabulation' ]
                                    #subfor_value   = _string_[ 'value' ]
                                    s, subfor_value, error = mainFor.FOR_BLOCK(normal_string = subfor_values[0][0][ tabulation : ],  
                                            data_base=self.DataBase, line=(self.line+for_line)).FOR( function = 'loop', interpreter = False, locked=False)
                                    
                                    if not error:
                                        error = LOOP( DataBase=self.DataBase, line=(self.line+for_line) ).SubLOOP( for_values=list(subfor_value[ 'value' ]), 
                                                    var_name = subfor_value[ 'variable' ], loop_list=(subfor_values[1], tabulation, '') )                     
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
                                    else: break
                                else: pass
                            else: pass
                        else: pass
                    if not error: 
                        if doubleKey is False: 
                            if broke is True: sys.exit()
                            else: pass 
                        else: break

                    else: break
                else : break
            return [None if not error else error ][0]
        return [None if not error else error ][0]
