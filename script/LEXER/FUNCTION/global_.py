from script                                 import control_string
from script.STDIN.LinuxSTDIN                import bm_configure     as bm

ne = bm.fg.red_L 
ie = bm.fg.blue_L
ae = bm.fg.cyan_L
te = bm.fg.magenta
ke = bm.fg.yellow_L
ve = bm.fg.green_L
se = bm.fg.yellow
we = bm.fg.white_L


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
                        if self.error is None:
                            self.global_var.append( self.name )

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

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR1(self, string: str):
        self._str_ = '{}type {}help( {}var_name{} ) {} for more informations. '.format(we, te, ke, te, we)
        error = '{}in {}<< {} >> .{}line: {}{}.\n{}'.format(ne, ve, string, we, ke, self.line, self._str_)
        self.error = '{}{} : {}global variable name {}ERROR '.format(ne, 'NameError', ke, ae) + error

        return self.error

