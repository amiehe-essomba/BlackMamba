import cython
from script                                         import control_string
from statement                                      import InternalStatement as IS
from script.PARXER.PARXER_FUNCTIONS._UNLESS_        import unless_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_        import switch_statement
from script.PARXER.PARXER_FUNCTIONS._IF_            import if_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_ import comment
from script.PARXER.PARXER_FUNCTIONS._IF_            import if_statement
from script.PARXER.LEXER_CONFIGURE                  import lexer_and_parxer
from script.STDIN.LinuxSTDIN                        import bm_configure as bm    
from script.PARXER.PARXER_FUNCTIONS._TRY_           import tryError     as tryE
from statement                                      import externalTry
from updatingDataBase                               import updating  
from CythonModules.Windows                          import fileError as fe 
from CythonModules.Windows                          import loop_for

@cython.cclass
class EXTERNAL_TRY_FOR_STATEMENT:
    def __init__(self, 
                master      :any, 
                data_base   :dict, 
                line        :int
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_par                = lexer_and_parxer

    def TRY_STATEMENT(self, 
                tabulation  : int   = 1, 
                loop_list   : list  = None, 
                _type_      : str   = 'try',
                keyPass     : bool  = False
                ):
        self.error                  = None
        self.locked_error           = []
        self.get_errors             = []
        self.active_calculations    = True
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_finally          = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'try' ]
        self.store_value            = [ 'try' ]
        self.color                  = bm.fg.rbg(255, 199, 0 )
        self.before                 = updating.UPDATE( data_base=self.data_base ).BEFORE()
        self.finally_key            = False
        self._finally_key_          = False
        self.except_key             = False
        self.loop_list              = loop_list
        self.next_line              = None
        self.locked                 = False
        
        ############################################################################
        self.keyPass                = keyPass
        self.max_emtyLine           = 5
        ############################################################################

        if self.keyPass is False:
            for j, _string_ in enumerate( self.loop_list ):
                
                if j != self.next_line:
                    self.if_line                        += 1
                    self.line                           += 1
                    self.normal_string, self.active_tab = _string_
                    self.string                         = self.normal_string
                    
                    #if self.string:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string,
                                                    normal_string=self.normal_string, data_base=self.data_base, line=self.line).BLOCKS(
                                                    tabulation=self.tabulation + 1, function=_type_, interpreter=True)
                                                          
                        if self.error  is None:
                            if self.get_block   == 'begin:'  :
                                self.next_line      = j + 1
                                self.before_init    = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.store_value.append(self.normal_string)
                                self.lastest        = self.history[ -1 ]

                                if self.keyPass is False:
                                    self.error = comment.COMMENT_LOOP_STATEMENT( self.master, self.data_base, 
                                            self.line ).COMMENT( self.tabulation + 1,  self.loop_list[ j + 1 ], keyPass = self.keyPass) 

                                    if self.error is None:
                                        #################################################
                                        self.history.append( 'begin' )
                                        self.space = 0
                                        ################################################

                                        if self.active_calculations is True: 
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after      = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error      = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None

                                    else:
                                        self.locked_error.append(self.error)
                                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append(self._error_)
                                else: 
                                    self.history.append( 'begin' )
                                    self.space = 0
                            elif self.get_block == 'if:'     :
                                self.next_line      = j + 1
                                self.before_init    = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.lastest        = self.history[-1]
                                self.store_value.append(self.normal_string)

                                if self.keyPass is False:
                                    self.error = if_statement.INTERNAL_IF_LOOP_STATEMENT( self.master,
                                                self.data_base, self.line ).IF_STATEMENT( self.value, self.tabulation + 1,
                                                self.loop_list[ self.next_line ], _type_= _type_,  keyPass = self.keyPass )

                                    if self.error is None:
                                        #################################################
                                        self.history.append( 'if' )
                                        self.space = 0
                                        ################################################
                                        if self.active_calculations is True:
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None
                                    else:
                                        self.locked_error.append( self.error )
                                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append( self._error_ )
                                else:
                                    self.history.append( 'if' )
                                    self.space = 0
                            elif self.get_block == 'try:'    :
                                
                                self.next_line      = j + 1
                                self.before_init    = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.lastest        = self.history[-1]
                                self.store_value.append( self.normal_string )

                                if self.keyPass is False:
                                    self._finally_key_, self.error = INTERNAL_TRY_FOR_STATEMENT( self.master,
                                                self.data_base, self.line ).TRY_STATEMENT( self.tabulation + 1,
                                                self.loop_list[ self.next_line ],  _type_= _type_,  keyPass = self.keyPass )
                                    
                                    if self.error is None:
                                        ###############################
                                        self.space = 0
                                        self.history.append( 'try' )
                                        ###############################
                                        
                                        if self.active_calculations is True:
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None

                                    else:
                                        if self._finally_key_ is not True:
                                            self.locked_error.append( self.error )
                                            self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                            self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                            self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                            self.get_errors.append( self._error_ )

                                        else:
                                            self.locked_error.append( self.error )
                                            self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                            self.get_errors.append( self._error_ )
                                else:
                                    self.history.append( 'try' )
                                    self.space = 0                                           
                            elif self.get_block == 'unless:' :
                                self.next_line      = j + 1
                                self.before_init    = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.lastest        = self.history[-1]
                                self.store_value.append(self.normal_string)

                                if self.keyPass is False:
                                    self.error = unless_statement.INTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                self.loop_list[ self.next_line ], _type_= _type_,  keyPass = self.keyPass)

                                    if self.error is None:
                                        #################################
                                        self.history.append( 'unless' )
                                        self.space = 0
                                        #################################
                                        
                                        if self.active_calculations is True:
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None

                                    else:
                                        self.locked_error.append(self.error)
                                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append(self._error_)
                                else:
                                    self.history.append( 'unless' )
                                    self.space = 0
                            elif self.get_block == 'for:'    :
                                self.next_line  = j + 1
                                self.before_init = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.store_value.append( self.normal_string )
                                self.lastest    = self.history[ -1 ]
                                self.history.append( 'for' )
                                self.space = 0
                                
                                self.var_name       = self.value[ 'variable' ]
                                self.for_values_init= self.value[ 'value' ]
                                
                                if self.var_name in self.data_base[ 'variables' ][ 'vars' ]:
                                    self.idd = self.data_base[ 'variables' ][ 'vars' ].index( self.var_name )
                                    self.data_base[ 'variables' ][ 'values' ] = self.for_values_init[ 0 ]

                                else:
                                    self.data_base[ 'variables' ][ 'values' ].append(self.for_values_init[ 0 ])
                                    self.data_base[ 'variables' ][ 'vars' ].append(self.var_name )

                                
                                if self.keyPass is False:
                                    self.error  = loop_for.LOOP( self.data_base, self.line ).LOOP( list(self.for_values_init),
                                                                        self.var_name, True, self.loop_list[ j + 1] )
                                    
                                    if self.error is None:    
                                        if self.active_calculations is True: 
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None
                                    else: 
                                        self.locked_error.append(self.error)
                                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append(self._error_)
                                else: pass 
                            elif self.get_block == 'switch:' :
                                self.next_line      = j+1
                                self.before_init    = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.lastest        = self.history[-1]
                                self.store_value.append(self.normal_string)

                                if self.keyPass is False:
                                    self.error = switch_statement.SWITCH_LOOP_STATEMENT( self.master , self.data_base,
                                                            self.line ).SWITCH( self.value, self.tabulation + 1, self.loop_list[ j + 1 ],
                                                                               _type_ = _type_, keyPass = self.keyPass )

                                    if self.error is None:
                                        #################################
                                        self.history.append( 'switch' )
                                        self.space = 0
                                        #################################

                                        if self.active_calculations is True:
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None

                                    else:
                                        self.locked_error.append(self.error)
                                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append(self._error_)
                                else:
                                    self.history.append( 'switch' )
                                    self.space = 0
                            elif self.get_block == 'empty'   :
                                if self.space <= self.max_emtyLine : self.space += 1
                                else:
                                    self.error = tryE.ERRORS( self.line ).ERROR4()
                                    break
                            elif self.get_block == 'any'     :
                                self.before_init = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.store_value.append( self.normal_string )

                                if self.data_base[ 'pass' ] is None:
                                    if self.locked is False:
                                        self.error = self.lex_par.LEXER_AND_PARXER( self.value, self.data_base,
                                                                        self.line ).ANALYZE( _id_ = 1, _type_ = _type_)
                                        if self.error is None:
                                            self.space = 0

                                            if self.active_calculations is True: pass
                                            elif self.active_calculations is False:
                                                if not self.get_errors: pass
                                                else:
                                                    self.error = True
                                                    self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                    self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                    self.error = None
                                        else:
                                            self.locked_error.append( self.error )
                                            self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                            self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                            self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                            self.get_errors.append( self._error_ )
                                    else: pass        
                                else: self.keyPass = True
                        else: break
                    else:
                        self.get_block, self.value, self.error = externalTry.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                                    data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)
                        
                        if self.error is None:
                            if   self.get_block == 'end:'    :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]

                                    if self.except_key is False and self.finally_key is False:
                                        self.error = tryE.ERRORS( self.line ).ERROR5()
                                        break
                                    else: break

                                else:
                                    self.error = tryE.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                    break
                            elif self.get_block == 'except:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'except' )
                                        self.bool_value         = self.value
                                        self.store_value        = []
                                        self.except_key         = True

                                        if self.locked is True:
                                            if type( self.value ) == type( str()):
                                                if self.get_errors:
                                                    if self.value in self.get_errors:
                                                        self.idd = self.get_errors.index( self.value )
                                                        del self.get_errors[ self.idd ]
                                                        del self.locked_error[ self.idd ]

                                                        self.active_calculations = True
                                                    else: self.active_calculations = False
                                                else: self.active_calculations = True

                                            else:
                                                for _error_ in self.value:
                                                    if self.get_errors:
                                                        if _error_ in self.get_errors:
                                                            self.idd = self.get_errors.index( _error_ )
                                                            del self.get_errors[ self.idd ]
                                                            del self.locked_error[ self.idd ]
                                                            self.active_calculations = True
                                                        else: self.active_calculations = False
                                                    else: self.active_calculations = True
                                        
                                        else: self.active_calculations = False
                                        
                                        self.data_base[ 'pass' ]    = None
                                        self.keyPass                = False

                                    else:
                                        self.error = tryE.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                        break
                                else:
                                    self.error = tryE.ERRORS( self.line ).ERROR1( 'finally' )
                                    break
                            elif self.get_block == 'finally:':
                                if self.index_finally < 1:
                                    if self.store_value:
                                        self.index_finally         += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append( 'finally' )
                                        self.active_calculations    = True
                                        self.finally_key            = True
                                        self.locked                 = False 

                                        if self.get_errors:
                                            self.error = True
                                            self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                            self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                            self.error = None
                                        else:  pass
                                        
                                        self.data_base[ 'pass' ]    = None
                                        self.keyPass                = False
                                    else:
                                        self.error = tryE.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = tryE.ERRORS( self.line ).ERROR3( 'finally' )
                                    break
                            elif self.get_block == 'empty'   :
                                if self.space <= self.max_emtyLine : self.space += 1
                                else:
                                    self.error = tryE.ERRORS( self.line ).ERROR4()
                                    break
                            else:
                                self.error = tryE.ERRORS( self.line ).ERROR4()
                                break
                        else: break
                    #pass
                else:
                    self.if_line        += 1
                    self.line           += 1
                    self.next_line      = None

            if self.error is None:
                if self.get_errors:
                    self.error = self.locked_error[ 0 ]
                    if self.finally_key is False :# and self._finally_key_ is None:
                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                    else: self._finally_key_ = self.finally_key
                else: pass
            else:pass
        else: pass

        ############################################################################
        return self._finally_key_, self.error

