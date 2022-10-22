from script.STDIN.LinuxSTDIN        import bm_configure as bm
from CythonModules.Windows          import fileError as fe


cdef class ERRORS:
    cdef public:
        unsigned long long int line
    cdef:
        str error, cyan, red, green, blue
        str yellow, magenta, white, reset
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

    cpdef str ERROR0(self, str string):
        self.error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error
        return self.error + self.reset

    cpdef str ERROR1(self, str string, str char1, str char2):
        self.error = '{}you cannot associate {}<< {} >> {}and {}<< {} >>. {}line: {}{}'.format(self.white, self.green, char1, self.white,
                                                                            self.red, char2, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error
        return self.error+self.reset

    cpdef str ERROR2(self, str string, str char1, str char2, str pos = 'after'):
        self.error = '{}due to {}<< {} >> {}{} {}<< {} >>. {}line: {}{}'.format(self.white, self.green, char1, self.red, pos, self.magenta, char2,
                                                                    self.white, self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error
        return self.error+self.reset

    cpdef str ERROR3(self, str string, str char1, str char2):
        self.error = '{}due to {}undefined {}space between {}<< {} >> {}and {}<< {} >>. {}line: {}{}'.format(self.white, self.green, self.white,
                                      self.red, char2, self.white, self.magenta, char1, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error
        return self.error+self.reset

    cpdef str ERROR4(self, str string, str char1):
        self.error = '{}due to {}<< {} >> {}at the end. {}line: {}{}'.format(self.white, self.green, char1, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error
        return self.error+self.reset

    cpdef str ERROR5(self, str string, list op):
        self.error = '{}due to {}too much operators {}<< {} >> . {}line: {}{}'.format(self.white, self.red, self.magenta, op,  self.white,
                                                                                self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error
        return self.error+self.reset