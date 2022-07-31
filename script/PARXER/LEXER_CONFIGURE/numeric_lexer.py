from colorama import Fore, init, Style
from script.LEXER import main_lexer
from script.LEXER import check_if_affectation
from script import control_string
from script.PARXER import numerical_value

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX
me = Fore.LIGHTCYAN_EX
le = Fore.RED

class NUMERCAL_LEXER:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.lexer          = main_lexer
        self.affectation    = check_if_affectation
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.numeric        = numerical_value

    def LEXER(self, main_string: str):
        self.error          = None
        self._return_       = None

        self.value, self.error = self.affectation.AFFECTATION(self.master, self.master,
                                                              self.data_base, self.line ).DEEP_CHECKING()
        if self.error is None:
            if 'operator' in list( self.value.keys() ):
                self.operators = self.value[ 'operator' ]
                self.error = ERRORS( self.line ).ERROR1( main_string, self.operators )

            else:
                self.lex, self.error = self.lexer.FINAL_LEXER( main_string,
                                            self.data_base, self.line).FINAL_LEXER(self.value, _type_=None)
                if self.error is None:
                    self.all_data = self.lex[ 'all_data' ]
                    if self.all_data is not None:
                        self.final_value, self.error = self.numeric.NUMERICAL(self.lex,
                                                        self.data_base, self.line).ANALYSE( main_string )
                        if self.error is None:
                            self._return_ = self.final_value[ 0 ]
                        else:
                            self.error = self.error
                    else:
                        self.error = ERRORS( self.line ).ERROR0( main_string )
                else:
                    self.error = self.error
        else:
            self.error = self.error

        return  self._return_, self.error

class ERRORS:
    def __init__(self, line:int):
        self.line           = line

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >> '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR1(self, string: str, char: str):
        error = '{}due to {}<< {} >>. {}line: {}{}'.format(ke, ne, char, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >> '.format(ke, 'SyntaxError', ae, string) + error

        return self.error
