from colorama import Fore, Style

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class STRING_ANALYSE(object):

    def __init__(self, data_base: dict, line: int):
        self.data_base              = data_base
        self.line                   = line
        self.function_non_accepted  = [ 'True', 'False', 'None', 'or', 'and', 'only', 'class', 'def', 'unless',  'until',
                                        'with', 'open', 'not', 'is', 'in', 'if', 'for', 'while', 'switch', 'end', 'next',
                                        'global', 'try', 'except', 'else', 'elif', 'return', 'pass', 'break',     'case',
                                        'function', 'finally', 'load', 'module', 'from', 'exit', 'continue',   'default',
                                        'lambda', 'raise', 'assert', 'begin', 'delete', 'exit', 'stop', 'print', '_int_',
                                        '_float_', '_string_', '_complex_', '_list_', '_dictionary_', '_tuple_',
                                        '_boolean_', '_sqrt_', '_length_', '_sum_', 'self', '__open__']

    def CHECK_NAME(self, name_string: str, _key_type_: bool=False):  # checking variable names used in list

        self.error          = None
        self.true_name      = None

        up_case     = STRING_ANALYSE(self.data_base, self.line).UPPER_CASE()                                 # upper case
        low_case    = STRING_ANALYSE(self.data_base, self.line).LOWER_CASE()                                # lower case

        try:
            name_string, self.error = STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( name_string )          # cleanning string

            if self.error is None:

                self.len_name = len( list( name_string ) )
                if self.len_name == 1:
                    if name_string in up_case+low_case:
                        self.true_name = name_string

                    else:
                        self.error = ERRORS( self.line ).ERROR1( name_string )

                else:
                    if name_string [0] in up_case+low_case:
                        self.check = []

                        for string_ in name_string:
                            if string_ in [str(x) for x in range(10)] + low_case + up_case + ['_']:
                                self.check.append(True)

                            else:
                                self.check.append(False)

                        if False not in self.check:
                            if name_string not in self.function_non_accepted:
                                self.true_name = name_string

                            else:
                                if _key_type_ is not False:
                                    self.true_name = name_string
                                else:
                                    self.error = ERRORS( self.line ).ERROR2( name_string )

                        else:
                            self.c_ = self.check.index( False )
                            if name_string[self.c_] not in [' ']:
                                self.error = ERRORS( self.line ).ERROR3( name_string, self.c_)

                            else:
                                self.error = ERRORS( self.line ).ERROR4( name_string )

                    else:
                        if name_string[0] in [str(x) for x in range(10)] + low_case + ['_']:
                            self.error = ERRORS( self.line ).ERROR5( name_string )

                        else:
                            self.error = ERRORS( self.line ).ERROR6( name_string )

            else:
                self.error = ERRORS( self.line ).ERROR0( name_string )

        except IndexError:
            self.error = ERRORS( self.line ).ERROR7()

        return  self.true_name, self.error

    def LOWER_CASE(self):  # UPPER CASE
        self.lower_case = list('abcdefghijklmnopqrstuvwxyz')

        return self.lower_case

    def UPPER_CASE(self):  # LOWER CASE
        self.upper_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        return self.upper_case

    def DELETE_SPACE(self, string: str):
        self.string_error = None
        ########################################################################
        # i use this function to delete space to left and rigth of the string
        ########################################################################

        try:
            # remove the space before the characters
            while string[0] in [' ']:
                self.new_string = string[1:]
                string = self.new_string

            # remove the space after the characters
            while string [len( string ) - 1] in [' ']:
                self.new_string = string[:-1]
                string = self.new_string

        except IndexError:
            self.string_error = ERRORS( self.line ).ERROR7()

        return string, self.string_error

    def DELETE_RIGTH(self, string: str):

        self.string_error = None

        try:
            # remove the space after the characters
            while string[len( string ) - 1] in [' ']:
                self.new_string = string[:-1]
                string = self.new_string

        except IndexError:
            self.string_error = ERRORS( self.line ).ERROR7()

        return string, self.string_error

    def DELETE_LEFT(self, string: str):
        self.string_error = None

        try:
            # remove the space before the characters
            while string[0] in [' ']:
                self.new_string = string[1:]
                string = self.new_string

        except IndexError:
            self.string_error = ERRORS( self.line ).ERROR7()

        return  string, self.string_error

    def BUILD_NON_CON(self, string: str, tabulation: int):

        string_ = ''
        self.state_value = list( str( string ))

        for i, str_ in enumerate( self.state_value ):

            if str_ != '\t':
                string_ += str_

            elif str_ == '\t':
                if i < tabulation:
                    string_ += 't'

                else:
                    string_ += ' '

        return string_

    def BUILD_CON(self, string: str, tabulation: int):

        string_, self.tab_activate, self.tab_key = '', False, False
        self.state_value = list(str(string))
        self.tab_number, self.error = 0, None

        for i, str_ in enumerate(self.state_value):
            if str_ not in [' ']:
                if str_ != '\t':
                    if tabulation == 1:
                        string_ += str_
                    else:
                        if i < (tabulation-1):
                            self.error = ERRORS( self.line ).ERROR8()
                            break
                        else:
                            string_ += str_

                elif str_ == '\t':
                    check = []
                    if i in [ x for x in range( tabulation ) ]:
                        self.tab_number += 1
                        self.tab_key    = True
                        string_ += 't'

                    else:
                        if i <= tabulation :
                            self.error = ERRORS( self.line ).ERROR8()
                            break

                        else:
                            string_ += ' '

            else:
                if i == tabulation:
                    self.error = ERRORS( self.line ).ERROR8()
                    break

                else:
                    pass

        if self.error is None:
            if self.tab_key == True:
                if self.tab_number == tabulation:
                    self.tab_activate = True

                else:
                    self.error = ERRORS( self.line ).ERROR8()
            else:
                pass

        else:
            pass

        return string_, self.tab_activate, self.error

