from script                                                 import control_string
from statement                                              import InternalStatement    as IS
from statement                                              import externalIF           as eIF
from script.PARXER.PARXER_FUNCTIONS._IF_                    import IfError
from script.LEXER.FUNCTION                                  import main
from script.PARXER.PARXER_FUNCTIONS._FOR_.IF.WINDOWS        import subWindowsIF         as swIF
from script.PARXER.PARXER_FUNCTIONS._FOR_.UNLESS            import WindowsUnless        as wU
from script.PARXER.PARXER_FUNCTIONS._FOR_.SWITCH.WINDOWS    import WindowsSwitch        as WSw
from script.PARXER.PARXER_FUNCTIONS._FOR_.WHILE.WINDOWS     import WindowsWhile         as WWh
from script.PARXER.PARXER_FUNCTIONS._FOR_.BEGIN.WINDOWS     import begin
from script.PARXER.PARXER_FUNCTIONS._FOR_.TRY.WIN           import WindowsTry           as wTry
from script.PARXER.PARXER_FUNCTIONS._FOR_.FOR.WIN           import subWindowsFor        as sWFor

class EXTERNAL_IF:
    def __init__(self, 
            master      : str,              
            data_base   : dict,             
            line        : int ,
            history     : list,
            store_value : list,
            space       : int,    
            else_block  : dict
            ) -> None:
        
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
        # else block 
        self.else_block         = else_block
     
    def IF(self, 
            bool_value  : bool, 
            loop        : list,
            tabulation  : int = 1,
            _type_      : str = 'conditional',
            c           : str = '',
            term        : str = ''
            ) -> tuple:
        """
        :param bool_value:
        :param tabulation:
        :param _type_:  {default value = 'conditional'}
        :return:
        """
           
        ################################################################################################
        self.if_line            = self.line                                     # counting 
        self.error              = None                                          # error 
        self.string             = ''                                            # concatented string
        self.normal_string      = ''                                            # normal string
        self.end                = ''                                            # canceling deff

        ################################################################################################
        self.active_tab         = None                                          # activating indentation 
        self.tabulation         = tabulation                                    # counting indentation 
        self.max_emtyLine       = 5                                             # max line for empty line
        self.index_else         = self.else_block['index_else']                 # contriling block else
        self.key_else_activation= self.else_block['key_else_activation']        # when elif is already activated 
        self.loop               = loop                                          # storing values
        self.if_cancel          = False                                         # canceling while loop
        ################################################################################################
        
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
                            self._values_, self.error = begin.COMMENT_WINDOWS(data_base=self.data_base,
                                                   line=self.line, term=term).COMMENT( tabulation=self.tabulation + 1, c=c)
                            if self.error is None:
                                self.history.append( 'begin' )
                                self.space = 0
                                self.loop.append( self._values_ )
                            else: break
                        # if block
                        elif self.get_block == 'if:'     :
                            self.store_value.append(self.normal_string)
                            self.loop.append( ( self.normal_string, True ) )
                            self._values_, self.error = swIF.INTERNAL_IF_WINDOWS(data_base=self.data_base, line=self.if_line, term=term ).TERMINAL(
                               bool_value= self.value, tabulation=self.tabulation + 1, _type_ = _type_, c=c )
                            
                            if self.error is None:
                                self.history.append('if')
                                self.space = 0
                                self.loop.append( self._values_ )
                            else:  break
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
                            self._values_, self.error = wU.EXTERNAL_UNLESS_WINDOWS(data_base=self.data_base, line=self.if_line, term=term ).TERMINAL(
                                        bool_value= self.value, tabulation=self.tabulation + 1, _type_ = _type_, c=c )
                            
                            if self.error is None:
                                self.history.append( 'unless' )
                                self.space = 0
                                self.loop.append( self._values_ )
                            else:  break
                        # while loop
                        elif self.get_block == 'while:'  :
                            self.store_value.append(self.normal_string)
                            self.loop.append( ( self.normal_string, True ) )
                            self._values_, self.error = WWh.EXTERNAL_WHILE_WINDOWS(data_base=self.data_base, line=self.if_line, term=term ).TERMINAL(
                                            bool_value= self.value, tabulation=self.tabulation + 1, _type_ = _type_, c=c)

                            if self.error is None:
                                self.history.append('while')
                                self.space = 0
                                self.loop.append( self._values_ )
                            else:  break
                        # for block 
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
                            self._values_, self.error = WSw.EXTERNAL_SWITCH_WINDOWS(data_base=self.data_base,  line=self.if_line, 
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
                                self.error = IfError.ERRORS( self.if_line ).ERROR4()
                                break
                        # value 
                        elif self.get_block == 'any'     :
                            self.store_value.append( self.normal_string )
                            self.space = 0
                            self.error      = main.SCANNER(master=self.value, data_base=self.data_base,  line=self.if_line).SCANNER(_id_ = 1,
                                                                                        _type_= _type_, _key_=True)
                            if self.error is None: self.loop.append( (self.normal_string, True) )
                            else: break
                    else:  break
                else:
                    self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                                    data_base=self.data_base, line=self.if_line).BLOCKS(tabulation=self.tabulation,
                                                    function=_type_, interpreter=False)
                   
                    if self.error is None:
                        # break if block
                        if   self.get_block == 'end:'  :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.loop.append( (self.normal_string, False) )
                                self.if_cancel = True
                                break
                            else:
                                self.error = IfError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                break
                        # elif block
                        elif self.get_block == 'elif:' :
                            if self.key_else_activation == None:
                                if self.store_value:
                                    self.history.append( 'elif' )
                                    self.store_value        = []
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                    break
                            else:
                                self.error = IfError.ERRORS( self.if_line ).ERROR1( 'else' )
                                break
                        # else block
                        elif self.get_block == 'else:' :
                            if self.index_else < 1:
                                if self.store_value:
                                    self.index_else             += 1
                                    self.key_else_activation    = True
                                    self.store_value            = []
                                    self.history.append( 'else' )
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = IfError.ERRORS( self.if_line ).ERROR2( self.history[ -1 ] )
                                    break

                            else:
                                self.error = IfError.ERRORS( self.if_line ).ERROR3( 'else' )
                                break
                        # empty line 
                        elif self.get_block == 'empty' :
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.loop.append( (self.normal_string, False) )
                            else:
                                self.error = IfError.ERRORS( self.if_line ).ERROR4()
                                break
                        # break line if error 
                        else:
                            self.error = IfError.ERRORS( self.if_line ).ERROR4()
                            break
                    else: break
            else:
                if self.tabulation == 1:  break
                else:
                    # if tabulation is false ( not indentation)
                    self.error = None
                    self.normal_string = self.analyse.BUILD_NON_CON(string=self.master,tabulation=self.tabulation)
                    
                    self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string,
                                            normal_string=self.normal_string, data_base=self.data_base, line=self.if_line).BLOCKS(
                                            tabulation=self.tabulation, function=_type_, interpreter=False)
                    if self.error is None:
                        # break if block
                        if   self.get_block == 'end:'   :
                            if self.store_value:
                                del self.store_value[:]
                                del self.history[:]
                                self.loop.append((self.normal_string, False))
                                self.if_cancel = True
                                break
                            else:
                                self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                break
                        # elif line 
                        elif self.get_block == 'elif:'  :
                            if self.key_else_activation == None:
                                if self.store_value:
                                    self.history.append('elif')
                                    self.store_value = []
                                    self.loop.append((self.normal_string, False))
                                else:
                                    self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                    break
                            else:
                                self.error = IfError.ERRORS(self.if_line).ERROR1('else')
                                break
                        # else block
                        elif self.get_block == 'else:'  :
                            if self.index_else < 1:
                                if self.store_value:
                                    self.index_else += 1
                                    self.key_else_activation = True
                                    self.store_value = []
                                    self.history.append('else')
                                    self.loop.append((self.normal_string, False))
                                else:
                                    self.error = IfError.ERRORS(self.if_line).ERROR2(self.history[-1])
                                    break

                            else:
                                self.error = IfError.ERRORS(self.if_line).ERROR3('else')
                                break
                        # empty line
                        elif self.get_block == 'empty'  :
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.loop.append((self.normal_string, False))
                            else:
                                self.error = IfError.ERRORS(self.if_line).ERROR4()
                                break
                        # break line if error
                        else:
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break
                    else:  break
            
        ############################################################################
        
        # updaing 
        self.else_block['index_else']           = self.index_else  
        self.else_block['key_else_activation']  = self.key_else_activation   
        
        return self.loop , self.if_cancel, self.error