@cython.cclass
class INTERNAL_TRY_FOR_STATEMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_par                = lexer_and_parxer

    def TRY_STATEMENT(self, 
                tabulation  : int, 
                loop_list   : list, 
                _type_      : str  = 'try',
                keyPass     : bool = False
                ):
        
        self.error                  = None
        self.locked_error           = []
        self.get_errors             = []
        self.active_calculations    = True
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_finally          = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'try' ]
        self.store_value            = [ 'try' ]
        self.color                  = bm.fg.rbg(0, 255, 255 )
        self.before                 = updating.UPDATE( data_base=self.data_base ).BEFORE()
        self.finally_key            = False
        self._finally_key_          = False
        self.except_key             = False
        self.loop_list              = loop_list
        self.next_line              = 0

        ############################################################################
        self.keyPass                = keyPass
        self.max_emtyLine           = 5
        self.locked                 = False
        ############################################################################

        if self.keyPass is False:
            for j, _string_ in enumerate( self.loop_list ):

                if j != self.next_line:
                    self.if_line                        += 1
                    self.line                           += 1
                    self.normal_string, self.active_tab = _string_
                    self.string                         = self.normal_string

                    #if self.string:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string,
                                                    normal_string=self.normal_string, data_base=self.data_base, line=self.line).BLOCKS(
                                                    tabulation=self.tabulation + 1, function=_type_, interpreter=True)

                        if self.error  is None:
                            if self.get_block   == 'begin:' :
                                self.next_line      = j + 1
                                self.before_init    = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.store_value.append(self.normal_string)
                                self.lastest        = self.history[ -1 ]

                                if self.keyPass is False:
                                    self.error = comment.COMMENT_LOOP_STATEMENT( self.master, self.data_base, 
                                            self.line ).COMMENT( self.tabulation + 1,  self.loop_list[ j + 1 ], keyPass = self.keyPass)

                                    if self.error is None:
                                        #################################################
                                        self.history.append( 'begin' )
                                        self.space = 0
                                        ################################################

                                        if self.active_calculations is True:
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None

                                    else:
                                        self.locked_error.append( self.error )
                                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append( self._error_ )
                                else:
                                    self.history.append( 'begin' )
                                    self.space = 0
                            elif self.get_block ==   'if:'  :
                                self.next_line      = j + 1
                                self.lastest        = self.history[-1]
                                self.before_init    = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.store_value.append(self.normal_string)

                                if self.keyPass is False:
                                    self.error = if_statement.EXTERNAL_IF_LOOP_STATEMENT(  self.master,
                                            self.data_base, self.line).IF_STATEMENT( self.value, self.tabulation + 1,
                                            self.loop_list[ self.next_line], _type_= _type_,  keyPass = self.keyPass)

                                    if self.error is None:
                                        #################################################
                                        self.history.append( 'if' )
                                        self.space = 0
                                        ################################################
                                        
                                        if self.active_calculations is True:
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None

                                    else:
                                        self.locked_error.append( self.error )
                                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append( self._error_ )
                                else:
                                    self.history.append( 'if' )
                                    self.space = 0
                            elif self.get_block == 'try:'   :
                                self.next_line      = j + 1
                                self.lastest        = self.history[-1]
                                self.before_init    = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.store_value.append(self.normal_string)

                                if self.keyPass is False:
                                    self._finally_key_, self.error = EXTERNAL_TRY_FOR_STATEMENT( self.master,
                                                self.data_base, self.line ).TRY_STATEMENT( self.tabulation + 1,
                                                self.loop_list[ self.next_line ], _type_= _type_,  keyPass = self.keyPass )
                                    if self.error is None:
                                        ################################
                                        self.space = 0
                                        self.history.append( 'try' )
                                        ################################
                                        
                                        if self.active_calculations is True:
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None

                                    else:
                                        if self._finally_key_ is not True:
                                            self.locked_error.append( self.error )
                                            self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                            self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                            self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                            self.get_errors.append( self._error_ )
                                            
                                        else:
                                            self.locked_error.append( self.error )
                                            self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                            self.get_errors.append( self._error_ )
                                else:
                                    self.history.append( 'try' )
                                    self.space = 0                                               
                            elif self.get_block == 'unless:':
                                self.next_line      = j + 1
                                self.lastest        = self.history[-1]
                                self.before_init    = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.store_value.append(self.normal_string)

                                if self.keyPass is False:
                                    self.error = unless_statement.EXTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                self.loop_list[ self.next_line], _type_= _type_,  keyPass = self.keyPass)

                                    if self.error is None:
                                        #################################################
                                        self.history.append( 'unless' )
                                        self.space = 0
                                        ################################################
                                        
                                        if self.active_calculations is True:
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None

                                    else:
                                        self.locked_error.append(self.error)
                                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append(self._error_)
                                else:
                                    self.history.append( 'unless' )
                                    self.space = 0
                            elif self.get_block == 'for:'   :
                                self.next_line  = j + 1
                                self.before     = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.lastes     = self.history[-1]
                                self.store_value.append( self.normal_string )
                                self.history.append( 'for' )
                                self.space = 0
                                
                                self.var_name       = self.value[ 'variable' ]
                                self.for_values_init= self.value[ 'value' ]
                                self.variables      = self.data_base['variables']['vars'].copy()
                                self._values_       = self.data_base['variables']['values'].copy()
                                
                                if self.var_name in self.variables:
                                    self.idd = self.variables.index( self.var_name )
                                    self._values_[ self.idd ] = self.for_values_init[ 0 ]
                                    self.data_base[ 'variables' ][ 'values' ] = self._values_

                                else:
                                    self.variables.append( self.var_name )
                                    self._values_.append( self.for_values_init[ 0 ] )
                                    self.data_base[ 'variables' ][ 'values' ]   = self._values_
                                    self.data_base[ 'variables' ][ 'vars' ]     = self.variables

                                if self.keyPass is False:
                                    self.error  = loop_for.LOOP( self.data_base, self.line ).LOOP( list(self.for_values_init),
                                                                        self.var_name, True, self.loop_list[ j + 1] )
                                    if self.error is None:    
                                        if self.active_calculations is True:
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None
                                    else: 
                                        self.locked_error.append(self.error)
                                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append(self._error_)
                                else: pass                                    
                            elif self.get_block == 'switch:':
                                self.next_line      = j+1
                                self.before_init    = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.lastest        = self.history[-1]
                                self.store_value.append(self.normal_string)

                                if self.keyPass is False:
                                    self.error = switch_statement.SWITCH_LOOP_STATEMENT( self.master , self.data_base,
                                                            self.line ).SWITCH( self.value, self.tabulation + 1, self.loop_list[ j + 1 ],
                                                                               _type_ = _type_, keyPass = self.keyPass )

                                    if self.error is None:
                                        #################################################
                                        self.history.append( 'switch' )
                                        self.space = 0
                                        ################################################

                                        if self.active_calculations is True:
                                            if self.lastest == 'try': self.locked = True 
                                            else: pass
                                        elif self.active_calculations is False:
                                            if not self.get_errors: pass
                                            else:
                                                self.error = True
                                                self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                self.error = None

                                    else:
                                        self.locked_error.append(self.error)
                                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append(self._error_)
                                else:
                                    self.history.append( 'switch' )
                                    self.space = 0
                            elif self.get_block == 'empty'  :
                                if self.space <= self.max_emtyLine : self.space += 1
                                else:
                                    self.error = tryE.ERRORS( self.line ).ERROR4()
                            elif self.get_block == 'any'    :
                                self.before_init = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                self.store_value.append( self.normal_string )

                                if self.data_base[ 'pass' ] is None:
                                    if self.locked is False:
                                        self.error = self.lex_par.LEXER_AND_PARXER(self.value, self.data_base,
                                                                self.line).ANALYZE(_id_ = 1, _type_ = _type_)

                                        if self.error is None:
                                            self.space = 0
                                            if self.active_calculations is True: pass
                                            elif self.active_calculations is False:
                                                if not self.get_errors: pass
                                                else:
                                                    self.error = True
                                                    self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                                    self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                                    self.error = None
                                        else:
                                            self.locked_error.append( self.error )
                                            self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                            self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                            self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                            self.get_errors.append( self._error_ )
                                    else: pass
                                else: self.keyPass = True
                        else: break
                    else:
                        self.get_block, self.value, self.error = externalTry.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                                    data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)

                        if self.error is None:
                            if   self.get_block == 'end:'    :
                                if self.store_value:
                                    del self.store_value[:]
                                    del self.history[:]

                                    if self.except_key is False and self.finally_key is False:
                                        self.error = tryE.ERRORS(self.line).ERROR5()
                                        break
                                    else: break
                                else:
                                    self.error = tryE.ERRORS(self.line).ERROR2(self.history[-1])
                                    break
                            elif self.get_block == 'except:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'except' )
                                        self.bool_value     = self.value
                                        self.store_value    = []
                                        self.except_key     = True

                                        if self.locked is False:
                                            if type( self.value ) == type( str() ):
                                                if self.get_errors:
                                                    if self.value in self.get_errors:
                                                        self.idd = self.get_errors.index( self.value )
                                                        del self.get_errors[ self.idd ]
                                                        del self.locked_error[ self.idd ]

                                                        self.active_calculations = True
                                                    else: self.active_calculations = False
                                                else: self.active_calculations = True

                                            else:
                                                for _error_ in self.value:
                                                    if self.get_errors:
                                                        if _error_ in self.get_errors:
                                                            self.idd = self.get_errors.index( _error_ )
                                                            del self.get_errors[ self.idd ]
                                                            del self.locked_error[ self.idd ]
                                                            self.active_calculations = True
                                                        else: self.active_calculations = False
                                                    else: self.active_calculations = True
                                        else: self.active_calculations = False 
                                        
                                        self.data_base[ 'pass' ]    = None
                                        self.keyPass                = False
                                    else:
                                        self.error = tryE.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = tryE.ERRORS(self.line).ERROR1('finally')
                                    break
                            elif self.get_block == 'finally:':
                                if self.index_finally < 1:
                                    if self.store_value:
                                        self.history.append('finally')
                                        self.index_finally          += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.active_calculations    = True
                                        self.finally_key            = True
                                        self.locked                 = False

                                        if self.get_errors:
                                            self.error = True
                                            self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                                            self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                                            self.error = None
                                        else: pass
                                        
                                        self.data_base[ 'pass' ]    = None
                                        self.keyPass                = False
                                    else:
                                        self.error = tryE.ERRORS(self.line).ERROR2(self.history[-1])
                                        break
                                else:
                                    self.error = tryE.ERRORS(self.line).ERROR3('finally')
                                    break
                            elif self.get_block == 'empty'   :
                                if self.space <= self.max_emtyLine: self.space += 1
                                else:
                                    self.error = tryE.ERRORS(self.line).ERROR4()
                                    break
                            else:
                                self.error = tryE.ERRORS(self.line).ERROR4()
                                break
                        else:  break
                    #else: pass
                else:
                    self.if_line        += 1
                    self.line           += 1
                    self.next_line      = None

            if self.error is None:
                if self.get_errors:
                    self.error = self.locked_error[ 0 ]
                    if self.finally_key is False:
                        self.after              = updating.UPDATE( data_base=self.data_base ).AFTER()
                        self.error              = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, 
                                                                                                        after=self.after, error=self.error )
                    else: self._finally_key_ = self.finally_key
                else: pass
            else:pass
        else: pass

        ############################################################################
        
        return self._finally_key_, self.error

