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
[not]    : checking if not Obj1
[not in] : checking if Obj1 is not in Obj2
[in]     : checking if Obj1 in Obj2
"""
from CythonModules.Windows.LEXER.seg                import num
from CythonModules.Windows.LEXER.seg                import segError
from script                                         import control_string   as CS
from CythonModules.Windows.LEXER.logical            import logicalError     as LE

cdef class LOGICAL_OPERATORS:
    cdef public:
        str master 
        dict data_base
        unsigned long long int line 
    cdef:
        str error 
        list logical_operators1, logical_operators2
        list bool_operators, bool_operators_
        list arithmetic_operators, accpeted_chars, accpeted_chars_
        list right_accepted, upper, lower
        unsigned long long int number
    cdef:
        unsigned long long int left, rigth,len_str_bool
        bint str_id, str_id_, key_bracket, activation_operators
        str string_in_true, string, chaine, _string_, new_string
        str string_logical, new_string_left, new_string_right_
        str new_string_right, string_clear, new_string_left_
        dict active_key
        list storage_operators, storage_data,logical_op
        list initialize, var_attribute

    def __cinit__(self, master, data_base, line):
        self.master                 = master
        self.long_chaine            = master
        self.data_base              = data_base
        self.line                   = line
        self.bool_operators         = ['or', 'and', 'only']
        self.bool_operators_        = ['||', '&&', '|&|']
        self.logical_operators1     = ['not', 'in']
        self.logical_operators2     = ['==', '!=', '>=', '<=', '<', '>', '?']
        self.arithmetic_operators   = ['+', '-', '*', '/', '^', '%']
        self.lower                  = CS.STRING_ANALYSE( self.data_base, self.line ).LOWER_CASE()
        self.upper                  = CS.STRING_ANALYSE( self.data_base, self.line ).UPPER_CASE()
        self.accpeted_chars         = self.lower+ self.upper + \
                                      ['_', '(', '[', '{', '.', '"', "'", ' '] + [str(x) for x in range(10)] + ['+', '-', '?']
        self.accpeted_chars_        = self.lower+ self.upper  + \
                                      ['_', ')', ']', '}', '.', '"', '"', ' '] + [str(x) for x in range(10)]
        self.right_accepted         = self.lower+ self.upper  + [str(x) for x in range(10)]+['_','.']
        self.number                 = int(num.NUMBER().number)
        self.left                   = 0
        self.rigth                  = 0
        self.initialize             = [None]
        self.active_key             = dict(s=False)
        self.error                  = ""
        self.str_id                 = False
        self.str_id_                = False
        self.key_bracket            = False
        self.string                 = ""
        self._string_               = ""
        self.new_string             = ""
        self.storage_operators      = []
        self.activation_operators   = False
        self.storage_data           = []
        self.chaine                 = ""
        self.string_logical         = ""
        self.logical_op             = []
        self.new_string_left        = ""
        self.new_string_right       = ""
        self.string_clear           = ""
        self.len_str_bool           = 0
        self.new_string_left_       = ""
        self.new_string_right_      = ""   

    cdef LOGICAL_OPAERATORS_INIT(self):
        cdef :
            unsigned long long int Len
            signed long long int i, k
            unsigned long long int l, r
            str str_, Open
            list list_of_chars = ['[', '(', '{', '"', "'"]
            unsigned long long int char1, char2, char3, char4, char5 
        
        self.master, self.error = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( self.master, name="cython" )

        if not self.error:
            for i, str_ in enumerate( self.master ):
                if str_ in list_of_chars:

                    if str_ == '(': char1 = str_.index('(')
                    else:  char1 = self.number
                    
                    if str_ == '[': char2 = str_.index('[')
                    else: char2 = self.number
                    
                    if str_ == '{': char3 = str_.index('{')
                    else: char3 = self.number
                    
                    if str_ == '"': char4 = str_.index('"')
                    else: char4 = self.number
                    
                    if str_ == "'": char5 = str_.index("'")
                    else: char5 = self.number

                    if self.initialize[0] is None:
                        if char1 < char2 and char1 < char3 and char1 < char4 and char1 < char5: self.initialize[0] = '('
                        if char2 < char1 and char2 < char3 and char2 < char4 and char2 < char5: self.initialize[0] = '['
                        if char3 < char1 and char3 < char2 and char3 < char4 and char3 < char5: self.initialize[0] = '{'
                        if char4 < char1 and char4 < char2 and char4 < char3 and char4 < char5: self.initialize[0] = '"'
                        if char5 < char1 and char5 < char2 and char5 < char3 and char5 < char4: self.initialize[0] = "'"
                        self.key_bracket = True
                    else:  pass
                else:
                    if str_ in [']', ')', '}'] and self.key_bracket is False:
                        Open = num.NUMBER().OPENING( str_ )
                        self.error = segError.ERROR(self.line).ERROR_TREATMENT2(self.long_chaine, str_)
                        break
                    else: pass
                
                if self.initialize[0] is not None:
                    if self.initialize[0] == '(': self.left, self.rigth = self.left + str_.count('('), self.rigth + str_.count(')')
                    if self.initialize[0] == '[': self.left, self.rigth = self.left + str_.count('['), self.rigth + str_.count(']')
                    if self.initialize[0] == '{': self.left, self.rigth = self.left + str_.count('{'), self.rigth + str_.count('}')
                    if self.initialize[0] == '"':
                        if self.str_id is False:
                            self.left, self.rigth = 1, 0
                            self.str_id = True
                        else:
                            if self.rigth <= 1: self.rigth = self.rigth + str_.count('"')
                            else:
                                self.error = segError.ERROR(self.line).ERROR_TREATMENT3(self.long_chaine)
                                break
                    if self.initialize[0] == "'":
                        if self.str_id_ is False:
                            self.left, self.rigth   = 1, 0
                            self.str_id_            = True
                        else:
                            if self.rigth <= 1: self.rigth = self.rigth + str_.count("'")
                            else:
                                self.error = segError.ERROR(self.line).ERROR_TREATMENT3(self.long_chaine)
                                break
                else:  pass

                if   self.left != self.rigth: self.active_key['s'] = True
                elif self.left == self.rigth and str_ in [')', ']', '}', '"', "'"]: self.active_key['s'] = False
                elif self.left == self.rigth and str_ not in ['(', '[', '{', '"', "'"]: self.active_key['s'] = 'dot'
                self._string_ += str_

                if self.active_key['s'] is True:  self.string += str_
                elif self.active_key['s'] is False:
                    self.string += str_

                    if i != len(self.master) - 1: pass
                    else:
                        self.string, self.error = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE(self.string, name="cython")
                        if not self.error:
                            if self.activation_operators is True:
                                if not self.error:  self.storage_data.append( self.string )
                                else:  break
                            else:  self.storage_data.append( self.string )
                        else:
                            self.error  = LE.ERRORS(self.line).ERROR0(self.master)
                            break

                    self.initialize[0]  = None
                    self.left           = 0
                    self.rigth          = 0
                    self.str_id         = False
                    self.key_bracket    = False
                else:
                    self.string  += str_
                    if i != len( self.master ) - 1:
                        if str_ not in [' ']:
                            self.string_logical += str_ 

                            if self.string_logical in self.logical_operators2:
                                self.len_str_bool                        = len( self.string_logical )

                                try:
                                    self.new_string_left                 = self.master[ : i + 1]
                                    self.new_string_left                 = self.string[ : - self.len_str_bool ]
                                    self.new_string_left, self.error     = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( 
                                                                                    self.new_string_left, name="cython" )
                                 
                                    self.new_string_right                = self.master[ i + 1 : ]
                                    self.new_string_right, self.error    = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( 
                                                                                self.new_string_right, name="cython" )
                                    self.string_clear , self.error       = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( 
                                                                                self.string, name="cython" )
                                except IndexError:
                                    if self.string_logical in [ '?' ]:  self.error = ""
                                    else:
                                        self.error = LE.ERRORS( self.line ).ERROR0( self.master )
                                        break

                                if not self.error:
                                    if len( self.string_logical ) == 1 and self.string_logical not in [ '?' ]:
                                        if self.new_string_right[ 0 ] in [ '=' ]:
                                            if not  self.error: pass
                                            else:  break
                                        else:
                                            try:
                                                if self.new_string_right[ 0 ] in self.accpeted_chars:
                                                    try:
                                                        if self.new_string_left[ -1 ] in self.accpeted_chars_:
                                                            if self.master [ i + 1 ] in [' ']:
                                                                self.storage_operators.append( self.string_logical )
                                                                self.string             = self.string[ : -self.len_str_bool]
                                                                self.string, self.error = CS.STRING_ANALYSE(self.data_base, 
                                                                                    self.line).DELETE_SPACE( self.string, name="cython" )

                                                                if not self.error:
                                                                    self.storage_data.append(self.string)
                                                                    self.activation_operators   = True
                                                                    self.string_logical         = ""
                                                                    self.string                 = ""
                                                                else:
                                                                    self.error = LE.ERRORS( self.line ).ERROR0( self.master )
                                                                    break
                                                            else:
                                                                self.error = LE.ERRORS(self.line).ERROR3(self.master,
                                                                                self.master[ i + 1 ], self.string_logical)
                                                                break
                                                        else:
                                                            self.error = LE.ERRORS(self.line).ERROR2(self.master,
                                                                    self.new_string_left[ -1 ],self.string_logical, pos='before')
                                                            break
                                                    except IndexError:
                                                        self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                                        break
                                                else:
                                                    self.error = LE.ERRORS(self.line).ERROR2(self.master,
                                                                            self.new_string_right[ 0 ],self.string_logical)
                                                    break
                                            except IndexError:
                                                self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                                break
                                    else:
                                        l, r   = len(self.master) - self.len_str_bool, i + 1
                                        try:
                                            if self.new_string_right[ 0 ] in self.accpeted_chars:
                                                if self.master[ i + 1] in [' ']:
                                                    try:
                                                        if self.new_string_left[ -1 ] in self.accpeted_chars_:

                                                            self.storage_operators.append( self.string_logical )
                                                            self.string = self.string[ : -self.len_str_bool]
                                                            self.string, self.error = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( 
                                                                                        self.string, name="cython" )
                                                            if not self.error:
                                                                self.storage_data.append( self.string )
                                                                self.activation_operators   = True
                                                                self.string_logical         = ""
                                                                self.string                 = ""
                                                            else:
                                                                self.error = LE.ERRORS( self.line ).ERROR0( self.master )
                                                                break
                                                        else:
                                                            self.error = LE.ERRORS(self.line).ERROR2(self.master,
                                                                self.new_string_left[ -1 ],self.string_logical, pos='before')
                                                            break
                                                    except IndexError:
                                                        if self.string_logical in [ '?' ]:
                                                            self.storage_operators.append( self.string_logical )
                                                            self.string                 = ""
                                                            self.string_logical         = ""
                                                            self.activation_operators   = True

                                                        else:
                                                            self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                                            break
                                                else:
                                                    self.error = LE.ERRORS(self.line).ERROR3(self.master,  self.master[ i + 1], 
                                                                                    self.string_logical)
                                                    break
                                            else:
                                                self.error = LE.ERRORS(self.line).ERROR2(self.master, self.new_string_right[ 0 ], self.string_logical)
                                                break
                                        except IndexError:
                                            self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                            break
                                else:
                                    self.error = LE.ERRORS( self.line ).ERROR0( self.master )
                                    break 
                            elif self.string_logical in self.logical_operators1:
                                self.len_str_bool                       = len( self.string_logical )

                                try:
                                    self.new_string_left                = self.master[ : i + 1]
                                    self.new_string_left                = self.string[ : - self.len_str_bool]
                                    self.new_string_left_               = self.new_string_left
                                    self.new_string_left, self.error    = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE(
                                                                            self.new_string_left, name="cython")

                                    self.new_string_right               = self.master[i + 1 : ]
                                    self.new_string_right_              = self.master[i + 1 : ]
                                    self.new_string_right, self.error   = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE(
                                                                            self.new_string_right, name="cython")
                                    self.string_clear, self.error       = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE(
                                                                            self.string, name="cython")
                                except IndexError:
                                    if self.string_logical in [ 'not' ]: self.error = ""
                                    else:
                                        self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                        break
                                
                                if not self.error:
                                    r = i + 1
                                    if self.master[ r ] in [' ']:
                                        try:
                                            if self.new_string_left_[ -1 ] in [' ']:
                                                if self.new_string_right[ 0 ] in self.accpeted_chars:
                                                    if self.new_string_left[ -1 ] in self.accpeted_chars_:
                                                        if self.string_logical in [ 'not' ]:
                                                            try:
                                                                if self.new_string_right[ :2 ] not in [ 'in' ]:
                                                                    self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                                                    break
                                                                else:
                                                                    if self.new_string_right[ 2 ] in [' ']:
                                                                        self.logical_op.append( self.string_logical )
                                                                        self.string_logical     = ""
                                                                        self.string             = self.new_string_left

                                                                    else:
                                                                        self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                                                        break
                                                            except IndexError:
                                                                self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                                                break
                                                        else:
                                                            self.logical_op.append( self.string_logical )
                                                            self.string = self.new_string_left

                                                            if len( self.logical_op ) == 1:
                                                                self.storage_operators.append(self.logical_op[ 0 ])
                                                                self.storage_data.append( self.string )
                                                                self.activation_operators   = True
                                                                self.string_logical         = ""
                                                                self.string                 = ""
                                                                self.logical_op             = []
                                                            else:
                                                                if self.logical_op[ 0 ] in [ 'not' ]:
                                                                    if self.logical_op[ 1 ] in [ 'in' ]:
                                                                        self.string_logical         = self.logical_op[ 0 ]+' '+self.logical_op[ 1 ]
                                                                        self.storage_operators.append( self.string_logical )
                                                                        self.storage_data.append( self.string )
                                                                        self.activation_operators   = True
                                                                        self.string_logical         = ""
                                                                        self.string                 = ""
                                                                        self.logical_op             = []
                                                                    else:
                                                                        self.error = LE.ERRORS( self.line ).ERROR1( self.master,
                                                                                    self.logical_op[ 0 ] , self.logical_op[ 1 ])
                                                                        break
                                                                else:
                                                                    self.error = LE.ERRORS(self.line).ERROR0( self.master )
                                                                    break
                                                    else:
                                                        self.error = LE.ERRORS(self.line).ERROR2(self.master,
                                                            self.new_string_left[ -1 ], self.string_logical, pos='before')
                                                        break
                                                else:
                                                    self.error = LE.ERRORS(self.line).ERROR2(self.master,
                                                                        self.new_string_right[ 0 ], self.string_logical)
                                                    break
                                            else:
                                                self.error = LE.ERRORS(self.line).ERROR3(self.master, self.string_logical, self.new_string_left_[ -1 ])
                                                break
                                        except IndexError:
                                            if self.string_logical in [ 'not' ]:
                                                try:
                                                    if self.new_string_right[ : 2 ] in [ 'in', 'is' ]:
                                                        if self.new_string_right[ 2 ] in [' ']:
                                                            self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                                            break
                                                        else:  pass
                                                    else:
                                                        if self.new_string_right[ 0 ] in self.accpeted_chars:
                                                            self.storage_operators.append( self.string_logical )
                                                            self.activation_operators   = True
                                                            self.string                 = ""
                                                            self.string_logical         = ""
                                                            self.logical_op             = []
                                                        else:
                                                            self.error = LE.ERRORS(self.line).ERROR2(self.master,
                                                                        self.new_string_right[0], self.string_logical)
                                                            break
                                                except IndexError:
                                                    if self.new_string_right[ 0 ] in self.accpeted_chars:
                                                        self.storage_operators.append( self.string_logical )
                                                        self.activation_operators   = True
                                                        self.string                 = ""
                                                        self.string_logical         = ""
                                                        self.logical_op             = []
                                                    else:
                                                        self.error = LE.ERRORS(self.line).ERROR2(self.master, self.new_string_right[0],
                                                                                self.string_logical)
                                                        break
                                            else:
                                                self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                                break
                                    else:
                                        if self.master[ r ] in self.right_accepted:  pass
                                        else:
                                            self.error = LE.ERRORS(self.line).ERROR3(self.master, self.string_logical, self.master[ r ])
                                            break
                                else:  break
                            else:  pass
                        else:  self.string_logical     = ""
                    else:
                        self.string_logical += str_
                        if self.string_logical in self.logical_operators1 + self.logical_operators2:
                            self.error = LE.ERRORS( self.line ).ERROR0( self.master )
                            break
                        else:
                            if str_ in self.accpeted_chars_:
                                self.string, self.error  = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( self.string, name="cython" )
                                if not self.error:
                                    if not self.error:  self.storage_data.append( self.string )
                                    else: break
                                else:
                                    self.error = LE.RRORS( self.line ).ERROR0( self.master )
                                    break
                            else:
                                self.error  = LE.ERRORS( self.line ).ERROR4( self.master, str_)
                                break
        else: pass 

        if not self.error:
            if len( self.storage_operators ) > 1:
                if len( self.storage_operators ) == 2:
                    if self.storage_operators[ 0 ] == '==' and self.storage_operators[ 1 ] == '?':
                        if len( self.storage_data ) == 2:  pass
                        else:  self.error = LE.ERRORS(self.line).ERROR0( self.master )

                    elif self.storage_operators[ 1 ] == '==' and self.storage_operators[ 0 ] == '?':
                        if len( self.storage_data ) == 2: pass
                        else:  self.error = LE.ERRORS( self.line ).ERROR0( self.master )
                    else:  self.error = LE.ERRORS(self.line).ERROR5(self.master, self.storage_operators)

                elif len( self.storage_operators ) == 3:
                    if self.storage_operators[ 0 ] == '?' and self.storage_operators[ 1 ] == '==' and \
                                                                            self.storage_operators[ 2 ] == '?':
                        if len(self.storage_data) == 2:  pass
                        else:  self.error = LE.ERRORS( self.line ).ERROR0( self.master )
                    else:  self.error = LE.ERRORS(self.line).ERROR5(self.master, self.storage_operators)
                else:  self.error = LE.ERRORS(self.line).ERROR5(self.master, self.storage_operators)
            else:
                if self.storage_operators:
                    if self.storage_operators[0] == '?':
                        if len( self.storage_data ) != 1:  self.error = LE.ERRORS( self.line ).ERROR0( self.master )
                        else:  pass
                    elif self.storage_operators[0] == 'not':
                        if len( self.storage_data ) != 1:  self.error = LE.ERRORS( self.line ).ERROR0( self.master )
                        else:  pass
                    else:
                        if len( self.storage_data ) == 2:  pass
                        else:  self.error = LE.ERRORS( self.line ).ERROR0( self.master )
                else:  pass
        else:pass

        return  self.storage_data, self.storage_operators, self.error


        