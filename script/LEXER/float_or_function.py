from script.LEXER                   import segmentation
from script                         import control_string
from script.LEXER.FUNCTION          import function, class_
from script.STDIN.WinSTDIN          import stdin
from script.STDIN.LinuxSTDIN        import bm_configure as bm
try:
    from CythonModules.Windows      import fileError as fe 
except ImportError:
    from CythonModules.Linux        import fileError as fe 


class DOT:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.long_chaine    = master

        self.number         = segmentation.NUMBER()
        self.string_error   = segmentation.ERROR( self.line )
        self.str_control    = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.accepted_chars = self.str_control.UPPER_CASE() + self.str_control.LOWER_CASE()

    def DOT(self, _char_: str):

        self.left                       = 0
        self.rigth                      = 0
        self.initialize                 = [None]
        self.active_key                 = None
        self.string                     = ''
        self.string_in_true             = ''
        self.string_inter               = ''
        self.error                      = None
        self.if_key_is_true             = None
        self.str_id                     = False
        self.str_id_                    = False
        self.key_bracket                = None
        self.var_attribute              = []
        self.count                      = 0
        self.dot_count                  = 0
        self.block_segmentation         = []
        self.final_value                = None

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

                else:
                    self.initialize = self.initialize

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

            elif self.left == self.rigth and str_ in [')', '}', ']', '"', "'"]:
                self.active_key = False

            elif self.left == self.rigth and str_ not in [')', '}', ']', '"', "'"]:
                self.active_key = None

            if   self.active_key == True:

                self.string += str_
                self.string_inter += str_

                if self.block_segmentation:
                    if self.block_segmentation[ 0 ][ -1 ] == ')':
                        if self.string_inter[ 0 ] != '[':
                            self.error = ERRORS( self.line ).ERROR0( self.master )
                            break
                        else: pass
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.master )
                        break
                else:  pass

            elif self.active_key == False:

                self.count += 1
                self.string_inter += str_

                if self.count <= 1:
                    self.string += str_
                    self.block_segmentation.append( self.string_inter )
                    self.string_inter = ''

                    if i != len( self.master ) - 1:

                        self.next = self.master[ i + 1 : ]
                        self.next, self.error = self.str_control.DELETE_SPACE( self.next )
                        if self.error is not  None: pass
                        else:
                            if str_ == ')':
                                if self.next[ 0 ] not in ['.', '[']:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                                else: pass

                            elif str_ in [ ']', '"', "'", '}' ]:
                                if self.next[ 0 ] not in [ '.' ]:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                                else: pass
                            else: pass

                    else:

                        if self.dot_count == 0:
                            if str_ in [ ')' ] and self.string[ 0 ] not in [ '(' ]:
                                self.func, self.error = DOT( self.string, self.data_base, self.line ).CHECK_SYNTAX()
                                if self.error is None:
                                    self.var_attribute.append( self.func )
                                else: break

                            elif str_ in [ ')' ] and self.string[ 0 ] in [ '(' ]:
                                self.string, self.error = self.str_control.DELETE_SPACE( self.string )
                                if self.var_attribute:
                                    self.func, self.error = DOT(self.string, self.data_base, self.line).CHECK_SYNTAX( )
                                    if self.error is None:
                                        end = self.var_attribute[ -1 ][ 'function_name' ]
                                        if end is not None:
                                            self.var_attribute.append( self.func )
                                        else:
                                            self.error = ERRORS(self.line).ERROR0(self.master)
                                            break
                                    else: break
                                else: self.var_attribute.append( self.string )

                            else:
                                self.string, self.error = self.str_control.DELETE_SPACE( self.string )
                                if self.var_attribute:
                                    self.func, self.error = DOT(self.string, self.data_base, self.line).CHECK_SYNTAX( True )
                                    if self.error is None:
                                        if self.var_attribute:
                                            end = self.var_attribute[ -1 ]
                                            end = end['function_name']

                                            if end is None:
                                                if self.string[ -1 ] == ')':
                                                    self.var_attribute.append(self.func)
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR0( self.master)
                                                    break
                                            else: self.var_attribute.append(self.func)
                                        else: self.var_attribute.append(self.func)

                                    else: break
                                else: self.var_attribute.append( self.string )

                        else:
                            self.error = ERRORS( self.line ).ERROR0( self.master )
                            break

                else:
                    if self.count == 2:
                        self.string += str_
                        self.string_inter_ = self.block_segmentation[ 0 ]

                        if self.string_inter_[ 0 ] in ['('] and self.string_inter_[ -1 ] in [ ')' ]:
                            if self.string_inter[ 0 ] in [ '[' ] and self.string_inter[ -1 ] in [ ']' ]:
                                if i == len( self.master ) - 1:
                                    if self.dot_count == 0:
                                        self.func, self.error = DOT(self.string, self.data_base, self.line).CHECK_SYNTAX(
                                            True)
                                        if self.error is None:
                                            self.var_attribute.append( self.func )
                                            self.string         = ''
                                            self.string_inter   = ''

                                        else: break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                            else:
                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                break
                        else:
                            self.error = ERRORS( self.line ).ERROR0( self.master )
                            break
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.master )
                        break

                self.initialize[ 0 ]    = None
                self.left               = 0
                self.rigth              = 0
                self.str_id             = False
                self.str_id_            = False
                self.key_bracket        = None

            else:
                self.string += str_
                if self.string:
                    self.count              = 0
                    self.block_segmentation = []
                else: pass

                if i < len( self.master ) - 1:
                    if str_ == '.':
                        try:
                            self.string, self.error  = self.str_control.DELETE_SPACE( self.string[: - 1] )

                            if  self.error is None:
                                if self.string[ -1 ] in [ ')' ]:
                                    if self.dot_count in [0, 1]: #########
                                        self.next = self.master[ i + 1 : ]
                                        self.next, self.error = self.str_control.DELETE_SPACE( self.next )
                                        if self.next[ 0 ] in self.accepted_chars:
                                            self.func, self.error = DOT( self.string, self.data_base, self.line).CHECK_SYNTAX()
                                            if self.error is None:
                                                self.var_attribute.append( self.func )
                                                self.string = ''
                                            else: break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                                elif self.string[ -1 ] in [ '"', "'", ']', '}' ]:
                                    start, end  = DOT( self.master, self.data_base, self.line).START_END( self.string[-1])

                                    if self.string[ 0 ] == start :
                                        if self.dot_count in[0, 1]: #####==0
                                            self.next = self.master[ i + 1 : ]
                                            self.next, self.error = self.str_control.DELETE_SPACE( self.next )
                                            if self.next[ 0 ] in self.accepted_chars:
                                                self.func, self.error = DOT( self.string, self.data_base,
                                                                             self.line).CHECK_SYNTAX( False )
                                                if self.error is None:
                                                    self.var_attribute.append( self.func )
                                                    self.string = ''
                                                else:break
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.string )
                                        break
                                    #here
                                else:
                                    self.before = self.string
                                    self.after  = self.master[ i + 1 : ]
                                    self.after, self.error = self.str_control.DELETE_SPACE( self.after )
                                    if self.error is None :
                                        if self.before[ 0 ] in [ str(x) for x in range(10)]:
                                            if self.before[ -1 ] in [ str(x) for x in range(10)]:
                                                if self.after[ 0 ] in [ str(x) for x in range(10)]:
                                                    if self.dot_count <= 2: ######1:
                                                        self.dot_count += 1
                                                        self.string += '.'
                                                    else:
                                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                                        break

                                                elif self.after[ 0 ] in ['e', 'E']:
                                                    try:
                                                        if self.after[ 1 ] in [str(x) for x in range(10)]:
                                                            if self.dot_count <= 2: #####1
                                                                self.dot_count += 1
                                                                self.string += '.'
                                                            else:
                                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                                break
                                                        else:
                                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                                            break
                                                    except IndexError:
                                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                                        break
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                                    break
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                break

                                        elif self.before[ 0 ] in self.accepted_chars:
                                            if self.after[ 0 ] in self.accepted_chars:
                                                if self.dot_count == 0:
                                                    self.func, self.error = DOT( self.string, self.data_base,
                                                                                 self.line).CHECK_SYNTAX( False )
                                                    if self.error is None:
                                                        self.var_attribute.append( self.func )
                                                        self.string = ''
                                                    else: break
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
                                        if self.after[ 0 ] in [str(x) for x in range(10)]:
                                            if self.dot_count <= 2: #####1
                                                if not self.var_attribute:
                                                    self.dot_count += 1
                                                    self.string += '.'
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                                    break
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.master )
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break

                            else:
                                if self.master[ i + 1 ] in [str(x) for x in range(10)]:
                                    if self.dot_count <= 2: ####1
                                        if not self.var_attribute:
                                            self.dot_count += 1
                                            self.string += '.'
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.master )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.master )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self.master )
                                    break
                        except IndexError:
                            self.error = ERRORS( self.line ).ERROR0( self.master )
                            break
                    else: pass

                else:
                    if self.var_attribute:
                        if type( self.var_attribute[ -1 ] ) == type( dict() ):
                            self.string, self.error = self.str_control.DELETE_SPACE( self.string )
                            self.func, self.error = DOT( self.string, self.data_base, self.line ).CHECK_SYNTAX( False )
                            if self.error is None:
                                self.var_attribute.append( self.func )
                            else: break
                        else:
                            self.error = ERRORS( self.line ).ERROR0( self.master )
                            break
                    else:
                        self.string, self.error = self.str_control.DELETE_SPACE( self.string )
                        self.var_attribute.append( self.string )

        if self.error is None:
            self.final_value, self.error = FINAL_TREATMENT(self.var_attribute, self.data_base,
                                                                           self.line ).FINAL( self.master )
        else:
            pass

        return self.final_value, self.error

    def CHECK_SYNTAX(self, list_:bool = False):

        self.master, err        = self.str_control.DELETE_SPACE( self.master )
        self.error              = None
        self.index              = 0
        self.left               = 0
        self.right              = 0
        self.string             = ''
        self.key                = False
        self.function_store     = {
            'function_name'     : None,
            'expression'        : None,
            'data_list'         : None
        }

        if self.master[ 0 ] not in ['"', "'", '[', '{']:
            for i, str_ in enumerate( self.master ):
                if str_ in [ '(' ]:
                    self.key = True
                    break
                else: self.string += str_

            if list_ == True:
                for i, str_ in enumerate( self.master ):
                    self.left, self.right = self.left + str_.count('(') , self.right + str_.count(')')
                    if self.left !=  self.right: pass
                    else:
                        if str_ in [ '[' ]:
                            self.index = i
                            break
                        else: pass

                self.new_string = self.master[ self.index : ]
                self.new_string, self.error                 = self.str_control.DELETE_SPACE( self.new_string )
                self.function_store['data_list']            = self.new_string

                if self.key == True:
                    self.string, self.error = self.str_control.DELETE_SPACE( self.string )
                    if self.error is None:

                        self.function_store['function_name']    = self.string
                        self.master_, self.error                = self.str_control.DELETE_SPACE( self.master[ : self.index] )
                        self.function_store['expression']       = self.master_

                    else: self.error = ERRORS( self.line ).ERROR0( self.master )

                else:
                    self.string, self.error = self.str_control.DELETE_SPACE( self.string[: self.index] )
                    if self.error is None:

                        self.function_store['function_name']    = self.string
                        self.master_, self.error                = self.str_control.DELETE_SPACE(self.master[: self.index])
                        self.function_store['expression']       = self.master_

                    else: self.error = ERRORS(self.line).ERROR0(self.master)

            else:
                self.string, self.error = self.str_control.DELETE_SPACE( self.string )
                if self.error is None:
                    self.function_store['function_name']        = self.string
                    self.master, self.error                     = self.str_control.DELETE_SPACE( self.master )
                    self.function_store['expression']           = self.master

                else:
                    self.function_store['expression'] = self.master
                    self.error = None
                    #self.error = ERRORS( self.line ).ERROR0( self.master )

        else: self.function_store[ 'expression' ] = self.master

        return self.function_store, self.error

    def START_END(self, end : str ):
        start = None
        if   end in ['"', '"']:     start = end
        elif end in [']']:          start = '['
        elif end in ['}']:          start = '{'
        elif end in [')']:          start = '('
        #else:                       start = ')'

        return start, end

