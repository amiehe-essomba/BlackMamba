"""
this module is used after of that of boolean operators.
It is specically used for looking for the logical operators
respectively [ == , ? ; !=, <, >, >= , <= , not in , in ]
in total 9 operators.

[?]      : is the same as type()
[!=]     : checking if two objects are differnt
[==]     : checking if two objects are identical
[<]      : checking if Obj1 is lower than Obj2
[>]      : checking if Obj1 if bigger than Obj2
[>=]     : checking if Obj1 is bigger or egal than Obj2
[<=]     : checking if Obj1 is lower or egal than Obj2
[not in] : checking if Obj1 is not in Obj2
[in]     : checking if Obj1 in Obj2

"""

from script.LEXER                   import segmentation
from script                         import control_string
from script.STDIN.LinuxSTDIN        import bm_configure as bm
try:  from CythonModules.Linux      import fileError as fe
except ImportError:
    from CythonModules.Windows      import fileError as fe

class LOGICAL_OPERATORS:
    def __init__(self, master: str, data_base: dict, line : int):
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
        self.logical_operators1     = ['not', 'in']
        self.logical_operators2     = ['==', '!=', '>=', '<=', '<', '>', '?']
        self.arithmetic_operators   = ['+', '-', '*', '/', '^', '%']
        self.accpeted_chars         = self.control.LOWER_CASE() + self.control.UPPER_CASE() + \
                                      ['_', '(', '[', '{', '.', '"', "'", ' '] + [str(x) for x in range(10)] + ['+', '-', '?']
        self.accpeted_chars_        = self.control.LOWER_CASE() + self.control.UPPER_CASE() + \
                                      ['_', ')', ']', '}', '.', '"', '"', ' '] + [str(x) for x in range(10)]
        self.right_accepted         = self.control.LOWER_CASE() + self.control.UPPER_CASE() + \
                                      [str(x) for x in range(10)]+['_','.']

    def LOGICAL_OPAERATORS_INIT(self):
        """
        * storage_data contains the splited values
        * storage_operators contains oprators
        :return: {self.storage_data : list, self.storage_operators : list, self.error : string }
        """

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

        self.string_logical         = ''
        self.storage_operators      = []
        self.logical_op             = []
        self.activation_operators   = None
        self.storage_data           = []
        self._string_               = ''

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
                else: pass

                if self.left != self.rigth:
                    self.active_key = True
                elif self.left == self.rigth and str_ in [')', ']', '}', '"', "'"]:
                    self.active_key = False
                elif self.left == self.rigth and str_ not in ['(', '[', '{', '"', "'"]:
                    self.active_key = 'dot'

                self._string_   += str_

                if self.active_key == True:  self.string += str_
                elif self.active_key == False:
                    self.string += str_

                    if i != len(self.master) - 1: pass
                    else:
                        self.string, self.error = self.control.DELETE_SPACE(self.string)
                        if self.error is None:
                            if self.activation_operators == True:
                                #self.string_, self.error    = BOOLEAN_OPERATORS(self.master, self.data_base,
                                #                                    self.line).VALUE_INSIDE_PARENTHESES(self.string)
                                if self.error is None:  self.storage_data.append( self.string )
                                else:  break
                            else:  self.storage_data.append( self.string )
                        else:
                            self.error  = ERRORS(self.line).ERROR0(self.master)
                            break

                    self.initialize[0]  = None
                    self.left           = 0
                    self.rigth          = 0
                    self.str_id         = False
                    self.key_bracket    = None
                else:
                    self.string  += str_
                    if i != len(self.master) - 1:
                        if str_ not in [' ']:
                            self.string_logical += str_

                            if self.string_logical in self.logical_operators2:
                                #if self.master[ i + 1] in [' ']:
                                self.len_str_bool                        = len( self.string_logical )

                                try:
                                    self.new_string_left                 = self.master[: i+1]
                                    self.new_string_left                 = self.string[: - self.len_str_bool ]
                                    self.new_string_left, self.error     = self.control.DELETE_SPACE( self.new_string_left )

                                    self.new_string_right                = self.master[i+1: ]
                                    self.new_string_right, self.error    = self.control.DELETE_SPACE( self.new_string_right )
                                    self.string_clear , self.error       = self.control.DELETE_SPACE( self.string )

                                except IndexError:
                                    if self.string_logical in ['?']:  self.error = None
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break

                                if self.error is None:
                                    if len( self.string_logical ) == 1 and self.string_logical not in [ '?' ]:
                                        if self.new_string_right[ 0 ] in [ '=' ]:
                                            if self.error is None: pass
                                            else:  break
                                        else:
                                            try:
                                                if self.new_string_right[ 0 ] in self.accpeted_chars:
                                                    try:
                                                        if self.new_string_left[ -1 ] in self.accpeted_chars_:

                                                            if self.master [i + 1] in [' ']:
                                                                self.storage_operators.append( self.string_logical )
                                                                self.string             = self.string[: -self.len_str_bool]
                                                                self.string, self.error = self.control.DELETE_SPACE( self.string )

                                                                if self.error is None:
                                                                    self.storage_data.append(self.string)
                                                                    self.activation_operators   = True
                                                                    self.string_logical         = ''
                                                                    self.string                 = ''
                                                                else:
                                                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                    break
                                                            else:
                                                                self.error = ERRORS(self.line).ERROR3(self.master,
                                                                                self.master[i+1], self.string_logical)
                                                                break
                                                        else:
                                                            self.error = ERRORS(self.line).ERROR2(self.master,
                                                                    self.new_string_left[ -1 ],self.string_logical, pos='before')
                                                            break
                                                    except IndexError:
                                                        self.error = ERRORS(self.line).ERROR0(self.master)
                                                        break
                                                else:
                                                    self.error = ERRORS(self.line).ERROR2(self.master,
                                                                            self.new_string_right[ 0 ],self.string_logical)
                                                    break
                                            except IndexError:
                                                self.error = ERRORS(self.line).ERROR0(self.master)
                                                break

                                    else:
                                        l, r   = len(self.master) - self.len_str_bool, i + 1
                                        try:
                                            if self.new_string_right[ 0 ] in self.accpeted_chars:
                                                if self.master[i+1] in [' ']:
                                                    try:
                                                        if self.new_string_left[ -1 ] in self.accpeted_chars_:

                                                            self.storage_operators.append( self.string_logical )
                                                            self.string = self.string[ : -self.len_str_bool]
                                                            self.string, self.error = self.control.DELETE_SPACE( self.string )

                                                            if self.error is None:
                                                                self.storage_data.append( self.string )
                                                                self.activation_operators   = True
                                                                self.string_logical         = ''
                                                                self.string                 = ''
                                                            else:
                                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                break
                                                        else:
                                                            self.error = ERRORS(self.line).ERROR2(self.master,
                                                                self.new_string_left[ -1 ],self.string_logical,
                                                                                                  pos='before')
                                                            break

                                                    except IndexError:
                                                        if self.string_logical in ['?']:
                                                            self.storage_operators.append(self.string_logical)
                                                            self.string                 = ''
                                                            self.string_logical         = ''
                                                            self.activation_operators   = True

                                                        else:
                                                            self.error = ERRORS(self.line).ERROR0(self.master)
                                                            break
                                                else:
                                                    self.error = ERRORS(self.line).ERROR3(self.master,
                                                                            self.master[i + 1], self.string_logical)
                                                    break

                                            else:
                                                self.error = ERRORS(self.line).ERROR2(self.master, self.new_string_right[ 0 ],
                                                                                                        self.string_logical)
                                                break

                                        except IndexError:
                                            self.error = ERRORS(self.line).ERROR0(self.master)
                                            break

                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                            elif self.string_logical in self.logical_operators1:
                                self.len_str_bool                       = len( self.string_logical )

                                try:
                                    self.new_string_left                = self.master[: i + 1]
                                    self.new_string_left                = self.string[: - self.len_str_bool]
                                    self.new_string_left_               = self.new_string_left
                                    self.new_string_left, self.error    = self.control.DELETE_SPACE(self.new_string_left)

                                    self.new_string_right               = self.master[i + 1:]
                                    self.new_string_right_              = self.master[i + 1:]
                                    self.new_string_right, self.error   = self.control.DELETE_SPACE(self.new_string_right)
                                    self.string_clear, self.error       = self.control.DELETE_SPACE(self.string)

                                except IndexError:
                                    if self.string_logical in ['not']:
                                        self.error                      = None
                                    else:
                                        self.error                      = ERRORS(self.line).ERROR0(self.master)
                                        break

                                if self.error is None:
                                    r = i + 1
                                    if self.master[ r ] in [' ']:
                                        try:
                                            if self.new_string_left_[ -1 ] in [' ']:
                                                if self.new_string_right[ 0 ] in self.accpeted_chars:
                                                    if self.new_string_left[ -1 ] in self.accpeted_chars_:
                                                        if self.string_logical in [ 'not' ]:
                                                            try:
                                                                if self.new_string_right[ :2 ] not in [ 'in' ]:
                                                                    self.error = ERRORS(self.line).ERROR0(self.master)
                                                                    break

                                                                else:
                                                                    if self.new_string_right[ 2 ] in [' ']:
                                                                        self.logical_op.append( self.string_logical )
                                                                        self.string_logical     = ''
                                                                        self.string             = self.new_string_left

                                                                    else:
                                                                        self.error = ERRORS(self.line).ERROR0(self.master)
                                                                        break

                                                            except IndexError:
                                                                self.error = ERRORS(self.line).ERROR0(self.master)
                                                                break

                                                        else:
                                                            self.logical_op.append( self.string_logical )
                                                            self.string = self.new_string_left

                                                            if len( self.logical_op ) == 1:

                                                                self.storage_operators.append(self.logical_op[0])
                                                                self.storage_data.append( self.string )
                                                                self.activation_operators   = True
                                                                self.string_logical         = ''
                                                                self.string                 = ''
                                                                self.logical_op             = []

                                                            else:
                                                                if self.logical_op[ 0 ] in [ 'not' ]:
                                                                    if self.logical_op[ 1 ] in [ 'in' ]:
                                                                        self.string_logical         = self.logical_op[ 0 ]+' '+\
                                                                                                        self.logical_op[ 1 ]

                                                                        self.storage_operators.append(self.string_logical)
                                                                        self.storage_data.append( self.string )
                                                                        self.activation_operators   = True
                                                                        self.string_logical         = ''
                                                                        self.string                 = ''
                                                                        self.logical_op             = []

                                                                    else:
                                                                        self.error = ERRORS( self.line ).ERROR1( self.master,
                                                                                    self.logical_op[0] , self.logical_op[1])
                                                                        break

                                                                else:
                                                                    self.error = ERRORS(self.line).ERROR0(self.master)
                                                                    break

                                                    else:
                                                        self.error = ERRORS(self.line).ERROR2(self.master,
                                                            self.new_string_left[ -1 ], self.string_logical, pos='before')
                                                        break

                                                else:
                                                    self.error = ERRORS(self.line).ERROR2(self.master,
                                                                        self.new_string_right[ 0 ], self.string_logical)
                                                    break

                                            else:
                                                self.error = ERRORS(self.line).ERROR3(self.master, self.string_logical,
                                                                                                self.new_string_left_[ -1 ])
                                                break

                                        except IndexError:
                                            if self.string_logical in [ 'not' ]:
                                                try:
                                                    if self.new_string_right[ :2 ] in [ 'in', 'is' ]:
                                                        if self.new_string_right[ 2 ] in [' ']:
                                                            self.error = ERRORS(self.line).ERROR0(self.master)
                                                            break
                                                        else:  pass
                                                    else:
                                                        if self.new_string_right[0] in self.accpeted_chars:
                                                            self.storage_operators.append( self.string_logical )
                                                            self.activation_operators = True
                                                            self.string = ''
                                                            self.string_logical = ''
                                                            self.logical_op = []
                                                        else:
                                                            self.error = ERRORS(self.line).ERROR2(self.master,
                                                                        self.new_string_right[0], self.string_logical)
                                                            break
                                                except IndexError:
                                                    if self.new_string_right[ 0 ] in self.accpeted_chars:
                                                        self.storage_operators.append( self.string_logical )
                                                        self.activation_operators   = True
                                                        self.string                 = ''
                                                        self.string_logical         = ''
                                                        self.logical_op             = []
                                                    else:
                                                        self.error = ERRORS(self.line).ERROR2(self.master,
                                                                    self.new_string_right[0],self.string_logical)
                                                        break
                                            else:
                                                self.error = ERRORS(self.line).ERROR0(self.master)
                                                break
                                    else:
                                        if self.master[ r ] in self.right_accepted:  pass
                                        else:
                                            self.error = ERRORS(self.line).ERROR3(self.master, self.string_logical,
                                                                                                        self.master[ r ])
                                            break
                                else:  break
                            else:  pass
                        else:  self.string_logical     = ''
                    else:
                        self.string_logical += str_
                        if self.string_logical in self.logical_operators1 + self.logical_operators2:
                            self.error = ERRORS( self.line ).ERROR0( self.master )
                            break
                        else:
                            if str_ in self.accpeted_chars_:
                                self.string, self.error  = self.control.DELETE_SPACE( self.string )
                                if self.error is None:
                                    #self.error = LOGICAL_OPERATORS(self.master, self.data_base,
                                    #                               self.line).HUNTER_OPERATORS( self.string)

                                    # to add if something happens
                                    if self.error is None:  self.storage_data.append( self.string )
                                    else: break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                            else:
                                self.error  = ERRORS( self.line ).ERROR4( self.master, str_)
                                break
        else:  pass

        if self.error is None:
            if len( self.storage_operators ) > 1:
                if len( self.storage_operators ) == 2:
                    if self.storage_operators[ 0 ] == '==' and self.storage_operators[ 1 ] == '?':
                        if len( self.storage_data ) == 2:
                            pass
                        else:
                            self.error = ERRORS(self.line).ERROR0( self.master )

                    elif self.storage_operators[ 1 ] == '==' and self.storage_operators[ 0 ] == '?':
                        if len( self.storage_data ) == 2:
                            pass
                        else:
                            self.error = ERRORS( self.line ).ERROR0( self.master )

                    else:
                        self.error = ERRORS(self.line).ERROR5(self.master, self.storage_operators)

                elif len( self.storage_operators ) == 3:
                    if self.storage_operators[ 0 ] == '?' and self.storage_operators[ 1 ] == '==' and \
                                                                            self.storage_operators[ 2 ] == '?':
                        if len(self.storage_data) == 2:
                            pass
                        else:
                            self.error = ERRORS( self.line ).ERROR0( self.master )
                    else:
                        self.error = ERRORS(self.line).ERROR5(self.master, self.storage_operators)

                else:
                    self.error = ERRORS(self.line).ERROR5(self.master, self.storage_operators)

            else:
                if self.storage_operators:
                    if self.storage_operators[0] == '?':
                        if len( self.storage_data ) != 1:
                            self.error = ERRORS( self.line ).ERROR0( self.master )

                        else:
                            pass

                    elif self.storage_operators[0] == 'not':
                        if len( self.storage_data ) != 1:
                            self.error = ERRORS( self.line ).ERROR0( self.master )

                        else:
                            pass

                    else:
                        if len( self.storage_data ) == 2:
                            pass
                        else:
                            self.error = ERRORS( self.line ).ERROR0( self.master )

                else:
                    pass
        else:pass

        return  self.storage_data, self.storage_operators, self.error

    def HUNTER_OPERATORS(self, string: str):
        """
        :param string:
        :return:
        """
        self.error      = None
        self.active_op  = False

        for i, str_ in enumerate( string ):
            if str_ in ['<', '>', '!']:
                j, k = i - 1, i + 1
                self.active_op = True
                try:
                    if string[k] in ['=']:
                        self._str_ = str_+'='
                        j, k = i -1 , i + 2
                        if string[j] in [' ']:
                            if string[k+1] in [' ']:  pass
                            else:
                                self.error = ERRORS(self.line).ERROR3(self.master, self._str_, string[k+1])
                                break
                        else:
                            self.error = ERRORS(self.line).ERROR3(self.master, string[j], self._str_)
                            break
                    else:
                        if str_ == '!':
                            self.error = ERRORS(self.line).ERROR0(self.master)
                            break

                        else:
                            if string[j] in [' ']:
                                if string[k] in [' ']:  pass
                                else:
                                    self.error = ERRORS(self.line).ERROR3(self.master, str_, string[k])
                                    break
                            else:
                                self.error = ERRORS(self.line).ERROR3(self.master, string[j], str_)
                                break
                except IndexError:
                    self.error = ERRORS(self.line).ERROR0(self.master)
                    break
            elif str_ in ['?']:
                j, k = i-1, i + 1

                try:
                    if string[j] in [' ']:
                        if string[k] in [' ']:  pass
                        else:
                            self.error = ERRORS(self.line).ERROR3(self.master, str_, string[k])
                            break
                    else:
                        self.error = ERRORS(self.line).ERROR3(self.master, string[j], str_)
                        break
                except IndexError:
                    self.error = ERRORS(self.line).ERROR0(self.master)
                    break
            elif str_ in ['=']:
                if self.active_op == True:  self.active_op = False
                else:
                    self.active_op  = True
                    j, k = i -1 , i + 1
                    try:
                        if string[k] in ['=']:
                            self._str_ = '=='
                            if string[j] in [' ']:
                                if string[k+1] in [' ']:  pass
                                else:
                                    self.error = ERRORS(self.line).ERROR3(self.master, self._str_, string[k+1])
                                    break
                            else:
                                self.error = ERRORS(self.line).ERROR3(self.master, string[j], self._str_)
                                break
                        else:
                            self.error = ERRORS(self.line).ERROR0(self.master)
                            break
                    except:
                        self.error = ERRORS(self.line).ERROR0(self.master)
                        break
            else:  pass

        return self.error

