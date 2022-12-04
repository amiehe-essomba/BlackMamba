from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import unless_interpreter
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.STDIN.WinSTDIN                              import stdin
from script.PARXER.PARXER_FUNCTIONS._IF_                import IfError              as Ie
from statement                                          import InternalStatement    as IS
from statement                                          import externalIF           as eIF

class EXTERNAL_IF_STATEMENT:
    def __init__(self, master, data_base, line):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def IF_STATEMENT(self, 
            tabulation  : int   = 1,
            loop_list   : list  = [],
            _type_      : str   = 'conditional'
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
        self.history                = [ 'if' ]
        self.loop                   = []
        self.loop_list              = loop_list
        self.next_line              = 0
        self.loop_loop              = []
        self.maxEmptyLine           = 2

        ############################################################################
        if self.loop_list:
            for  j, _string_ in enumerate( self.loop_list ):
                self.if_line    += 1
                self.line       += 1
                
                if _string_ :
                    if _type_ != 'conditional': pass 
                    else:  _string_ = '\t'+_string_
                    
                    if j >= self.next_line:
                        k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)                   
                        self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                            self.line ).STDIN_FOR_INTERPRETER( k, _string_ )
                        if self.error is None:
                            if self.active_tab is True:
                                
                                self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                            data_base=self.data_base, line=self.line).INTERPRETER_BLOCKS(tabulation=k+1, function=_type_, typ='if',
                                                                                                interpreter = False)
                                
                                if self.error  is None:
                                    
                                    if   self.get_block == 'if:'     :
                                        self.next_line              = j+1
                                        self.loop.append( ( self.normal_string, True ) )
                                        self.isbreak    = True
                                        self.NewLIST1    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).IF(self.tabulation, 
                                                                        self.loop_list[self.next_line : ])
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = INTERNAL_IF_STATEMENT(self.master,
                                                                self.data_base, self.line).IF_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('if')
                                                self.space      = 0
                                                self.loop.append( self._values_ )
                                            
                                            else: break
                                        else: 
                                            self.error = Ie.ERRORS( self.line ).ERROR4()
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
                                            self.error = Ie.ERRORS( self.line ).ERROR4()
                                            break                                                          
                                    elif self.get_block == 'empty'   :
                                        if self.space <= self.maxEmptyLine:
                                            self.space += 1
                                            self.loop.append( (self.normal_string, True) )
                                        else:
                                            self.error = Ie.ERRORS( self.line ).ERROR4()
                                            break
                                    elif self.get_block == 'any'     :
                                        self.store_value.append( self.normal_string )
                                        self.space = 0
                                        self.loop.append( (self.normal_string, True) )

                                    #############################################################
                                    #############################################################
                                    
                                    elif self.get_block == 'end:'    :
                                        self.loop.append( (self.normal_string, False) )
                                    elif self.get_block == 'elif:'   :
                                        self.history.append( 'elif' )
                                        self.store_value        = []
                                        self.loop.append( (self.normal_string, False) )
                                    elif self.get_block == 'else:'   :
                                        self.history.append( 'else' )
                                        self.loop.append( (self.normal_string, False) )                                     
                                    else:
                                        self.error = Ie.ERRORS( self.line ).ERROR4()
                                        break
                                    
                                else:break

                            else:
                                self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                        data_base=self.data_base, line=self.line).BLOCKS( tabulation=self.tabulation, function=_type_, 
                                                                                        interpreter=True)
                                
                                if self.error is None:
                                    if   self.get_block == 'end:'   :
                                        self.loop.append( (self.normal_string, False) )
                                        break    
                                    elif self.get_block == 'elif:'  :
                                        self.history.append( 'elif' )
                                        self.store_value        = []
                                        self.loop.append( (self.normal_string, False) )
                                    elif self.get_block == 'else:'  :
                                        self.history.append( 'else' )
                                        self.loop.append( (self.normal_string, False) )
                                    elif self.get_block == 'empty'  :
                                        if self.space <= self.maxEmptyLine:
                                            self.space += 1
                                            self.loop.append( (self.normal_string, False) )
                                        else:
                                            self.error = Ie.ERRORS( self.line ).ERROR4()
                                            break
                                    else:
                                        self.error = Ie.ERRORS( self.line ).ERROR4()
                                        break
                                
                                else: break
                        else: break
                    else:  pass
                else:
                    self.error = Ie.ERRORS( self.line ).ERROR4()
                    break
        else:  self.error = Ie.ERRORS( self.line ).ERROR5()
        ############################################################################
        
        return self.loop , self.error

