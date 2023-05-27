from script                     import control_string
from script.LEXER               import dictionnary_analysis
from script.LEXER               import segmentation
from script.LEXER               import looking_for_bool_operators
from script.LEXER               import looking_for_logical_operators
from script.LEXER               import float_or_function
from script.LEXER               import particular_str_selection
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from CythonModules.Windows      import fileError as fe 


class ARITHMETIC_OPERATORS:

    def __init__(self, master: str , data_base:dict, line: int):
        self.line                   = line
        self.master                 = master
        self.long_chaine            = master
        self.data_base              = data_base

        self.dict                   = dictionnary_analysis
        self.number                 = segmentation.NUMBER()
        self.string_error           = segmentation.ERROR( self.line )
        self.all_chars              = segmentation.CHARS()
        self.control                = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.float_or_function      = float_or_function
        self.bool_operators         = ['or', 'and', 'only']
        self.bool_operators_        = ['||', '&&', '|&|']
        self.logical_operators1     = ['not', 'in']
        self.logical_operators2     = ['==', '!=', '>=', '<=', '<', '>', '?']
        self.arithmetic_operators   = ['+', '-', '*', '/', '^', '%']
        self.accpeted_chars         = self.control.LOWER_CASE() + self.control.UPPER_CASE() + \
                                      ['_', '(', '[', '{', '.', '"', "'", ' '] + [str(x) for x in range(10)]
        self.accpeted_chars_        = self.control.LOWER_CASE() + self.control.UPPER_CASE() + \
                                      ['_', ')', ']', '}', '.', '"', '"', ' '] + [str(x) for x in range(10)]

    def ARITHMETIC_OPAERATORS_INIT(self):

        self.left                   = 0
        self.rigth                  = 0
        self.initialize             = [None]
        self.active_key             = None
        self.string                 = ''
        self.string_in_true         = ''
        self.error                  = None
        self.if_key_is_true         = None
        self.str_id                 = False
        self.str_id_                = False
        self.key_bracket            = None
        self.var_attribute          = []

        ################################################################################################################

        self.storage_operators      = []
        self.activation_operators   = None
        self.storage_data           = []
        self._string_               = ''
        self.numerical_num          = False
        self.string_num             = ''

        ################################################################################################################

        self.master, self.error = self.control.DELETE_SPACE( self.master )

        if self.error is None:
            for i, str_ in enumerate( self.master ):

                if str_ in ['[', '(', '{', '"', "'"]:

                    if str_ == '(': char1 = str_.index('(')
                    else: char1 = int(self.number.number)

                    if str_ == '[': char2 = str_.index('[')
                    else:  char2 = int(self.number.number)

                    if str_ == '{': char3 = str_.index('{')
                    else: char3 = int(self.number.number)

                    if str_ == '"':  char4 = str_.index('"')
                    else: char4 = int(self.number.number)

                    if str_ == "'": char5 = str_.index("'")
                    else:  char5 = int(self.number.number)

                    if self.initialize[0] is None:

                        if char1 < char2 and char1 < char3 and char1 < char4 and char1 < char5:
                            self.initialize[0] = '('

                        if char2 < char1 and char2 < char3 and char2 < char4 and char2 < char5:
                            self.initialize[0] = '['

                        if char3 < char1 and char3 < char2 and char3 < char4 and char3 < char5:
                            self.initialize[0] = '{'

                        if char4 < char1 and char4 < char2 and char4 < char3 and char4 < char5:
                            self.initialize[0] = '"'

                        if char5 < char1 and char5 < char2 and char5 < char3 and  char5 < char4:
                            self.initialize[0] = "'"

                        self.key_bracket = True

                    else: self.initialize = self.initialize

                else:
                    if str_ in [']', ')', '}'] and self.key_bracket is None:
                        self.open = self.number.OPENING(str_)
                        self.error = self.string_error.ERROR_TREATMENT2(self.long_chaine, str_)
                        break

                    else: pass

                if self.initialize[0] is not None:
                    if self.initialize[0] == '(':
                        self.left, self.rigth = self.left + str_.count('('), self.rigth + str_.count(')')

                    if self.initialize[0] == '[':
                        self.left, self.rigth = self.left + str_.count('['), self.rigth + str_.count(']')

                    if self.initialize[0] == '{':
                        self.left, self.rigth = self.left + str_.count('{'), self.rigth + str_.count('}')

                    if self.initialize[0] == '"':
                        if self.str_id == False: self.left, self.rigth, self.str_id  = 1, 0, True
                        else:
                            if self.rigth <= 1:
                                self.rigth = self.rigth + str_.count('"')
                                self.left = self.left
                            else:
                                self.error = self.string_error.ERROR_TREATMENT3(self.long_chaine)
                                break

                    if self.initialize[ 0 ] == "'":
                        if self.str_id_ == False:
                            self.left, self.rigth = 1, 0
                            self.str_id_ = True
                        else:
                            if self.rigth <= 1:
                                self.rigth = self.rigth + str_.count( "'" )
                                self.left = self.left

                            else:
                                self.error = self.string_error.ERROR_TREATMENT3(self.long_chaine)
                                break
                else: pass

                if self.left != self.rigth:
                    self.active_key = True

                elif self.left == self.rigth and str_ in [')', ']', '}', '"', "'"]:
                    self.active_key = False

                elif self.left == self.rigth and str_ not in ['(', '[', '{', '"', "'"]:
                    self.active_key = 'dot'

                self._string_ += str_

                if self.active_key == True:
                    self.string += str_

                elif self.active_key == False:
                    self.string += str_

                    if i != len( self.master ) - 1:
                        self.string, self.error == self.control.DELETE_SPACE( self.string )
                        if self.error is None: pass
                        else: self.error = None

                    else:
                        self.new_string, self.error = self.control.DELETE_SPACE( self.string )
                        if self.error is None:

                            self.dict_value, self.error     = self.dict.DICTIONNARY( self.new_string, self.data_base,
                                                                         self.line ).ANALYSES( self.master )
                            if self.error is None:

                                if len( self.dict_value ) == 1:
                                    self.__string__, self._key_, self.error = ARITHMETIC_OPERATORS(self.master,
                                                            self.data_base, self.line).BRACKET_ANALYSES( self.string )

                                    if self.error is None:
                                        if self._key_ in [ False, 'tuple' ]:

                                            self.string = self.__string__
                                            self.error = ARITHMETIC_OPERATORS( self.new_string, self.data_base,
                                                                               self.line).SCANNER( self.new_string )

                                            if self.error is None:
                                                try:
                                                    if self.new_string[ 0 ] in ['"', "'"]: pass
                                                    else:
                                                        self.new_string, self.error = ARITHMETIC_OPERATORS(self.new_string,
                                                                                        self.data_base, self.line).CHECK_CHAR()
                                                except IndexError: pass

                                                if self.error is None:
                                                    if self.numerical_num == False:
                                                        self.error = ARITHMETIC_OPERATORS( self.master, self.data_base,
                                                                                self.line).FUNC_CHECK( self.new_string)
                                                        if self.error is None :
                                                            self.final_value, self.error = self.float_or_function.DOT(
                                                                self.new_string, self.data_base, self.line).DOT( _char_='.')

                                                            if self.error is None: self.storage_data.append( self.final_value )
                                                            else: break
                                                        else: break
                                                    else:

                                                        self.s1, self.op1, self.error = ARITHMETIC_OPERATORS( self.new_string,
                                                            self.data_base, self.line).DOUBLE_SCAN(self.master, self.string_num)
                                                        if self.error is None:
                                                            if self.op1:
                                                                self.storage_data.append( self.s1 )
                                                                self.storage_operators.append( self.op1 )
                                                            else: self.storage_data.append( self.s1 )
                                                        else: break
                                                else: break
                                            else: break

                                        elif self._key_ is True:
                                            self.error = ARITHMETIC_OPERATORS( self.__string__, self.data_base,
                                                                               self.line ).SCANNER( self.new_string )

                                            if self.error is None:
                                                self.store_data, self.store_operators, self.error = ARITHMETIC_OPERATORS(
                                                                self.__string__, self.data_base,
                                                                self.line).ARITHMETIC_OPAERATORS()

                                                if self.error is None:
                                                    if self.store_operators:
                                                        if len( self.store_data ) > 1:
                                                            self.storage_data.append( self.store_data )
                                                            self.storage_operators.append( self.store_operators )
                                                        else:
                                                            if len( self.store_operators ) <= 1 :
                                                                self.storage_data.append( self.store_data[ 0 ] )
                                                                self.storage_operators.append( self.store_operators[ 0 ] )
                                                            else:
                                                                self.storage_data.append( self.store_data )
                                                                self.storage_operators.append( self.store_operators )

                                                    else: self.storage_data.append( self.store_data[ 0 ] )
                                                else: break
                                            else: break
                                    else: break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                            else: break

                        else: self.error = None

                    self.initialize[0]      = None
                    self.left               = 0
                    self.rigth              = 0
                    self.str_id             = False
                    self.str_id_            = False
                    self.key_bracket        = None

                else:
                    if i == 0:
                        if str_ in ['+', '-']:
                            self.new_string                     = self.master[1 : ]
                            self.new_string, self.error         = self.control.DELETE_SPACE( self.new_string )

                            if self.error is None:
                                if self.new_string[ 0 ] in self.accpeted_chars:
                                    self.storage_operators.append( str_ )
                                    self.string                 = ''
                                    self.activation_operators   = True
                                else: break
                            else:
                                self.error = ERRORS(self.line).ERROR2(self.master, self.new_string[0], str_)
                                break
                        elif str_ in ['*', '^', '/', '%']:
                            self.error = ERRORS(self.line).ERROR1(self.master, str_)
                            break
                        else:
                            if i == len( self.master ) - 1 :
                                if str_ in self.control.LOWER_CASE()+self.control.UPPER_CASE()+[str(x) for x in range(10)]:
                                    self.final_value, self.error = self.float_or_function.DOT( str_, self.data_base,
                                                                                    self.line).DOT( _char_='.')
                                    if self.error is None:
                                        self.storage_data.append( self.final_value ) #str_)
                                    else: break
                                else:
                                    self.error = ERRORS(self.line).ERROR5(self.master, str_)
                                    break
                            else: self.string += str_

                    elif i != len( self.master ) - 1:
                        if str_ in ['+', '-', '*', '/', '^', '%']:
                            try:
                                self.new_string                 = self.string
                                self.new_string, self.error     = self.control.DELETE_SPACE( self.new_string )
                                self.new_left_string            = self.master[: i]
                                self.new_right_string           = self.master[i + 1 : ]

                                if self.error is None:
                                    if self.new_left_string[ -1 ] in self.accpeted_chars_:
                                        if self.new_right_string[ 0 ] in self.accpeted_chars:
                                            self.storage_operators.append( str_ )

                                            self._value_, self.error = self.dict.DICTIONNARY( self.string, self.data_base,
                                                                        self.line).ANALYSES( self.master )

                                            if self.error is None:
                                                if len( self._value_ ) == 1:
                                                    self.__string__, self._key_, self.error = ARITHMETIC_OPERATORS(self.master,
                                                                 self.data_base, self.line).BRACKET_ANALYSES( self.string )

                                                    if self.error is None:

                                                        if self._key_ == False:
                                                            self.error = ARITHMETIC_OPERATORS(self.new_string,
                                                                    self.data_base, self.line).SCANNER( self.new_string )

                                                            if self.error is None:
                                                                self.new_string, self.error = ARITHMETIC_OPERATORS(
                                                                    self.new_string, self.data_base, self.line).CHECK_CHAR()
                                                                if self.error is None:
                                                                    if self.new_string[ -1 ] in [ 'e', 'E' ]:
                                                                        if self.new_string[ 0 ] not in ['.']+[str(x) for x in range(10)]:
                                                                            if self.numerical_num == False:
                                                                                self.error = ARITHMETIC_OPERATORS( self.master,
                                                                                        self.data_base, self.line).FUNC_CHECK(
                                                                                    self.new_string, end = False)
                                                                                if self.error is None:
                                                                                    self.final_value, self.error = self.float_or_function.DOT(
                                                                                        self.new_string, self.data_base,
                                                                                        self.line).DOT(_char_='.')
                                                                                    if self.error is None:
                                                                                        self.storage_data.append( self.final_value )
                                                                                        self.string         = ''
                                                                                        self.new_string     = ''
                                                                                    else: break
                                                                                else: break

                                                                            else:
                                                                                self._op_ = None
                                                                                if self.storage_operators:
                                                                                    self._op_ = self.storage_operators[-1]
                                                                                    #del self.storage_operators[-1]
                                                                                else: pass
                                                                                self.s1, self.op1, self.error = ARITHMETIC_OPERATORS(
                                                                                    self.new_string, self.data_base, self.line
                                                                                    ).DOUBLE_SCAN(self.master, self.string_num)

                                                                                if self.error is None:
                                                                                    if self.op1:
                                                                                        self.storage_data.append( self.s1 )
                                                                                        self.storage_operators.append( self.op1 )
                                                                                        if self._op_ is None: pass
                                                                                        else: self.storage_operators.append( self._op_)
                                                                                    else: self.storage_data.append(self.new_string)
                                                                                    
                                                                                    self.string         = ''
                                                                                    self.numerical_num  = False
                                                                                    self.string_num     = ''
                                                                                    self.new_string     = ''

                                                                                else: break

                                                                        else:
                                                                            if self.new_string[ 0 ] == '.':
                                                                                if len( self.new_string ) <= 2:
                                                                                    self.error = ERRORS( self.line ).ERROR0(self.master )
                                                                                    break
                                                                                else:
                                                                                    if self.new_string[ 1 ] != '.': pass
                                                                                    else:
                                                                                        self.error = ERRORS(self.line).ERROR0(
                                                                                            self.master)
                                                                                        break

                                                                            else: pass

                                                                            if self.error is None:
                                                                                if str_ in [ '+', '-' ]:
                                                                                    self.string         = self.new_string+str_
                                                                                    self.string_num     = self.new_string+str_

                                                                                    del self.storage_operators[ -1 ]
                                                                                    self.numerical_num  = True

                                                                                else:
                                                                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                                    break

                                                                            else: break

                                                                    else:
                                                                        if self.numerical_num == False:
                                                                            self.error = ARITHMETIC_OPERATORS(self.master,
                                                                                    self.data_base, self.line).FUNC_CHECK(
                                                                                                self.new_string, end=False )
                                                                            if self.error is None:
                                                                                self.final_value, self.error = self.float_or_function.DOT(
                                                                                    self.new_string, self.data_base, self.line
                                                                                ).DOT( _char_='.')
                                                                                if self.error is None:
                                                                                    self.storage_data.append( self.final_value )
                                                                                    self.string         = ''
                                                                                    self.new_string     = ''
                                                                                else: break
                                                                            else: break

                                                                        else:
                                                                            self._op_ = None
                                                                            if self.storage_operators: self._op_ = self.storage_operators[ -1 ]
                                                                                #del self.storage_operators[ -1 ]
                                                                            else: pass
                                                                            
                                                                            self.s1, self.op1, self.error = ARITHMETIC_OPERATORS(
                                                                                self.new_string, self.data_base, self.line
                                                                            ).DOUBLE_SCAN( self.master, self.string_num )

                                                                            if self.error is None:
                                                                                if self.op1:
                                                                                    self.storage_data.append( self.s1 )
                                                                                    self.storage_operators.append( self.op1 )
                                                                                    if self._op_ is None: pass
                                                                                    else: self.storage_operators.append( self._op_ )
                                                                                else:  self.storage_data.append( self.s1)

                                                                                self.string         = ''
                                                                                self.new_string     = ''
                                                                                self.string_num     = ''
                                                                                self.numerical_num  = False

                                                                            else: break
                                                                else: break
                                                            else: break

                                                        else:
                                                            self.previous_op = self.storage_operators[ -1 ]
                                                            del self.storage_operators[ -1 ]

                                                            self.error = ARITHMETIC_OPERATORS(self.__string__,
                                                                    self.data_base, self.line).SCANNER( self.new_string )

                                                            if self.error is None:
                                                                self.store_data, self.store_operators, self.error = ARITHMETIC_OPERATORS(
                                                                                        self.__string__, self.data_base,
                                                                                        self.line).ARITHMETIC_OPAERATORS()

                                                                if self.error is None:
                                                                    if self.store_operators:
                                                                        if len( self.store_data ) > 1:
                                                                            self.storage_data.append( self.store_data )
                                                                            self.storage_operators.append( self.store_operators )

                                                                        else:
                                                                            if len( self.store_operators ) <= 1:
                                                                                self.storage_data.append( self.store_data[ 0 ] )
                                                                                self.storage_operators.append( self.store_operators[ 0 ] )
                                                                            else:
                                                                                self.storage_data.append( self.store_data )
                                                                                self.storage_operators.append( self.store_operators )
                                                                    else: self.storage_data.append( self.store_data[0] )

                                                                    self.storage_operators.append( self.previous_op )
                                                                else: break
                                                            else: break

                                                            self.string         = ''
                                                            self.numerical_num  = False
                                                            self.new_string     = ''

                                                    else: break
                                                else:
                                                    if self.numerical_num == False :
                                                        if self.new_string[ 0 ] not in ['[', '(', '"', "'"]:
                                                            self._main_     = self._value_[ 0 ]
                                                            self._main_, self.error = self.control.DELETE_SPACE( self._main_ )
                                                            if self.error is None:
                                                                self.dict_store     = {
                                                                    'values'        : None,
                                                                    'operators'     : None,
                                                                    'names'         : [],
                                                                    'type'          : 'dictionnary'
                                                                }

                                                                self.v1, self.op1, self.error = ARITHMETIC_OPERATORS(
                                                                    self._main_, self.data_base, self.line
                                                                                            ).ARITHMETIC_OPAERATORS()
                                                                if self.error is None:
                                                                    self.dict_store[ 'values' ]      =  self.v1
                                                                    self.dict_store[ 'operators' ]   = self.op1

                                                                    for _val_ in self._value_[ 1: ]:

                                                                        self._val_, self.error = self.control.DELETE_SPACE(
                                                                                                            _val_ )
                                                                        if self.error is None:
                                                                            self.name, self.error = self.control.CHECK_NAME(
                                                                                self._val_ )
                                                                            if self.error is None: self.dict_store[ 'names' ].append( self.name )
                                                                            else: break
                                                                        else:
                                                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                            break

                                                                    if self.error is None: self.storage_data.append( self.dict_store )
                                                                    else: break
                                                                else: break
                                                            else:
                                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                break
                                                        else:
                                                            self.error = ERRORS( self.line ).ERROR0( self.new_string )
                                                            break

                                                    else:
                                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                                        break

                                                    self.string         = ''
                                                    self.new_string     = ''
                                                    self.numerical_num  = False

                                            else: break

                                            self.activation_operators       = True
                                        else:
                                            self.error = ERRORS(self.line).ERROR2(self.master, self.new_right_string[0],str_)                                                                
                                            break

                                    else:
                                        self.error = ERRORS(self.line).ERROR2(self.master, self.new_left_string[ -1 ],
                                                                                                    str_, pos='before')
                                        break

                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                            except IndexError:
                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                break
                        else: self.string  += str_
                    else:
                        if str_ in self.accpeted_chars_:
                            self.string += str_
                            self.new_string, self.error = self.control.DELETE_SPACE( self.string )

                            if self.error is None:
                                self.error = ARITHMETIC_OPERATORS( self.new_string, self.data_base,
                                                                   self.line).SCANNER( self.new_string )
                                if self.error is None:
                                    self.new_string, self.error == ARITHMETIC_OPERATORS(self.new_string,
                                                                    self.data_base, self.line).CHECK_CHAR()

                                    self._value_, self.error = self.dict.DICTIONNARY(self.new_string, self.data_base,
                                                                            self.line).ANALYSES( self.master )
                                    if self.error is None:
                                        if len( self._value_ ) == 1:
                                            if self.error is None:
                                                if self.numerical_num == True:

                                                    self.s1, self.op1, self.error = ARITHMETIC_OPERATORS( self.new_string,
                                                        self.data_base, self.line).DOUBLE_SCAN(self.master, self.string_num)

                                                    if self.error is None:
                                                        if self.op1:
                                                            self.storage_data.append( self.s1 )
                                                            self.storage_operators.append( self.op1 )
                                                        else: self.storage_data.append( self.s1 )
                                                    else: break

                                                else:
                                                    self.error = ARITHMETIC_OPERATORS( self.master, self.data_base,
                                                                        self.line ).FUNC_CHECK( self.new_string, end=False)
                                                    if self.error is None:
                                                        self.final_value, self.error = self.float_or_function.DOT(
                                                            self.new_string, self.data_base, self.line).DOT( _char_='.' )

                                                        if self.error is None: self.storage_data.append( self.final_value )
                                                        else: break
                                                    else: break
                                            else: break

                                        else:
                                            self.dict_store = {
                                                'values'    : None,
                                                'names'     : [],
                                                'operators' : None,
                                                'type'      : 'dictionnary'
                                            }
                                            self._main_string   = self._value_[ 0 ]
                                            if self.numerical_num == True :
                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                break

                                            else:
                                                if self.new_string[ 0 ] not in ['[', '(', '"', "'"]:
                                                    self.v1, self.op1, self.error = ARITHMETIC_OPERATORS(self._main_string,
                                                            self.data_base, self.line).ARITHMETIC_OPAERATORS()

                                                    if self.error is None:
                                                        self.dict_store[ 'values' ]     = self.v1
                                                        self.dict_store[ 'operators' ]  = self.op1

                                                        for _name_ in self._value_[ 1: ]:
                                                            self._name_, self.error = self.control.DELETE_SPACE( _name_ )
                                                            if self.error is None:
                                                                self.name, self.error = self.control.CHECK_NAME( _name_ )

                                                                if self.error is None: self.dict_store[ 'names' ].append( self.name )
                                                                else: break
                                                            else:
                                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                break

                                                        if self.error is None:
                                                            self.storage_data.append( self.dict_store )
                                                        else: break

                                                    else: break
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR0( self.new_string )
                                                    break
                                    else: break
                                else: break
                            else:
                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                break
                        else:
                            self.error = ERRORS(self.line).ERROR3(self.master, str_)
                            break
        else:  self.error = ERRORS( self.line ).ERROR0( self.master )

        return  self.storage_data, self.storage_operators, self.error

    def ARITHMETIC_OPAERATORS(self):

        self.left                   = 0
        self.rigth                  = 0
        self.initialize             = [None]
        self.active_key             = None
        self.string                 = ''
        self.string_in_true         = ''
        self.error                  = None
        self.if_key_is_true         = None
        self.str_id                 = False
        self.key_bracket            = None
        self.var_attribute          = []

        ################################################################################################################

        self.storage_operators      = []
        self.activation_operators   = None
        self.storage_data           = []
        self._string_               = ''
        self.numerical_num          = False
        self.string_num             = ''

        ################################################################################################################

        self.master, self.error = self.control.DELETE_SPACE( self.master )

        if self.error is None:
            for i, str_ in enumerate( self.master ):

                if str_ in ['[', '(', '{', '"', "'"]:

                    if str_ == '(':
                        char1 = str_.index('(')
                    else:
                        char1 = int(self.number.number)

                    if str_ == '[':
                        char2 = str_.index('[')
                    else:
                        char2 = int(self.number.number)

                    if str_ == '{':
                        char3 = str_.index('{')
                    else:
                        char3 = int(self.number.number)

                    if str_ == '"':
                        char4 = str_.index('"')
                    else:
                        char4 = int(self.number.number)

                    if self.initialize[0] is None:

                        if char1 < char2 and char1 < char3 and char1 < char4:
                            self.initialize[0] = '('

                        if char2 < char1 and char2 < char3 and char2 < char4:
                            self.initialize[0] = '['

                        if char3 < char1 and char3 < char2 and char3 < char4:
                            self.initialize[0] = '{'

                        if char4 < char1 and char4 < char2 and char4 < char3:
                            self.initialize[0] = '"'

                        self.key_bracket = True

                    else:
                        self.initialize = self.initialize

                else:
                    if str_ in [']', ')', '}'] and self.key_bracket is None:
                        self.open = self.number.OPENING(str_)
                        self.error = self.string_error.ERROR_TREATMENT2(self.long_chaine, str_)
                        break

                    else:
                        pass

                if self.initialize[0] is not None:
                    if self.initialize[0] == '(':
                        self.left, self.rigth = self.left + str_.count('('), self.rigth + str_.count(')')

                    if self.initialize[0] == '[':
                        self.left, self.rigth = self.left + str_.count('['), self.rigth + str_.count(']')

                    if self.initialize[0] == '{':
                        self.left, self.rigth = self.left + str_.count('{'), self.rigth + str_.count('}')

                    if self.initialize[0] == '"':
                        if self.str_id == False:
                            self.left, self.rigth = 1, 0
                            self.str_id = True

                        else:
                            if self.rigth <= 1:
                                self.rigth = self.rigth + str_.count('"')
                                self.left = self.left

                            else:
                                self.error = self.string_error.ERROR_TREATMENT3(self.long_chaine)
                                break

                else:
                    pass

                if self.left != self.rigth:
                    self.active_key = True

                elif self.left == self.rigth and str_ in [')', ']', '}', '"', "'"]:
                    self.active_key = False

                elif self.left == self.rigth and str_ not in ['(', '[', '{', '"', "'"]:
                    self.active_key = 'dot'

                self._string_ += str_

                if self.active_key == True:
                    self.string += str_

                elif self.active_key == False:
                    self.string += str_

                    if i != len( self.master ) - 1:
                        self.string, self.error == self.control.DELETE_SPACE( self.string )
                        if self.error is None:
                            pass
                        else:
                            self.error = None

                    else:
                        self.new_string, self.error = self.control.DELETE_SPACE( self.string )
                        if self.error is None:

                            self.dict_value, self.error     = self.dict.DICTIONNARY( self.new_string, self.data_base,
                                                                         self.line ).ANALYSES( self.master )

                            if self.error is None:

                                if len( self.dict_value ) == 1:
                                    self.__string__, self._key_, self.error = ARITHMETIC_OPERATORS(self.master,
                                                            self.data_base, self.line).BRACKET_ANALYSES( self.string )

                                    if self.error is None:

                                        if self._key_ in [ False, 'tuple' ]:

                                            self.string = self.__string__
                                            self.error = ARITHMETIC_OPERATORS( self.new_string, self.data_base,
                                                                               self.line).SCANNER( self.new_string )

                                            if self.error is None:
                                                try:
                                                    if self.new_string[ 0 ] in [ '"', "'"]:
                                                        pass
                                                    else:
                                                        self.new_string, self.error = ARITHMETIC_OPERATORS(self.new_string,
                                                                                    self.data_base, self.line).CHECK_CHAR()
                                                except IndexError:
                                                    pass

                                                if self.error is None:
                                                    if self.numerical_num == False:

                                                        self.error = ARITHMETIC_OPERATORS( self.master, self.data_base,
                                                                                self.line).FUNC_CHECK( self.new_string)
                                                        if self.error is None :
                                                            self.final_value, self.error = self.float_or_function.DOT(
                                                                self.new_string, self.data_base, self.line).DOT( _char_='.')

                                                            if self.error is None:
                                                                self.storage_data.append( self.final_value )

                                                            else:
                                                                self.error = self.error
                                                                break

                                                        else:
                                                            self.error = self.error
                                                            break

                                                    else:

                                                        self.s1, self.op1, self.error = ARITHMETIC_OPERATORS( self.new_string,
                                                            self.data_base, self.line).DOUBLE_SCAN(self.master, self.string_num)
                                                        if self.error is None:
                                                            if self.op1:
                                                                self.storage_data.append( self.s1 )
                                                                self.storage_operators.append( self.op1 )
                                                            else:
                                                                self.storage_data.append( self.s1 )

                                                        else:
                                                            self.error = self.error
                                                            break

                                                else:
                                                    self.error = self.error
                                                    break

                                            else:
                                                self.error = self.error
                                                break

                                        elif self._key_ is True:
                                            self.error = ARITHMETIC_OPERATORS( self.__string__, self.data_base,
                                                                               self.line ).SCANNER( self.new_string )

                                            if self.error is None:
                                                self.store_data, self.store_operators, self.error = ARITHMETIC_OPERATORS(
                                                                        self.__string__, self.data_base,
                                                                            self.line).ARITHMETIC_OPAERATORS_INIT()

                                                if self.error is None:
                                                    if self.store_operators:
                                                        if len( self.store_data ) > 1:
                                                            self.storage_data.append( self.store_data )
                                                            self.storage_operators.append( self.store_operators )
                                                        else:
                                                            if len( self.store_operators ) <= 1:
                                                                self.storage_data.append( self.store_data[0] )
                                                                self.storage_operators.append( self.store_operators[ 0 ] )
                                                            else:
                                                                self.storage_data.append( self.store_data )
                                                                self.storage_operators.append( self.store_operators )

                                                    else:
                                                        self.storage_data.append( self.store_data[0] )

                                                else:
                                                    self.error = self.error
                                                    break
                                            else:
                                                self.error = self.error
                                                break

                                    else:
                                        self.error = self.error
                                        break

                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                            else:
                                self.error = self.error
                                break

                        else:
                            self.error = None

                    self.initialize[0]      = None
                    self.left               = 0
                    self.rigth              = 0
                    self.str_id             = False
                    self.key_bracket        = None

                else:
                    if i == 0:
                        if str_ in ['+', '-']:
                            self.new_string                     = self.master[1 : ]
                            self.new_string, self.error         = self.control.DELETE_SPACE( self.new_string )

                            if self.error is None:
                                if self.new_string[ 0 ] in self.accpeted_chars:
                                    self.storage_operators.append( str_ )
                                    self.string                 = ''
                                    self.activation_operators   = True

                                else:
                                    break

                            else:
                                self.error = ERRORS(self.line).ERROR2(self.master, self.new_string[0], str_)
                                break

                        elif str_ in ['*', '^', '/', '%']:
                            self.error = ERRORS(self.line).ERROR1(self.master, str_)
                            break

                        else:
                            if i == len( self.master ) - 1 :
                                if str_ in self.control.LOWER_CASE()+self.control.UPPER_CASE()+[str(x) for x in range(10)]:
                                    self.final_value, self.error = self.float_or_function.DOT( str_, self.data_base,
                                                                                    self.line).DOT( _char_='.')
                                    if self.error is None:
                                        self.storage_data.append( self.final_value )
                                    else:
                                        self.error = self.error
                                        break

                                else:
                                    self.error = ERRORS(self.line).ERROR5(self.master, str_)
                                    break

                            else:
                                self.string += str_

                    elif i != len( self.master ) - 1:
                        if str_ in ['+', '-', '*', '/', '^', '%']:
                            try:
                                self.new_string                 = self.string
                                self.new_string, self.error     = self.control.DELETE_SPACE( self.new_string )
                                self.new_left_string            = self.master[: i]
                                self.new_right_string           = self.master[i + 1 : ]

                                if self.error is None:
                                    if self.new_left_string[ -1 ] in self.accpeted_chars_:
                                        if self.new_right_string[ 0 ] in self.accpeted_chars:
                                            self.storage_operators.append( str_ )

                                            self._value_, self.error = self.dict.DICTIONNARY( self.string, self.data_base,
                                                                        self.line).ANALYSES( self.master )

                                            if self.error is None:

                                                if len( self._value_ ) == 1:
                                                    self.__string__, self._key_, self.error = ARITHMETIC_OPERATORS(self.master,
                                                                 self.data_base, self.line).BRACKET_ANALYSES( self.string )

                                                    if self.error is None:

                                                        if self._key_ == False:
                                                            self.error = ARITHMETIC_OPERATORS(self.new_string,
                                                                    self.data_base, self.line).SCANNER( self.new_string )

                                                            if self.error is None:
                                                                self.new_string, self.error = ARITHMETIC_OPERATORS(
                                                                    self.new_string, self.data_base, self.line).CHECK_CHAR()

                                                                if self.error is None:
                                                                    if self.new_string[ -1 ] in [ 'e', 'E' ]:
                                                                        if self.new_string[ 0 ] not in ['.']+[str(x) for x in range(10)]:
                                                                            if self.numerical_num == False:
                                                                                self.error = ARITHMETIC_OPERATORS( self.master,
                                                                                        self.data_base, self.line).FUNC_CHECK(
                                                                                    self.new_string, end = False)
                                                                                if self.error is None:
                                                                                    self.final_value, self.error = self.float_or_function.DOT(
                                                                                        self.new_string, self.data_base,
                                                                                        self.line).DOT(_char_='.')
                                                                                    if self.error is None:
                                                                                        self.storage_data.append( self.final_value )
                                                                                        self.string         = ''
                                                                                        self.new_string     = ''
                                                                                    else:
                                                                                        self.error = self.error
                                                                                        break
                                                                                else:
                                                                                    self.error = self.error
                                                                                    break

                                                                            else:
                                                                                self._op_ = None
                                                                                if self.storage_operators:
                                                                                    self._op_ = self.storage_operators[-1]
                                                                                    #del self.storage_operators[-1]
                                                                                else:
                                                                                    pass
                                                                                self.s1, self.op1, self.error = ARITHMETIC_OPERATORS(
                                                                                    self.new_string, self.data_base, self.line
                                                                                    ).DOUBLE_SCAN(self.master, self.string_num)

                                                                                if self.error is None:
                                                                                    if self.op1:
                                                                                        self.storage_data.append( self.s1 )
                                                                                        self.storage_operators.append( self.op1 )
                                                                                        if self._op_ is None:
                                                                                            pass
                                                                                        else:
                                                                                            self.storage_operators.append( self._op_)
                                                                                    else:
                                                                                        self.storage_data.append(self.new_string)
                                                                                    self.string         = ''
                                                                                    self.numerical_num  = False
                                                                                    self.string_num     = ''
                                                                                    self.new_string     = ''

                                                                                else:
                                                                                    self.error = self.error
                                                                                    break

                                                                        else:
                                                                            if self.new_string[ 0 ] == '.':
                                                                                if len( self.new_string ) <= 2:
                                                                                    self.error = ERRORS( self.line ).ERROR0(self.master )
                                                                                    break
                                                                                else:
                                                                                    if self.new_string[ 1 ] != '.':
                                                                                        pass
                                                                                    else:
                                                                                        self.error = ERRORS(self.line).ERROR0(
                                                                                            self.master)
                                                                                        break

                                                                            else:
                                                                                pass

                                                                            if self.error is None:
                                                                                if str_ in [ '+', '-' ]:
                                                                                    self.string         = self.new_string+str_
                                                                                    self.string_num     = self.new_string+str_

                                                                                    del self.storage_operators[ -1 ]
                                                                                    self.numerical_num  = True

                                                                                else:
                                                                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                                    break

                                                                            else:
                                                                                self.error = self.error
                                                                                break

                                                                    else:
                                                                        if self.numerical_num == False:
                                                                            self.error = ARITHMETIC_OPERATORS(self.master,
                                                                                    self.data_base, self.line).FUNC_CHECK(
                                                                                                self.new_string, end=False )
                                                                            if self.error is None:
                                                                                self.final_value, self.error = self.float_or_function.DOT(
                                                                                    self.new_string, self.data_base, self.line
                                                                                ).DOT( _char_='.')
                                                                                if self.error is None:
                                                                                    self.storage_data.append( self.final_value )
                                                                                    self.string         = ''
                                                                                    self.new_string     = ''
                                                                                else:
                                                                                    self.error = self.error
                                                                                    break
                                                                            else:
                                                                                self.error = self.error
                                                                                break

                                                                        else:
                                                                            self._op_ = None
                                                                            if self.storage_operators:
                                                                                self._op_ = self.storage_operators[ -1 ]
                                                                                #del self.storage_operators[ -1 ]

                                                                            else:
                                                                                pass
                                                                            self.s1, self.op1, self.error = ARITHMETIC_OPERATORS(
                                                                                self.new_string, self.data_base, self.line
                                                                            ).DOUBLE_SCAN( self.master, self.string_num )

                                                                            if self.error is None:
                                                                                if self.op1:
                                                                                    self.storage_data.append( self.s1 )
                                                                                    self.storage_operators.append( self.op1 )
                                                                                    if self._op_ is None:
                                                                                        pass
                                                                                    else:
                                                                                        self.storage_operators.append( self._op_ )
                                                                                else:
                                                                                    self.storage_data.append( self.s1)

                                                                                self.string         = ''
                                                                                self.new_string     = ''
                                                                                self.string_num     = ''
                                                                                self.numerical_num  = False

                                                                            else:
                                                                                self.error = self.error
                                                                                break

                                                                else:
                                                                    self.error = self.error
                                                                    break

                                                            else:
                                                                self.error = self.error
                                                                break

                                                        else:
                                                            self.previous_op = self.storage_operators[ -1 ]
                                                            del self.storage_operators[ -1 ]

                                                            self.error = ARITHMETIC_OPERATORS(self.__string__,
                                                                    self.data_base, self.line).SCANNER( self.new_string )

                                                            if self.error is None:
                                                                self.store_data, self.store_operators, self.error = ARITHMETIC_OPERATORS(
                                                                                        self.__string__, self.data_base,
                                                                                        self.line).ARITHMETIC_OPAERATORS_INIT()

                                                                if self.error is None:
                                                                    if self.store_operators:
                                                                        if len( self.store_data ) > 1:
                                                                            self.storage_data.append( self.store_data )
                                                                            self.storage_operators.append( self.store_operators )
                                                                        else:
                                                                            if len( self.store_operators ) <= 1:
                                                                                self.storage_data.append(self.store_data[ 0 ])
                                                                                self.storage_operators.append(self.store_operators[ 0 ])
                                                                            else:
                                                                                self.storage_data.append( self.store_data )
                                                                                self.storage_operators.append( self.store_operators )
                                                                    else:
                                                                        self.storage_data.append( self.store_data[0] )

                                                                    self.storage_operators.append( self.previous_op )

                                                                else:
                                                                    self.error = self.error
                                                                    break
                                                            else:
                                                                self.error = self.error
                                                                break

                                                            self.string         = ''
                                                            self.numerical_num  = False
                                                            self.new_string     = ''

                                                    else:
                                                        self.error = self.error
                                                        break

                                                else:
                                                    if self.numerical_num == False :
                                                        if self.new_string[ 0 ] not in ['[', '(', '"', "'"]:
                                                            self._main_     = self._value_[ 0 ]
                                                            self._main_, self.error = self.control.DELETE_SPACE( self._main_ )
                                                            if self.error is None:
                                                                self.dict_store     = {
                                                                    'values'        : None,
                                                                    'operators'     : None,
                                                                    'names'         : [],
                                                                    'type'          : 'dictionnary'
                                                                }

                                                                self.v1, self.op1, self.error = ARITHMETIC_OPERATORS(
                                                                    self._main_, self.data_base, self.line
                                                                                            ).ARITHMETIC_OPAERATORS_INIT()
                                                                if self.error is None:
                                                                    self.dict_store[ 'values' ]      =  self.v1
                                                                    self.dict_store[ 'operators' ]   = self.op1

                                                                    for _val_ in self._value_[ 1: ]:

                                                                        self._val_, self.error = self.control.DELETE_SPACE(
                                                                                                            _val_ )
                                                                        if self.error is None:
                                                                            self.name, self.error = self.control.CHECK_NAME(
                                                                                self._val_ )
                                                                            if self.error is None:
                                                                                self.dict_store[ 'names' ].append( self.name )

                                                                            else:
                                                                                self.error = self.error
                                                                                break
                                                                        else:
                                                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                            break

                                                                    if self.error is None:
                                                                        self.storage_data.append( self.dict_store )

                                                                    else:
                                                                        self.error = self.error
                                                                        break

                                                                else:
                                                                    self.error = self.error
                                                                    break

                                                            else:
                                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                break
                                                        else:
                                                            self.error = ERRORS( self.line ).ERROR0( self.new_string )
                                                            break
                                                    else:
                                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                                        break

                                                    self.string         = ''
                                                    self.new_string     = ''
                                                    self.numerical_num  = False

                                            else:
                                                self.error = self.error
                                                break

                                            self.activation_operators       = True

                                        else:
                                            self.error = ERRORS(self.line).ERROR2(self.master, self.new_right_string[0],
                                                                                                                str_)
                                            break

                                    else:
                                        self.error = ERRORS(self.line).ERROR2(self.master, self.new_left_string[ -1 ],
                                                                                                    str_, pos='before')
                                        break

                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break

                            except IndexError:
                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                break

                        else:
                            self.string  += str_

                    else:
                        if str_ in self.accpeted_chars_:
                            self.string += str_
                            self.new_string, self.error = self.control.DELETE_SPACE( self.string )

                            if self.error is None:
                                self.error = ARITHMETIC_OPERATORS( self.new_string, self.data_base,
                                                                   self.line).SCANNER( self.new_string )

                                if self.error is None:
                                    self.new_string, self.error == ARITHMETIC_OPERATORS(self.new_string,
                                                                    self.data_base, self.line).CHECK_CHAR()

                                    self._value_, self.error = self.dict.DICTIONNARY(self.new_string, self.data_base,
                                                                            self.line).ANALYSES( self.master )
                                    if self.error is None:
                                        if len( self._value_ ) == 1:
                                            if self.error is None:
                                                if self.numerical_num == True:

                                                    self.s1, self.op1, self.error = ARITHMETIC_OPERATORS( self.new_string,
                                                        self.data_base, self.line).DOUBLE_SCAN(self.master, self.string_num)
                                                    if self.error is None:
                                                        if self.op1:
                                                            self.storage_data.append( self.s1 )
                                                            self.storage_operators.append( self.op1 )
                                                        else:
                                                            self.storage_data.append( self.s1 )
                                                    else:
                                                        self.error = self.error
                                                        break

                                                else:
                                                    self.error = ARITHMETIC_OPERATORS( self.master, self.data_base,
                                                                        self.line ).FUNC_CHECK( self.new_string, end=False)
                                                    if self.error is None:
                                                        self.final_value, self.error = self.float_or_function.DOT(
                                                            self.new_string, self.data_base, self.line).DOT( _char_='.' )
                                                        if self.error is None:
                                                            self.storage_data.append( self.final_value )
                                                        else:
                                                            self.error = self.error
                                                            break
                                                    else:
                                                        self.error = self.error
                                                        break

                                            else:
                                                self.error = self.error
                                                break

                                        else:
                                            if self.new_string[ 0 ] not in ['[', '(', '"', "'"]:
                                                self.dict_store = {
                                                    'values'    : None,
                                                    'names'     : [],
                                                    'operators' : None,
                                                    'type'      : 'dictionnary'
                                                }
                                                self._main_string   = self._value_[ 0 ]
                                                if self.numerical_num == True :
                                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                                    break

                                                else:
                                                    self.v1, self.op1, self.error = ARITHMETIC_OPERATORS(self._main_string,
                                                                            self.data_base, self.line).ARITHMETIC_OPAERATORS_INIT()

                                                    if self.error is None:
                                                        self.dict_store[ 'values' ]     = self.v1
                                                        self.dict_store[ 'operators' ]  = self.op1

                                                        for _name_ in self._value_[ 1: ]:
                                                            self._name_, self.error = self.control.DELETE_SPACE( _name_ )
                                                            if self.error is None:
                                                                self.name, self.error = self.control.CHECK_NAME( _name_ )

                                                                if self.error is None:
                                                                    self.dict_store[ 'names' ].append( self.name )

                                                                else:
                                                                    self.error = self.error
                                                                    break
                                                            else:
                                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                break

                                                        if self.error is None:
                                                            self.storage_data.append( self.dict_store )

                                                        else:
                                                            self.error = self.error
                                                            break

                                                    else:
                                                        self.error = self.error
                                                        break
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.new_string )
                                                break
                                    else:
                                        self.error = self.error
                                        break
                                else:
                                    self.error = self.error
                                    break

                            else:
                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                break

                        else:
                            self.error = ERRORS(self.line).ERROR3(self.master, str_)
                            break
        else:
            pass

        return  self.storage_data, self.storage_operators, self.error

    def BRACKET_ANALYSES(self, string: str):
        self.error      = None
        self._string    = None
        self.left       = ['(', '{', '[', "'", '"']
        self.right      = [')', '}', ']', "'", '"']
        self.key        = False

        self.string, self.error = self.control.DELETE_SPACE( string )

        if self.error is None :
            if self.string[ 0 ] not in self.left:
                self.key                = self.key
                self._string            = self.string

            else:
                self.value, self.error = particular_str_selection.SELECTION(self.string, self.string, self.data_base,
                                                                            self.line   ).CHAR_SELECTION( '.' )
                if self.error is None:
                    if len( self.value ) == 1:
                        self.get_opposite = self.left.index( self.string[ 0 ] )
                        if self.string[ -1 ] == self.right[ self.get_opposite ]:
                            if self.string[ 0 ] == '(':
                                l, r            = 0, 0
                                self.count      = 0
                                self.if_comma   = False

                                for str_ in self.string:
                                    if str_ != ',':
                                        l, r = l + str_.count('('), r + str_.count(')')
                                        if l == r:
                                            if self.count <= 1:
                                                self.count += 1
                                                l, r  = 0, 0
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.string )
                                                break
                                        else: pass

                                    else:
                                        self.if_comma = True
                                        break
                                
                                if self.error is None:
                                    if self.if_comma == False:
                                        self.key                    = True
                                        self.string_, self.error    = self.control.DELETE_SPACE( self.string[1 : -1] )

                                        if self.error is None:
                                            self._string            = self.string_
                                        else:
                                            self.error = None
                                            self._string            = self.string
                                            self.key                = 'tuple'
                                            #self.error = ERRORS( self.line ).ERROR4( self.master, self.string )
                                    else:
                                        self.string_, self.error = self.control.DELETE_SPACE(self.string[1: -1])
                                        self.key                    = 'tuple' #self.key
                                        self._string                = self.string
                                else: pass
                            else:
                                self.key        = self.key
                                self._string    = self.string
                        else: self.error = ERRORS( self.line ).ERROR0( self.string )
                    else:
                        self.key        = self.key
                        self._string    = self.string
                else: pass
        else: self.error = None

        return self._string, self.key, self.error

    def CHECK_CHAR(self):
        self.chars = ['<', '>', '!', '?', '|', '&']
        self.error = None

        """
        for str_ in self.master :
            if str_ in self.chars:
                self.error = ERRORS( self.line ).ERROR0( self.master )
                break
            else: pass
        """
        return self.master, self.error

    def SCANNER(self, main_string: str):
        self.error      = None
        self.ll = looking_for_logical_operators.LOGICAL_OPERATORS( self.master, self.data_base, self.line )
        self.lb = looking_for_bool_operators.BOOLEAN_OPERATORS( self.master, self.data_base, self.line)

        self.test_bool, self.bool_op_, self.error = self.lb.BOOLEAN_OPAERATORS()

        if self.error is None:
            if not self.bool_op_:
                self.test_logical, self.logical_op_, self.error = self.ll.LOGICAL_OPAERATORS_INIT()
                if self.error is None:
                    if not self.logical_op_: pass
                    else: self.error = ERRORS( self.line ).ERROR0( main_string )
                else: self.error = ERRORS( self.line ).ERROR0( main_string )
            else: self.error = ERRORS( self.line ).ERROR0( main_string )
        else: self.error = ERRORS( self.line ).ERROR0( main_string )

        return self.error

    def DOUBLE_SCAN(self, main_string: str, string: str):

        self.error          = None
        self.string , err   = self.control.DELETE_SPACE( string )
        self.len            = 0
        self.string_init    = ''
        self.op             = self.string[ -1 ]
        self.store_value    = []
        self.store_op       = []
        self._return_       = {
            'values'        : None,
            'operators'     : None,
            'names'         : None,
            'type'          : 'numeric'
        }

        if self.op == '+': self.len = len( self.string ) - 1
        else: self.len = len( self.string ) - 1

        self.string_init            = self.master[ self.len : ]
        self.string_init, err       = self.control.DELETE_SPACE( self.string_init )

        self.store_value.append( self.master[ : self.len ] )
        self.data , self.opeators, self.error = ARITHMETIC_OPERATORS( self.string_init, self.data_base,
                                                                      self.line).ARITHMETIC_OPAERATORS()
        if self.error is None:
            if self.opeators:
                self.store_value.append( self.data )
                self._return_[  'operators' ]   = self.opeators
                self._return_[ 'values' ] = self.store_value
            else:
                self.store_value.append( self.data )
                self._return_[ 'values' ] = self.store_value
        else: self.error = self.error

        return self._return_, self.store_op,  self.error

    def FUNC_CHECK(self, string:  str, end : bool = True):

        self.new_string         = string
        self.error              = None

        if self.new_string[ : 4 ] == 'func':
            try:
                self.next = self.new_string[ 4 : ]
                self.next, self.error = self.control.DELETE_SPACE( self.next )
                if self.error is None:
                    if self.next[ 0 ] == '(':
                        self.error = ERRORS( self.line ).ERROR6( self.master, 'func( ... )' )
                    elif self.next[ 0 ] == '[':
                        self.error = ERRORS( self.line ).ERROR6( self.master, 'func[ ... ]' )
                    elif self.next[ 0 ] == '{':
                        self.error = ERRORS( self.line ).ERROR6( self.master, 'func{ ... }' )
                    elif self.next[ 0 ] == '"':
                        self.error = ERRORS( self.line ).ERROR6( self.master, 'func" ... "' )
                    elif self.next[ 0 ] == "'":
                        self.error = ERRORS( self.line ).ERROR6( self.master, "func' ... '" )
                    else: pass
                else:
                    if end == True: self.error = ERRORS( self.line ).ERROR6( self.master, 'func' )
                    else:
                        if self.new_string == 'func': self.error = ERRORS( self.line ).ERROR6( self.master, 'func' )
                        else: self.error = None

            except IndexError:
                if end == True: self.error = ERRORS( self.line).ERROR6( self.master, 'func' )
                else:
                    if self.new_string == 'func': self.error = ERRORS( self.line ).ERROR6( self.master, 'func' )
                    else: self.error = None
        else: self.error = None

        return self.error

