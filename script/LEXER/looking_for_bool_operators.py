from colorama import  Fore
from script.LEXER import segmentation
from script import  control_string

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class BOOLEAN_OPERATORS:

    def __init__(self, master, data_base, line):
        self.master                 = master
        self.long_chaine            = master
        self.data_base              = data_base
        self.line                   = line
        self.number                 = segmentation.NUMBER()
        self.string_error           = segmentation.ERROR( self.line )
        self.all_chars              = segmentation.CHARS()
        self.control                = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.bool_operators         = ['or', 'and', 'only']
        self.bool_operators_        = ['||', '&&', '|&|']
        self.logical_operators      = ['is', 'not', 'in', '==', '!=', '>=', '<=', '<', '>', '?']
        self.arithmetic_operators   = ['+', '-', '*', '/', '^', '%']
        self.accpeted_chars         = self.control.LOWER_CASE()+self.control.UPPER_CASE()+['_']+[str(x) for x in range(10)]
        self.accpeted_chars_        = self.accpeted_chars + self.arithmetic_operators + ['<', '>', '=', '!', '?', '.', ' ','$']

    def BOOLEAN_OPAERATORS(self):

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

        self._string_               = ''
        self.string_boolean         = ''
        self.storage_operators      = []
        self.logical_op             = []
        self.activation_operators   = None
        self.storage_data           = []
        self.invisible_string       = ''

        ################################################################################################################

        self.master, self.error     = self.control.DELETE_SPACE( self.master )

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
                        self.error = self.string_error.ERROR_TREATMENT2( self.long_chaine, str_ )
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
                                self.error = self.string_error.ERROR_TREATMENT3( self.long_chaine )
                                break

                else:
                    pass

                if self.left != self.rigth:
                    self.active_key = True

                elif self.left == self.rigth and str_ in [')', ']', '}', '"', "'"]:
                    self.active_key = False

                elif self.left == self.rigth and str_ not in ['(', '[', '{', '"', "'"]:
                    self.active_key = 'dot'

                self._string_   += str_

                if self.active_key == True:

                    self.string += str_

                    if self.invisible_string:
                        self.check_chars = []

                        for _str_ in self.invisible_string:
                            if _str_ in self.accpeted_chars_:
                                self.check_chars.append(True)
                            else:
                                self.check_chars.append(False)
                                break

                        if False not in self.check_chars:
                            self.invisible_string   = ''
                        else:
                            self.id = self.check_chars.index(False)
                            self.error = ERRORS( self.line ).ERROR5(self.invisible_string, self.invisible_string[self.id])
                            break

                    else:
                        pass

                elif self.active_key == False:
                    self.string += str_

                    if i != len( self.master ) - 1:
                        pass

                    else:
                        self.string, self.error = self.control.DELETE_SPACE(self.string)
                        if self.error is None:
                            if self.activation_operators == True:
                                self.string_, self.error    = BOOLEAN_OPERATORS(self.master, self.data_base,
                                                                    self.line).VALUE_INSIDE_PARENTHESES(self.string)

                                if self.error is None:
                                    self.error = BOOLEAN_OPERATORS(self.master, self.data_base,
                                            self.line).SYNTAX_PARENTHESIS( self.string, self.storage_operators[ -1 ] )

                                    if self.error is None:
                                        self.storage_data.append( self.string )

                                    else:
                                        self.error = self.error
                                        break

                                else:
                                    self.error = self.error
                                    break

                            else:
                                self.storage_data.append( self.string )

                        else:
                            self.error  = ERRORS(self.line).ERROR0(self.master)
                            break

                    self.initialize[0] = None
                    self.left = 0
                    self.rigth = 0
                    self.str_id = False
                    self.key_bracket = None

                else:
                    self.string  += str_
                    self.invisible_string   += str_

                    if i != len(self.master) - 1:
                        if str_ not in [' ']:
                            self.string_boolean += str_

                            if self.string_boolean in self.bool_operators + self.bool_operators_:
                                self.len_str_bool                        = len( self.string_boolean )


                                try:
                                    self.new_string_left                 = self.master[: i+1]
                                    self.new_string_left                 = self.string[: - self.len_str_bool ]
                                    self.new_string_left_                = self.new_string_left
                                    self.new_string_left, self.error     = self.control.DELETE_SPACE( self.new_string_left )

                                    self.new_string_right                = self.master[i+1: ]
                                    self.new_string_right, self.error    = self.control.DELETE_SPACE( self.new_string_right )
                                    self.string_clear , self.error       = self.control.DELETE_SPACE( self.string )

                                except IndexError:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break

                                if self.error is None:

                                    l, r   = len(self.master) - self.len_str_bool, i + 1

                                    if self.master[ r ] in [' ']:

                                        if self.new_string_left_[ -1 ] in [' ']:
                                            if self.new_string_left[ -1 ] in [ ')' ]:
                                                if self.new_string_right[ 0 ] in [ '(' ]:
                                                    if self.string_clear[ 0 ] in [ '(' ]:

                                                        self.string_boolean = INV().INV_TRANSFORM(self.string_boolean)
                                                        self.storage_operators.append( self.string_boolean )
                                                        self.string = self.string[ : -self.len_str_bool]
                                                        self.string, self.error = self.control.DELETE_SPACE( self.string )

                                                        if self.error is None:
                                                            self.string_, self.error     = BOOLEAN_OPERATORS(self.master,
                                                                self.data_base, self.line).VALUE_INSIDE_PARENTHESES( self.string )

                                                            if self.error is None:

                                                                self.error = BOOLEAN_OPERATORS(self.master, self.data_base,
                                                                        self.line).SYNTAX_PARENTHESIS(self.string,
                                                                                                    self.string_boolean)

                                                                if self.error is None:
                                                                    self.storage_data.append( self.string )
                                                                    self.activation_operators   = True
                                                                    self.string_boolean         = ''
                                                                    self.string                 = ''
                                                                    self.invisible_string       = ''

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
                                                        self.error  = ERRORS( self.line ).ERROR2(self.string,
                                                                            self.string_boolean, self.string_clear[ 0 ])
                                                        break

                                                else:
                                                    self.error = ERRORS( self.line ).ERROR2(self.master, self.string_boolean,
                                                                                    self.new_string_right[ 0 ], 'after')
                                                    break

                                            else:
                                                self.error = ERRORS( self.line ).ERROR2(self.master, self.string_boolean,
                                                                                            self.new_string_left[ -1 ])
                                                break

                                        else:
                                            if self.string_boolean in ['or', 'and', 'only']:
                                                self.error = ERRORS(self.line).ERROR1(self.master, self.new_string_left_[ -1 ],
                                                                                                    self.string_boolean,)
                                                break

                                            else:
                                                if self.new_string_left[ -1 ] in [ ')' ]:
                                                    if self.new_string_right[0] in ['(']:
                                                        if self.string_clear[0] in ['(']:
                                                            self.string_boolean     = INV().INV_TRANSFORM(self.string_boolean)
                                                            self.storage_operators.append(self.string_boolean)
                                                            self.string             = self.string[: -self.len_str_bool]
                                                            self.string, self.error = self.control.DELETE_SPACE(self.string)

                                                            if self.error is None:
                                                                self.string_, self.error = BOOLEAN_OPERATORS(self.master,
                                                                    self.data_base, self.line).VALUE_INSIDE_PARENTHESES(
                                                                    self.string)

                                                                if self.error is None:

                                                                    self.error = BOOLEAN_OPERATORS(self.master,
                                                                        self.data_base, self.line).SYNTAX_PARENTHESIS(
                                                                                    self.string, self.string_boolean)
                                                                    if self.error is None:
                                                                        self.storage_data.append( self.string )
                                                                        self.activation_operators   = True
                                                                        self.string_boolean         = ''
                                                                        self.string                 = ''
                                                                        self.invisible_string       = ''

                                                                    else:
                                                                        self.error = self.error
                                                                        break

                                                                else:
                                                                    self.error = self.error
                                                                    break

                                                            else:
                                                                self.error = ERRORS(self.line).ERROR0(self.master)
                                                                break

                                                        else:
                                                            self.error = ERRORS(self.line).ERROR2(self.string,
                                                                            self.string_boolean,self.string_clear[0])
                                                            break

                                                    else:
                                                        self.error = ERRORS(self.line).ERROR2(self.master,
                                                                    self.string_boolean,self.new_string_right[0],'after')
                                                        break

                                                else:
                                                    self.error = ERRORS(self.line).ERROR2(self.master,
                                                                        self.string_boolean,self.new_string_left[-1])
                                                    break

                                    else:
                                        if self.string_boolean in self.bool_operators_:
                                            if self.new_string_left[ -1 ] in [ ')' ]:
                                                if self.new_string_right[0] in [ '(' ]:
                                                    if self.string_clear[ 0 ] in [ '(' ]:
                                                        self.string_boolean = INV().INV_TRANSFORM(self.string_boolean)
                                                        self.storage_operators.append(self.string_boolean)
                                                        self.string = self.string[: -self.len_str_bool]
                                                        self.string, self.error = self.control.DELETE_SPACE(self.string)

                                                        if self.error is None:
                                                            self.string_, self.error = BOOLEAN_OPERATORS(self.master,
                                                                    self.data_base,self.line).VALUE_INSIDE_PARENTHESES(
                                                                    self.string )

                                                            if self.error is None:

                                                                self.error = BOOLEAN_OPERATORS(self.master, self.data_base,
                                                                            self.line).SYNTAX_PARENTHESIS(self.string,
                                                                                                self.string_boolean)

                                                                if self.error is None:
                                                                    self.storage_data.append( self.string )
                                                                    self.activation_operators   = True
                                                                    self.string_boolean         = ''
                                                                    self.string                 = ''
                                                                    self.invisible_string       = ''

                                                                else:
                                                                    self.error = self.error
                                                                    break

                                                            else:
                                                                self.error = self.error
                                                                break

                                                        else:
                                                            self.error = ERRORS(self.line).ERROR0(self.master)
                                                            break

                                                    else:
                                                        self.error  = ERRORS( self.line ).ERROR2(self.string,
                                                                            self.string_boolean, self.string_clear[ 0 ])
                                                        break

                                                else:
                                                    self.error = ERRORS(self.line).ERROR2(self.master, self.string_boolean,
                                                                                          self.new_string_right[0], 'after')
                                                    break

                                            else:
                                                self.error = ERRORS(self.line).ERROR2(self.master, self.string_boolean,
                                                                                                self.new_string_left[ -1 ])
                                                break

                                        else:
                                            if self.master[ r ] in self.accpeted_chars:
                                                self.string_boolean = ''

                                            else:
                                                self.error  = ERRORS( self.line ).ERROR1(self.master,
                                                                                self.string_boolean,self.master[ r ] )
                                                break

                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break

                            else:
                                pass

                        else:
                            self.string_boolean     = ''

                    else:
                        self.string_boolean += str_

                        if self.string_boolean in self.bool_operators + self.bool_operators_:
                            self.error = ERRORS(self.line).ERROR0(self.master)
                            break

                        else:
                            if str_ in self.accpeted_chars:
                                self.string, self.error  = self.control.DELETE_SPACE(self.string)
                                if self.error is None:
                                    if self.storage_operators:
                                        if self.string[-1] in [')']:
                                            self.error = BOOLEAN_OPERATORS(self.master, self.data_base,
                                                                    self.line).SYNTAX_PARENTHESIS(self.string,
                                                                                        self.storage_operators[ -1 ])
                                            if self.error is None:
                                                self.storage_data.append(self.string)
                                            else:
                                                self.error = self.error
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                    else:
                                        self.storage_data.append(self.string)

                                else:
                                    self.error = ERRORS(self.line).ERROR0(self.master)
                                    break

                            else:
                                self.error  = ERRORS( self.line ).ERROR4( self.master, str_ )
                                break

        else:
            pass

        if self.error is None:
            if self.storage_operators:
                if 'only' in self.storage_operators:
                    if len( self.storage_operators ) > 1:
                        if 'or' not in self.storage_operators and 'and' not in self.storage_operators:
                            self.error = ERRORS(self.line).ERROR7(self.master)
                        else:
                            if 'or' in self.storage_operators and 'and' not in self.storage_operators:
                                self.id = self.storage_operators.index('or')
                                self.error = ERRORS(self.line).ERROR8(self.master,self.storage_operators[self.id])
                            elif 'and' in self.storage_operators and 'or' not in self.storage_operators:
                                self.id = self.storage_operators.index('and')
                                self.error = ERRORS(self.line).ERROR8(self.master,self.storage_operators[self.id])
                            else:
                                self.id = self.storage_operators.index('or')
                                self.error = ERRORS(self.line).ERROR8(self.master, self.storage_operators[self.id])
                    else:
                        pass
                else:
                    pass
            else:
                pass

        else:
            self.error = self.error

        return  self.storage_data, self.storage_operators, self.error

    def VALUE_INSIDE_PARENTHESES(self, string):
        self.string_ = string[1 : -1]
        self.string_, self.error = self.control.DELETE_SPACE( self.string_ )

        if self.error is None:
            pass
        else:
            error       = '{}due to {}no values {}inside {}<< {} >>. {}line: {}{}'.format(ke, ve, ke, ne, string, we, ke,
                                                                                                            self.line )
            self.error  = '{}{} : invalid syntax in {}<< {} >> '.format(ke, 'SyntaxError', ae, self.master)+error

        return string, self.error

    def SYNTAX_PARENTHESIS(self, string: str, operator: str):
        self.r              = 0
        self.l              = 0
        self.count          = 0
        self.error          = None

        for str_ in string :
            if str_ in [ '(' ]:
                self.l += 1
            elif str_ in [ ')' ]:
                self.r += 1
            else:
                pass

            if self.r == self.l :
                if self.count <= 1:
                    self.count += 1
                    self.r, self.l  = 0, 0

                else:
                    self.error = ERRORS( self.line ).ERROR6( self.master, string, operator)
                    break

            else:
                pass

        return self.error

