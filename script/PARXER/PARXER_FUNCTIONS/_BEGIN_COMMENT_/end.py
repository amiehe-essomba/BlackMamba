from script                                             import  control_string
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:  from CythonModules.Windows                        import fileError as fe 
except ImportError: from CythonModules.Linux            import fileError as fe

class EXTERNAL_BLOCKS:
    def __init__(self, string: str, normal_string, data_base: dict, line: int):
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def BLOCKS(self, tabulation: int):
        self.tabulation                 = tabulation
        self.back_end                   = self.tabulation - 1
        self._return_                   = None
        self.value                      = None
        self.error                      = None

        self.string                     = self.string[ self.back_end : ]
        self.normal_string              = self.normal_string[ self.back_end : ]

        try:
            self.string, self.error         = self.control.DELETE_SPACE( self.string )
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                try:
                    if   self.normal_string[ : 3 ] == 'end' :
                        if  self.normal_string[ -1 ] == ':':
                            self.error = EXTERNAL_BLOCKS( self.string, self.normal_string, self.data_base,
                                                          self.line ).END_BLOCK_TREATMENT( 3 )
                            if self.error is None:  self._return_ = 'end:'
                            else: pass
                        else: self.error = ERRORS(self.line).ERROR1( 'begin' )

                    elif self.normal_string[ : 4 ] == 'save':
                        if self.normal_string[ - 1] == ':':
                            self.value, self.error = SAVE_COMMENT( self.normal_string[ : -1], self.data_base,
                                                                      self.line ).SAVE()
                            if self.error is None: self._return_ = 'save:'
                            else:pass
                        else: self.error = ERRORS(self.line).ERROR1( 'save' )
                    
                    else: self.error = ERRORS( self.line ).ERROR4()

                except IndexError:
                    self.error = ERRORS( self.line ).ERROR0( self.normal_string )
            else:
                self._return_   = 'empty'
                self.error      = None

        except IndexError:
            self._return_ = 'empty'
            self.error = None

        return self._return_, self.value, self.error

    def END_BLOCK_TREATMENT(self, num: int):
        self.error                          = None

        self.new_normal_string              = self.normal_string[ num : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None:
            self.error = ERRORS( self.line ).ERROR0( self.normal_string )
        else:  self.error = None

        return  self.error

class INTERNAL_BLOCKS:
    def __init__(self, string: str, normal_string, data_base: dict, line: int):
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def BLOCKS(self, tabulation: int):
        self.tabulation     = tabulation
        self.back_end       = self.tabulation - 1
        self._return_       = None
        self.error          = None
        self.value          = None

        self.string                 = self.string[ self.back_end : ]
        self.normal_string          = self.normal_string[ self.back_end : ]

        try:
            self.string, self.error         = self.control.DELETE_SPACE( self.string )
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                self.value      = self.normal_string
                self._return_   = 'any'

            else:
                self._return_   = 'empty'
                self.error      = None

        except IndexError:
            self.error      = None
            self._return_   = 'empty'
            self.value      = ''

        return self._return_, self.value, self.error

class SAVE_COMMENT:
    def __init__(self, master:str, data_base:dict, line:int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def SAVE(self):
        self.error          = None
        self._return_       = None

        if self.master[ : 4] == 'save':
            try:
                if self.master[ 4 ] in [ ' ' ]:
                    self.string = self.master[ 4: ]
                    self.string, self.error = self.control.DELETE_SPACE( self.string )
                    if self.error is None:
                        try:
                            if self.string[ :2 ] == 'as':
                                if self.string[ 2 ] in [ ' ' ]:
                                    self.new_tring = self.string[ 2 : ]
                                    self.new_tring, self.error = self.control.DELETE_SPACE( self.new_tring )
                                    if self.error is None:
                                        self.name, self.error = self.control.CHECK_NAME( self.new_tring )
                                        if self.error is None:
                                            self._return_ = self.name
                                        else:
                                            self.error = self.error
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                else:
                                    self.error = ERRORS(self.line).ERROR0(self.string)
                            else:
                                self.error = ERRORS( self.line ).ERROR0( self.string )
                        except IndexError:
                            self.error = ERRORS(self.line).ERROR0(self.string)
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.master)

                else:
                    self.error = ERRORS( self.line ).ERROR4()
            except IndexError:
                self.error = ERRORS( self.line ).ERROR4()
        else:
            self.error = ERRORS( self.line ).ERROR4()

        return  self._return_, self.error

class ERRORS:
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

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,
                                                                                                       self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str = 'else'):
        error = '{}<< : >> {}is not defined at the end of {}<< end >>. {}line: {}{}'.format(self.red, self.white, self.green, self.white, self.yellow,
                                                                               self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> {}block. '.format(self.white,
                                                                                    self.cyan, string, self.white) + error

        return self.error+self.reset

    def ERROR4(self):
        self.error =  fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                    self.white, self.yellow, self.line )
        return self.error+self.reset













