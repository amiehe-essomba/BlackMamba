from script                                 import control_string
from script.STDIN.LinuxSTDIN                import bm_configure     as bm
from CythonModules.Windows                  import fileError    as fe


class GLOBAL:
    def __init__(self, master: str, data_base: dict, line: int):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line)

    def GLOBAL(self, value: str):
        self.main_string    = ''
        self.string         = ''
        self.error          = None
        self.global_var     = []
        self.main_string    = value

        for i, str_ in enumerate( self.main_string ):

            if str_ in [',']:
                if i != len( self.main_string ) - 1:
                    if i != 0:
                        self.string, self.error     = self.control.DELETE_SPACE( self.string )
                        if self.error is None:
                            self.name, self.error = self.control.CHECK_NAME( self.string )
                            if self.error is None:
                                self.global_var.append( self.name )
                                self.string = ''
                            else:
                                self.error  = ERRORS( self.line ).ERROR1( self.string )
                                break
                        else:
                            self.error = ERRORS( self.line ).ERROR0( self.master )
                            break
                    else:
                        self.error = ERRORS(self.line).ERROR0(self.master)
                        break
                else:
                    self.error = ERRORS( self.line ).ERROR0( self.master )
                    break
            else:
                self.string += str_
                if i != len( self.main_string ) - 1:
                    pass
                else:
                    self.string, self.error = self.control.DELETE_SPACE( self.string )
                    if self.error is None:
                        self.name, self.error = self.control.CHECK_NAME( self.string )
                        if self.error is None: self.global_var.append( self.name )
                        else:
                            self.error = ERRORS( self.line ).ERROR1( self.string )
                            break
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.master )
                        break

        return {'global' : self.global_var} , self.error

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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ ': invalid syntax in {}<< {} >>. '.format(self.cyan, string) + error
        return self.error+self.reset

    def ERROR1(self, string: str):
        self._str_ = '{}type {}help( {}var_name{} ) {} for more informations. '.format(self.white, self.magenta, self.yellow, self.magenta
                                                                                       , self.white)
        error = '{}in {}<< {} >> .{}line: {}{}.\n{}'.format(self.red, self.green, string, self.white, self.yellow, self.line, self._str_)
        self.error = fe.FileErrors( 'NameError').Errors()+'{}global variable name {}ERROR '.format(self.blue, self.white) + error
        return self.error+self.reset
      

