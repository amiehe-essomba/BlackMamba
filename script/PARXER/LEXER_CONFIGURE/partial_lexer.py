from script.LEXER       import main_lexer
from script.LEXER       import check_if_affectation
from script             import control_string
from colorama           import  Fore

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class PARTIAL_LEXER:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.lexer          = main_lexer
        self.affectation    = check_if_affectation
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

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
                        self.boolean_operator       = self.all_data[ 'bool_operator' ]
                        self.logical_operator       = self.all_data[ 'logical_operator' ]
                        self.arithmetic_operator    = self.all_data[ 'arithmetic_operator' ]
                        if len( self.boolean_operator ) == 1:
                            if len( self.logical_operator ) == 1:
                                if len( self.arithmetic_operator ) == 1:
                                    if self.arithmetic_operator[ 0 ] is None and self.logical_operator[ 0 ] is None :
                                        if self.boolean_operator[ 0 ] is None:
                                            pass
                                        else:
                                            ERRORS(self.line).ERROR0(self.master)
                                    else:
                                        ERRORS( self.line ).ERROR0( self.master )
                                else:
                                    ERRORS(self.line).ERROR0(self.master)
                            else:
                                ERRORS(self.line).ERROR0(self.master)
                        else:
                            ERRORS(self.line).ERROR0(self.master)

                        self._return_ = self.all_data[ 'value' ][ 0 ]
                        self._return_ = self._return_[ 0 ]
                    else:
                        self.error = ERRORS( self.line ).ERROR0( main_string )
                else:
                    self.error = self.error
        else:
            self.error = self.error

        return  self._return_, self.error

class LEXER:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.lexer          = main_lexer
        self.affectation    = check_if_affectation
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def MAIN_LEXER(self, main_string: str, _type_:any=None, _key_:bool = False):
        self.error          = None
        self._return_       = None

        self.value, self.error = self.affectation.AFFECTATION(self.master, self.master,
                                                              self.data_base, self.line ).DEEP_CHECKING()
        if self.error is None:
            self.lex, self.error = self.lexer.FINAL_LEXER( main_string,
                                        self.data_base, self.line).FINAL_LEXER(self.value, _type_=_type_, _key_=_key_)
            if self.error is None:
                self._return_ = self.lex
            else:
                self.error = self.error
        else:
            self.error = self.error

        return self._return_, self.error

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