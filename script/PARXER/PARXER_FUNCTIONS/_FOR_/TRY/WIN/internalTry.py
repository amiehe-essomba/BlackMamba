from script                                                 import control_string
from statement                                              import InternalStatement    as IS
from script.PARXER.PARXER_FUNCTIONS._FOR_.IF.WINDOWS        import WindowsIF            as wIF
from script.PARXER.PARXER_FUNCTIONS._FOR_.UNLESS            import WindowsUnless        as wU
from script.PARXER.LEXER_CONFIGURE                          import lexer_and_parxer
from script.PARXER.PARXER_FUNCTIONS._FOR_.SWITCH.WINDOWS    import WindowsSwitch        as WSw
from script.PARXER.PARXER_FUNCTIONS._FOR_.WHILE.WINDOWS     import WindowsWhile         as WWh
from script.PARXER.PARXER_FUNCTIONS._FOR_.BEGIN.WINDOWS     import begin
from script.PARXER.PARXER_FUNCTIONS._FOR_.FOR.WIN           import subWindowsFor        as sWFor
from script.PARXER.PARXER_FUNCTIONS._FOR_.TRY.WIN           import WindowsTry           as wTry
from script.PARXER.PARXER_FUNCTIONS._TRY_                   import tryError             as TE
from statement                                              import externalTry 