class ERRORS:
    def __init__(self, line):
        self.line       = line

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we,ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR1(self, string1: str, string2: str, char: str):
        error = '{}due to {}undefined {}space between {}<< {} >> {}and {}<< {} >>. {}line: {}{}'.format(ke, ve, ke,
                                                                            ne, string2, ke, ie, char, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string1) + error

        return self.error

    def ERROR2(self, string1: str, string2: str, char: str, s = 'before'):
        error = '{}due to {}<< {} >> {}{} {}<< {} >>. {}line: {}{}'.format(ke, ne, char, ke, s, ve, string2, we,
                                                                                                        ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string1) + error

        return self.error

    def ERROR3(self, string1: str, char1: str, char2: str):
        error = '{}due to {}<< {} >> {}and {}<< {} >>. {}line: {}{}'.format(ke, ne, char1, ke, ve, char2, we, ke,
                                                                                                            self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string1) + error

        return self.error

    def ERROR4(self, string: str, char: str):
        error = '{}due to {}<< {} >> {}at the end. {}line: {}{}'.format(ke, ve, char, ke, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR5(self, string: str, char: str):
        error = '{}due to bad {}char, {}<< {} >>. {}line: {}{}'.format(ke, ne, ve, char, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >> '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR6(self, string1: str, string2: str, char: str):
        error = '{}because of {}<< {} >> {}put {}<< {} >> {}inside {}<< ( ) >>. {}line: {}{}'.format(ke, ne, char, ke,
                                                                    ve, string2, ke, ae, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string1) + error

        return self.error

    def ERROR7(self, string: str):
        error = '{}due to {}too much {}<< only >> {}operators. {}line: {}{}'.format(ke, ne, ve, ke, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >> '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR8(self, string: str, op: str):
        error = '{}you cannot associate {}<< only >> {}with {}<< {} >>. {}line: {}{}'.format(ke, ne, ke, ve, op, we,
                                                                                                        ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >> '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

class INV:
    def INV_TRANSFORM(self, string):
        if string == '||':
            string = 'or'
        elif string == '&&':
            string = 'and'
        elif string == '|&|':
            string = 'only'
        else:
            pass

        return string