from script                                 import control_string
from script.LEXER                           import particular_str_selection
from script.LEXER                           import float_or_function
from script.STDIN.LinuxSTDIN                import bm_configure as bm
from CythonModules.Windows                  import fileError    as fe

class DICTIONNARY:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.selection      = particular_str_selection
        self.float_or_func  = float_or_function

    def ANALYSES(self, main_string: str):

        self.error          = None
        self.master, err    = self.control.DELETE_SPACE( self.master )
        if err is None:
            self.final_value    = []
            self.value, self.error = self.selection.SELECTION( self.master, self.master, self.data_base,
                                                               self.line ).CHAR_SELECTION('$')

            if self.error is None:
                if len( self.value ) == 1: self.final_value.append( self.master )
                else:
                    for val in self.value:
                        if val == '':
                            self.error = ERRORS(self.line).ERROR1( self.master )
                            break
                        else: pass

                    if self.error is None:
                        self.init           = self.value[1 : ]
                        self._value_, self.error = self.control.DELETE_SPACE( self.value [ 0 ])
                        if self.error is None:
                            self.final_value.append( self._value_ )

                            if self.error is None:
                                for val in self.init :
                                    self.val, self.error = self.control.DELETE_SPACE( val )
                                    if self.error is None:
                                        self.name, self.error = self.control.CHECK_NAME( self.val )
                                        if self.error is None: self.final_value.append( self.val )
                                        else: break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                            else: self.error = ERRORS( self.line ).ERROR0( self.master )
                        else: self.error = ERRORS( self.line ).ERROR0( self.master )
                    else: pass
            else: pass
        else:  self.error = ERRORS( self.line ).ERROR0(self.master)

        return self.final_value, self.error

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
        error = '{}due to bad {}<< $ >> {}position. {}line: {}{}'.format(self.white, self.green, self.red, 
                                                            self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error+self.reset
    