class INTERNAL_TRY:
    def __init__(self, 
            master      : str,              
            data_base   : dict,             
            line        : int ,
            history     : list,
            store_value : list,
            space       : int,
            try_block   : dict
            ):
        
        # main string
        self.master             = master
        # current line in the IDE
        self.line               = line
        # data base 
        self.data_base          = data_base
        # history of command 
        self.history            = history
        # canceling def when any command was not typed
        self.store_value        = store_value
        # counting empty line 
        self.space              = space
        # try block only for except and finally
        self.try_block          = try_block
        #contriling string
        self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)
        # lexer and parxer 
        self.lex_par            = lexer_and_parxer

    def TRY(self, 
            loop        : list,
            tabulation  : int = 1,
            _type_      : str = 'try',
            c           : str = '',
            term        : str = '' 
            ):
        
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.active_tab             = None
        self.tabulation             = tabulation
        self.max_emtyLine           = 5
        self.try_cancel             = False
        
        ############################################################################
        self.index_finally          = self.try_block['index_finally']
        self.locked_error           = self.try_block['locked_error']
        self.get_errors             = self.try_block['get_errors']
        self.key_else_activation    = self.try_block['key_else_activation']
        self.finally_key            = self.try_block['finally_key']
        self.except_key             = self.try_block['except_key']
        self.active_calculations    = self.try_block['active_calculations']
        self.loop                   = loop
        ############################################################################
        

        for i in range(1): 
            # concatening string and extraction of string concatenated , tabulation for and indensation and error        
            self.string, self.active_tab, self.error = self.analyse.BUILD_CON(string=self.master,
                                                                        tabulation=self.tabulation)

            if self.error is None:
                # build normal string 
                self.normal_string = self.analyse.BUILD_NON_CON(string=self.master, tabulation=self.tabulation)
                # when indentation is True
                if self.active_tab is True:
                    self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                            data_base=self.data_base, line=self.line).BLOCKS(tabulation = self.tabulation + 1, function = _type_,
                                                                                interpreter = False, locked=True)
            
                    if self.error  is None:
                        # begin block
                        if self.get_block   == 'begin:'  :
                            self.store_value.append(self.normal_string)
                            self.loop.append( ( self.normal_string, True ) )
                            self._values_, self.error  = begin.COMMENT_WINDOWS(data_base=self.data_base,  line=self.line, 
                                                                            term=term).COMMENT( tabulation=self.tabulation + 1, c=c)
                            if self.error is None:
                                self.history.append( 'begin' )
                                self.space = 0
                                self.loop.append( self._values_ )
                            else: break 
                        # if statement block
                        elif self.get_block == 'if:'     :
                            self.store_value.append( self.normal_string )
                            self.loop.append( (self.normal_string, True ) )

                            self._values_, self.error = wIF.EXTERNAL_IF_WINDOWS(data_base=self.data_base, line=self.line, term=term ).TERMINAL(
                               bool_value= self.value, tabulation=self.tabulation + 1, _type_ = _type_, c=c )

                            if self.error is None:
                                self.history.append( 'if' )
                                self.space = 0
                                self.loop.append( self._values_ )
                            else: break
                        # try block
                        elif self.get_block == 'try:'    :
                            self.store_value.append( self.normal_string )
                            self.loop.append( (self.normal_string, True) )

                            self._values_, self.error = wTry.EXTERNAL_TRY_WINDOWS(data_base=self.data_base, line=self.line, term=term ).TERMINAL(
                               tabulation=self.tabulation + 1, _type_ = _type_, c=c )
                            if self.error is None:
                                self.history.append( 'unless' )
                                self.space = 0
                                self.loop.append( self._values_ )
                            else:  break
                        # unless statement block
                        elif self.get_block == 'unless:' :
                            self.store_value.append(self.normal_string)
                            self.loop.append((self.normal_string, True))

                            self._values_, self.error  = wU.EXTERNAL_UNLESS_WINDOWS(data_base=self.data_base, line=self.line, 
                                    term=term ).TERMINAL(  bool_value= self.value, tabulation=self.tabulation + 1, _type_ = _type_, c=c )

                            if self.error is None:
                                self.history.append( 'unless' )
                                self.space = 0
                                self.loop.append( self._values_ )
                            else:  break
                        # for loop
                        elif self.get_block == 'for:'    :
                            self.store_value.append(self.normal_string)
                            self.loop.append( ( self.normal_string, True ) )
                            
                            self._loop_, self.tab, self.error  = sWFor.INTERNAL_FOR_WINDOWS(data_base=self.data_base, line=self.line,
                                    term=term ).TERMINAL( tabulation=self.tabulation + 1, _type_ = _type_, c=c )
                            if self.error is None:
                                self.history.append( 'for' )
                                self.space = 0
                                self.loop.append( (self._loop_, self.tab, self.error) )
                            else: break 
                        # switch statement block
                        elif self.get_block == 'switch:' :
                            self.loop.append((self.normal_string, True))
                            self._values_, self.error  = WSw.EXTERNAL_SWITCH_WINDOWS(data_base=self.data_base,
                                       line=self.if_line, term=term).TERMINAL( bool_value=self.value, tabulation=self.tabulation + 1, _type_=_type_, c=c)
                            
                            if self.error is None:
                                self.history.append( 'switch' )
                                self.space = 0
                                self.loop.append( self._values_ )
                            else:  break
                        # while loop
                        elif self.get_block == 'while:'  :
                            self.loop.append((self.normal_string, True))
                            self._values_, self.error  = WWh.EXTERNAL_WHILE_WINDOWS(data_base=self.data_base, line=self.if_line, term=term ).TERMINAL(
                                            bool_value= self.value, tabulation=self.tabulation + 1, _type_ = _type_, c=c)
                            
                            if self.error is None:
                                self.history.append( 'while' )
                                self.space = 0
                                self.loop.append( self._values_ )
                            else:  break
                        # empty line 
                        elif self.get_block == 'empty'   :
                            if self.space <= self.max_emtyLine :
                                self.space += 1
                                self.loop.append( ( self.normal_string, True ) )
                            else:
                                self.error = TE.ERRORS( self.line ).ERROR4()
                                break
                        # value
                        elif self.get_block == 'any'     :
                            self.store_value.append(self.normal_string)
                            self.space = 0
                            self.loop.append( (self.normal_string, True) )
                    else:  break
                else:
                    self.get_block, self.value, self.error = externalTry.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string, 
                                                data_base=self.data_base, line=self.line).BLOCK( tabulation=self.tabulation)
                    
                    if self.error is None:
                        # end block
                        if   self.get_block == 'end:'    :
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
                        # exception block
                        elif self.get_block == 'except:' :
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
                        # finally block
                        elif self.get_block == 'finally:':
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
                        # empty line
                        elif self.get_block == 'empty'   :
                            if self.space <= self.max_emtyLine :
                                self.space += 1
                                self.loop.append(( self.normal_string, False ))
                            else:
                                self.error = TE.ERRORS( self.line ).ERROR4()
                                break
                        # if error
                        else:
                            self.error = TE.ERRORS( self.line ).ERROR4()
                            break
                    else:  break
            else:
                if self.tabulation == 1: break
                else:
                    # if tabulation is false ( not indentation)
                    self.error = None
                    self.normal_string = self.analyse.BUILD_NON_CON(string=self.master,tabulation=self.tabulation)
                    self.get_block, self.value, self.error = externalTry.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string, 
                                            data_base=self.data_base, line=self.line).BLOCK( tabulation=self.tabulation)

                    if self.error is None:
                        # end block
                        if   self.get_block == 'end:'    :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.loop.append( (self.normal_string, False) )
                                self.try_cancel = True
                                if self.except_key is True or self.finally_key is True:  break
                                elif self.except_key is True and self.finally_key is True:  break
                                else:
                                    self.error = TE.ERRORS( self.line ).ERROR5()
                                    break

                            else:
                                self.error = TE.ERRORS( self.line ).ERROR2(self.history[ -1 ] )
                                break
                        # exception block
                        elif self.get_block == 'except:' :
                            if self.key_else_activation == None:
                                if self.store_value:
                                    self.history.append( 'except' )
                                    self.bool_value     = self.value
                                    self.store_value    = []
                                    self.except_key     = True
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = TE.ERRORS( self.line ).ERROR2(self.history[-1])
                                    break
                            else:
                                self.error = TE.ERRORS( self.line ).ERROR1( 'finally' )
                                break
                        # finally block
                        elif self.get_block == 'finally:':
                            if self.index_finally < 1:
                                if self.store_value:
                                    self.index_finally += 1
                                    self.key_else_activation = True
                                    self.store_value = []
                                    self.history.append( 'finally' )
                                    self.active_calculations    = True
                                    self.finally_key            = True
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = TE.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                    break
                            else:
                                self.error = TE.ERRORS( self.line ).ERROR3( 'finally' )
                                break
                        # empty line
                        elif self.get_block == 'empty'   :
                            if self.space <= self.max_emtyLine :
                                self.space += 1
                                self.loop.append( (self.normal_string, False ) )
                            else:
                                self.error = TE.ERRORS( self.line ).ERROR4()
                                break
                        # if error
                        else:
                            self.error = TE.ERRORS( self.line ).ERROR4()
                            break
                    else:  break

        ############################################################################
        self.try_block['index_finally']         = self.index_finally        
        self.try_block['locked_error']          = self.locked_error           
        self.try_block['get_errors']            = self.get_errors             
        self.try_block['key_else_activation']   = self.key_else_activation    
        self.try_block['finally_key']           = self.finally_key            
        self.try_block['except_key']            = self.except_key
        self.try_block['active_calculations']   = self.active_calculations
        #############################################################################            

        return self.loop,  self.try_cancel, self.error
