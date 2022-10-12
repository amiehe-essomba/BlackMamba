from script.STDIN.LinuxSTDIN                        import bm_configure as bm
from CythonModules.Windows                          import fileError    as fe

cdef class ERRORS:
    cdef public :
        unsigned long int line 
    cdef :
        str error 
        str cyan 
        str green
        str red 
        str yellow
        str magenta
        str blue
        str white
        str reset

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
        self.error      = ''

    cpdef str ERROR0(self, str string):
        cdef:
            str error = ''

        error = ' {}line: {}{}'.format( self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>.'.format(self.white, self.cyan, string)+error

        return self.error+self.reset

    cpdef str ERROR1(self, str string):
        cdef:
            str error = ''

        error = '{}due to bad {}backslash {}<< \ >> {}position . {}line: {}{}'.format(self.white, self.red, self.magenta,
                                                                                      self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string)+error

        return self.error+self.reset

    cpdef str ERROR2(self):
        cdef:
            str error = ''

        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}syntax error, {}EMPTY {}value was detected. {}line : {}{}'.format(self.white, 
                                                                                self.white, self.yellow, self.white, self.yellow, self.line)
        return  self.error+self.reset

    cpdef  str  ERROR3(self):
        self.error = fe.FileErrors( 'IndentationError' ).Errors() + '{}unexpected an indented block. {}line : {}{}'.format(self.yellow, 
                                                self.white, self.yellow, self.line)
        return  self.error+self.reset

    cpdef str ERROR4(self, str string):
        cdef:
            str error = ''

        error = '{}due to bad char {}after {}<< \ >>. {}line: {}{}'.format(self.white, self.red, self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string)+error

        return  self.error+self.reset
    
    cpdef str ERROR5(self, str string, str _open_):
        cdef:
            str error = ''

        error       = '{}close the {}opening {}<< {} >>. {}line: {}{}'.format( self.white, self.red, self.blue, _open_,self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