class ERRORS:
    def __init__(self, line):
        self.line       = line
        self.cyan       = bm.init.bold + bm.fg.rbg(0,255,255)
        self.red        = bm.init.bold + bm.fg.rbg(255,0,0)
        self.green      = bm.init.bold + bm.fg.rbg(0,255,0)
        self.yellow     = bm.init.bold + bm.fg.rbg(255,255,0)
        self.magenta    = bm.init.bold + bm.fg.rbg(255,0,255)
        self.white      = bm.init.bold + bm.fg.rbg(255,255,255)
        self.blue       = bm.init.bold + bm.fg.rbg(0,0,255)
        self.reset      = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str, char1: str):
        error = '{}due to {}<< {} >> {}at the beginning. {}line: {}{}'.format(self.white, self.green, char1, self.yellow,
                                                                             self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR2(self, string: str, char1: str, char2: str, pos = 'after'):
        error = '{}due to {}<< {} >> {}{} {}<< {} >>. {}line: {}{}'.format(self.white, self.green, char1, self.magenta, pos, self.red, char2,
                                                                                                    self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR3(self, string: str, char: str):
        error = '{}due to {}<< {} >> {}at the end. {}line: {}{}'.format(self.white, self.green, char, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR4(self, string: str, char: str):
        error   = '{}due to {}no values inside {}<< {} >> {}line: {}{}'.format(self.white, self.green, self.red, char, self.white,
                                                                               self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax, '.format(self.white, 'SyntaxError') + error

        return self.error+self.reset

    def ERROR5(self, string: str, char: str):
        error = '{}due to bad {}char, {}<< {} >>. {}line: {}{}'.format(self.white, self.red, self.green, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR6(self, string: str, char: str ):
        error = '{}due to the {}function {}{}. {}line: {}{}'.format(self.white, self.red, self.magenta, char, self.white, self.yellow, self.line)
        self.error =fe.FileErrors( 'SyntaxError' ).Errors() + '{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset


