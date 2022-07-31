from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._IF_                import end_else_elif
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import unless_statement, unless_interpreter
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment, cmt_interpreter
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.LEXER.FUNCTION                              import main
from script.STDIN.WinSTDIN                              import stdin
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:  from CythonModules.Windows                        import fileError as fe 
except ImportError: from CythonModules.Linux            import fileError as fe

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
                    _type_      : str   = 'conditional',
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

                                self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS( self.string,
                                                self.normal_string, self.data_base, self.line ).INTERPRETER_BLOCKS( k +1, function = _type_ )
                                
                                if self.error  is None:
                                    
                                    if   self.get_block == 'if:'     :
                                        self.next_line              = j+1
                                        self.loop.append( ( self.normal_string, True ) )
                                        self.isbreak    = True
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        
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
                                            self.error = ERRORS( self.line ).ERROR4()
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
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break
                                                                
                                    elif self.get_block == 'empty'   :
                                        if self.space <= self.maxEmptyLine:
                                            self.space += 1
                                            self.loop.append( (self.normal_string, True) )
                                        else:
                                            self.error = ERRORS( self.line ).ERROR4()
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
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break
                                    
                                else:break

                            else:
                                self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS( self.string,
                                            self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )
                                
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
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break

                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break
                                
                                else: break

                        else: break
                    else:  pass
                else:
                    self.error = ERRORS( self.line ).ERROR4()
                    break
        else:
            self.error = ERRORS( self.line ).ERROR5()
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

                                self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS( self.string,
                                                self.normal_string, self.data_base, self.line ).INTERPRETER_BLOCKS( k + 1, function = _type_ )
                                
                                if self.error  is None:
                                    if   self.get_block == 'if:'     :
                                        self.next_line              = j+1
                                        self.loop.append( ( self.normal_string, True ) )
            
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                    
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
                                            self.error = ERRORS( self.line ).ERROR4()
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
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break
                                                                
                                    elif self.get_block == 'empty'   :
                                        if self.space <= self.maxEmptyLine:
                                            self.space += 1
                                            self.loop.append( (self.normal_string, True ) )
                                        else:
                                            self.error = ERRORS( self.line ).ERROR4()
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
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break
                                    
                                else:break
                            else:
                                self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS( self.string,
                                            self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )
                                
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
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break

                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break
                                
                                else: break

                        else: break
                    else:  pass
                else: 
                    self.error = ERRORS( self.line ).ERROR4()
                    break
        else:
            self.error = ERRORS( self.line ).ERROR5()
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
            
class ERRORS:
    def __init__(self, line: int):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,
                                                                                                       self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str = 'else'):
        error = '{}is already defined. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. {}<< {} >> {}block '.format(self.white,
                                                                                self.cyan, string, self.green) + error
        return self.error+self.reset

    def ERROR2(self, string):
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format(self.green, self.white, self.cyan, string, self.green,
                                                                                             self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax '.format( self.white ) + error

        return self.error+self.reset

    def ERROR3(self, string: str = 'else'):
        error = 'due to {}many {}<< {} >> {}blocks. {}line: {}{}'.format(self.green, self.cyan, string, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax '.format( self.white ) + error

        return self.error+self.reset

    def ERROR4(self):
        self.error =  fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                    self.white, self.yellow, self.line )
        return self.error+self.reset
    
    def ERROR5(self, _str_ : str = 'if'):
        error = '{}close the opening statement {}<< {} >> {}block. {}line: {}{}'.format(self.yellow, self.blue, _str_, self.yellow,
                                                                                        self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. '.format( self.white ) + error

        return self.error+self.reset
