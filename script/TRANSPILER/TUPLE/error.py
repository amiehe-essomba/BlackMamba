from script.STDIN.LinuxSTDIN                        import bm_configure as bm
try:
    from CythonModules.Windows                      import fileError as fe 
except ImportError:
    from CythonModules.Linux                        import fileError as fe
    
class ERRORS:
    def __init__(self, line:int):
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{} invalid syntax in {}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str, char: str):
        error = '{}due to {}<< {} >>. {}line: {}{}'.format( self.white, self.red, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR2(self, string: str, char:str):
        error = '{}the {}keyword {}of value {}<< {} >> {}is not defined. {}line: {}{}'.format( self.white, self.yellow, self.white, self.red, char, self.white,
                                                                                               self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR3(self, string: str, char1: str = 'keyword', char2:str='value', char: str = None):
        error = '{}{} {}is not defined for the {}{} {}<< {} >>. {}line: {}{}'.format(self.red, char, self.white, self.green, char2, self.magenta, char,
                                                                                self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR4(self, string: str, char: str):
        error = '{}due to the fact that {}<< {} >> {}is {}EMPTY. {}line: {}{}'.format( self.white, self.red, char, self.white, self.yellow,
                                                                                                    self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR5(self, string: str, char: str):
        error = '{}keyword {}<< {} >> {}is repeated. {}line: {}{}'.format(self.white, self.red, char, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR6(self, string: str, char: str):
        error = '{}argument {}<< {} >> {}is repeated. {}line: {}{}'.format(self.white, self.red, char, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR7(self, char: str, func = 'get( )'):
        error = '{}<< {} >>. {}line: {}{}'.format(self.red, char,  self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors()+'{}<< {} >> {}has not attributed '.format(self.cyan, func, self.white) + error

        return self.error+self.reset

    def ERROR8(self, string: str = 'a list'):
        error = '{}{}. {}line: {}{}'.format(self.yellow, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}tuple {}object cannot contain '.format(self.cyan, self.white) + error

        return self.error+self.reset