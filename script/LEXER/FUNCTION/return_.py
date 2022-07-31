from colorama import Fore
from script import control_string
from script.LEXER import particular_str_selection
from script.PARXER.LEXER_CONFIGURE import numeric_lexer

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class RETURN:
    def __init__(self, master, data_base, line):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line)
        self.selection      = particular_str_selection

    def RETURN(self, value: str):
        self.error          = None
        self.main_string    = value
        self.long_string    = 'return ' + self.main_string

        self.list_of_values, self.error = self.selection.SELECTION( self.main_string, self.main_string,
                                                                    self.data_base, self.line ).CHAR_SELECTION( ',' )
        for i, _value_ in enumerate( self.list_of_values ):
            self.string, self.error = self.control.DELETE_SPACE( _value_ )
            if self.error is None:
                self._value_, self.error = numeric_lexer.NUMERCAL_LEXER( self.string, self.data_base,
                                    self.line).LEXER( self.long_string )
                if self.error is None:
                    self.list_of_values[ i ] = self._value_

                else:
                    self.error = self.error
                    break
            else:
                self.error = ERRORS( self.line ).ERROR0( self.string )
                break

        return self.list_of_values, self.error

class ERRORS:
    def __init__(self, line):
        self.line       = line

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR1(self, string: str):
        error = '{}was not found. {}line: {}{}.'.format(ne, we, ke, self.line)
        self.error = '{}{} : {}<< {} >> '.format(ne, 'NameError', ie, string) + error

        return self.error