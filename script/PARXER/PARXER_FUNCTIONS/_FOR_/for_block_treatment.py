from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from updatingDataBase                                   import updating
from CythonModules.Windows                          import loop_for


class TREATMENT:
    def __init__(self, data_base:dict, line:int):
        self.data_base              = data_base
        self.line                   = line
        self.lex_par                = lexer_and_parxer
        self.variables              = data_base[ 'variables' ][ 'vars' ]
        self._values_               = data_base[ 'variables' ][ 'values' ]

    def FOR( self, 
            main_string     : str, 
            for_values      : list,
            name_var        : str, 
            interpreter     : bool   = False, 
            loop_list       : tuple  =()
            ):
        
        self.error                  = None
        self.before                 = updating.UPDATE( data_base=self.data_base ).BEFORE()
        self.for_values_init        = for_values[ : ]
        self.var_name               = name_var
        self.loop_for               = None
        self.print_values           = []
        self.finally_values         = []
        self.counting               = 0
        self.lex_lex                = None
    
        
        if self.var_name in self.variables:
            self.idd = self.variables.index( self.var_name )
            self._values_[ self.idd ] = self.for_values_init[ 0 ]
            self.data_base[ 'variables' ][ 'values' ] = self._values_

        else:
            self.variables.append( self.var_name )
            self._values_.append( self.for_values_init[ 0 ] )
            self.data_base[ 'variables' ][ 'values' ]   = self._values_
            self.data_base[ 'variables' ][ 'vars' ]     = self.variables

        
        """
        for i, value in enumerate( self.for_values_init ):
            self.for_line   = 0
            self.counting   += 1

            UPDATE_VAR_NAME( self.data_base ).UPDATE( value, self.var_name  )

            if self.error is None:
                if i == 0:
                    self.loop_for, self.tabulation, self.error = for_statement.EXTERNAL_FOR_STATEMENT( None,
                                                                self.data_base, self.line).FOR_STATEMENT( 1 )
                else:
                    self.loop_for = self.loop_for

                if self.error is None:
                    self.master = self.loop_for[ 'for' ]

                    for j, _string_ in enumerate( self.master[ : ] ):
                        self.for_line       += 1
                        self.line           += self.for_line

                        if type( _string_ ) == type( dict() ):
                            self.keys   = list( _string_.keys() )

                            if 'if' in self.keys        :
                                self.if_values      = _string_[ 'if' ]
                                self.tabulation     = _string_[ 'tabulation' ]
                                self.boolean_value  = _string_[ 'value' ]

                                self.error = if_statement.INTERNAL_IF_LOOP_STATEMENT( None , self.data_base,
                                        self.line ).IF_STATEMENT( self.boolean_value, self.tabulation - 1, self.if_values )
                                if self.error is None:
                                    pass
                                else:
                                    break

                            elif 'unless' in self.keys  :
                                self.unless_values  = _string_[ 'unless' ]
                                self.tabulation     = _string_[ 'tabulation' ]
                                self.boolean_value  = _string_[ 'value' ]
                                self.error = unless_statement.INTERNAL_UNLESS_FOR_STATEMENT( None , self.data_base,
                                        self.line ).UNLESS_STATEMENT( self.boolean_value, self.tabulation-1,
                                                                                        self.unless_values )
                                if self.error is None:
                                    pass
                                else:
                                    break

                            elif 'try' in self.keys     :
                                self.try_values     = _string_[ 'try' ]
                                self.tabulation     = _string_[ 'tabulation' ]
                                self.boolean_value  = _string_[ 'value' ]
                                self.finally_key, self.error = try_statement.EXTERNAL_TRY_FOR_STATEMENT( None ,
                                        self.data_base, self.line ).TRY_STATEMENT( self.tabulation - 1, self.try_values )

                                if self.error is None:
                                    self.len    = len( self.data_base[ 'print' ] )
                                    for x in range( self.len ):
                                        self.print_values.append( self.data_base[ 'print' ][ x ] )

                                    if i == len( self.for_values_init ) - 1:
                                        if self.print_values:
                                            self.data_base[ 'print' ] = self.print_values
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    if self.finally_key is True:
                                        self.finally_values.append( self.error )
                                        self.error          = None
                                        self.finally_key    = None

                                    else:
                                        break

                            elif 'empty' in self.keys   :
                                self.empty_values   = _string_[ 'empty' ]
                                self.tabulation     = _string_[ 'tabulation' ]
                                pass

                            elif 'any' in self.keys     :

                                self.any_values                         = _string_[ 'any' ]
                                self.normal_string, self.active_tab     = self.any_values
                                #self.lexer, self.active_tab             = self.any_values
                                self.tabulation                         = _string_[ 'tabulation' ]
                                #self.error = parxer_assembly.ASSEMBLY( self.lexer, self.data_base, self.line ).ASSEMBLY(
                                #                                                                    main_string, True)

                                #if self.counting -1 == 0 :
                                self.error = self.lex_par.NEXT_ANALYZE(self.normal_string, self.data_base,
                                                    self.line ).SUB_ANALYSZE( _type_ = 'loop' )
                                #else:
                                #    self.error = self.lex_par.NEXT_ANALYZE(self.normal_string, self.data_base,
                                #                self.line).SUB_ANALYSZE(_type_='loop', index=self.counting - 1, lexer_init = self.lex_lex)

                                if self.error is None: pass
                                else: break

                        elif type( _string_  ) == type( tuple() ):
                            if _string_[ 0 ] == 'else:': pass
                            else: pass
                        else: pass
                else: break
            else: break
        
        """
        
        self.error      = loop_for.LOOP( self.data_base, self.line ).LOOP( list(self.for_values_init), self.var_name, loop_list )
        self.after      = updating.UPDATE( data_base=self.data_base ).AFTER()
        self.error      = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, after=self.after, error=self.error )

        return  self.finally_values, self.error

class UPDATE_VAR_NAME:
    def __init__(self, data_base:dict):
        self.data_base          = data_base
        self.variables          = self.data_base[ 'variables' ][ 'vars' ]

    def UPDATE(self, value_of_variable: any, var_name : str):
        self.idd        = self.variables.index( var_name )
        self.data_base[ 'variables' ][ 'values' ][ self.idd ] = value_of_variable