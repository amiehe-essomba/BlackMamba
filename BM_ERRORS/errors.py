from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from CythonModules.Windows                      import fileError    as fe

class mamba_error:
    def __init__(self, line: int = 0):
        self.r          = bm.init.reset 
        self.w          = bm.init.bold + bm.fg.rbg(255, 255, 255)
        self.y          = bm.init.bold + bm.fg.rbg(255,255,0)
        self.c          = bm.init.bold + bm.fg.rbg(255, 0, 255)
        self.m          = bm.init.bold + bm.fg.rbg(0, 255, 255)
        self.red        = bm.init.bold + bm.fg.rbg(255, 0, 0)
        self.line       = 0

    def ERROR1( self, string : str ):
        error = '{}{}. {}line: {}{}'.format( self.m, string, self.w, self.y, self.line)
        self.error = fe.FileErrors( 'SystemError' ).Errors()+ '{}you cannot run this package on '.format(self.c) + error
        return self.error+self.r 
    
    def ERROR2( self, string : str ):
        error = '{}is empty. {}line: {}{}'.format( self.m, self.w, self.y, self.line)
        self.error = fe.FileErrors( 'FileError' ).Errors()+ '{}your {}{}.bm '.format(self.w, self.c, string) + error
        return self.error+self.r 
    
    def ERROR3( self, string : str ):
        error = '{}is not a {} BLACK MAMBA {}file. {}line: {}{}'.format(self.w, self.red,
                                                                        self.y, self.w, self.y, self.line)
        self.error = fe.FileErrors( 'FileNameError' ).Errors() +'{}{} '.format(self.c, string) + error

        return self.error+self.r
    
    def ERROR4( self, string : str ):
        error = '{}is not recognized. {}line: {}{}'.format( self.m, self.w, self.y, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors()+ '{}IDE name = {}{} '.format(self.y, self.c, string) + error
        return self.error+self.r 

    def ERROR5(self, string : str ):
        error = '{}but got {}{}. {}line: {}{}'.format( self.w, self.m, string, self.w, self.y, self.line)
        self.error = fe.FileErrors( 'KeyError' ).Errors()+ '{}expected {}--T '.format(self.w, self.c) + error
        return self.error+self.r 
    
    def ERROR6(self):
        error = '{}command line error. {}line: {}{}'.format( self.m, self.w, self.y, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ error
        return self.error+self.r 
    
    def ERROR7( self, string : str ):
        error = '{}is not a file. {}line: {}{}'.format( self.m, self.w, self.y, self.line)
        self.error = fe.FileErrors( 'FileError' ).Errors()+ '{}your {}{}.bm '.format(self.w, self.c, string) + error
        return self.error+self.r 
    
    def ERROR8( self, string : str ):
        error = '{}directory {}{}{} is not found. {}line: {}{}'.format( self.m, self.c, string, self.m, self.w, self.y, self.line)
        self.error = fe.FileErrors( 'DirectoryNotFoundError' ).Errors()+ error
        return self.error+self.r 
    
    def ERROR9( self ):
        error = '{}you have to update your python version at least 3.8.10 for running {}Black Mamba '.format(self.m, self.c)
        self.error = fe.FileErrors( 'ModuleError' ).Errors()+ error
        return self.error+self.r 


    