class INTERNAL_IF_STATEMENT:
    def __init__(self, master, data_base, line):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def IF_STATEMENT(self, 
                    tabulation     : int   = 1, 
                    loop_list      : list  = [], 
                    _type_         : str   = 'conditional',
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
        self.history                = [ 'if' ]
        self.loop                   = []
        self.loop_list              = loop_list
        self.next_line              = 0
        self.loop_loop              = []
        self.maxEmptyLine           = 2

        ############################################################################
        if self.loop_list:
            for  j, _string_ in enumerate( self.loop_list ):
                
                if _string_:
                    if _type_ != 'conditional': pass 
                    else:  _string_ = '\t'+_string_
                
                    self.if_line    += 1
                    self.line       += 1
                
                    if j >= self.next_line:
                        k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)                      
                        self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                            self.line ).STDIN_FOR_INTERPRETER( k, _string_ )
                        if self.error is None:
                            if self.active_tab is True:

                                self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                            data_base=self.data_base, line=self.line).INTERPRETER_BLOCKS(tabulation=k+1, function=_type_, typ='if',
                                                                                                         interpreter = False)
                                
                                if self.error  is None:
                                    if   self.get_block == 'if:'     :
                                        self.next_line              = j+1
                                        self.loop.append( ( self.normal_string, True ) )
                                        
                                        self.NewLIST1    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).IF(self.tabulation, 
                                                                        self.loop_list[self.next_line : ])
                                        #print(self.NewLIST)
                                        #print(self.NewLIST1, '@@@')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = EXTERNAL_IF_STATEMENT(self.master,
                                                                self.data_base, self.line).IF_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('if')
                                                self.space      = 0
                                                self.loop.append( self._values_)
                                            else: break
                                        else: 
                                            self.error = Ie.ERRORS( self.line ).ERROR4()
                                            break                             
                                    elif self.get_block == 'unless:' :
                                        self.next_line              = j+1
                                        self.loop.append( ( self.normal_string, True ) )
            
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                    
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = unless_interpreter.EXTERNAL_UNLESS_STATEMENT(self.master,
                                                                self.data_base, self.line).UNLESS_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('unless')
                                                self.space      = 0
                                                self.loop.append( self._values_)
                                            else: break
                                        else: 
                                            self.error = Ie.ERRORS( self.line ).ERROR4()
                                            break                                                        
                                    elif self.get_block == 'empty'   :
                                        if self.space <= self.maxEmptyLine:
                                            self.space += 1
                                            self.loop.append( (self.normal_string, True ) )
                                        else:
                                            self.error = Ie.ERRORS( self.line ).ERROR4()
                                            break
                                    elif self.get_block == 'any'     :
                                        self.store_value.append( self.normal_string )
                                        self.space = 0
                                        self.loop.append( (self.normal_string, True) )
                                        
                                    #############################################################
                                    #############################################################
                                    
                                    elif self.get_block == 'end:'    :
                                        self.loop.append( (self.normal_string, False) )                                                   
                                    elif self.get_block == 'elif:'   :
                                        self.history.append( 'elif' )
                                        self.store_value        = []
                                        self.loop.append( (self.normal_string, False) )
                                    elif self.get_block == 'else:'   :
                                        self.history.append( 'else' )
                                        self.loop.append( (self.normal_string, False) )
                                    else:
                                        self.error = Ie.ERRORS( self.line ).ERROR4()
                                        break                                  
                                else:break
                            else:
                                self.get_block, self.value, self.error = eIF.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                        data_base=self.data_base, line=self.line).BLOCKS( tabulation=self.tabulation, function=_type_, 
                                                                                        interpreter=True)
                                if self.error is None:
                                    if   self.get_block == 'end:'   :
                                        self.loop.append( (self.normal_string, False) )
                                        break
                                    elif self.get_block == 'elif:'  :
                                        self.history.append( 'elif' )
                                        self.loop.append( (self.normal_string, False) )
                                    elif self.get_block == 'else:'  :
                                        self.history.append( 'else' )
                                        self.loop.append( (self.normal_string, False) )
                                    elif self.get_block == 'empty'  :
                                        if self.space <= self.maxEmptyLine:
                                            self.space += 1
                                            self.loop.append( (self.normal_string, False) )
                                        else:
                                            self.error = Ie.ERRORS( self.line ).ERROR4()
                                            break
                                    else:
                                        self.error = Ie.ERRORS( self.line ).ERROR4()
                                        break    
                                else: break
                        else: break
                    else:  pass
                else: 
                    self.error = Ie.ERRORS( self.line ).ERROR4()
                    break
        else:
            self.error = Ie.ERRORS( self.line ).ERROR5()
        ############################################################################
        
        return self.loop , self.error

class EMPTY:
    def __init__(self, data_base: dict, line: int ):
        self.data_base  = data_base 
        self.line       = line
    
    def EMPTY(self, last : str = '', string : str = '' ):
        k               = None 
        self.newString  = ''
        
        self.list   = ['if', 'unless', 'else', 'elif']
       
        if last in self.list:
            k = stdin.STDIN(self.data_base, self.line ).ENCODING( string ) + 2
        else: k = stdin.STDIN(self.data_base, self.line ).ENCODING( string )+1
        
        self.newString += '\t'*k+"'@'"
        
        return  self.newString
            