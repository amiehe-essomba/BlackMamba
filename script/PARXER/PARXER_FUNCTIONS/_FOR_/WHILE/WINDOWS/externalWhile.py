from script                                                 import control_string
from script.LEXER.FUNCTION                                  import main
from script.PARXER.PARXER_FUNCTIONS.WHILE                   import whileError           as WEr
from statement                                              import InternalStatement    as IS
from statement.comment                                      import externalCmt
from script.PARXER.PARXER_FUNCTIONS._FOR_.UNLESS            import WindowsUnless        as wU
from script.PARXER.PARXER_FUNCTIONS._FOR_.IF.WINDOWS        import WindowsIF            as wIF
from script.PARXER.PARXER_FUNCTIONS._FOR_.SWITCH.WINDOWS    import WindowsSwitch        as WSw
from script.PARXER.PARXER_FUNCTIONS._FOR_.WHILE.WINDOWS     import WindowsWhile         as wwh
from script.PARXER.PARXER_FUNCTIONS._FOR_.TRY.WIN           import WindowsTry           as wTry
from script.PARXER.PARXER_FUNCTIONS._FOR_.BEGIN.WINDOWS     import begin
from script.PARXER.PARXER_FUNCTIONS._FOR_.FOR.WIN           import subWindowsFor        as sWFor


class EXTERNAL_WHILE:
    def __init__(self, 
            master      : str,              
            data_base   : dict,             
            line        : int ,
            history     : list,
            store_value : list,
            space       : int,    
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
        #canceling def 
        self.def_cancel         = False
        #contriling string
        self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)
   
    def WHILE(self, 
                    bool_value  : bool, 
                    loop        : list,
                    tabulation  : int = 1,
                    _type_      : str = 'loop',
                    c           : str = '',
                    term        : str = '',
                    callbacks   : dict= {}
                    ):
        
        ############################################################################
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.if_line                = self.line

        ############################################################################
        self.active_tab             = None
        self.tabulation             = tabulation
        self.loop                   = loop
        self.max_emtyLine           = 5
        self.while_cancel           = False
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
                            data_base=self.data_base, line=self.if_line).BLOCKS(tabulation = self.tabulation + 1, function = _type_,
                                                                                interpreter = False)

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
                        # if block
                        elif self.get_block == 'if:'     :
                            self.store_value.append(self.normal_string)
                            self.loop.append( ( self.normal_string, True ) )
                            self._values_, self.error = wIF.EXTERNAL_IF_WINDOWS(data_base=self.data_base, 
                                            line=self.if_line, term=term ).TERMINAL(
                                            bool_value= self.value, tabulation=self.tabulation + 1, 
                                            _type_ = _type_, c=c, callbacks=callbacks)
                            
                            if self.error is None:
                                self.history.append('if')
                                self.space = 0
                                self.loop.append( self._values_ )

                            else:  break                  
                        # while loop
                        elif self.get_block == 'while:'  :
                            self.store_value.append(self.normal_string)
                            self.loop.append( ( self.normal_string, True ) )
                            self._values_, self.error = wwh.EXTERNAL_WHILE_WINDOWS(data_base=self.data_base, 
                                            line=self.if_line, term=term ).TERMINAL(
                                            bool_value= self.value, tabulation=self.tabulation + 1, 
                                            _type_ = _type_, c=c, callbacks=callbacks)

                            if self.error is None:
                                self.history.append('while')
                                self.space = 0
                                self.loop.append( self._values_ )
                            else: break
                        # try block
                        elif self.get_block == 'try:'    :
                            self.store_value.append(self.normal_string)
                            self.loop.append( ( self.normal_string, True ) )
                            
                            self._values_, self.error = wTry.EXTERNAL_TRY_WINDOWS(data_base=self.data_base, line=self.line, term=term ).TERMINAL(
                               tabulation=self.tabulation + 1, _type_ = _type_, c=c )

                            if self.error is None:
                                self.history.append( 'try' )
                                self.space = 0
                                self.loop.append( self._values_ )

                            else: break 
                        # unless block
                        elif self.get_block == 'unless:' :
                            self.store_value.append(self.normal_string)
                            self.loop.append((self.normal_string, True))
                            # calling unless modules
                            self._values_, self.error = wU.EXTERNAL_UNLESS_WINDOWS(data_base=self.data_base, 
                                    line=self.if_line, term=term ).TERMINAL(
                                    bool_value= self.value, tabulation=self.tabulation + 1, 
                                    _type_ = _type_, c=c , callbacks=callbacks)
                            
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
                        # switch block
                        elif self.get_block == 'switch:' :
                            self.store_value.append(self.normal_string)
                            self.loop.append((self.normal_string, True))
                            self._values_, self.error = WSw.EXTERNAL_SWITCH_WINDOWS(data_base=self.data_base, line=self.if_line, 
                                                term=term).TERMINAL(  bool_value=self.value, tabulation=self.tabulation + 1, _type_=_type_, c=c)
                            
                            if self.error is None:
                                self.history.append( 'switch' )
                                self.space = 0
                                self.loop.append( self._values_ )
                            else:  break
                        # empty line
                        elif self.get_block == 'empty'   :
                            self.store_value.append(self.normal_string)
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.loop.append( (self.normal_string, True) )
                            else:
                                self.error = WEr.ERRORS( self.if_line ).ERROR4()
                                break
                        # checking value 
                        elif self.get_block == 'any'     :
                            self.store_value.append( self.normal_string )
                            self.space = 0
                            self.error      = main.SCANNER(self.value, self.data_base,
                                                        self.line).SCANNER(_id_ = 1, _type_= _type_, _key_=True)
                            if self.error is None: self.loop.append( (self.normal_string, True) )
                            else: break
                    else:  break
                else:
                    self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(normal_string=self.normal_string,
                                data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)

                    if self.error is None:
                        # break loop while if "end" is detected 
                        if   self.get_block == 'end:'  :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.loop.append( (self.normal_string, False) )
                                self.while_cancel = True
                                break
                            else:
                                self.error =  WEr.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                break
                        # empty line
                        elif self.get_block == 'empty' :
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.loop.append( (self.normal_string, False) )
                            else:
                                self.error =  WEr.ERRORS( self.if_line ).ERROR4()
                                break
                        else:
                            self.error =  WEr.ERRORS( self.if_line ).ERROR4()
                            break
                    else: break

            else:
                if self.tabulation == 1:  break
                else:
                    # if tabulation is false ( not indentation)
                    self.error = None
                    self.normal_string = self.analyse.BUILD_NON_CON(string=self.master,tabulation=self.tabulation)
                    
                    self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(normal_string=self.normal_string,
                                data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)

                    if self.error is None:
                        # break loop while if "end" is detected 
                        if   self.get_block == 'end:'  :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.loop.append( (self.normal_string, False) )
                                self.while_cancel = True
                                break
                            else:
                                self.error =  WEr.ERRORS( self.if_line ).ERROR2(self.history[ -1 ] )
                                break
                        # empty line
                        elif self.get_block == 'empty' :
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.loop.append( (self.normal_string, False) )
                            else:
                                self.error =  WEr.ERRORS(  self.if_line ).ERROR4()
                                break
                        else:
                            self.error =  WEr.ERRORS( self.if_line ).ERROR4()
                            break
                    else:  break

        ############################################################################

        return self.loop , self.while_cancel, self.error