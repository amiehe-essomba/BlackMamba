from colorama import Fore, init, Back, Style
from script import control_string
from script.LEXER import particular_str_selection
from script.MATHS import integer
from script.MATHS import real
from script.MATHS import complex
from script.MATHS import my_list
from script.MATHS import string as string_init
from script.MATHS import tuple as TP
from script.MATHS import boolean

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class DICTIONARY:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.selection      = particular_str_selection

    def MAIN_DICTIONARY(self):
        self.value          = None
        self.error          = None
        self._return_       = dict()

        self.string         = self.master[1 : -1]
        self.string, self.error = self.control.DELETE_SPACE( self.string )
        if self.error is None:
            self.new_data, self.error = self.selection.SELECTION( self.string, self.string, self.data_base,
                                                                  self.line ).CHAR_SELECTION( ',' )
            if self.error is None:
                for i, string in enumerate( self.new_data ):
                    self._string_, self.error = self.control.DELETE_SPACE( string )
                    if self.error is None:
                        self.name_value, self.error = self.selection.SELECTION( self._string_, self._string_,
                                                                self.data_base, self.line ).CHAR_SELECTION(':')
                        if self.error is None:
                            self.name, self.error = self.control.DELETE_SPACE( self.name_value[ 0 ] )
                            if self.error is None:
                                self.name = self.name[1: -1]
                                self._value_, self.error = self.control.DELETE_SPACE( self.name_value[ 1 ] )
                                if self.error is None:
                                    if self._value_[ 0 ] in [str(x) for x in range(10)]+['+', '-']:
                                        self.num = None
                                        if self._value_[ -1 ] not in [ 'j' ]:
                                            self.check, self.error = self.selection.SELECTION( self._value_, self._value_,
                                                                        self.data_base, self.line).CHAR_SELECTION('.')
                                            if self.error is None:
                                                if len( self.check ) == 1:
                                                    self.num, self.error = integer.INTEGER( self._value_ , self.data_base,
                                                                                self.line).INTEGER()
                                                    if self.error is None:
                                                        pass
                                                    else:
                                                        break
                                                else:
                                                    self.num, self.error = real.REAL( self._value_, self.data_base,
                                                                                      self.line ).REAL()
                                                    if self.error is None:
                                                        pass
                                                    else:
                                                        break
                                            else:
                                                self.error = self.error
                                                break
                                        else:
                                            self.num, self.error = complex.COMPLEX( self._value_, self.data_base,
                                                                                    self.line).COMPLEX()
                                            if self.error is None:
                                                pass
                                            else:
                                                break

                                        self._return_[ self.name ] = self.num

                                    elif self._value_[ 0 ] in ['{']:
                                        self.num, self.error = DICTIONARY( self._value_, self.data_base,
                                                                           self.line).DICTIONARY()
                                        if self.error is None:
                                            self._return_[ self.name ] = self.num
                                        else:
                                            self.error = self.error
                                            break

                                    elif self._value_[ 0 ] in ['[']:
                                        self.num, self.error = my_list.LIST( self._value_, self.data_base,
                                                                            self.line ).MAIN_LIST()
                                        if self.error is None:
                                            self._return_[ self.name ] = self.num

                                        else:
                                            self.error = self.error
                                            break

                                    elif self._value_[ 0 ] in ['"', "'"]:
                                        self.num = string_init.STRING(self._value_, self.data_base, self.line).STRING()
                                        self._return_[ self.name ] = self.num

                                    elif self._value_[ 0 ] in ['(']:
                                        self.sub_string = self._value_[ 1 : -1 ]
                                        self.sub_string, self.error = self.control.DELETE_SPACE( self.sub_string )
                                        if self.error is None:
                                            self.sub_string_, self.error = self.selection.SELECTION( self.sub_string,
                                                        self.sub_string, self.data_base, self.line).CHAR_SELECTION(',')
                                            if len( self.sub_string_ ) == 1:
                                                self.num, self.error = complex.COMPLEX( self._value_, self.data_base,
                                                                                        self.line ).COMPLEX()
                                                if self.error is None:
                                                    self._return_[ self.name ] = self.num
                                                else:
                                                    break
                                            else:
                                                self.num, self.error = TP.TUPLE( self._value_, self.data_base,
                                                                                 self.line ).TUPLE()
                                                if self.error is None:
                                                    self._return_[ self.name ] = self.num
                                                else:
                                                    self.error = self.error
                                                    break
                                        else:
                                            self.error = None
                                            self._return_[ self.name ] = ()

                                    elif self._value_ in [ 'True', 'False' ]:
                                        self.num = boolean.BOOLEAN( self._value_, self.data_base, self.line ).BOOLEAN()
                                        self._return_[ self.name ] = self.num

                                    elif self._value_ in [ 'None' ]:
                                        self._return_[ self.name ] = None

                                    elif self._value_ in ['inf']:
                                        self.num, self.error = real.REAL(self._value_, self.data_base, self.line).REAL()
                                        if self.error is None:
                                            self._return_[ self.name ] = self.num
                                        else:
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                            else:
                                self.error = self.error = ERRORS( self.line ).ERROR0( self.master )
                                break
                        else:
                            self.error = self.error
                            break
                    else:
                        self.error = self.error = ERRORS( self.line ).ERROR0( self.master )
                        break
            else:
                self.error = self.error
        else:
            self.error = None
            self._return_ = self._return_

        return  self._return_, self.error

    def DICTIONARY(self):
        self.value = None
        self.error = None
        self._return_ = dict()

        self.string = self.master[1: -1]
        self.string, self.error = self.control.DELETE_SPACE(self.string)
        if self.error is None:
            self.new_data, self.error = self.selection.SELECTION(self.string, self.string, self.data_base,
                                                                 self.line).CHAR_SELECTION(',')
            if self.error is None:
                for i, string in enumerate(self.new_data):
                    self._string_, self.error = self.control.DELETE_SPACE(string)
                    if self.error is None:
                        self.name_value, self.error = self.selection.SELECTION(self._string_, self._string_,
                                                self.data_base, self.line).CHAR_SELECTION(':')

                        if self.error is None:
                            self.name, self.error = self.control.DELETE_SPACE( self.name_value[ 0 ] )
                            if self.error is None:
                                self.name = self.name[1: -1]
                                self._value_, self.error = self.control.DELETE_SPACE(self.name_value[ 1 ])
                                if self.error is None:
                                    if self._value_[ 0 ] in [str(x) for x in range(10)]+['+', '-']:
                                        self.num = None
                                        if self._value_[ -1 ] not in [ 'j' ]:
                                            self.check, self.error = self.selection.SELECTION(self._value_, self._value_,
                                                                        self.data_base,self.line).CHAR_SELECTION('.')
                                            if self.error is None:
                                                if len(self.check) == 1:
                                                    self.num, self.error = integer.INTEGER(self._value_, self.data_base,
                                                                               self.line).INTEGER()
                                                    if self.error is None:
                                                        pass
                                                    else:
                                                        break
                                                else:
                                                    self.num, self.error = real.REAL(self._value_, self.data_base,
                                                                                     self.line).REAL()
                                                    if self.error is None:
                                                        pass
                                                    else:
                                                        break
                                            else:
                                                self.error = self.error
                                                break
                                        else:
                                            self.num, self.error = complex.COMPLEX(self._value_, self.data_base,
                                                                                   self.line).COMPLEX()
                                            if self.error is None:
                                                pass
                                            else:
                                                break

                                        self._return_[self.name] = self.num

                                    elif self._value_[ 0 ] in ['{']:
                                        self.num, self.error = DICTIONARY(self._value_, self.data_base,
                                                                                        self.line).MAIN_DICTIONARY()
                                        if self.error is None:
                                            self._return_[ self.name ] = self.num
                                        else:
                                            self.error = self.error
                                            break

                                    elif self._value_[ 0 ] in ['[']:
                                        self.num, self.error = my_list.LIST( self._value_, self.data_base,
                                                                             self.line ).MAIN_LIST()
                                        if self.error is None:
                                            self._return_[ self.name ] = self.num
                                        else:
                                            self.error = self.error
                                            break

                                    elif self._value_[ 0 ] in ['"', "'"]:
                                        self.num = string_init.STRING( self._value_, self.data_base, self.line ).STRING()
                                        self._return_[ self.name ] = self.num

                                    elif self._value_[ 0 ] in [ '(' ]:
                                        self.sub_string = self._value_[1: -1]
                                        self.sub_string, self.error = self.control.DELETE_SPACE(self.sub_string)
                                        if self.error is None:
                                            self.sub_string_, self.error = self.selection.SELECTION(self.sub_string,
                                                            self.sub_string,self.data_baseself.line).CHAR_SELECTION(',')

                                            if len(self.sub_string_) == 1:
                                                self.num, self.error = complex.COMPLEX(self._value_, self.data_base,
                                                                                                self.line).COMPLEX()
                                                if self.error is None:
                                                    self._return_[self.name] = self.num
                                                else:
                                                    break
                                            else:
                                                self.num, self.error = TP.TUPLE(self._value_, self.data_base,
                                                                                                    self.line).TUPLE()
                                                if self.error is None:
                                                    self._return_[self.name] = self.num
                                                else:
                                                    self.error = self.error
                                                    break
                                        else:
                                            self.error = None
                                            self._return_[self.name] = ()

                                    elif self._value_ in ['True', 'False']:
                                        self.num = boolean.BOOLEAN(self._value_, self.data_base, self.line).BOOLEAN()
                                        self._return_[self.name] = self.num

                                    elif self._value_ in ['None']:
                                        self._return_[ self.name ] = None

                                    elif self._value_ in ['inf']:
                                        self.num, self.error = real.REAL( self._value_, self.data_base,
                                                                                 self.line).REAL()
                                        if self.error is None:
                                            self._return_[ self.name ] = self.num
                                        else:
                                            break

                                    else:
                                        self.error = ERRORS( self.line ).ERROR0(self.master)
                                        break

                                else:
                                    self.error = self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                            else:
                                self.error = self.error = ERRORS( self.line ).ERROR0( self.master )
                                break
                        else:
                            self.error = self.error
                            break
                    else:
                        self.error = self.error = ERRORS( self.line ).ERROR0( self.master )
                        break
            else:
                self.error = self.error
        else:
            self.error = None
            self._return_ = self._return_

        return self._return_, self.error

class ERRORS:
    def __init__(self, line ):
        self.line           = line

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

