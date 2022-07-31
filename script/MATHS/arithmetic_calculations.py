from colorama import Fore, init, Back, Style
from script.LEXER import particular_str_selection
from script.MATHS import integer
from script.MATHS import real
from script.MATHS import complex
from script.MATHS import dictionary
from script.MATHS import my_list
from script.MATHS import string as string_int
from script.MATHS import tuple as TP
from script.MATHS import boolean
from script import control_string
from script.STDIN.WinSTDIN import stdin

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class MAGIC_MATH_BASE:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.selection          = particular_str_selection
        self.numbers            = [ str(x) for x in range(10)]
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )

    def ARITHMETIC(self):
        self.error              = None
        self.string_len         = len( self.master )
        self.type               = None
        self.final_value        = None

        if self.master[ 0 ] in self.numbers:
            if self.master[ -1 ] not in [ 'j' ]:
                self.check_int_or_real, self.error = self.selection.SELECTION( self.master, self.master,
                                                                               self.data_base, self.line).CHAR_SELECTION( '.' )
                if self.error is None:
                    if len( self.check_int_or_real ) == 1:
                        self.type = type( int() )
                        self.final_value, self.error = integer.INTEGER( self.master, self.data_base, self.line ).INTEGER()
                    else:
                        self.type = type( float() )
                        self.final_value, self.error = real.REAL( self.master, self.data_base, self.line ).REAL()

                else:
                    self.error = self.error

            else:
                self.final_value, self.error = complex.COMPLEX( self.master, self.data_base, self.line ).COMPLEX()
                self.type = type( self.final_value )

        elif self.master[ 0 ] in [ '{' ]:
            self.type = type( dict() )
            self.final_value, self.error = dictionary.DICTIONARY( self.master, self.data_base,
                                                                  self.line ).MAIN_DICTIONARY()

        elif self.master[ 0 ] in [ '[' ]:
            self.type = type( list() )
            self.final_value, self.error = my_list.LIST( self.master, self.data_base, self.line ).MAIN_LIST()

        elif self.master[ 0 ] in [ '(' ]:
            self._string_ = self.master[ 1: -1 ]
            self._string_, self.error = self.control.DELETE_SPACE( self._string_ )
            if self.error is None:
                self._value_, self.error = self.selection.SELECTION( self._string_, self._string_, self.data_base,
                                                                      self.line ).CHAR_SELECTION( ',' )
                if self.error is None:
                    if len( self._value_ ) == 1:
                        self.final_value, self.error = complex.COMPLEX( self.master, self.data_base, self.line ).COMPLEX()
                    else:
                        self.final_value, self.error = TP.TUPLE( self.master, self.data_base, self.line).MAIN_TUPLE()
            else:
                self.final_value = ()
                self.error = None

        elif self.master in [ 'True', 'False' ]:
            self.final_value = boolean.BOOLEAN( self.master, self.data_base, self.line ).BOOLEAN()

        elif self.master in [ 'None' ]:
            self.final_value = None

        elif self.master[ 0 ] in [ '"', "'" ]:
            self.final_value = string_int.STRING( self.master, self.data_base, self.line ).STRING()

        elif self.master in ['inf']:
            self.final_value, self.error = real.REAL(self.master, self.data_base, self.line).REAL()

        return self.final_value, self.error

