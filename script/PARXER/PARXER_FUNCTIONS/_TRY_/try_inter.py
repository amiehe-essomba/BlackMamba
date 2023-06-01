from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import unless_interpreter
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.STDIN.WinSTDIN                              import stdin
from script.PARXER.PARXER_FUNCTIONS._IF_                import IfError              as Ie
from statement                                          import InternalStatement    as IS
from statement                                          import externalTry
from script.PARXER.PARXER_FUNCTIONS._TRY_               import tryError          as TE
from script.PARXER.PARXER_FUNCTIONS._IF_                import if_inter

class EXTERNAL_TRY_STATEMENT:
    def __init__(self, master, data_base, line):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def TRY_STATEMENT(self, 
            tabulation  : int   = 1,
            loop_list   : list  = [],
            _type_      : str   = 'try'
            ):
        
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_else             = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'try' ]
        self.loop                   = []
        self.loop_list              = loop_list
        self.next_line              = 0
        self.loop_loop              = []
        self.maxEmptyLine           = 5
        self.index_finally         = 0
        ############################################################################
        
        if self.loop_list:
            for  j, _string_ in enumerate( self.loop_list ):
                self.if_line    += 1
                self.line       += 1
                
                if _string_ :
                    if _type_ != 'try': pass 
                    else:  _string_ = '\t'+_string_
                    
                    if j >= self.next_line:
                        k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)                   
                        self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                            self.line ).STDIN_FOR_INTERPRETER( k, _string_ )
                        if self.error is None:
                            if self.active_tab is True:
                                
                                self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                            data_base=self.data_base, line=self.line).INTERPRETER_BLOCKS(tabulation=k+1, function=_type_, typ='try',
                                                                                                interpreter = False)
                                 
                                if self.error  is None:
                                    if   self.get_block == 'if:'     :
                                        self.next_line              = j+1
                                        self.loop.append( ( self.normal_string, True ) )
                                        self.isbreak    = True
                                        #self.NewLIST1    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, 
                                        #                                self.loop_list[self.next_line : ], index = 'int')
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).IF(self.tabulation, 
                                                                        self.loop_list[self.next_line : ])
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = if_inter.INTERNAL_IF_STATEMENT(self.master,
                                                                self.data_base, self.line).IF_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('if')
                                                self.space      = 0
                                                self.loop.append( self._values_ )
                                            else: break
                                        else: 
                                            self.error = TE.ERRORS( self.line ).ERROR4()
                                            break
                                    elif self.get_block == 'try:'    :
                                        self.next_line              = j+1
                                        self.loop.append( ( self.normal_string, True ) )
                                        self.isbreak    = True
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, 
                                                                        self.loop_list[self.next_line : ], index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = INTERNAL_TRY_STATEMENT(self.master,
                                                                self.data_base, self.line).TRY_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('try')
                                                self.space      = 0
                                                self.loop.append( self._values_ )
                                            else: break
                                        else: 
                                            self.error = TE.ERRORS( self.line ).ERROR4()
                                            break
                                    elif self.get_block == 'unless:' :
                                        self.next_line              = j+1
                                        self.loop.append( ( self.normal_string, True ) )
                                        self.isbreak    = True
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, 
                                                                self.loop_list[self.next_line : ], index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = unless_interpreter.INTERNAL_UNLESS_STATEMENT(self.master,
                                                                self.data_base, self.line).UNLESS_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('unless')
                                                self.space      = 0
                                                self.loop.append( self._values_ )
                                            else: break
                                        else: 
                                            self.error = TE.ERRORS( self.line ).ERROR4()
                                            break                                                          
                                    elif self.get_block == 'empty'   :
                                        if self.space <= self.maxEmptyLine:
                                            self.space += 1
                                            self.loop.append( (self.normal_string, True) )
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR4()
                                            break
                                    elif self.get_block == 'any'     :
                                        self.store_value.append( self.normal_string )
                                        self.space = 0
                                        self.loop.append( (self.normal_string, True) )

                                    #############################################################
                                    #############################################################
                                    
                                    elif self.get_block == 'end:'       :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.loop.append( (self.normal_string, False) )
                                            self.try_cancel = True
                                            if self.except_key is False and self.finally_key is False:
                                                self.error = TE.ERRORS( self.line ).ERROR5()
                                                break
                                            else:  break
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break
                                    elif self.get_block == 'except:'    :
                                        if self.key_else_activation == None:
                                            if self.store_value:
                                                self.history.append( 'except' )
                                                self.store_value        = []
                                                self.except_key         = True
                                                self.loop.append( (self.normal_string, False) )
                                            else:
                                                self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                                break
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR1( 'finally' )
                                            break
                                    elif self.get_block == 'finally:'   :
                                        if self.index_finally < 1:
                                            if self.store_value:
                                                self.index_finally         += 1
                                                self.key_else_activation    = True
                                                self.store_value            = []
                                                self.history.append( 'finally' )
                                                self.finally_key            = True
                                                self.loop.append( (self.normal_string, False) )
                                            else:
                                                self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                                break     
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR3( 'finally' )
                                            break                              
                                    else:
                                        self.error = TE.ERRORS( self.line ).ERROR4()
                                        break
                                else: break

                            else:
                                self.get_block, self.value, self.error = externalTry.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                                    data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)
                                   
                                if self.error is None:
                                    if   self.get_block == 'end:'       :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.loop.append( (self.normal_string, False) )
                                            self.try_cancel = True
                                            if self.except_key is False and self.finally_key is False:
                                                self.error = TE.ERRORS( self.line ).ERROR5()
                                                break
                                            else:  break
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break
                                    elif self.get_block == 'except:'    :
                                        if self.key_else_activation is None:
                                            if self.store_value:
                                                self.history.append( 'except' )
                                                self.store_value        = []
                                                self.except_key         = True
                                                self.loop.append( (self.normal_string, False) )
                                            else:
                                                self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                                break
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR1( 'finally' )
                                            break
                                    elif self.get_block == 'finally:'   :
                                        if self.index_finally < 1:
                                            if self.store_value:
                                                self.index_finally         += 1
                                                self.key_else_activation    = True
                                                self.store_value            = []
                                                self.history.append( 'finally' )
                                                self.finally_key            = True
                                                self.loop.append( (self.normal_string, False) )
                                            else:
                                                self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                                break     
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR3( 'finally' )
                                            break                              
                                    elif self.get_block == 'empty'      :
                                        if self.space <= self.maxEmptyLine :
                                            self.space += 1
                                            self.loop.append( (self.normal_string, False ) )
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR4()
                                            break
                                    else:
                                        self.error = TE.ERRORS( self.line ).ERROR4()
                                        break
                                else: break
                        else: break
                    else:  pass
                else:
                    self.error = TE.ERRORS( self.line ).ERROR4()
                    break
        else:  self.error = Ie.ERRORS( self.line ).ERROR5()
        ############################################################################
        
        return self.loop , self.error
    
