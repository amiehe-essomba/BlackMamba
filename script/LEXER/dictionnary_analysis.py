from colorama import  Fore
from script import  control_string
from script.LEXER import particular_str_selection
from script.LEXER import float_or_function


ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class DICTIONNARY:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.selection      = particular_str_selection
        self.float_or_func  = float_or_function

    def ANALYSES(self, main_string: str):

        self.error          = None
        self.master, err    = self.control.DELETE_SPACE( self.master )
        if err is None:
            self.final_value    = []
            self.value, self.error = self.selection.SELECTION( self.master, self.master, self.data_base,
                                                               self.line ).CHAR_SELECTION('$')

            if self.error is None:
                if len( self.value ) == 1:
                    self.final_value.append( self.master )

                else:
                    for val in self.value:
                        if val == '':
                            self.error = ERRORS(self.line).ERROR1( self.master )
                            break
                        else:
                            pass

                    if self.error is None:
                        self.init           = self.value[1 : ]
                        self._value_, self.error = self.control.DELETE_SPACE( self.value [ 0 ])
                        if self.error is None:
                            self.final_value.append( self._value_ )

                            if self.error is None:
                                for val in self.init :
                                    self.val, self.error = self.control.DELETE_SPACE( val )
                                    if self.error is None:
                                        self.name, self.error = self.control.CHECK_NAME( self.val )
                                        if self.error is None:
                                            self.final_value.append( self.val )

                                        else:
                                            self.error = self.error
                                            break

                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                            else:
                                self.error = ERRORS( self.line ).ERROR0( self.master )
                        else:
                            self.error = ERRORS( self.line ).ERROR0( self.master )

                    else:
                        self.error = self.error

            else:
                self.error = self.error
        else:
            self.error = ERRORS( self.line ).ERROR0(self.master)

        return self.final_value, self.error

class ERRORS:
    def __init__(self, line: int):
        self.line       = line

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR1(self, string: str):
        error = '{}due to bad {}<< $ >> {}position. {}line: {}{}'.format(ke, ie, ke, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string) + error

        return self.error