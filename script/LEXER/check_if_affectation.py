from colorama import  Fore
from script import control_string
from script.LEXER import segmentation
from script.LEXER import var_name_checking
from script.LEXER import particular_str_selection

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX

class AFFECTATION:
    def __init__(self, master, long_chaine, data_base, line):
        self.master         = master
        self.long_chaine    = long_chaine
        self.data_base      = data_base
        self.line           = line
        self.symbols        = ['=', '+=', '-=', '*=', '/=', '^=', '%=']
        self.sub_symbols    = ['+', '-', '*', '/', '^', '%']
        self.operators      = ['=', '<', '>', '!', '?']
        self.str_control    = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.upper_case     = self.str_control.UPPER_CASE()
        self.lower_case     = self.str_control.LOWER_CASE()
        self.number         = segmentation.NUMBER()
        self.string_error   = segmentation.ERROR( self.line )

    def DEEP_CHECKING(self):

        self.left                   = 0                                                                                 # firt left bracket
        self.rigth                  = 0                                                                                 # last right bracket
        self.initialize             = [None]                                                                            # initialization bracket research
        self.active_key             = None                                                                              # when left braket was detected
        self.string                 = ''                                                                                # string
        self.string_in_true         = ''                                                                                # string used in True block
        self.storage_value          = []                                                                                # storing list
        self.error                  = None                                                                              # error
        self.count                  = 0
        self.chars                  = []
        self.var_attribute          = dict()
        self.if_key_is_true         = None                                                                              # if left and rigth bracket was found
        self.str_id_                = False
        self.str_id                 = False                                                                             # id string, used to compte ['"', "'"] when self.id it's False i start counting of left
                                                                                                                        #   .the left value takes 1 as a value and self.id takes True values and i start counting the rigth values
                                                                                                                        #   .however the max left and right is 1, it means that for this you cannot have more than 1 ['"' or "'"]
        self.key_bracket            = None                                                                              # key bracket it means that you cannot have right bracket before letf bracket
                                                                                                                        #   [, {, ( come before '), }, ] else self.key_bracket stays None and you get an error
        try:
            self.master , self.error        = self.str_control.DELETE_SPACE( self.master )                              # removing right and left space
            self.long_chaine, self.error    = self.str_control.DELETE_SPACE( self.long_chaine )                         # removing right and left space

            if self.error is None:

                for i, str_ in enumerate( self.long_chaine ):

                    if str_ in [ '[', '(', '{', '"', "'" ]:

                        if str_ == '(':
                            char1 = str_.index( '(' )
                        else:
                            char1 = int( self.number.number )

                        if  str_ == '[':
                            char2 = str_.index( '[' )
                        else:
                            char2 = int( self.number.number )

                        if  str_ == '{':
                            char3 = str_.index( '{' )
                        else:
                            char3 = int( self.number.number )

                        if  str_ == '"':
                            char4 = str_.index( '"' )
                        else:
                            char4 = int( self.number.number)

                        if  str_ == "'":
                            char5 = str_.index( "'" )
                        else:
                            char5 = int( self.number.number)

                        if self.initialize[ 0 ] is None:

                            if char1 < char2 and char1 < char3 and char1 < char4 and char1 < char5:
                                self.initialize[ 0 ] = '('

                            if char2 < char1 and char2 < char3 and char2 < char4 and char2 < char5:
                                self.initialize[ 0 ] = '['

                            if char3 < char1 and char3 < char2 and char3 < char4 and char3 < char5:
                                self.initialize[ 0 ] = '{'

                            if char4 < char1 and char4 < char2 and char4 < char3 and char4 < char5:
                                self.initialize[ 0 ] = '"'
                            if char5 < char1 and char5 < char2 and char5 < char3 and char5 < char4:
                                self.initialize[ 0 ] = "'"

                            self.key_bracket = True

                        else:
                            self.initialize = self.initialize

                    else:
                        if str_ in [']', ')', '}'] and self.key_bracket is None:
                            self.open   = self.number.OPENING( str_ )                                                   # if srtr_ = ( so, self.open = )
                            self.error =  self.string_error.ERROR_TREATMENT2( self.long_chaine, str_ )
                            break

                        else:
                            pass

                    if self.initialize [ 0 ] is not None :
                        if self.initialize[0] == '(' :
                            self.left, self.rigth = self.left + str_.count('('), self.rigth + str_.count(')')

                        if self.initialize[ 0 ] == '[':
                            self.left, self.rigth = self.left + str_.count('['), self.rigth + str_.count(']')

                        if self.initialize[ 0 ] == '{':
                            self.left, self.rigth = self.left + str_.count('{'), self.rigth + str_.count('}')

                        if self.initialize[ 0 ] == '"':
                            if self.str_id == False:
                                self.left, self.rigth = 1, 0
                                self.str_id = True

                            else:
                                if self.rigth <= 1:
                                    self.rigth  = self.rigth + str_.count('"')
                                    self.left   = self.left

                                else:
                                    self.error = self.string_error.ERROR_TREATMENT3( self.long_chaine )
                                    break

                        if self.initialize[ 0 ] == "'":
                            if self.str_id_ == False:
                                self.left, self.rigth = 1, 0
                                self.str_id_ = True

                            else:
                                if self.rigth <= 1:
                                    self.rigth  = self.rigth + str_.count( "'" )
                                    self.left   = self.left

                                else:
                                    self.error = self.string_error.ERROR_TREATMENT3( self.long_chaine )
                                    break
                    else:
                        pass

                    if self.left != self.rigth :                                                                        # condition to make self.active_key True
                        self.active_key = True

                    else:
                        self.active_key = False

                    if self.active_key == True :
                        self.string += str_

                    else:
                        self.string +=  str_

                        if i < len(self.long_chaine) - 1:
                            if str_ == '=':
                                j, k = i - 1, i + 1
                                try:
                                    if self.long_chaine[ j ] not in self.sub_symbols + self.operators:
                                        if self.long_chaine[ k ] != '=':
                                            if self.count < 1:
                                                self.variable, self.error = self.str_control.DELETE_SPACE(
                                                                                                    self.string[: - 1])
                                                if self.error is None:
                                                    self.var_attribute['variable']      = self.variable
                                                    self.var_attribute['operator']      = self.long_chaine[ i ]
                                                    self.count += 1
                                                    self.string                         = ''

                                                else:
                                                    self.error = ERRORS(self.line).ERROR3(self.long_chaine)
                                                    break
                                            else:
                                                self.op = self.long_chaine[ i ]
                                                self.error = ERRORS(self.line).ERROR2(self.long_chaine,
                                                                            self.op, self.var_attribute['operator'])
                                                break

                                        else:
                                            pass

                                    else:
                                        if self.long_chaine[ j ] in self.operators:  pass
                                        elif self.long_chaine[ j ] in self.sub_symbols:
                                            try:
                                                j_moins, j_plus = j - 1, k

                                                if self.long_chaine[ j_moins ] in [' ']:
                                                    if self.long_chaine[ j_plus ] in [' ']:
                                                        if self.count < 1:
                                                            self.variable, self.error = self.str_control.DELETE_SPACE(
                                                                self.string[: -2])
                                                            if self.error is None:
                                                                self.var_attribute['variable']  = self.variable
                                                                self.var_attribute['operator']  = self.long_chaine[j] + \
                                                                                                 self.long_chaine[ i ]
                                                                self.count += 1
                                                                self.string                     = ''

                                                            else:
                                                                self.error = ERRORS(self.line).ERROR3(self.long_chaine)
                                                                break

                                                        else:
                                                            self.op     = self.long_chaine[ j ] + self.long_chaine[ i ]
                                                            self.error  = ERRORS(self.line).ERROR2(self.long_chaine,
                                                                            self.op,self.var_attribute['operator'])
                                                            break

                                                    else:
                                                        self.error = ERRORS(self.line).ERROR1(self.long_chaine,
                                                                    self.long_chaine[ i ],self.long_chaine[ j_plus ])
                                                        break

                                                else:
                                                    self.error = ERRORS(self.line).ERROR1(self.long_chaine,
                                                                    self.long_chaine[ j_moins ],self.long_chaine[ j ])
                                                    break

                                            except IndexError:
                                                self.error = ERRORS(self.line).ERROR0(self.long_chaine)
                                                break

                                except IndexError:
                                    self.error = ERRORS(self.line).ERROR0(self.long_chaine)
                                    break
                            else: pass
                        else:
                            if str_ != '=':
                                self.value, self.error = self.str_control.DELETE_SPACE(self.string)
                                if self.error is None:
                                    self.var_attribute['value'] = self.value
                                else:
                                    self.error = ERRORS(self.line).ERROR4(self.long_chaine)
                            else: self.error = ERRORS(self.line).ERROR5(self.long_chaine)

                        self.initialize[ 0 ]    = None
                        self.left               = 0
                        self.rigth              = 0
                        self.str_id             = False
                        self.str_id_            = False
                        self.key_bracket        = None

            else: pass

            if self.error is None:

                self.item_list = list( self.var_attribute.keys() )

                if 'operator' in self.item_list:
                    self.chars.append( self.var_attribute['variable'] )
                    self.chars.append( self.var_attribute['value'] )
                    self._variable_     = None
                    self._attributes_   = None

                    for i, string in enumerate( self.chars ):

                        if self.error is None:
                            self.str_select = particular_str_selection.SELECTION(string, string,self.data_base, self.line)
                            self.value, self.error = self.str_select.CHAR_SELECTION( ',' )
                            if self.error is None:
                                if i == 0:
                                    self._variable_ = self.value[ : ]
                                else:
                                    self._attributes_   = self.value[ : ]

                            else:
                                self.error = self.error
                                break
                        else:
                            self.error = self.error
                            break

                    if self.error is None:
                        if len( self._attributes_ ) == len( self._variable_ ):
                            self.var_attribute['variable']      = self._variable_
                            self.var_attribute['value']         = self._attributes_

                        else:
                            if len( self._attributes_ ) > len( self._variable_ ):
                                self.error = ERRORS(self.line).ERROR8()

                            else:
                                self.error = ERRORS(self.line).ERROR9()

                    else:
                        self.error = self.error

                else:
                    string     = self.var_attribute['value']

                    self.str_select = particular_str_selection.SELECTION(string, string, self.data_base, self.line)
                    self.value, self.error = self.str_select.CHAR_SELECTION( ',' )

                    if self.error is None:
                        self.var_attribute['value'] = self.value

                    else:
                        self.error  = self.error

            else: self.error = self.error

        except IndexError:
            pass

        self.var_attribute = AFFECTATION( self.var_attribute, self.long_chaine, self.data_base,
                                                                        self.line ).DATA_TRANSFORMATION()
        return self.var_attribute, self.error

    def ATTRIBUTES(self, master_init: str):

        self.left                       = 0
        self.rigth                      = 0
        self.initialize                 = [None]
        self.active_key                 = None
        self.string                     = ''
        self.string_in_true             = ''
        self.error                      = None
        self.if_key_is_true             = None
        self.str_id                     = False
        self.key_bracket                = None
        self.var_attribute              = []

        try:
            self.master_init, self.error    = self.str_control.DELETE_SPACE(master_init)

            if self.error is None:

                for i, str_ in enumerate( self.master_init ):

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

                    else:
                        self.active_key = False

                    if self.active_key == True:
                        self.string += str_

                    else:
                        self.string += str_
                        if i != len( self.master_init ) - 1:
                            if str_ == ',':
                                self.value, self.error = self.str_control.DELETE_SPACE( self.string[:-1] )
                                if  self.error is None:
                                    self.var_attribute.append(self.value)
                                    self.string = ''

                                else:
                                    self.error = ERRORS(self.line).ERROR7(master_init)
                                    break

                            else:
                                pass
                        else:
                            if str_ != ',':
                                self.value, self.error = self.str_control.DELETE_SPACE(self.string)
                                self.var_attribute.append( self.value )
                            else:
                                self.error = ERRORS(self.line).ERROR6( master_init, ',' )
                                break

                        self.initialize[0]      = None
                        self.left               = 0
                        self.rigth              = 0
                        self.str_id             = False
                        self.key_bracket        = None

            else:
                pass

        except IndexError:
            pass

        return self.var_attribute, self.error

    def DATA_TRANSFORMATION(self):
        self._item_list_ = list( self.master.keys() )

        if 'operator' in self._item_list_:
            self.operator   = self.master[ 'operator' ]
            self.values     = self.master[ 'value' ]
            self.variables  = self.master[ 'variable' ]
            self._return_   = None

            if self.operator in [ '=' ]:
                self._return_ = self.master

            elif self.operator in [ '+=' ]:
                self.master[ 'operator' ] = '='
                for i, value in enumerate( self.values ):
                    self.values[ i ] = self.variables[ i ] + ' ' + '+' + ' ' + self.values[ i ]
                self.master[ 'value' ] = self.values
                self._return_ = self.master

            elif self.operator in [ '-=' ]:
                self.master[ 'operator' ] = '='
                for i, value in enumerate( self.values ):
                    self.values[ i ] = self.variables[ i ] + ' ' + '-' + ' ' + self.values[ i ]
                self.master[ 'value' ] = self.values
                self._return_ = self.master

            elif self.operator in [ '*=' ]:
                self.master[ 'operator' ] = '='
                for i, value in enumerate( self.values ):
                    self.values[ i ] = self.variables[ i ] + ' ' + '*' + ' ' + self.values[ i ]
                self.master[ 'value' ] = self.values
                self._return_ = self.master

            elif self.operator in [ '/=' ]:
                self.master[ 'operator' ] = '='
                for i, value in enumerate( self.values ):
                    self.values[ i ] = self.variables[ i ] + ' ' + '/' + ' ' + self.values[ i ]
                self.master[ 'value' ] = self.values
                self._return_ = self.master

            elif self.operator in [ '^=' ]:
                self.master[ 'operator' ] = '='
                for i, value in enumerate( self.values ):
                    self.values[ i ] = self.variables[ i ] + ' ' + '^' + ' ' + self.values[ i ]
                self.master[ 'value' ] = self.values
                self._return_ = self.master

            elif self.operator in [ '%=' ]:
                self.master[ 'operator' ] = '='
                for i, value in enumerate( self.values ):
                    self.values[ i ] = self.variables[ i ] + ' ' + '%' + ' ' + self.values[ i ]
                self.master[ 'value' ] = self.values
                self._return_ = self.master

        else:
            self._return_ = self.master

        return self._return_