class FINAL_TREATMENT:
    def __init__(self, master: list, data_base: dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base

        self.class_             = class_
        self.function           = function
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.accepted_chars     = self.control.UPPER_CASE()+self.control.LOWER_CASE()

    def FINAL(self, main_string: str):
        self.error              = None
        self._return_           = {
            'names'             : [],
            'numeric'           : None,
            'add_params'        : [],
            'expressions'       : [],
            'type'              : None
        }

        if len( self.master ) == 1:
            self.string             = self.master[ 0 ]

            if type( self.string ) == type( str() ):
               
                if   self.string[ 0 ] in [ '.' ] + [ str(x) for x in range(10) ]:
                    self.count      = 0
                    self._count_c_  = 0
                    self._key_      = None

                    for i, str_ in enumerate( self.string ):
                        if self.error is None:
                            if str_ in self.accepted_chars:
                                if str_ in [ 'e', 'E' ] :
                                    if self.count <= 1:
                                        self.count += 1
                                        if i < len( self.string ) - 1:
                                            pass
                                        else:
                                            if self.count > 1:
                                                self.error = ERRORS(self.line).ERROR0(main_string)
                                                break
                                            else: pass
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( main_string )
                                        break
                                elif str_ in [ 'j' ]:
                                    if self._count_c_ <= 1:
                                        self._count_c_ += 1
                                        self._key_ = 'complex'
                                        if i < len( self.string ) - 1:
                                            pass
                                        else:
                                            if self._count_c_ > 1:
                                                self.error = ERRORS(self.line).ERROR0(main_string)
                                                break
                                            else: pass
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( main_string )
                                        break

                                else:
                                    self.error = ERRORS(self.line).ERROR0( main_string )
                                    break
                            else: pass
                        else: break

                    if self.error is None:
                        if self._key_ is None:
                            self._return_[ 'numeric' ] = self.master
                            self._return_[ 'type' ] = 'numeric'
                        else:
                            self._return_['numeric'] = self.master
                            self._return_[ 'type' ] = 'complex'

                    else: pass
                elif self.string[ 0 ] in ['['] or self.string[ -1 ] in [ ']' ]:
                    self._return_['numeric']    = self.master
                    self._return_[ 'type' ]     = 'list'
                elif self.string[ 0 ] in ['(']:
                    self._return_['numeric']    = self.master
                    self._return_[ 'type' ]     = 'tuple'
                elif self.string[ 0 ] in ['{']:
                    self._return_['numeric']    = self.master
                    self._return_[ 'type' ]     = 'dictionnary'
                elif self.string[ 0 ] in ['"']:
                    self._return_['numeric']    = self.master
                    self._return_[ 'type' ]     = 'string'
                elif self.string[ 0 ] in ["'"]:
                    self._return_['numeric']    = self.master
                    self._return_[ 'type' ]     = 'string'
                elif self.string in [ 'True', 'False' ]:
                    self._return_[ 'numeric' ]  = self.master
                    self._return_[ 'type' ]     = 'boolean'
                elif self.string in [ 'None' ] :
                    self._return_[ 'numeric' ]  = self.master
                    self._return_[ 'type' ]     = 'none'
                else: self._return_[ 'numeric' ] = self.master

            else:
                self.data_list                      = self.master[ 0 ] [ 'data_list' ]
                self._return_[ 'expressions' ]      = self.master[ 0 ] [ 'expression' ]
                self._return_[ 'add_params' ]       = self.data_list
                self._return_['type']               = 'function'

                self.name, self.error               =  self.control.CHECK_NAME( self.master[ 0 ] [ 'function_name' ] )
                if self.error is None: self._return_[ 'names' ]        = [ self.name ]
                else: self.error = ERRORS( self.line ).ERROR1( main_string )

        else:
            for i, value in enumerate( self.master):
                self.function_expression    = [ value[ 'expression' ] ]
                self.data_list              = value[ 'data_list' ]
                self._return_[ 'add_params' ].append( value[ 'data_list' ] )

                if value[ 'function_name' ] != None:
                    self.name, self.error = self.control.CHECK_NAME( value[ 'function_name' ] )
                    if i == 0: self._return_[ 'type' ] = 'class'
                    else: pass

                else:
                    if len( self.master ) == 2:
                        self.name = None
                        if i == 0:
                            if value[ 'expression' ][ 0 ] in ['['] and value[ 'expression' ][ -1 ] in [']']:
                                self._return_[ 'type' ] = 'list'
                            elif value[ 'expression' ][ 0 ] in ['{'] and value[ 'expression' ][ -1 ] in ['}']:
                                self._return_[ 'type' ] = 'dictionnary'
                            elif value[ 'expression' ][ 0 ] in ['('] and value[ 'expression' ][ -1 ] in [')']:
                                self._return_[ 'type' ] = 'tuple'
                            elif value[ 'expression' ][ 0 ] in ['"'] and value[ 'expression' ][ -1 ] in ['"']:
                                self._return_[ 'type' ] = 'string'
                            elif self.function_expression[ 0 ] in ["'"] and self.function_expression[ -1 ] in ["'"]:
                                self._return_[ 'type' ] = 'string'
                        else: pass

                    else:
                        self.error = ERRORS( self.line ).ERROR0( main_string )
                        break

                if self.error is None:
                    self._return_[ 'names' ].append( self.name )

                    if ')' == self.function_expression[ 0 ][ -1 ]:
                        self._return_[ 'expressions' ].append( value[ 'expression' ] )
                    else:
                        self.function_expression = self.function_expression[ 0 ]
                        self._return_[ 'expressions' ].append( self.function_expression )
                else:
                    self.error = ERRORS( self.line ).ERROR1( value[ 'function_name' ] )
                    break

        return self._return_, self.error

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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors() +'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str):
        self._str_ = '{}type {}help( {}function_name{} ) {}or {}help( {}class_name{} ) ' \
                     '{} for more informations. '.format(self.white, self.magenta, self.yellow, self.magenta, self.green,
                                                         self.magenta, self.yellow, self.magenta, self.white)
        error = '{}in {}<< {} >> .{}line: {}{}.\n{}'.format(self.white, self.cyan, string, self.white, self.yellow, self.line, self._str_)
        self.error = fe.FileErrors( 'NameError' ).Errors() +'{}function / {}class {}name {}ERROR '.format(self.magenta,
                                                                                                    self.green, self.yellow, self.cyan) + error

        return self.error+self.reset
