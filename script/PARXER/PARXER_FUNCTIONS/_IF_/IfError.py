from script.STDIN.LinuxSTDIN                                import bm_configure as bm
try                 : from CythonModules.Windows            import fileError as fe
except ImportError  : from CythonModules.Linux              import fileError as fe

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
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format(self.green, self.white, self.cyan,
                                                                        string, self.green,  self.white, self.yellow, self.line)
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