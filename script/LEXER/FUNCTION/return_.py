from script                                             import control_string
from script.LEXER                                       import particular_str_selection
from script.PARXER.LEXER_CONFIGURE                      import numeric_lexer
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from CythonModules.Windows                              import fileError as fe 


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
        if self.error is None :
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
        else: pass 
        
        return self.list_of_values, self.error

class ERRORS:
    def __init__(self, line):
        self.line       = line
        self.cyan       = bm.init.bold + bm.fg.rbg(0,255,255)
        self.red        = bm.init.bold + bm.fg.rbg(255,0,0)
        self.green      = bm.init.bold + bm.fg.rbg(0,255,0)
        self.yellow     = bm.init.bold + bm.fg.rbg(255,255,0)
        self.magenta    = bm.init.bold + bm.fg.rbg(255,0,255)
        self.white      = bm.init.bold + bm.fg.rbg(255,255,255)
        self.blue       = bm.init.bold + bm.fg.rbg(0,0,255)
        self.reset      = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}was not found. {}line: {}{}.'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors()+'{}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.error