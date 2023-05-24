from script.STDIN.LinuxSTDIN    import bm_configure as bm
from CythonModules.Windows      import fileError as fe 


class ERRORS:
    def __init__(self, line):
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() + '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleLoadError' ).Errors() + '{}module {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR2(self, string: str):
        error = '{}is not a file. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileError' ).Errors() +'{}{} '.format(self.cyan, string) + error
        
        return self.error+self.reset
        
    def ERROR3(self, string: str):
        error = '{}is not {} a BLACK MAMBA {}file. {}line: {}{}'.format(self.white, self.red,
                                                                        self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleError' ).Errors() +'{}{} '.format(self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR4(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'FileNotFoundError' ).Errors() + '{}file {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR5(self, string: str, typ = 'file'):
        error = '{}{}. {}line: {}{}'.format(self.red, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() + '{}duplicated {}{} '.format( self.white, self.cyan, typ) + error

        return self.error+self.reset

    def ERROR6(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'DirectoryNotFoundError' ).Errors() + '{}directory {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR7(self, string: str):
        error = '{}is incorrect. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'OSError' ).Errors() + '{}directory path {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR8(self, string: str):
        error = '{}is not already {}open. {}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleError' ).Errors() +'{}The module {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR9(self, string: str, mod: str):
        error = '{}has not {}{} {}as a module. {}line: {}{}'.format(self.white, self.red, mod, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleLoadError' ).Errors() +'{}The file {}{} '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR10(self, string: str):
        error = '{}have been found in the file {}{}. {}line: {}{}'.format(self.white, self.red, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleLoadError' ).Errors() +'{}Any modules '.format(self.white ) + error

        return self.error+self.reset
    
    def ERROR11(self, mod: list):
        error = '{}has not any modules to load. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleLoadError' ).Errors() +'{}The file {}{} '.format(self.white, self.cyan, mod ) + error

        return self.error+self.reset
    
    def ERROR12(self, string: str):
        error = '{}is already {}open. {}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ModuleLoadError' ).Errors() + '{}The module {}{} '.format( self.white, self.cyan, string) + error

        return self.error+self.reset