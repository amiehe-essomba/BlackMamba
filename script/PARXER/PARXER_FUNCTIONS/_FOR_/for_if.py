from script                                             import control_string
from script.STDIN.WinSTDIN                              import  stdin

from script.PARXER.PARXER_FUNCTIONS._IF_                import end_else_elif
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_unless, for_begin, for_switch
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.LEXER.FUNCTION                              import main
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:
    from CythonModules.Windows                          import fileError as fe 
except ImportError:
    from CythonModules.Linux                            import fileError as fe

class EXTERNAL_IF_STATEMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def IF_STATEMENT(self, 
                    bool_value  : bool, 
                    tabulation  : int = 1,
                    _type_      : str = 'conditional'
                    ):
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_else             = 0
        self.if_line                = self.line

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'if' ]
        self.color                  = bm.fg.rbg(0,255, 0)
        ke                          = bm.fg.rbg(255,255, 0)
        self.loop                   = []
        self.max_emtyLine           = 5

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.if_line ).STDIN({ '0': ke, '1': self.color }, self.tabulation )
                if self.error is None:
                    if self.active_tab is True:

                        self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.if_line ).BLOCKS( self.tabulation + 1 )

                        if self.error  is None:
                            if self.get_block   == 'begin:'  :
                                self.store_value.append(self.normal_string)
                                self.def_starage.append( ( self.normal_string, True ) )
                                self._values_, self.error = for_begin.COMMENT_STATEMENT( self.master, self.data_base, 
                                                                                        self.line  ).COMMENT( self.tabulation + 1, self.color )
                                if self.error is None:
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    self.def_starage.append( self._values_ )

                                else: break 
                            
                            elif self.get_block == 'if:'     :
                                self.store_value.append(self.normal_string)
                                self.loop.append( ( self.normal_string, True ) )
                                self._values_, self.error = INTERNAL_IF_STATEMENT( self.master,
                                            self.data_base, self.if_line ).IF_STATEMENT( self.value, self.tabulation + 1)

                                if self.error is None:
                                    self.history.append('if')
                                    self.space = 0
                                    self.loop.append( self._values_ )

                                else:  break

                            elif self.get_block == 'try:'    :
                                self.store_value.append(self.normal_string)
                                self.error = try_statement.INTERNAL_TRY_STATEMENT(self.master,
                                        self.data_base, self.if_line).TRY_STATEMENT( self.tabulation + 1 )

                                if self.error is None:
                                    self.history.append( 'try' )
                                    self.space = 0

                                else:  break

                            elif self.get_block == 'unless:' :
                                self.store_value.append(self.normal_string)
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_unless.EXTERNAL_UNLESS_STATEMENT( self.master,
                                            self.data_base, self.line ).UNLESS_STATEMENT( self._return_, self.tabulation + 1)
                                if self.error is None:
                                    self.history.append( 'unless' )
                                    self.space = 0
                                    self.loop.append( self._values_ )

                                else:  break

                            elif self.get_block == 'switch:' :
                                self.store_value.append(self.normal_string)
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_switch.SWITCH_STATEMENT( self.master, 
                                            self.data_base, self.line ).SWITCH( self.value, self.tabulation + 1)
                                
                                if self.error is None:
                                    self.history.append( 'switch' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else:  break

                            elif self.get_block == 'empty'   :
                                self.store_value.append(self.normal_string)
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append( (self.normal_string, True) )
                                else:
                                    self.error = ERRORS( self.if_line ).ERROR4()
                                    break

                            elif self.get_block == 'any'     :
                                self.store_value.append( self.normal_string )
                                self.space = 0
                                self.error      = main.SCANNER(self.value, self.data_base,
                                                            self.line).SCANNER(_id_ = 1, _type_= _type_, _key_=True)
                                if self.error is None: self.loop.append( (self.normal_string, True) )
                                else: break

                        else:  break

                    else:
                        self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.if_line ).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'  :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append( (self.normal_string, False) )

                                    break
                                else:
                                    self.error = ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                    break

                            elif self.get_block == 'elif:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'elif' )
                                        self.store_value        = []
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                        break
                                else:
                                    self.error = ERRORS( self.if_line ).ERROR1( 'else' )
                                    break

                            elif self.get_block == 'else:' :
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append( 'else' )
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = ERRORS( self.if_line ).ERROR2( self.history[ -1 ] )
                                        break

                                else:
                                    self.error = ERRORS( self.if_line ).ERROR3( 'else' )
                                    break

                            elif self.get_block == 'empty' :
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = ERRORS( self.if_line ).ERROR4()
                                    break

                            else:
                                self.error = ERRORS( self.if_line ).ERROR4()
                                break
                        else: break

                else:
                    if self.tabulation == 1:  break

                    else:
                        self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS(self.string,
                                            self.normal_string, self.data_base, self.if_line ).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'  :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append( (self.normal_string, False) )

                                    break
                                else:
                                    self.error = ERRORS( self.if_line ).ERROR2(self.history[ -1 ] )
                                    break

                            elif self.get_block == 'elif:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'elif' )
                                        self.store_value        = []
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = ERRORS(self.if_line).ERROR2(self.history[ -1 ])
                                        break
                                else:
                                    self.error = ERRORS(self.if_line).ERROR1( 'else' )
                                    break

                            elif self.get_block == 'else:' :
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append( 'else' )
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = ERRORS(self.if_line).ERROR2(self.history[-1])
                                        break
                                else:
                                    self.error = ERRORS(self.if_line).ERROR3( 'else' )
                                    break

                            elif self.get_block == 'empty' :
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = ERRORS(  self.if_line ).ERROR4()
                                    break

                            else:
                                self.error = ERRORS( self.if_line ).ERROR4()
                                break
                        else:  break

            except KeyboardInterrupt:
                self.error = ERRORS( self.if_line ).ERROR4()
                break

        ############################################################################

        return self.loop , self.error

