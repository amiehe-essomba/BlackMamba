from colorama           import Fore, init, Style
from script             import control_string
from script.STDIN.WinSTDIN       import  stdin

from script.PARXER.PARXER_FUNCTIONS._IF_                import end_else_elif
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_unless
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.PARXER.PARXER_FUNCTIONS._TRY_               import end_except_finaly_else

from script.LEXER.FUNCTION                              import main

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX
me = Fore.LIGHTCYAN_EX
le = Fore.RED

class EXTERNAL_IF_STATEMENT:
    def __init__(self, master, data_base, line):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def IF_STATEMENT(self, bool_value: bool, tabulation : int = 1):
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
        self.color                  = te
        self.loop                   = []

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            self.line       += 1

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.line ).STDIN({ '0': ke, '1': self.color }, self.tabulation )
                if self.error is None:
                    if self.active_tab is True:

                        self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )

                        if self.error  is None:
                            if self.get_block   == 'begin:'  :

                                self.error = comment.COMMENT_STATEMENT(self.master,
                                            self.data_base, self.line).COMMENT( self.tabulation + 1)

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'begin' )
                                    self.space = 0

                                else: break
                            elif self.get_block == 'if:'     :
                                self.loop.append( ( self.normal_string, True ) )
                                self._values_, self.error = INTERNAL_IF_STATEMENT( self.master,
                                            self.data_base, self.line ).IF_STATEMENT( self.value, self.tabulation + 1)

                                if self.error is None:
                                    self.history.append( 'if' )
                                    self.space = 0
                                    self.loop.append( self._values_ )

                                else: break
                            elif self.get_block == 'try:'    :
                                self.error = try_statement.INTERNAL_TRY_STATEMENT(self.master,
                                        self.data_base, self.line).TRY_STATEMENT( self.tabulation + 1 )

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'try' )
                                    self.space = 0

                                else: break
                            elif self.get_block == 'unless:' :
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_unless.INTERNAL_UNLESS_STATEMENT( self.master,
                                            self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1)

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'unless' )
                                    self.space = 0
                                    self.loop.append( self._values_ )

                                else: break
                            elif self.get_block == 'switch:' :
                                self.error = switch_statement.SWITCH_STATEMENT( self.master,
                                            self.data_base, self.line ).SWITCH( self.value, self.tabulation + 1)

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'switch' )
                                    self.space = 0

                                else: break
                            elif self.get_block == 'empty'   :
                                if self.space <= 2:
                                    self.space += 1
                                    self.loop.append( (self.normal_string, True) )
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break
                            elif self.get_block == 'any'     :
                                self.store_value.append( self.normal_string )
                                self.space = 0
                                self.loop.append( (self.normal_string, True) )
                        else:break

                    else:
                        self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation, 'def' )

                        if self.error is None:
                            if   self.get_block == 'end:'  :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append( (self.normal_string, False) )

                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                    break
                            elif self.get_block == 'elif:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'elif' )
                                        self.store_value        = []
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR1( 'else' )
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
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                        break

                                else:
                                    self.error = ERRORS( self.line ).ERROR3( 'else' )
                                    break
                            elif self.get_block == 'empty' :
                                if self.space <= 2:
                                    self.space += 1
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break
                            else:
                                self.error = ERRORS( self.line ).ERROR4()
                                break
                        else:
                            self._error_    = end_except_finaly_else.GET_ERROR( self.error, self.data_base,
                                                                                self.line).ERROR()
                            if self._error_ != '{}{}'.format(ke, 'SyntaxError'):
                                self.error  = None
                                if   self.normal_string[ : 4 + (self.tabulation-1)] == 't'*(self.tabulation-1) + 'elif' :
                                    if self.key_else_activation == None:
                                        if self.store_value:
                                            self.history.append( 'elif' )
                                            self.store_value = []
                                            self.loop.append( (self.normal_string, False) )

                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = ERRORS(self.line).ERROR1( 'else' )
                                        break
                                elif self.normal_string[ : 5 + (self.tabulation-1)] == 't'*(self.tabulation-1) + 'empty':
                                    if self.space <= 2:
                                        self.space += 1
                                        self.loop.append( ( self.normal_string, False ) )
                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR4()
                                    break
                            else: break
                else:
                    if self.tabulation == 1:
                        break

                    else:
                        self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS(self.string,
                                            self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation, 'def' )

                        if self.error is None:
                            if   self.get_block == 'end:'  :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append( (self.normal_string, False) )

                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR2(self.history[ -1 ] )
                                    break
                            elif self.get_block == 'elif:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'elif' )
                                        self.store_value        = []
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = ERRORS(self.line).ERROR2(self.history[ -1 ])
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR1( 'else' )
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
                                        self.error = ERRORS(self.line).ERROR2(self.history[-1])
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR3( 'else' )
                                    break
                            elif self.get_block == 'empty' :
                                if self.space <= 2:
                                    self.space += 1
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = ERRORS(  self.line ).ERROR4()
                                    break
                            else:
                                self.error = ERRORS( self.line ).ERROR4()
                                break
                        else:
                            self._error_ = end_except_finaly_else.GET_ERROR(self.error, self.data_base,
                                                                            self.line).ERROR()
                            if self._error_ != '{}{}'.format(ke, 'SyntaxError'):
                                self.error = None
                                if   self.normal_string[ : 4 + (self.tabulation-1)] == 't'*(self.tabulation-1) + 'elif' :
                                    if self.key_else_activation == None:
                                        if self.store_value:
                                            self.history.append( 'elif' )
                                            self.store_value = []
                                            self.loop.append( ( self.normal_string, False ) )

                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR1( 'else' )
                                        break
                                elif self.normal_string[ : 5 + (self.tabulation-1)] == 't'*(self.tabulation-1) + 'empty':
                                    if self.space <= 2:
                                        self.space += 1
                                        self.loop.append(( self.normal_string, False ) )
                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break
                            else: break

            except KeyboardInterrupt:
                self.error = ERRORS( self.line ).ERROR4()
                break

        ############################################################################

        return self.loop , self.error

