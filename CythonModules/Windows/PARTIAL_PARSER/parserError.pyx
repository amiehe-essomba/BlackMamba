from script.STDIN.LinuxSTDIN                        import bm_configure as bm
from CythonModules.Windows                          import fileError as fe 


cdef class ERRORS:
    cdef public:
        unsigned long long int line 
    cdef:
        str error, cyan, red, green, yellow, magenta, white, blue, reset

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
        self.error      = ""

    cpdef str  ERROR0(self, str string):
        self.error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + self.error

        return self.error+self.reset

    cpdef str ERROR1(self, str string, str  _char_ = 'an integer()' ):
        self.error = '{}is not {}{} {}type. {}line: {}{}'.format(self.white, self.blue, _char_, self.yellow,
                                                            self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors() +'{}<< {} >> '.format(self.magenta, string) + self.error

        return self.error+self.reset
    
    cpdef str ERROR2(self, str func ):
        self.error = '{}returns no values. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors() +'{}{} '.format(self.cyan, func) + self.error

        return self.error+self.reset