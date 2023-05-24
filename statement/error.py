from script.STDIN.LinuxSTDIN                        import bm_configure as bm
from CythonModules.Windows                          import fileError as fe


class ERRORS:
    def __init__(self, line: int):
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str = 'else'):
        error = '{}<< : >> {}is not defined at the {}end. {}line: {}{}'.format(self.red, self.white, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> {}block. '.format(self.white, self.cyan,
                                                                                                                    string, self.yellow) + error

        return self.error+self.reset

    def ERROR4(self):
        self.error =  fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                    self.white, self.yellow, self.line )
        return self.error+self.reset
    
    def ERROR5(self, string: str ):
        error = '{}due to {}<< : >> {}at the {}end. {}line: {}{}'.format(self.white, self.red, self.white, self.yellow,
                                                                         self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string)

        return self.error+self.reset

    