class INTERNAL_TRY_STATEMENT:
    def __init__(self, master, data_base, line):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def TRY_STATEMENT(self, 
            tabulation  : int   = 1,
            loop_list   : list  = [],
            _type_      : str   = 'try'
            ):
        
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_else             = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'try' ]
        self.loop                   = []
        self.loop_list              = loop_list
        self.next_line              = 0
        self.loop_loop              = []
        self.maxEmptyLine           = 5
        self.index_finally         = 0
        ############################################################################
        
        if self.loop_list:
            for  j, _string_ in enumerate( self.loop_list ):
                self.if_line    += 1
                self.line       += 1
                
                if _string_ :
                    if _type_ != 'try': pass 
                    else:  _string_ = '\t'+_string_
                    
                    if j >= self.next_line:
                        k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)                   
                        self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                            self.line ).STDIN_FOR_INTERPRETER( k, _string_ )
                        if self.error is None:
                            if self.active_tab is True:
                                
                                self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                            data_base=self.data_base, line=self.line).INTERPRETER_BLOCKS(tabulation=k+1, function=_type_, typ='try',
                                                                                                interpreter = False)
                                 
                                if self.error  is None:
                                    if   self.get_block == 'if:'     :
                                        self.next_line              = j+1
                                        self.loop.append( ( self.normal_string, True ) )
                                        self.isbreak    = True
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).IF(self.tabulation, 
                                                                        self.loop_list[self.next_line : ])
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = if_inter.INTERNAL_IF_STATEMENT(self.master,
                                                                self.data_base, self.line).IF_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('if')
                                                self.space      = 0
                                                self.loop.append( self._values_ )
                                            else: break
                                        else: 
                                            self.error = TE.ERRORS( self.line ).ERROR4()
                                            break
                                    elif self.get_block == 'try:'    :
                                        self.next_line              = j+1
                                        self.loop.append( ( self.normal_string, True ) )
                                        self.isbreak    = True
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation,
                                                                 self.loop_list[self.next_line : ], index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = EXTERNAL_TRY_STATEMENT(self.master,
                                                                self.data_base, self.line).TRY_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('try')
                                                self.space      = 0
                                                self.loop.append( self._values_ )
                                            else: break
                                        else: 
                                            self.error = TE.ERRORS( self.line ).ERROR4()
                                            break
                                    elif self.get_block == 'unless:' :
                                        self.next_line              = j+1
                                        self.loop.append( ( self.normal_string, True ) )
                                        self.isbreak    = True
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = unless_interpreter.INTERNAL_UNLESS_STATEMENT(self.master,
                                                                self.data_base, self.line).UNLESS_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('unless')
                                                self.space      = 0
                                                self.loop.append( self._values_ )
                                            else: break
                                        else: 
                                            self.error = TE.ERRORS( self.line ).ERROR4()
                                            break                                                          
                                    elif self.get_block == 'empty'   :
                                        if self.space <= self.maxEmptyLine:
                                            self.space += 1
                                            self.loop.append( (self.normal_string, True) )
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR4()
                                            break
                                    elif self.get_block == 'any'     :
                                        self.store_value.append( self.normal_string )
                                        self.space = 0
                                        self.loop.append( (self.normal_string, True) )

                                    #############################################################
                                    #############################################################
                                    
                                    elif self.get_block == 'end:'       :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.loop.append( (self.normal_string, False) )
                                            self.try_cancel = True
                                            if self.except_key is False and self.finally_key is False:
                                                self.error = TE.ERRORS( self.line ).ERROR5()
                                                break
                                            else:  break
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break
                                    elif self.get_block == 'except:'    :
                                        if self.key_else_activation == None:
                                            if self.store_value:
                                                self.history.append( 'except' )
                                                self.store_value        = []
                                                self.except_key         = True
                                                self.loop.append( (self.normal_string, False) )
                                            else:
                                                self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                                break
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR1( 'finally' )
                                            break
                                    elif self.get_block == 'finally:'   :
                                        if self.index_finally < 1:
                                            if self.store_value:
                                                self.index_finally         += 1
                                                self.key_else_activation    = True
                                                self.store_value            = []
                                                self.history.append( 'finally' )
                                                self.finally_key            = True
                                                self.loop.append( (self.normal_string, False) )
                                            else:
                                                self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                                break     
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR3( 'finally' )
                                            break                              
                                    else:
                                        self.error = TE.ERRORS( self.line ).ERROR4()
                                        break
                                else: break

                            else:
                                self.get_block, self.value, self.error = externalTry.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                                    data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)
                                   
                                if self.error is None:
                                    if   self.get_block == 'end:'       :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.loop.append( (self.normal_string, False) )
                                            self.try_cancel = True
                                            if self.except_key is False and self.finally_key is False:
                                                self.error = TE.ERRORS( self.line ).ERROR5()
                                                break
                                            else:  break
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break
                                    elif self.get_block == 'except:'    :
                                        if self.key_else_activation is None:
                                            if self.store_value:
                                                self.history.append( 'except' )
                                                self.store_value        = []
                                                self.except_key         = True
                                                self.loop.append( (self.normal_string, False) )
                                            else:
                                                self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                                break
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR1( 'finally' )
                                            break
                                    elif self.get_block == 'finally:'   :
                                        if self.index_finally < 1:
                                            if self.store_value:
                                                self.index_finally         += 1
                                                self.key_else_activation    = True
                                                self.store_value            = []
                                                self.history.append( 'finally' )
                                                self.finally_key            = True
                                                self.loop.append( (self.normal_string, False) )
                                            else:
                                                self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                                break     
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR3( 'finally' )
                                            break                              
                                    elif self.get_block == 'empty'      :
                                        if self.space <= self.maxEmptyLine :
                                            self.space += 1
                                            self.loop.append( (self.normal_string, False ) )
                                        else:
                                            self.error = TE.ERRORS( self.line ).ERROR4()
                                            break
                                    else:
                                        self.error = TE.ERRORS( self.line ).ERROR4()
                                        break
                                else: break
                        else: break
                    else:  pass
                else:
                    self.error = TE.ERRORS( self.line ).ERROR4()
                    break
        else:  self.error = Ie.ERRORS( self.line ).ERROR5()
        ############################################################################
        
        return self.loop , self.error