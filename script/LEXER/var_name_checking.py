from colorama       import Fore
from script         import  control_string
from script.LEXER                       import particular_str_selection
from script.PARXER.INTERNAL_FUNCTION    import get_list
from script.PARXER.LEXER_CONFIGURE      import partial_lexer
from script.PARXER.INTERNAL_FUNCTION    import get_dictionary
from script.PARXER                      import numerical_value
from script.STDIN.WinSTDIN                       import stdin

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class NAME_CHECKING:

    def __init__(self, master:str, data_base: dict, line:int):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.analyze        = control_string.STRING_ANALYSE(self.data_base, self.line)
        self.variables      = self.data_base[ 'variables' ][ 'vars' ]
        self._values_       = self.data_base[ 'variables' ][ 'values' ]
        self.selection      = particular_str_selection
        self.chars          = self.analyze.UPPER_CASE()+self.analyze.LOWER_CASE()

    def MAIN_CHECKING(self):
        self.error          = None
        self.name           = None
        self._return_       = None
        self.info           = None
        self.key_names      = None

        self.main_dict, self.error = partial_lexer.PARTIAL_LEXER( self.master, self.data_base,
                                                                  self.line ).LEXER( self.master )
        if self.error is None:
            self.list_values = list( self.main_dict.keys() )
            if 'values' not in self.list_values:

                self.type = self.main_dict[ 'type' ]
                if self.type is None:
                    self._name_ = self.main_dict[ 'numeric' ][ 0 ]
                    self.name, self.error = self.analyze.CHECK_NAME( self._name_ )
                    if self.error is None:
                        self._return_ = self.name
                    else:
                        self.error = self.error

                elif self.type == 'list':
                    self._name_ = self.main_dict['numeric'][ 0 ]
                    self._return_, self.info, self.error = NAME_CHECKING( self._name_, self.data_base,
                                                               self.line ).TYPE1( self.main_dict )
                else:
                    self.error = ERRORS( self.line ).ERROR7( self.master )
            else:
                self._return_, self.key_names, self.info, self.error = numerical_value.DICT( self.main_dict,
                                                                self.data_base, self.line).VAR_NAMES( self.master )

        else:
            self.error = self.error

        return self._return_, self.key_names, self.info,  self.error

    def TYPE1(self, value: dict):
        self.error                  = None
        self.main_list              = value
        self.string                 = ''
        self.idd                    = None
        self.info                   = None
        self.name                   = None

        for i, str_ in enumerate( self.master ):
            if str_ in ['[', '(', '{', '$']:
                self.idd = i
                break
            else:
                self.string += str_

        if self.idd != 0:
            self._name_, self.error = self.analyze.DELETE_SPACE( self.string )
            if self.error is None:
                self._name_, self.error = self.analyze.CHECK_NAME(self._name_)
                if self.error is None:
                    self.name = self._name_
                    self.final_value, self.info, self.data, self.error = get_list.LIST( self.main_list,
                                            self.data_base, self.line).VAR_NAMES( self.master )
            else:
                self.error = ERRORS( self.line ).ERROR0( self.master )

            return self.name,  self.info,  self.error

        else:
            self.name, self.error = self.analyze.CHECK_NAME( self.master )
            return None, None, self.error

class ERRORS:
    def __init__(self, line):
        self.line       = line

    def ERROR0(self, string: str):
        error       = '{}line: {}{}'.format(we, ke, self.line)
        self.error  = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR1(self, string: str):
        error       = '{}line: {}{}'.format(we, ke, self.line)
        self.error  = '{}{} : {}<< {} >>, {}was not found. '.format(ne, 'NameError', ae, string, ne) + error

        return self.error

    def ERROR2(self, string: str):
        error = '{}due to {}EMPTY {}value. {}line: {}{}'.format(ke, ve, ke, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR3(self, string: str, char: str):
        error = '{}due to many {}<< : >> {}in {}<< {} >> . {}line: {}{}'.format(ke, ve, ke, ne, char, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR4(self, string: str):
        error = '{}is not  {}a list() {}or {}a tuple() {}type . {}line: {}{}'.format(te, ne, te, ve, te, we, ke, self.line)
        self.error = '{}{} : {}<< {} >>, '.format(te, 'TypeError', ae, string) + error

        return self.error

    def ERROR5(self, string: str):
        error = '{}is not  {}dict() {}type . {}line: {}{}'.format(te, ie, te, we, ke, self.line)
        self.error = '{}{} : {}<< {} >> '.format(te, 'TypeError', ae, string) + error

        return self.error

    def ERROR6(self, string1: str, string2: str):
        error       = '{}in {}<< {} >>. {}line: {}{}'.format(ke, ne, strin2, we, ke, self.line)
        self.error  = '{}{} : {}<< {} >>, {}was not found '.format(ke, 'KeyError', ae, string1, ke) + error

        return self.error

    def ERROR7(self, string: str):
        self._str_ = '{}type {}help( {}var_name{} ) {}for more informations. '.format(we, te, ke, te, we)
        error = '{}as a character in {}<< {} >>. {}line: {}{}.\n{}'.format(ne, ve, string, we, ke, self.line,
                                                                           self._str_)
        self.error = '{}{} : you cannot use {}space '.format(ne, 'NameError', ae) + error

        return self.error