class ERRORS:

    def __init__(self, line):
        self.line           = line

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR1(self, string: str, char1: str, char2: str):
        error = '{}due to {}undefined {}space between {}<< {} >> {}and {}<< {} >>, {}line: {}{}'.format(ke, ae, ke, ve,
                                                                            char1, ke, ne, char2, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR2(self, string: str, op1: str, op2: str):
        error = '{}due many {}operators, {}<< {} >> {}and {}<< {} >>. {}line: {}{}'.format(ke, ve, ne, op1, ke,
                                                                                            ie, op2, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR3(self, string: str):
        error = '{}due to the {}EMPTY {}name of variable. {}line: {}{}'.format(ne, ke, ne, we, ke, self.line)
        self.error = '{}{} : {}invalid syntax in {}<< {} >>, '.format(ne, 'NameError', ke, ae, string) + error

        return self.error

    def ERROR4(self, string: str):
        error = '{}due to the {}no value. {}line: {}{}'.format(ve, ve, we, ke, self.line)
        self.error = '{}{} : {}invalid syntax in {}<< {} >>, '.format(ve, 'ValueError', ke, ae, string) + error

        return self.error

    def ERROR5(self, string: str):
        error = '{}due to {}<< = >> {}at the end. {}line: {}{}'.format(ke, ne, ke, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR6(self, string: str, char: str=','):
        error = '{}due to {}<< {} >> {}at the end. {}line: {}{}'.format(ke, ne, char, ke, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR7(self, string: str, char: str=','):
        error = '{}due to {}no value {}before {}<< {} >>. {}line: {}{}'.format(ke, ve, ke, ne, char, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>, '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR8(self):
        error = '{}many values and less variables. {}line: {}{}'.format(ke, we, ke, self.line)
        self.error = '{}{} : '.format(ae, 'AttributeError') + error

        return self.error

    def ERROR9(self):
        error = '{}many variables and less values. {}line: {}{}'.format(ke, we, ke, self.line)
        self.error = '{}{} : '.format(ae, 'AttributeError') + error

        return self.error