from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from CythonModules.Windows                      import fileError    as fe


class ERRORS:
    def __init__(self, line: int):
        self.line           = line
        self.cyan           = bm.fg.cyan_L
        self.red            = bm.fg.red_L
        self.green          = bm.fg.green_L
        self.yellow         = bm.fg.yellow_L
        self.magenta        = bm.fg.magenta_M
        self.white          = bm.fg.white_L
        self.blue           = bm.fg.blue_L
        self.reset          = bm.init.reset

    def ERROR0(self, name_func: str, name_class: str):
        error = '{}is already defined in the {}{}( ) {}class. {}line: {}{}'.format(self.white, self.blue, name_class, self.red,
                                                                          self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors()+ '{}the function {}{}( ) '.format(self.white, self.green,
                                                                name_func ) + error
        return self.error+self.reset

    def ERROR1(self, class_name: str ):
        error = '{}initialize( ) {}function is already defined in {}{}( ) {}{}. {}line : {}{}'.format(self.red,
                                                                self.white, self.blue, class_name, self.red, 'class',
                                                                 self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ error
        return self.error+self.reset

    def ERROR2(self ):
        error = '{}set {}initialize( ) {}function before any orthers functions. {}line : {}{}'.format( self.white, self.red,
                                                self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ error
        return self.error+self.reset
    
    def ERROR3( self, string ):
        error = '{}cannot be {}a class. {}line: {}{}'.format(self.white, self.yellow, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}The subclass {}{} '.format(self.white,  self.red, string) + error
        return self.error + self.reset
    
    def ERROR4( self, string ):
        error = '{}<< {} >>. {}line: {}{}'.format(self.cyan, string, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}invalid syntax in '.format( self.white) + error
        return self.error + self.reset

    def ERROR10( self ):
        self.error = fe.FileErrors('IndentationError').Errors() + '{}unexpected an indented block, {}line: {}{}'.format(
                                                self.yellow,  self.white, self.yellow, self.line)
        return self.error + self.reset

    def ERROR17( self, string ):
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format(self.green,
                                                self.white, self.cyan, string, self.white, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}invalid syntax. '.format(self.white) + error
        return self.error + self.reset
    
    def ERROR18( self, string ):
        error = '{}already exits. {}line: {}{}'.format(self.yellow, self.white, self.yellow,self.line)
        self.error = fe.FileErrors('NameError').Errors() + '{}the class name {}{} '.format(self.white, self.red, string,) + error
        return self.error + self.reset