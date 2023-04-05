from script.STDIN.LinuxSTDIN               import bm_configure as bm
from CythonModules.Linux                   import fileError as fe 

    
cdef class ERROR:
    cdef public:
        unsigned int line 
    cdef:
        str cyan, red, green, yellow, magenta, white, blue, reset, error
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
        self.error      = ''

    cdef str ERROR0(self, str string ):
        self.error = ' {}line: {}{}'.format( self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>.'.format(self.white, self.cyan, string)+self.error

        return self.error+self.reset

    cdef str ERROR1(self, str string ):
        self.error      = '{}due to {}<< , >> {}at the beginning. {}line: {}{}'.format(self.white, self.red, self.yellow, 
                                                                                   self.white, self.yellow,self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax, in {}<< {} >> '.format(self.white, self.cyan, string) + self.error

        return self.error+self.reset

    cdef str ERROR2(self):
        self.error       = '{}<< , >> {}on the previous line. {}line: {}{}'.format(self.red, self.yellow, 
                                                                              self.white,self.yellow, (self.line-1) )
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax, due to '.format(self.white) + self.error

        return self.error+self.reset

    cdef str ERROR3(self):
        self.error       = '{}<< , >> {}was not set on the previous line. {}line: {}{}'.format(self.red, self.yellow,
                                                                                          self.white, self.yellow, (self.line - 1) )
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax '.format(self.white) + self.error

        return self.error+self.reset

    cdef str ERROR4(self, str _open_, str _close_):
        self.error      = '{}<< {} {} >> {}line: {}{}'.format(self.blue, _open_,  _close_, 
                                                          self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax, due no value inside '.format(self.white) + self.error

        return  self.error+self.reset

    cdef str ERROR5(self, str string):
        self.error      = '{}due to no value {}before << {},{} >>. line: {}{}'.format(self.white, self.red, self.green, self.white, self.yellow, self.line )
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {} << {} >>, '.format(self.white, self.cyan, string) + self.error

        return self.error+self.reset

    cdef str ERROR6(self):
        self.error       = '{}<< , >> {} at the end on the previous line. line: {}{}'.format(self.red, self.white, self.yellow, (self.line - 1))
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax, due to '.format(self.white) + self.error

        return  self.error+self.reset

    cdef str ERROR7(self, str mains_tring, str sub_string):

        self.error = '{}due to bad {}char, {}<< {} >>. {}line: {}{}'.format(self.white, self.red, self.green, sub_string, 
                                                                       self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, mains_tring) + self.error

        return self.error+self.reset

    cdef str ERROR8(self):
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}syntax error, {}EMPTY {}value was detected. {}line : {}{}'.format(self.white,
                                                    self.green, self.yellow, self.white, self.yellow, self.line)

        return  self.error+self.reset

    cdef str ERROR9(self):
        self.error = fe.FileErrors( 'IndentationError' ).Errors() + '{}unexpected an indented block. {}line : {}{}'.format(self.yellow, 
                                                self.white, self.yellow, self.line)

        return self.error+self.reset

    cdef str ERROR_TREATMENT1(self, str string, str _open_):
        self.error      = '{}close {}the {}opening {}<< {} >>. {}line: {}{}'.format(self.green, self.white, self.red, self.blue,
                                                                        _open_, self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + self.error

        return self.error+self.reset

    cdef str ERROR_TREATMENT2(self, str string, str _close_):
        self.error       = '{}open {}<< {} >> {}before {}closing. {}line: {}{}'.format(self.green, self.blue, _close_, self.white, self.red, 
                                                                                  self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + self.error

        return self.error+self.reset

    cdef str ERROR_TREATMENT3(self, str string):
        self.error       = '{}due to, too much  {}<< " >> {}characters. {}line: {}{}'.format(self.white, self.red, self.yellow,
                                                                                self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + self.error

        return self.error+self.reset

    cdef str ERROR_TREATMENT4(self, str string, str _open_):
        self.error       = '{}due to many {}opening {}<< {} >>. {}line: {}{}'.format(self.white, self.green, self.red, _open_, 
                                                                                self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + self.error

        return self.error+self.reset