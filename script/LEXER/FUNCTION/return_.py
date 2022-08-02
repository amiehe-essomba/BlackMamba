from colorama import Fore
from script                                             import control_string
from script.LEXER                                       import particular_str_selection
from script.PARXER.LEXER_CONFIGURE                      import numeric_lexer
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:
    from CythonModules.Windows                          import fileError as fe 
except ImportError:
    from CythonModules.Linux                            import fileError as fe 


class RETURN:
    def __init__(self, master, data_base, line):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line)
        self.selection      = particular_str_selection

    def RETURN(self, value: str):
        self.error          = None
        self.main_string    = value
        self.long_string    = 'return ' + self.main_string

        self.list_of_values, self.error = self.selection.SELECTION( self.main_string, self.main_string,
                                                                    self.data_base, self.line ).CHAR_SELECTION( ',' )
        for i, _value_ in enumerate( self.list_of_values ):
            self.string, self.error = self.control.DELETE_SPACE( _value_ )
            if self.error is None:
                self._value_, self.error = numeric_lexer.NUMERCAL_LEXER( self.string, self.data_base,
                                    self.line).LEXER( self.long_string )
                if self.error is None:  self.list_of_values[ i ] = self._value_
                else: break
            else:
                self.error = ERRORS( self.line ).ERROR0( self.string )
                break

        return self.list_of_values, self.error

class ERRORS:
    def __init__(self, line):
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}was not found. {}line: {}{}.'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors()+'{}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.error