from script.STDIN.LinuxSTDIN                import bm_configure as bm
from CythonModules.Windows                  import fileError    as fe 


class ERRORS:
    def __init__(self, line : int) -> str:
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str, _char_ = 'an integer()' ):
        error = '{}is not {}{} {}type. {}line: {}{}'.format(self.white, self.blue, _char_, self.yellow,
                                                            self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors() +'{}<< {} >> '.format(self.magenta, string) + error

        return self.error+self.reset
    
    def ERROR2(self, func: str ):
        error = '{}returns no values. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors() +'{}{} '.format(self.cyan, func) + error

        return self.error+self.reset
    
    def ERROR3(self, l1 : list, l2 : list):
        error = '{}{} {}into {}{}. {}line: {}{}'.format(self.red, l2, self.white, self.green, l1, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}could not broadcast input ndarray from ndim '.format( self.white ) + error
        
        return self.error+self.reset