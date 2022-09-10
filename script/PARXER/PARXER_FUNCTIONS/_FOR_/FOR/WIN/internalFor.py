from statement.comment                                      import externalCmt
from script                                                 import control_string
from statement                                              import InternalStatement as IS
from script.PARXER.PARXER_FUNCTIONS._FOR_.FOR               import forError as fe
from script.PARXER.PARXER_FUNCTIONS._FOR_.IF.WINDOWS        import WindowsIF as wIF
from script.PARXER.PARXER_FUNCTIONS._FOR_.UNLESS            import WindowsUnless as wU
from script.PARXER.LEXER_CONFIGURE                          import lexer_and_parxer
from script.PARXER.PARXER_FUNCTIONS._FOR_.SWITCH.WINDOWS    import WindowsSwitch as WSw
from script.PARXER.PARXER_FUNCTIONS._FOR_.WHILE.WINDOWS     import WindowsWhile as WWh
from script.PARXER.PARXER_FUNCTIONS._FOR_.BEGIN.WINDOWS     import begin
from script.PARXER.PARXER_FUNCTIONS._FOR_.FOR.WIN           import WindowsFor as wFor


class INTERNAL_FOR:
    def __init__(self, 
            master      : str,              
            data_base   : dict,             
            line        : int ,
            history     : list,
            store_value : list,
            space       : int
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
        #contriling string
        self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)
        # lexer and parxer 
        self.lex_par                = lexer_and_parxer
      
    def FOR(self, 
            loop        : list,
            tabulation  : int = 1,
            _type_      : str = 'loop',
            c           : str = '',
            term        : str = '' 
            ):
        
         ############################################################################
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.index_else             = 0
        self.if_line                = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.loop_for               = loop
        self.max_emptyLine          = 5
        self.for_cancel             = False
        ############################################################################

        for i in range(1): 
            # concatening string and extraction of string concatenated , tabulation for and indensation and error        
            self.string, self.active_tab, self.error = self.analyse.BUILD_CON(string=self.master,
                                                                        tabulation=self.tabulation)
            if self.error is None:
                # build normal string 
                self.normal_string = self.analyse.BUILD_NON_CON(string=self.master, tabulation=self.tabulation)
                # when indentation is True
                
                # when indentation is True
                if self.active_tab is True:
                    self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                            data_base=self.data_base, line=self.if_line).BLOCKS(tabulation = self.tabulation + 1, function = _type_,
                                                                                interpreter = False)

                    if self.error  is None:
                        # if block
                        if self.get_block   == 'if:'            :
                            self.store_if_values    = []
                            self.store_if_values.append( (self.normal_string, True) )
                            self.if_values, self.error = wIF.EXTERNAL_IF_WINDOWS(data_base=self.data_base, line=self.line, term=term ).TERMINAL(
                               bool_value= self.value, tabulation=self.tabulation + 1, _type_ = _type_, c=c )
                 
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'if' )
                                self.store_if_values.append( self.if_values )
                                self.loop_for.append( {'if' : self.store_if_values, 'value' : self.value, 'tabulation' : (self.tabulation + 1) } )
                                self.store_if_values = []
                            else:break 
                        # unless block
                        elif self.get_block == 'unless:'        :
                            self.store_if_values    = []
                            self.store_if_values.append( (self.normal_string, True) )
                            self.if_values, self.error  = wU.EXTERNAL_UNLESS_WINDOWS(data_base=self.data_base, line=self.if_line, 
                                    term=term ).TERMINAL(  bool_value= self.value, tabulation=self.tabulation + 1, _type_ = _type_, c=c )
                            
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'unless' )
                                self.store_if_values.append( self.if_values )
                                self.loop_for.append( {'unless' : self.store_if_values, 'value' : self.value, 'tabulation' : (self.tabulation + 1) } )
                                self.store_if_values = []
                            else: break
                        # switch block
                        elif self.get_block == 'switch:'        :
                            self.store_if_values    = []
                            self.store_if_values.append( (self.normal_string, True) )
                            self.if_values, self.error  = WSw.EXTERNAL_SWITCH_WINDOWS(data_base=self.data_base,
                                       line=self.if_line, term=term).TERMINAL( bool_value=self.value, tabulation=self.tabulation + 1, _type_=_type_, c=c)
                            
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'switch' )
                                self.store_if_values.append( self.if_values )
                                self.loop_for.append( {'switch' : self.store_if_values, 'value' : self.value, 'tabulation' : (self.tabulation + 1) } )
                                self.store_if_values = []
                            else: break
                        # while loop
                        elif self.get_block == 'while:'         :
                            self.store_if_values    = []
                            self.store_if_values.append( (self.normal_string, True) )
                            self.if_values, self.error  = WWh.EXTERNAL_WHILE_WINDOWS(data_base=self.data_base, line=self.if_line, term=term ).TERMINAL(
                                            bool_value= self.value, tabulation=self.tabulation + 1, _type_ = _type_, c=c)
                            
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'while' )
                                self.store_if_values.append( self.if_values )
                                self.loop_for.append( {'while' : self.store_if_values, 'value' : self.value, 'tabulation' : (self.tabulation + 1) } )
                                self.store_if_values = []
                            else: break
                         # for loop
                        elif self.get_block == 'for:'           :
                            self.store_if_values    = []
                            self.store_if_values.append( (self.normal_string, True) )
                            self.if_values, self.tab, self.error  = wFor.EXTERNAL_FOR_WINDOWS(data_base=self.data_base, line=self.line, term=term ).TERMINAL(
                                    tabulation=self.tabulation + 1, _type_ = _type_, c=c )
                            
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'for' )
                                self.store_if_values.append( self.if_values )
                                self.loop_for.append( {'for' : self.store_if_values, 'value' : self.value, 'tabulation' : (self.tabulation + 1) } )
                                self.store_if_values = []
                            else: break
                        # multi-line comments
                        elif self.get_block == 'begin:'         :
                            self.store_if_values    = []
                            self.store_if_values.append( (self.normal_string, True) )
                            self.if_values, self.error  = begin.COMMENT_WINDOWS(data_base=self.data_base,  line=self.line, 
                                                                            term=term).COMMENT( tabulation=self.tabulation + 1, c=c)
                            
                            if self.error is None:
                                self.store_value.append( self.normal_string )
                                self.history.append( 'begin' )
                                self.store_if_values.append( self.if_values )
                                self.loop_for.append( {'begin' : self.store_if_values, 'value' : self.value, 'tabulation' : (self.tabulation + 1) } )
                                self.store_if_values = []
                            else: break
                        # try block
                        elif self.get_block == 'try:'           :
                            pass
                        # empty line 
                        elif self.get_block == 'empty'          :
                            if self.space <= self.max_emptyLine:
                                self.space += 1
                                self.loop_for.append( {'empty' : (self.normal_string, True), 'value': None,  'tabulation' : (self.tabulation + 1) } )
                            else:
                                self.error = fe.ERRORS( self.line ).ERROR4()
                                break
                        # checking variables
                        elif self.get_block == 'any'            :
                            self.store_value.append( self.normal_string )
                            self._lexer_, self.error = self.lex_par.MAIN(self.value, self.data_base,
                                                                self.line).MAIN_LEXER( _id_=1, _type_='loop' )
                            if self.error is None:
                                self.loop_for.append( {'any' : (self.value, True), 'value' : None,
                                                        'tabulation' : (self.tabulation + 1), 'lex' : self._lexer_} )
                                self.space  = 0
                            else:break
                    else:break
                else:
                    self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(normal_string=self.normal_string,
                            data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)

                    if self.error is None:
                        if   self.get_block == 'end:'  :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.loop_for.append( (self.normal_string, False) )
                                self.for_cancel = True
                                break
                            else:
                                self.error = fe.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                break                        
                        elif self.get_block == 'empty' :
                            if self.space <= self.max_emptyLine:
                                self.space += 1
                                self.loop_for.append( (self.normal_string, False ))
                            else:
                                self.error = fe.ERRORS( self.line ).ERROR4()
                                break
                        else:
                            self.error = fe.ERRORS( self.line ).ERROR4()
                            break
                    else:break
            else:
                if self.tabulation == 1: break
                else:
                    # if tabulation is false ( not indentation)
                    self.error = None
                    self.normal_string = self.analyse.BUILD_NON_CON(string=self.master,tabulation=self.tabulation)
                    
                    self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(normal_string=self.normal_string,
                            data_base=self.data_base, line=self.line).BLOCKS(tabulation=self.tabulation)

                    if self.error is None:
                        if   self.get_block == 'end:'  :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.loop_for.append( (self.normal_string, False ))
                                self.for_cancel = True
                                break
                            else:
                                self.error = fe.ERRORS( self.line ).ERROR2(self.history[ -1 ] )
                                break
                        elif self.get_block == 'empty' :
                            if self.space <= self.max_emptyLine:
                                self.space += 1
                                self.loop_for.append((self.normal_string, False))
                            else:
                                self.error = fe.ERRORS(  self.line ).ERROR4()
                                break
                        else:
                            self.error = fe.ERRORS( self.line ).ERROR4()
                            break
                    else:break
    
        ############################################################################
        return self.loop_for, self.for_cancel, self.error