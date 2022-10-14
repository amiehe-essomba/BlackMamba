cdef class ERRORS:
    cdef public:
        unsigned long long int line 
    cdef:
        cyan, red, green, yellow, magenta, white, blue, reset, error
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
        self.error      = ""

    def str ERROR0(self, str string):
        self.error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + self.error

        return self.error+self.reset

    def str ERROR1(self, str string):
        self._str_ = '{}type {}help( {}function_name{} ) {}or {}help( {}class_name{} ) ' \
                     '{} for more informations. '.format(self.white, self.magenta, self.yellow, self.magenta, self.green,
                                                         self.magenta, self.yellow, self.magenta, self.white)
        self.error = '{}in {}<< {} >> .{}line: {}{}.\n{}'.format(self.white, self.cyan, string, self.white, self.yellow, self.line, self._str_)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}function / {}class {}name {}ERROR '.format(self.magenta,
                                                                                                    self.green, self.yellow, self.cyan) + self.error

        return self.error+self.reset