class ERRORS:
    def __init__(self, line: int):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors() + '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error + self.reset

    def ERROR1(self, string: str, char1: str, char2: str):
        error = '{}you cannot associate {}<< {} >> {}and {}<< {} >>. {}line: {}{}'.format(self.white, self.green, char1, self.white,
                                                                            self.red, char2, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error+self.reset

    def ERROR2(self, string: str, char1: str, char2: str, pos = 'after'):
        error = '{}due to {}<< {} >> {}{} {}<< {} >>. {}line: {}{}'.format(self.white, self.green, char1, self.red, pos, self.magenta, char2,
                                                                    self.white, self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error+self.reset

    def ERROR3(self, string: str, char1: str, char2: str):
        error = '{}due to {}undefined {}space between {}<< {} >> {}and {}<< {} >>. {}line: {}{}'.format(self.white, self.green, self.white,
                                      self.red, char2, self.white, self.magenta, char1, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error+self.reset

    def ERROR4(self, string: str, char: str):
        error = '{}due to {}<< {} >> {}at the end. {}line: {}{}'.format(self.white, self.green, char, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error+self.reset

    def ERROR5(self, string: str, op: list):
        error = '{}due to {}too much operators {}<< {} >> . {}line: {}{}'.format(self.white, self.red, self.magenta, op,  self.white,
                                                                                self.yellow, self.line)
        self.error = fe.FileErrors('SyntaxError').Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error+self.reset