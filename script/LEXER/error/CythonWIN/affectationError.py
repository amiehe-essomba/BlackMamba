from script.STDIN.LinuxSTDIN                        import bm_configure as bm
try                 : from CythonModules.Windows    import fileError as fe
except ImportError  : from CythonModules.Linux      import fileError as fe

class ERRORS:
    
    def __init__(self, line):
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error+self.reset

    def ERROR1(self, string: str, char1: str, char2: str):
        error = '{}due to undefined space between {}<< {} >> {}and {}<< {} >>, {}line: {}{}'.format(self.white, self.green, char1, self.white, 
                                                            self.red,  char2, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error + self.reset

    def ERROR2(self, string: str, op1: str, op2: str):
        error = '{}due many operators, {}<< {} >> {}and {}<< {} >>. {}line: {}{}'.format( self.white, self.green, op1, self.white, self.red, op2,
                                                                                    self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error + self.reset

    def ERROR3(self, string: str):
        error = '{}due to the empty {}name of variable. {}line: {}{}'.format(self.white, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error + self.reset

    def ERROR4(self, string: str):
        error = '{}due to the {}no value. {}line: {}{}'.format(self.white, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error + self.reset

    def ERROR5(self, string: str):
        error = '{}due to << {}= {}>> {}at the end. {}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.white, self.yellow,
                                                                        self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error + self.reset

    def ERROR6(self, string: str, char: str=','):
        error = '{}due to {}{} {}at the end. {}line: {}{}'.format(self.white, self.red, char, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error + self.reset

    def ERROR7(self, string: str, char: str=','):
        error = '{}due to no value {}before {}<< {}{}{} >>. line: {}{}'.format(self.white, self.green, self.white, self.red, char,
                                                                            self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error + self.reset

    def ERROR8(self):
        error = '{}many values and less variables. {}line: {}{}'.format(self.yellow, self.white , self.yellow, self.line)
        self.error = self.error = fe.FileErrors( 'AttributeError' ).Errors() + error

        return self.error + self.reset

    def ERROR9(self):
        error = '{}many values and less variables. {}line: {}{}'.format(self.yellow, self.white , self.yellow, self.line)
        self.error = self.error = fe.FileErrors( 'AttributeError' ).Errors() + error

        return self.error + self.reset