class INTERNAL_IF_STATEMENT:
    def __init__(self, master, data_base, line):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def IF_STATEMENT(self,tabulation:int):
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
        self.color                  = ve
        self.loop                   = []

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            self.line       += 1

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.line ).STDIN({'0': ke, '1': self.color}, self.tabulation )

                if self.error is None:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1)

                        if self.error  is None:
                            if self.get_block   == 'begin:' :
                                self.error = comment.COMMENT_STATEMENT(self.master,
                                                    self.data_base, self.line).COMMENT( self.tabulation + 1)

                                if self.error is None:
                                    self.store_value.append(self.normal_string)
                                    self.history.append( 'begin' )
                                    self.space = 0

                                else:break
                            elif self.get_block == 'if:'    :
                                self.loop.append( (self.normal_string, True) )
                                self._values_, self.error = EXTERNAL_IF_STATEMENT(  self.master,
                                        self.data_base, self.line).IF_STATEMENT( self.value, self.tabulation + 1)
                                if self.error is None:
                                    self.store_value.append(self.normal_string)
                                    self.history.append( 'if' )
                                    self.space = 0
                                    self.loop.append( self._values_ )

                                else:break
                            elif self.get_block == 'try:'   :
                                self.error = try_statement.EXTERNAL_TRY_STATEMENT(self.master,
                                                    self.data_base,self.line).TRY_STATEMENT(self.tabulation + 1)

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'try' )
                                    self.space = 0

                                else:break
                            elif self.get_block == 'unless:':
                                self.loop.append((self.normal_string, True))
                                self._values_, self.error = for_unless.EXTERNAL_UNLESS_STATEMENT( self.master,
                                            self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1)

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'unless' )
                                    self.space = 0
                                    self.loop.append( self._values_ )

                                else:break
                            elif self.get_block == 'switch:':
                                self.error = switch_statement.SWITCH_STATEMENT(self.master,
                                                 self.data_base, self.line).SWITCH(self.value, self.tabulation + 1)

                                if self.error is None:
                                    self.store_value.append(self.normal_string)
                                    self.history.append('switch')
                                    self.space = 0

                                else:break
                            elif self.get_block == 'empty'  :
                                if self.space <= 2:
                                    self.space += 1
                                    self.loop.append( self.normal_string )
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                            elif self.get_block == 'any'    :
                                self.store_value.append(self.normal_string)
                                self.space = 0
                                self.loop.append( (self.normal_string, True ) )
                        else:break

                    else:
                        self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation, 'def' )
                        if self.error is None:
                            if self.get_block   == 'end:' :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop.append( (self.normal_string, False) )

                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                    break
                            elif self.get_block == 'elif:':
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'elif' )
                                        self.store_value        = []
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR1( 'else' )
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
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR3( 'else' )
                                    break
                            elif self.get_block == 'empty':
                                if self.space <= 2:
                                    self.space += 1
                                    self.loop.append( (self.normal_string, False) )
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break
                            else:break

                        else:
                            self._error_ = end_except_finaly_else.GET_ERROR(self.error, self.data_base,
                                                                            self.line).ERROR()
                            if self._error_ != '{}{}'.format(ke, 'SyntaxError'):
                                self.error = None
                                if   self.normal_string[ : 4 + (self.tabulation-1)] == 't'*(self.tabulation-1) + 'elif'  :
                                    if self.key_else_activation == None:
                                        if self.store_value:
                                            self.history.append('elif')
                                            self.store_value = []
                                            self.loop.append( (self.normal_string, False) )

                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR1( 'else' )
                                        break
                                elif self.normal_string[ : 5 + (self.tabulation-1)] == 't'*(self.tabulation-1) + 'empty' :
                                    if self.space <= 2:
                                        self.space += 1
                                        self.loop.append( (self.normal_string, False) )
                                    else:
                                        self.error = ERRORS(self.line).ERROR4()
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR4()
                                    break
                            else: break

                else:

                    self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS(self.string,
                                self.normal_string, self.data_base,self.line).BLOCKS( self.tabulation, 'def' )
                    if self.error is None:
                        if self.get_block   == 'end:' :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.loop.append( (self.normal_string, False) )

                                break
                            else:
                                self.error = ERRORS(self.line).ERROR2(self.history[ -1 ])
                                break
                        elif self.get_block == 'elif:':
                            if self.key_else_activation == None:
                                if self.store_value:
                                    self.history.append( 'elif' )
                                    self.store_value            = []
                                    self.loop.append( (self.normal_string, False) )

                                else:
                                    self.error = ERRORS(self.line).ERROR2(self.history[ -1 ])
                                    break
                            else:
                                self.error = ERRORS( self.line ).ERROR1( 'else' )
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
                                    self.error = ERRORS(self.line).ERROR2(self.history[ -1 ])
                                    break
                            else:
                                self.error = ERRORS(self.line).ERROR3( 'else' )
                                break
                        elif self.get_block == 'empty':
                            if self.space <= 2:
                                self.space += 1
                                self.loop.append( (self.normal_string, False) )
                            else:
                                self.error = ERRORS(self.line).ERROR4()
                                break
                        else:
                            self.error = ERRORS( self.line ).ERROR4()
                            break
                    else:

                        self._error_ = end_except_finaly_else.GET_ERROR(self.error, self.data_base,
                                                                        self.line).ERROR()
                        if self._error_ != '{}{}'.format(ke, 'SyntaxError'):
                            self.error = None
                            if   self.normal_string[ : 4 + (self.tabulation-1)] == 't'*(self.tabulation-1) + 'elif' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'elif' )
                                        self.store_value = []
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = ERRORS(self.line).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR1( 'else' )
                                    break
                            elif self.normal_string[ : 5 + (self.tabulation-1)] == 't'*(self.tabulation-1) + 'empty':
                                if self.space <= 2:
                                    self.space += 1
                                    self.loop.append( ( self.normal_string, False ) )
                                else:
                                    self.error = ERRORS(self.line).ERROR4()
                                    break
                            else:
                                self.error = ERRORS(self.line).ERROR4()
                                break
                        else: break

            except KeyboardInterrupt:
                self.error = ERRORS( self.line ).ERROR4()
                break

        ############################################################################

        return self.loop , self.error

class ERRORS:
    def __init__(self, line: int):
        self.line           = line

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR1(self, string: str = 'else'):
        error = '{}is already defined. {}line: {}{}'.format(ke, we, ke, self.line)
        self.error = '{}{} : invalid syntax. {}<< {} >> {}block '.format(ke, 'SyntaxError', ae, string, ke) + error

        return self.error

    def ERROR2(self, string):
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format(ve, ke, ae, string, ke,
                                                                                             we, ke, self.line)
        self.error = '{}{} : invalid syntax. '.format(ke, 'SyntaxError') + error

        return self.error

    def ERROR3(self, string: str = 'else'):
        error = '{}due to {}many {}<< {} >> {}blocks. {}line: {}{}'.format(ke, ve, ae, string, ke, we, ke, self.line)
        self.error = '{}{} : invalid syntax '.format(ke, 'SyntaxError') + error

        return self.error

    def ERROR4(self):
        self.error = '{}{} : {}unexpected an indented block, {}line: {}{}'.format(ie, 'IndentationError',
                                                                                  ne, we, ke, self.line)
        return self.error