class INTERNAL_IF_STATEMENT:
    def __init__(self, 
                master      :any, 
                data_base   :dict, 
                line        :int
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def IF_STATEMENT(self,
                    bool_value  : bool,
                    tabulation  : int,
                    _type_      : str = 'conditional'
                    ):
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_else             = 0
        self.if_line                = self.line

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'if' ]
        self.color                  = bm.fg.rbg(0,255, 255)
        ke                          = bm.fg.rbg(255,255,0)
        self.loop                   = []
        self.max_emtyLine           = 5

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
    
            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.if_line ).STDIN({'0': ke, '1': self.color}, self.tabulation )

                if self.error is None:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.if_line ).BLOCKS( self.tabulation + 1)

                        if self.error  is None:
                            if self.get_block   == 'begin:'     :
                                self.store_value.append(self.normal_string)
                                self.def_starage.append( ( self.normal_string, True ) )
                                self._values_, self.error = for_begin.COMMENT_STATEMENT( self.master, self.data_base, 
                                                                                        self.line  ).COMMENT( self.tabulation + 1, self.color )
                                if self.error is None:
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    self.def_starage.append( self._values_ )

                                else: break 

                            elif self.get_block == 'if:'        :
                                self.store_value.append(self.normal_string)
                                self.loop.append( (self.normal_string, True) )
                                self._values_, self.error = EXTERNAL_IF_STATEMENT(  self.master,
                                        self.data_base, self.if_line).IF_STATEMENT( self.value, self.tabulation + 1)
                                if self.error is None:
                                    self.history.append( 'if' )
                                    self.space = 0
                                    self.loop.append( self._values_ )

                                else:  break

                            elif self.get_block == 'try:'       :
                                self.store_value.append(self.normal_string)
                                self.error = try_statement.EXTERNAL_TRY_STATEMENT(self.master,
                                                    self.data_base,self.if_line).TRY_STATEMENT(self.tabulation + 1)

                                if self.error is None:
                                    self.history.append( 'try' )
                                    self.space = 0

                                else: break

                            elif self.get_block == 'unless:'    :
                                self.store_value.append(self.normal_string)
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_unless.EXTERNAL_UNLESS_STATEMENT( self.master,
                                            self.data_base, self.if_line ).UNLESS_STATEMENT( self.value, self.tabulation + 1)

                                if self.error is None:
                                    self.history.append( 'unless' )
                                    self.space = 0
                                    self.loop.append( self._values_ )

                                else:  break

                            elif self.get_block == 'switch:'    :
                                self.store_value.append(self.normal_string)
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_switch.SWITCH_STATEMENT( self.master, 
                                            self.data_base, self.line ).SWITCH( self.value, self.tabulation + 1)
                                
                                if self.error is None:
                                    self.history.append( 'switch' )
                                    self.space = 0
                                    self.loop.append( self._values_ )
                                else:  break
                            
                            elif self.get_block == 'empty'      :
                                self.store_value.append(self.normal_string)
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append( self.normal_string )
                                else:  self.error = ERRORS( self.if_line ).ERROR4()

                            elif self.get_block == 'any'        :
                                self.store_value.append(self.normal_string)
                                self.space = 0
                                self.error      = main.SCANNER(self.value, self.data_base,
                                                            self.line).SCANNER(_id_ = 1, _type_= _type_, _key_=True)
                                if self.error is None: self.loop.append( (self.normal_string, True) )
                                else: break
                        else: break

                    else:
                        self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.if_line ).BLOCKS( self.tabulation )

                        if self.error is None:
                            if self.get_block   == 'end:' :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append( (self.normal_string, False) )

                                    break
                                else:
                                    self.error = ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                    break

                            elif self.get_block == 'elif:':
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'elif' )
                                        self.store_value        = []
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                        break
                                else:
                                    self.error = ERRORS( self.if_line ).ERROR1( 'else' )
                                    break

                            elif self.get_block == 'else:':
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append('else')
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = ERRORS( self.if_line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = ERRORS( self.if_line ).ERROR3( 'else' )
                                    break

                            elif self.get_block == 'empty':
                                if self.space <= self.max_emtyLine:
                                    self.space += 1
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = ERRORS( self.if_line ).ERROR4()
                                    break

                            else:
                                self.error = ERRORS( self.if_line ).ERROR4()
                                break

                        else:  break

                else:
                    self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS(self.string,
                                self.normal_string, self.data_base, self.if_line ).BLOCKS( self.tabulation )

                    if self.error is None:
                        if self.get_block   == 'end:' :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.loop.append( (self.normal_string, False) )

                                break
                            else:
                                self.error = ERRORS( self.if_line ).ERROR2(self.history[ -1 ])
                                break

                        elif self.get_block == 'elif:':
                            if self.key_else_activation == None:
                                if self.store_value:
                                    self.history.append( 'elif' )
                                    self.store_value            = []
                                    self.loop.append( (self.normal_string, False) )

                                else:
                                    self.error = ERRORS( self.if_line ).ERROR2(self.history[ -1 ])
                                    break
                            else:
                                self.error = ERRORS( self.if_line ).ERROR1( 'else' )
                                break

                        elif self.get_block == 'else:':
                            if self.index_else < 1:
                                if self.store_value:
                                    self.index_else             += 1
                                    self.key_else_activation    = True
                                    self.store_value            = []
                                    self.history.append( 'else' )
                                    self.loop.append( (self.normal_string, False) )

                                else:
                                    self.error = ERRORS( self.if_line ).ERROR2(self.history[ -1 ])
                                    break
                            else:
                                self.error = ERRORS( self.if_line ).ERROR3( 'else' )
                                break

                        elif self.get_block == 'empty':
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.loop.append( (self.normal_string, False) )
                            else:
                                self.error = ERRORS( self.if_line ).ERROR4()
                                break

                        else:
                            self.error = ERRORS( self.if_line ).ERROR4()
                            break

                    else:  break

            except KeyboardInterrupt:
                self.error = ERRORS( self.if_line ).ERROR4()
                break

        ############################################################################

        return self.loop , self.error

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