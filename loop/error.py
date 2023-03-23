from script.STDIN.LinuxSTDIN          import bm_configure as bm
from CythonModules.Windows            import fileError    as fe


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
        self.error = fe.FileErrors('SyntaxError').Errors() +'{}invalid syntax in {}<< {} >>. '.format(self.white,
                                                                                        self.cyan,string) + error
        return self.error + self.reset

    def ERROR1(self, string: str = 'else'):
        error = '{}<< : >> {}is not defined at the {}end of the line. {}line: {}{}'.format(self.red, self.white,
                                                                     self.green,self.white, self.yellow,  self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}invalid syntax in {}<< {} >> {}block. '.format(
                                        self.white,  self.cyan, string, self.yellow) + error
        return self.error + self.reset

    def ERROR4(self):
        self.error = fe.FileErrors('IndentationError').Errors() + '{}unexpected an indented block, {}line: {}{}'.format(
                                                self.yellow, self.white, self.yellow, self.line)
        return self.error + self.reset

    def ERROR5(self, value):
        error = '{}a tuple(), {}a range(), {}or a string(), {}type. {}line: {}{}'.format(self.blue, self.green,
                                            self.cyan, self.yellow,self.white, self.yellow,  self.line)
        self.error = fe.FileErrors('TypeError') + '{}<< {} >> {}is not {}a list(), '.format(self.white, value,
                                                                        self.magenta, self.yellow) + error
        return self.error + self.reset

    def ERROR6(self, value):
        error = ' {}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors('ValueError') + '{}<< {} >> {}is {}EMPTY.'.format(self.cyan, value, self.white,
                                                                                     self.yellow) + error
        return self.error + self.reset