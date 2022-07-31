from script                                     import control_string
from script.PARXER.LEXER_CONFIGURE              import numeric_lexer, partial_lexer
from script.PARXER                              import numerical_value
from script.PARXER.PARXER_FUNCTIONS._TRY_       import end_except_finaly_else

from script.STDIN.LinuxSTDIN                    import bm_configure as bm
try:
    from CythonModules.Windows                  import fileError as fe
except ImportError:
    from CythonModules.Linux                    import fileError as fe

class EXTERNAL_BLOCKS:
    def __init__(self, string: str, normal_string, data_base: dict, line: int):
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def BLOCKS(self, tabulation: int):
        self.tabulation                 = tabulation
        self.back_end                   = self.tabulation - 1
        self._return_                   = None
        self.value                      = None
        self.error                      = None

        self.string                     = self.string[ self.back_end : ]
        self.normal_string              = self.normal_string[ self.back_end : ]

        try:
            self.string, self.error         = self.control.DELETE_SPACE( self.string )
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                try:
                    if   self.normal_string[ : 3 ] == 'end'  :
                        if  self.normal_string[ -1 ] == ':':
                            self.error = EXTERNAL_BLOCKS( self.string, self.normal_string, self.data_base,
                                                          self.line ).END_BLOCK_TREATMENT( )
                            if self.error is None:  self._return_ = 'end:'
                            else:   self.error = self.error
                        else:   self.error = ERRORS(self.line).ERROR1( 'end' )
                    else:   self.error = ERRORS( self.line ).ERROR4()
                except IndexError:  self.error = ERRORS( self.line ).ERROR0( self.normal_string )
            else:
                self._return_ = 'empty'
                self.error = None
        except IndexError:
            self._return_ = 'empty'
            self.error = None

        return self._return_, self.value, self.error

    def END_BLOCK_TREATMENT( self ):
        self.error                          = None

        self.new_normal_string              = self.normal_string[ 3 : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None:  self.error = ERRORS( self.line ).ERROR0( self.normal_string )
        else:   self.error = None

        return  self.error

class INTERNAL_BLOCKS:
    def __init__(self, string: str, normal_string, data_base: dict, line: int):
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        #self.lex_parxer     = numeric_lexer

    def BLOCKS(self, tabulation: int, loop : bool = False):
        self.tabulation     = tabulation
        self.back_end       = self.tabulation - 1
        self._return_       = None
        self.error          = None
        self.value          = None

        self.string                 = self.string[ self.back_end : ]
        self.normal_string          = self.normal_string[ self.back_end : ]

        try:
            self.string, self.error         = self.control.DELETE_SPACE( self.string )
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                try:
                    if self.normal_string[ : 3 ]   == 'def'     :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                self.data_base, self.line).BLOCK_TREATMENT( 3, 'def')
                            if self.error is None:
                                self._return_   = self._value_
                                self.value      = self.normal_string
                            else: pass
                        else:   self.error = ERRORS(self.line).ERROR1( 'def' )
                    elif self.normal_string[ : 5 ] == 'class'   :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                self.data_base, self.line).BLOCK_TREATMENT( )
                            if self.error is None:
                                self._return_   = self._value_
                                self.value      = self.normal_string
                            else: pass
                        else:   self.error = ERRORS(self.line).ERROR1( 'class' )
                    elif self.normal_string[ :3 ]  == 'end'     :
                        if loop == True:
                            self.error = EXTERNAL_BLOCKS(self.string, self.normal_string, self.data_base, self.line).END_BLOCK_TREATMENT()
                            if self.error is None:
                                self._return_ = 'end:'
                            else: pass
                        else: self.error = ERRORS(self.line).ERROR4()
                    else: self.error      = ERRORS( self.line ).ERROR4()
                except IndexError:  self.error = ERRORS(self.line).ERROR0( self.normal_string )
            else:
                self._return_   = 'empty'
                self.error      = None
        except IndexError:
            self._return_ = 'empty'
            self.error = None

        return self._return_, self.value, self.error

    def BLOCK_TREATMENT(self, num :int = 5, function : any = 'class' ):
        self.error                          = None
        self._return_                       = None
        self.new_normal_string              = self.normal_string[ num : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None:  self._return_ = function+':'
        else: self.error = ERRORS( self.line ).ERROR0( self.normal_string )

        return self._return_, self.error

class ERRORS:
    def __init__(self, line: int):
        self.line           = line
        self.cyan           = bm.fg.cyan_L
        self.red            = bm.fg.red_L
        self.green          = bm.fg.green_L
        self.yellow         = bm.fg.yellow_L
        self.magenta        = bm.fg.magenta_M
        self.white          = bm.fg.white_L
        self.blue           = bm.fg.blue_L
        self.reset          = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white,
                                                                self.cyan, string) + error
        return self.error+self.reset

    def ERROR1(self, string: str = 'else'):
        error = '{}<< : >> {}is not defined at the {}end. {}line: {}{}'.format(self.red, self.white, self.green,
                                                                            self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >> {}block. '.format(self.white,
                                                                            self.cyan, string, self.yellow) + error
        return self.error+self.reset

    def ERROR4(self):
        self.error = fe.FileErrors('IndentationError').Errors() + '{}unexpected an indented block, {}line: {}{}'.format(
            self.yellow, self.white, self.yellow, self.line)
        return self.error + self.reset

    def ERROR5(self, value ):
        error = '{}a tuple(), {}a range(), {}or a string(), {}type. {}line: {}{}'.format(self.blue, self.green,
                                                                self.cyan, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeErrorError' ).Errors()+'{}<< {} >> {}is not {}a list(), '.format(self.cyan,
                                                value, self.white, self.yellow) + error

        return self.error+self.reset