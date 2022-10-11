from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from CythonModules.Windows                      import fileError as fe

cdef class ERRORS:
    cdef public:
        unsigned long int line 
    cdef:
        str cyan, red, green, yellow, magenta, white, blue, reset

    def __cinit__(self, line):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    cdef str ERROR0(self, str string):
        self.error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error

        return self.error+self.reset

    cdef str ERROR1(self, str string):
        self.error = '{}due to {}<< . >> .{}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error

        return self.error+self.reset

    cdef str ERROR2(self, str string):
        self.error = '{}was not found. {}line: {}{}'.format(ne, we, ke, self.line)
        self.error = '{}{} : {}<< {} >> '.format(ne, 'NameError', ae, string) + self.error

        return self.error+self.reset

    cdef str ERROR3(self, string, str _char_ = 'an integer()' ):
        self.error = '{}is not {}{} {}type. {}line: {}{}'.format(self.white, self.red, _char_, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}<< {}{}{} >> '.format(self.green, self.cyan, string, self.green) + self.error

        return self.error+self.reset

    cdef str ERROR4(self, str string, str  _char_ = 'an integer'):
        self.error = '{}to  {}{}() {}type. {}line: {}{}'.format(self.white, self.yellow, _char_, self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}impossible to convert {}<< {} >> '.format(self.white, self.cyan, string) + self.error

        return self.error+self.reset

    cdef str ERROR5(self, list string, str key):
        cdef :
            str newS
        string = list(string)
        if len(string) <= 4 :  pass 
        else:
            newS  = f"[{string[0]}, ..., {string[2]}, ..., {string[4]}]"
        self.error = '{}was not found in {}<< {} >>. {}line: {}{}'.format(self.white, self.red, newS, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'KeyError' ).Errors()+'{}<< {} >> '.format(self.cyan, key) + self.error

        return self.error+self.reset

    cdef str  ERROR6(self, value):
        self.error = '{}a tuple(), {}or a string(), {}type. {}line: {}{}'.format(self.cyan, self.magenta, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> {}is not {}a list(), '.format(self.cyan, value, self.white, self.yellow) + self.error
        return self.error+self.reset

    cdef str ERROR7(self, op, ob1, ob2):
        self.error = '{}<< {}{} >>, {} and {}<< {}{} >>. {}type. {}line: {}{}'.format(self.white, ob1, self.white, self.magenta, 
                                                    self.white, ob2, self.white, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}<< {}{}{} >> {}not supported between '.format(self.cyan, self.yllow, op, 
                                                                                            self.cyan, self.green) + self.error
        return self.error+self.reset

    cdef str ERROR8(self, value):
        self.error = '{}<< EMPTY >>. {}line: {}{}'.format(self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}<< {} >> {}is '.format(self.cyan, value, self.white) + self.error
        return self.error+self.reset

    cdef str ERROR9(self, str string = 'float' ):
        self.error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'OverFlowError' ).Errors()+'{}infinity {}{} {}number. '.format(self.yellow, self.magenta, string, 
                                                                                                   self.green) + self.error

        return self.error+self.reset