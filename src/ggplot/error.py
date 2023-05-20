from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from CythonModules.Windows                      import fileError    as fe

def write(  string : str = ""  ):
    color = bm.init.bold + bm.fg.rbg(255, 255, 255)
    _string_ = bm.words(string=string, color= color).final()

    return _string_

class ERRORS:
    def __init__(self, line):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    def ERROR0(self, string: str, data : str):
        data = write(string=data)
        error = '{} {}line: {}{}'.format(data, self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}{} {}not in '.format(self.cyan, string, self.white) + error
        return self.error+self.reset
    
    def ERROR1(self, shape1 : list, shape2 : list): 
        error = '{}X = {}{} <---> {}Y = {} . {}line: {}{}.'.format( self.green, shape1, self.white, self.red, shape2,
                                                                    self.white, self.yellow, self.line)
        self.error =  fe.FileErrors(  'ValueError' ).Errors()+'{}dimension Error '.format( self.cyan ) + error
        return self.error+self.reset
    
    def ERROR2(self, string: str): 
        error = '{}{} {}should be 1D. {}line: {}{}.'.format( self.green, string, self.white, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{} dimension Error '.format( self.cyan ) + error 
        return self.error+self.reset
       
    def ERROR3(self): 
        error = '{}line: {}{}.'.format(self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}figure size dimension Error '.format( self.cyan ) + error
        return self.error+self.reset
    
    def ERROR4(self, data : str, index ): 
        data = write(string=data)
        error = '{}{} {}is not an {}integer(). {}line: {}{}.'.format(self.green, index, self.white,
                                                            self.red, self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'ValueError' ).Errors()+'{}in {}{} '.format( self.white, self.cyan, data ) + error
        return self.error+self.reset



