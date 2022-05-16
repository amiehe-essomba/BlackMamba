"""
I create the ansi code for black mamba code
"""

class fg:
    def __init__(self, char: str, line: int):
        self.char                   = char
        self.line                   = line

    def fg(self):
        self.error                  = None
        self.ansi                   = ''
        self.num, self.error        = number( self.char, self.line ).get_number(  )
        if self.error is None:
            self.num                = self.num[ 0 ]
            if self.num in [ 30, 31, 32, 33, 34, 35, 36, 37]:
                self.ansi       = f"\u001b[{self.num}m"
            else:
                self.error = ERROR( self.line ).ERROR0( 'fountground' )
        else : pass

        return self.ansi, self.error

    def l_fg(self):
        self.error                  = None
        self.ansi                   = ''
        self.num, self.error        = number( self.char, self.line ).get_number(  )

        if self.error is None:
            self.num                = self.num[ 0 ]
            if self.num in [30, 31, 32, 33, 34, 35, 36, 37]:
                self.ansi = f"\u001b[{self.num};1m"
            else:
                self.error = ERROR( self.line ).ERROR0( 'fountground' )
        else: pass

        return self.ansi, self.error

class bg:
    def __init__(self, char, line: int):
        self.char                   = char
        self.line                   = line

    def bg(self):
        self.error                  = None
        self.ansi                   = ''
        self.num, self.error        = number( self.char, self.line ).get_number(  )

        if self.error is None:
            self.num                = self.num[ 1 ]
            if self.num in [40, 41, 42, 43, 44, 45, 46, 47]:
                self.ansi = f"\u001b[{self.num}m"
            else:
                self.error = ERROR( self.line ).ERROR0( 'background' )
        else: pass

        return self.ansi, self.error

    def l_bg(self):
        self.error                  = None
        self.ansi                   = ''
        self.num, self.error        = number( self.char, self.line ).get_number( )

        if self.error is None:
            self.num                = self.num[ 1 ]
            if self.num in [40, 41, 42, 43, 44, 45, 46, 47]:
                self.ansi = f"\u001b[{self.num};1m"
            else:
                self.error = ERROR( self.line ).ERROR0( 'background' )
        else: pass

        return self.ansi, self.error

class reset:
    def __init__(self, char: str, line :int):
        self.char               = char
        self.line               = line

    def reset(self):
        self.error              = None
        self.ansi               = ''
        self.num, self.error    = number( self.char, self.line ).get_number( )

        if self.error is None:
            self.num            = self.num[ 0 ]
            if self.num in [ 0 ]:
                self.ansi   = u'\u001b[0m'
            else:
                self.error = ERROR( self.line ).ERROR0( 'init' )
        else: pass

        return self.ansi, self.error

class config:
    def __init__(self, char: str, line: int):
        self.char               = char
        self.line               = line

    def bold(self):
        self.error              = None
        self.ansi               = ''
        self.num, self.error    = number( self.char, self.line ).get_number()

        if self.error is None:
            self.num            = self.num[ 0 ]
            if self.num in [ 1 ]:
                self.ansi = u'\u001b[1m'
            else:
                self.error = ERROR(self.line).ERROR0( 'config' )
        else : pass

        return self.ansi, self.error

    def underline(self):
        self.error              = None
        self.ansi               = ''
        self.num, self.error    = number( self.char, self.line ).get_number()

        if self.error is None:
            self.num            = self.num[ 0 ]
            if self.num in [ 4 ]:
                self.ansi = u'\u001b[4m'
            else:
                self.error = ERROR(self.line).ERROR0('underline')
        else: pass

        return self.ansi, self.error

class output:
    def __init__(self, char: int, line: int, _type_:str):
        self.line       = line
        self.char       = char
        self._type_     = _type_

    def output(self):
        self.ansi       = ''
        self.error      = None

        if   self._type_ in [ 'fg']:
            self.ansi, self.error = fg( self.char, self.line ).fg()
        elif self._type_ in [ 'fgl']:
            self.ansi, self.error = fg( self.char, self.line ).l_fg()
        elif self._type_ in [ 'bg']:
            self.ansi, self.error = bg( self.char, self.line ).bg()
        elif self._type_ in [ 'bgl']:
            self.ansi, self.error = bg( self.char, self.line ).l_bg()
        elif self._type_ in [ 'bd']:
            self.ansi, self.error = config( self.char, self.line ).bold()
        elif self._type_ in [ 'ul']:
            self.ansi, self.error = config( self.char, self.line ).underline()
        elif self._type_ in [ 'r']:
            self.ansi, self.error = reset( self.char, self.line ).reset()
        else:
            self.error = ERROR( self.line ).ERROR1( self._type_ )

        return self.ansi, self.error

class number:
    def __init__(self, char: str, line : int):
        self.char           = char
        self.line           = line
    def get_number(self):
        self.error = None

        if   self.char == 'R'    :      return (31, 41), None
        elif self.char == 'G'    :      return (32, 42), None
        elif self.char == 'Y'    :      return (33, 43), None
        elif self.char == 'B'    :      return (34, 44), None
        elif self.char == 'M'    :      return (35, 45), None
        elif self.char == 'C'    :      return (36, 46), None
        elif self.char == 'W'    :      return (37, 47), None
        elif self.char == 'BL'   :      return (30, 40), None
        elif self.char == 'reset':      return (0, 0)  , None
        elif self.char == 'bold' :      return (1, 1)  , None
        elif self.char == 'uline':      return (4, 4)  , None
        elif self.char == 'rev'  :      return (7, 7)  , None
        else:                           return None    , ERROR( self.line ).ERROR2( self.char )

class ERROR:
    def __init__(self, line: int):
        self.line           = line
        self.ve             = u"\u001b[32;1m"
        self.ae             = u"\u001b[36;1m"
        self.ne             = u"\u001b[31;1m"
        self.we             = u"\u001b[37;1m"
        self.ke             = u"\u001b[33;1m"
        self.reset          = u"\u001b[0m"
        self.func           = '{}in {}ansi( ) function. '.format(self.ae, self.ve)

    def ERROR0(self, string: str):
        error = '{}line: {}{} '.format(self.we, self.ke, self.line)
        self.error = '{}{} : bad {}{} {}ansi {}number '.format(self.ve, 'ValueError', self.ae, string,
                                                               self.ne, self.ve) + error + self.fucn + self.reset

        return self.error

    def ERROR1(self, string: str):
        error = '{}line: {}{} '.format(self.we, self.ke, self.line)
        self.error = '{}{} : {}<< {} >> {}bad {}ansi {}char '.format(self.ve, 'ValueError', self.ae, string, self.ve,
                                                                   self.ne, self.ve ) + error + self.fucn + self.reset

        return self.error

    def ERROR2(self, string : str):
        error = '{}line: {}{} '.format(self.we, self.ke, self.line)
        self.error = '{}{} : {}color {}<< {} >> {}not found. '.format(self.ve, 'ValueError', self.ke, self.ae, string,
                                                                    self.ve ) + error + self.func + self.reset

        return self.error
