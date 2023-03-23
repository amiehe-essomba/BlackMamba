from script                                     import control_string
from script.LEXER.FUNCTION                      import global_, return_
from script.LEXER                               import segmentation
from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from CythonModules.Windows                      import fileError    as fe

class FUNCTION_INIT:
    def __init__(self, master: str, data_base: dict, line: int):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.control        = control_string.STRING_ANALYSE(self.data_base, self.line)
        self.accepted_chars = self.control.LOWER_CASE()+self.control.UPPER_CASE()+['_']+[str(x) for x in range(10)]
        self.number         = segmentation.NUMBER()
        self.string_error   = segmentation.ERROR(self.line)

    def FUNCTION_INIT(self):

        self.error          = None
        self.function       = [ 'if', 'def', 'for', 'try', 'while', 'class', 'switch',
                               'global', 'return', 'pass', 'exit', 'break', 'continue',
                               'elif', 'else', 'case', 'default', 'finally', 'except', 'end',
                               'until', 'unless','next', 'lambda', 'begin', 'delete', 'print', '_int_',
                                '_float_', '_string_', '_complex_', '_list_', '_tuple_', '_dictionary_', '_boolean_',
                                '_sqrt_', '_length_', '_sum_', '_rang_', '__ansii__', '__show__', '__rand__',
                                '_get_line_', '_mean_', '__scan__', '_max_', '_min_', '_var_', '_std_', '__open__', '__maths__', '__prompt__']
        self.count          = [ 2, 3, 3, 3, 5, 5, 6, 6, 6, 4, 4, 5, 8, 4, 4, 4, 7, 7, 6, 3, 5, 6, 4, 6, 5, 6, 5, 5, 7, 8,
                                9, 6, 7, 12, 9, 6, 8, 5, 5, 9, 8, 8, 10, 6, 8, 5, 5, 5, 5, 8, len('__prompt__')]
        self.sub_function   = [ 'if', 'def', 'for', 'try', 'while', 'class', 'switch',
                               'global', 'return' 'unless', 'until', 'begin', 'delete', 'print', '_int_', '_float_',
                                '_string_', '_complex_', 'lambda' ]
        self.break_function = [ 'break', 'exit', 'pass', 'continue', 'next' ]
        self.anotherfunc    = [ 'elif', 'else', 'case', 'default', 'finally', 'except', 'end' ]
        self.lambda_        = [ 'lambda' ]

        self.string         = ''
        self.function_type  = []
        self.data           = []
        self.stop           = False
        self.str_id_        = False
        self.str_id         = False
        self.left           = 0
        self.rigth          = 0
        self.active_key     = None
        self.initialize     = [None]
        self.key_bracket    = None

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

                if str_ == "'":
                    char5 = str_.index("'")
                else:
                    char5 = int(self.number.number)

                if self.initialize[0] is None:

                    if char1 < char2 and char1 < char3 and char1 < char4 and char1 < char5:
                        self.initialize[0] = '('

                    if char2 < char1 and char2 < char3 and char2 < char4 and char2 < char5:
                        self.initialize[0] = '['

                    if char3 < char1 and char3 < char2 and char3 < char4 and char3 < char5:
                        self.initialize[0] = '{'

                    if char4 < char1 and char4 < char2 and char4 < char3 and char4 < char5:
                        self.initialize[0] = '"'

                    if char5 < char1 and char5 < char2 and char5 < char3 and char5 < char4:
                        self.initialize[0] = "'"

                    self.key_bracket = True

                else:  self.initialize = self.initialize
            else:
                if str_ in [']', ')', '}'] and self.key_bracket is None:
                    self.open = self.number.OPENING(str_)
                    self.error = self.string_error.ERROR_TREATMENT2(self.long_chaine, str_)
                    break
                else:  pass

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

                if self.initialize[0] == "'":
                    if self.str_id_ == False:
                        self.left, self.rigth = 1, 0
                        self.str_id_ = True
                    else:
                        if self.rigth <= 1:
                            self.rigth = self.rigth + str_.count("'")
                            self.left = self.left
                        else:
                            self.error = self.string_error.ERROR_TREATMENT3(self.long_chaine)
                            break
            else: pass

            if self.left != self.rigth:
                self.active_key = True

            elif self.left == self.rigth and str_ in ['}', ']', ')', "'", '"']:
                self.active_key = False

            elif self.left == self.rigth and str_ in ['}', ']', ')', "'", '"']:
                self.active_key = None

            if self.active_key is True:
                self.string += str_
            elif self.active_key is False:
                self.string += str_
                if i < len( self.master ) - 1: pass
                else:
                    self.data.append( self.string )

                self.initialize[ 0 ]    = None
                self.left               = 0
                self.rigth              = 0
                self.str_id             = False
                self.str_id_            = False
                self.key_bracket        = None
                self.active_key         = None

            else:
                if self.error is None:
                    if str_ in [' ']:
                        if self.string in self.function:
                            if not self.data:
                                if not self.function_type:
                                    if self.string in [ 'global' ]:
                                        self.function_type.append( self.string )
                                        self.string = ''

                                    elif self.string in [ 'return' ]:
                                        self.function_type.append( self.string )
                                        self.string = ''

                                    elif self.string in [ 'delete' ]:
                                        self.function_type.append( self.string )
                                        self.string = ''

                                    elif self.string in [ 'lambda' ]:
                                        self.function_type.append( self.string )
                                        self.string = ''

                                    elif self.string in [ 'pass' ]:
                                        self.function_type.append( self.string )
                                        self.string = ''

                                    elif self.string in [ 'print' ]:
                                        self.function_type.append( self.string )
                                        self.string = ''

                                    elif self.string in [ '_int_', '_float_', '_string_', '_complex_', '_length_',
                                                        '_list_', '_tuple_', '_dictionary_', '_boolean_', '_sqrt_',
                                                          '_sum_', '_rang_', '__ansii__', '__show__', '__rand__',
                                                          '_get_line_', '_mean_', '__scan__', '_max_', '_min_', '_var_', 
                                                          '_std_', '__open__', '__maths__', '__prompt__']:
                                        self.function_type.append( self.string )
                                        self.string = ''

                                    elif self.string in [ 'break' ]:
                                        self.function_type.append( self.string )
                                        self.string = ''

                                    elif self.string in [ 'exit' ]:
                                        self.function_type.append( self.string )
                                        self.string = ''

                                    elif self.string in [ 'continue' ]:
                                        self.function_type.append( self.string )
                                        self.string = ''

                                    elif self.string in [ 'next' ]:
                                        self.function_type.append( self.string )
                                        self.string = ''

                                    elif self.string in [ 'lambda' ]:
                                        pass

                                    elif self.string in self.anotherfunc:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break

                                    else:
                                        if self.master[ -1 ] in [ ':' ]:
                                            if self.string not in [ 'try', 'begin' ]:
                                                self.function_type.append( self.string )
                                                self.string = ''
                                            else:
                                                k = i + 1
                                                self.next = self.master[ k : - 1]
                                                self.string_test, self.error = self.control.DELETE_SPACE( self.next )
                                                if self.error is None:
                                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                                    break

                                                else:
                                                    self.function_type.append( self.string )
                                                    self.error = None
                                                    break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR1( self.master )
                                            break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                            else:
                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                break
                        else:
                            if self.function_type:
                                if self.function_type[ 0 ] in self.break_function + self.anotherfunc:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                                else: self.string += str_
                            else: self.string += str_
                    else:
                        self.string += str_
                        if i < len( self.master ) - 1:
                            try:
                                for j in range( len( self.count ) ):
                                    if self.string[: self.count[ j ] ] in self.function:
                                        if self.master[ i + 1 ] in [' ']: pass
                                        elif self.master[ i + 1] in self.accepted_chars: pass
                                        else:
                                            if self.master[ i + 1 ] in [ ':' ]:
                                                try:
                                                    if self.string in [ 'try', 'begin' ]:
                                                        self.function_type.append( self.string )
                                                        self.stop = True
                                                        break
                                                    else:
                                                        self.error = ERRORS( self.line ).ERROR3( self.master, self.string )
                                                        break
                                                except IndexError: pass
                                            else:
                                                self.error = ERRORS( self.line ).ERROR3( self.master, self.string[: self.count[ j ]] )
                                                break
                                    else: pass

                                if self.stop == True: break
                                else: pass

                            except IndexError: pass

                        else:
                            if self.string in self.sub_function+self.anotherfunc:
                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                break

                            elif self.string in self.break_function:
                                if not self.function_type:
                                    if not self.data:
                                        self.function_type.append( self. string )
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break

                            else:
                                if self.function_type:
                                    if  self.function_type[ 0 ] in [ 'global', 'return', 'delete', 'print', '_int_',
                                                                '_float_', '_string_', '_complex_', '_sqrt_', '_length_',
                                                                '_list_', '_tuple_', '_dictionary_', '_boolean_',
                                                                '_sum_', '_rang_', '__ansii__', '__show__', '__rand__',
                                                                '_get_line_', '_mean_', '__scan__','_max_', '_min_', '_var_', 
                                                                '_std_', '__open__', '__maths__', 'lambda', '__prompt__']:
                                        self.data.append( self.string )

                                    elif self.function_type[ 0 ] in self.break_function+self.anotherfunc:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break

                                    else:
                                        self.string     = self.string[ : -1]
                                        self.string, self.error = self.control.DELETE_SPACE( self.string )

                                        if self.error is None:
                                            if self.string not in self.function:
                                                self.data.append( self.string )
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                break
                                        else:
                                            if self.data: self.error = None
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                break
                                else:  self.data.append( self.string )
                else: break

        return  self.data, self.function_type, self.error

class ERRORS:
    def __init__(self, line):
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,self.cyan, string) + error
        return self.error+self.reset

    def ERROR1(self, string: str):
        error = '{}due to the fact that {}<< : >> {}was not defined at the {}end. {}line: {}{}'.format(self.white, 
                                                         self.green, self.white, self.red, self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error+self.reset

    def ERROR2(self, string: str, char: str):
        error = '{}due to bad char {}<< {} >>. {}line: {}{}'.format(self.white,  self.green, char, self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error+self.reset

    def ERROR3(self, string: str, key: str):
        error = '{}because of the function {}<< {} >>. {}line: {}{}'.format(self.white,  self.green, key, self.white, self.yellow, self.line)     
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error
        return self.error+self.reset

