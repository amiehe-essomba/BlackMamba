from script.STDIN.LinuxSTDIN                                import bm_configure as bm
try                 : from CythonModules.Windows            import fileError as fe
except ImportError  : from CythonModules.Linux              import fileError as fe
from script.PARXER.PARXER_FUNCTIONS._IF_                    import IfError

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
        return IfError.ERRORS( self.line ).ERROR0( string )

    def ERROR1(self, string: str = 'else'):
        return IfError.ERRORS( self.line ).ERROR1( string )

    def ERROR2(self, string : str = ''):
        return IfError.ERRORS( self.line ).ERROR2( string )

    def ERROR3(self, string: str = 'else'):
        return IfError.ERRORS( self.line ).ERROR3( string )

    def ERROR4(self):
        return IfError.ERRORS( self.line ).ERROR4( )

    def ERROR5(self, _str_: str = 'if'):
        error = '{}close the opening statement {}<< {} >> . {}line: {}{}'.format(self.yellow, self.blue, _str_,
                                                                                 self.white, self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}invalid syntax. '.format(self.white) + error

        return self.error + self.reset