class ERRORS:
    def __init__(self, line):
        self.line       = line
        self._str_      = '{}type {}help( {}var_name{} ) {}for more informations. '.format(we, te, ke, te, we)

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >> '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR1(self, string: str):
        error = '{}<< {} >> {}was not accepted as a character, {}line: {}{}.\n{}'.format(ae, string, ne, we, ke,
                                                                                        self.line, self._str_)
        self.error = '{}{} : '.format(ne, 'NameError') + error

        return  self.error

    def ERROR2(self, string: str):
        error = '{}as a name of variable. {}line: {}{}.\n{}'.format(ne, we, ke, self.line, self._str_)
        self.error  = '{}{} : you cannot use {}<< {} >> '.format(ne, 'NameError', ke, string) + error

        return self.error

    def ERROR3(self, string: str, id: int):
        error = '{}as a character in {}<< {} >>. {}line: {}{}.\n{}'.format(ne, ve, string, we, ke, self.line, self._str_)
        self.error = '{}{} : you cannot use {}<< {} >> '.format(ne, 'NameError', ae, string[ id ]) + error

        return self.error

    def ERROR4(self, string: str):
        error = '{}as a character in {}<< {} >>. {}line: {}{}.\n{}'.format(ne, ve, string, we, ke, self.line, self._str_)
        self.error = '{}{} : you cannot use {}space '.format(ne, 'NameError', ae) + error

        return self.error

    def ERROR5(self, string: str):
        error = '{}character in {}<< {} >>. {}line: {}{}.\n{}'.format(ne, ve, string, we, ke, self.line, self._str_)
        self.error = '{}{} : {}<< {} >> {}was not accepted as an initial '.format(ne, 'NameError', ae,
                                                                                                string[0], ne) + error

        return  self.error

    def ERROR6(self, string: str):
        error = '{}as a character in {}<< {} >>. {}line: {}{}.\n{}'.format(ne, ve, string, we, ke, self.line, self._str_)
        self.error = '{}{} : you cannot use {}<< {} >> '.format(ne, 'NameError', ae, string[ 0 ]) + error

        return self.error

    def ERROR7(self):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax, {}no string {}detected. '.format(ke, 'SyntaxError', ae, ke) + error

        return self.error

    def ERROR8(self):
        self.error = '{}{} : {}unexpected an indented block, {}line: {}{}'.format(ie, 'IndentationError',
                                                                                  ne, we, ke, self.line)
        return self.error
