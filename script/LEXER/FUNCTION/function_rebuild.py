from colorama import Fore
from script import control_string
from script.LEXER import looking_for_init_function

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class FUNCTION:
    def __init__(self, master: dict, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base

        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.function       = looking_for_init_function

    def FUNCTION(self, main_string: str):

        self.master         = self.master[ 'value' ]
        self.error          = None
        self.data_storage   = []
        self.function_type  = []
        self.first          = [ 'if', 'def', 'for', 'try', 'while', 'class', 'switch',
                                'unless', 'until', 'break', 'exit', 'pass', 'continue',
                                'next', 'begin']
        self.second         = [ 'return', 'global', 'delete', 'print', '_int_', '_float_', '_string_', '_complex_','lambda',
                                '_list_', '_tuple_', '_dictionary_', '_boolean_', '_sqrt_', '_length_', '_sum_', '_rang_',
                                '__ansii__', '__show__', '__rand__', '_get_line_', '_mean_', '__scan__','_max_', '_min_',
                                '_var_', '_std_', '__open__', '__maths__', '__prompt__']
        
        self.b_p_c_n_e      = [ 'break', 'pass', 'continue', 'next', 'exit' ]
        self.true_data      = []

        for value in self.master:
            self.new_data, self.new_function, self.error = self.function.FUNCTION_INIT( value, self.data_base,
                                                                                        self.line).FUNCTION_INIT()
            if self.error is None:
                if self.new_function:
                    if not self.function_type:
                        if not self.data_storage:
                            self.function_type = self.new_function

                            if self.new_function[ 0 ] in self.b_p_c_n_e: pass
                            else:
                                if self.new_data:
                                    for str_ in self.new_data:
                                        self.data_storage.append( str_ )
                                else: pass

                        else:
                            self.error = ERRORS( self.line ).ERROR0( main_string )
                            break

                    else:
                        self.error = ERRORS( self.line ).ERROR0( main_string )
                        break

                else:
                    if self.new_data:
                        for str_ in self.new_data:
                            self.data_storage.append( str_ )
                    else: pass

            else:
                self.error = self.error
                break

        if self.error is None:
            if self.function_type:

                if self.function_type[ 0 ] in self.first:
                    if len( self.master ) > 1:
                        self.error = ERRORS( self.line ).ERROR0( main_string )

                    else:
                        self.string     = FUNCTION( self.data_storage, self.data_base, self.line ).REBUILD( char = ' ')
                        self.true_data  = [ self.string ]

                else:
                    if len( self.data_storage ) > 1:
                        self.string     = FUNCTION( self.data_storage, self.data_base, self.line ).REBUILD()
                        self.true_data  = [ self.string ]

                    else: self.true_data  = self.data_storage

            else:
                self.string     = FUNCTION( self.data_storage, self.data_base, self.line).REBUILD()
                self.true_data  = [ self.string ]

        else: self.error = self.error

        return self.true_data, self.function_type, self.error

    def REBUILD( self, char = ',' ):
        self.string = ''

        for i, str_ in enumerate( self.master ):
            if len(self.master) == 1:
                self.string = str_
            else:
                if i < len(self.master) - 1:
                    self.string = self.string + str_ + char
                else: self.string += str_

        return self.string

class ERRORS:
    def __init__(self, line):
        self.line           = line

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string) + error

        return self.error
