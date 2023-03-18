from itertools import cycle
from script.STDIN.LinuxSTDIN                import bm_configure as bm
from CythonModules.Linux                    import fileError as fe

cdef class ERRORS:
    cdef public :
        unsigned long long int line 
    cdef :
        str error, cyan, red, green, yellow, magenta, white, blue, reset 
    def __cinit__(self, line):
        self.line           = line
        self.cyan           = bm.fg.cyan_L
        self.red            = bm.fg.red_L
        self.green          = bm.fg.green_L
        self.yellow         = bm.fg.yellow_L
        self.magenta        = bm.fg.magenta_M
        self.white          = bm.fg.white_L
        self.blue           = bm.fg.blue_L
        self.reset          = bm.init.reset
        self.error          = ""

    cpdef ERROR0(self, str string):
        self.error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error
        return self.error+self.reset

    cpdef str ERROR1(self, str string, str char1, str char2):
        self.error  = '{}due to undefined space between {}<< {} >> {}and {}<< {} >>, {}line: {}{}'.format(self.white, self.green, char1, self.white, 
                                                            self.red,  char2, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error 
        return self.error + self.reset

    cpdef str ERROR2(self, str string, str op1, str op2):
        self.error = '{}due many operators, {}<< {} >> {}and {}<< {} >>. {}line: {}{}'.format( self.white, self.green, op1, self.white, self.red, op2,
                                                                                    self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error 
        return self.error + self.reset

    cpdef str ERROR3(self, str string):
        self.error = '{}due to the empty {}name of variable. {}line: {}{}'.format(self.white, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error 

    cpdef str ERROR4(self, str string):
        self.error = '{}due to the {}no value. {}line: {}{}'.format(self.white, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error 
        return self.error + self.reset

    cpdef str ERROR5(self, str string):
        self.error = '{}due to << {}= {}>> {}at the end. {}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.white, self.yellow,
                                                                        self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error 
        return self.error + self.reset

    cpdef str ERROR6(self, str string, str char=','):
        self.error = '{}due to {}{} {}at the end. {}line: {}{}'.format(self.white, self.red, char, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error

        return self.error + self.reset

    cpdef str ERROR7(self, str string, str char=','):
        self.error = '{}due to no value {}before {}<< {}{}{} >>. line: {}{}'.format(self.white, self.green, self.white, self.red, char,
                                                                            self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error 

        return self.error + self.reset

    cpdef str ERROR8(self):
        self.error = '{}many values and less variables. {}line: {}{}'.format(self.green, self.white , self.yellow, self.line)
        self.error = self.error = fe.FileErrors( 'AttributeError' ).Errors() + self.error

        return self.error + self.reset

    cpdef str ERROR9(self):
        self.error = '{}many values and less variables. {}line: {}{}'.format(self.green, self.white , self.yellow, self.line)
        self.error = self.error = fe.FileErrors( 'AttributeError' ).Errors() + self.error

        return self.error + self.reset