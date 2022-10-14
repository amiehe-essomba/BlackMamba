from script                             import control_string   as CS
from CythonModules.Windows.LEXER.seg    import num
from CythonModules.Windows.LEXER.seg    import segError
from script.LEXER.error.CythonWIN       import float_or_funcError as FFE

cdef START_END(str end ):
        start = ""
        if   end in ['"', '"']:     start = end
        elif end in [']']:          start = '['
        elif end in ['}']:          start = '{'
        elif end in [')']:          start = '('

        return start, end

cdef class DOT:
    cdef public:
        str master
        dict data_base
        unsigned long int line 
    cdef:
        unsigned long long int number, count
        unsigned long int left, rigth
        list initialize
        bint active_key, if_key_is_true
        str error, string_in_true, string, chaine, string_inter
        bint str_id, str_id_, key_bracket
        list type_of_chaine, var_attribute, block_segmentation 
        unsigned int dot_count
        str string_inter_
        list accepted_chars
    
    def __cinit__(self, master, data_base, line):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.left           = 0
        self.rigth          = 0
        self.initialize     = [None]
        self.active_key     = False
        self.error          = ""
        self.string_in_true = ""
        self.string         = ""
        self.if_key_is_true = False
        self.str_id         = False
        self.str_id_        = False
        self.key_bracket    = False
        self.chaine         = ""
        self.var_attribute  = []
        self.type_of_chaine = ['.eq.', '.ne.', '.le.', '.ge.', '.lt.', '.gt.']
        self.number         = int(num.NUMBER().number)
        self.string_inter   = ""
        self.block_segmentation = []
        self.count          = 0
        self.dot_count      = 0
        self.string_inter_  = ""
        self.accepted_chars = CS.STRING_ANALYSE(self.data_base, self.line).UPPER_CASE() + \
                        CS.STRING_ANALYSE(self.data_base, self.line).LOWER_CASE()

    cdef CHAR_SELECTION(self, str _char_ = ""):
        cdef :
            unsigned long long int i, Len
            str str_, Open
            list list_of_chars = ['[', '(', '{', '"', "'"]
            unsigned long long int char1, char2, char3, char4, char5 
            str node = ""
            str end, start 
            dict func, final_value

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
                        if self.rigth <= 1:
                            self.rigth = self.rigth + str_.count('"')
                        else:
                            self.error = segError.ERROR(self.line).ERROR_TREATMENT3(self.long_chaine)
                            break
                if self.initialize[0] == "'":
                    if self.str_id_ is False:
                        self.left, self.rigth   = 1, 0
                        self.str_id_            = True
                    else:
                        if self.rigth <= 1:
                            self.rigth = self.rigth + str_.count("'")
                        else:
                            self.error = segError.ERROR(self.line).ERROR_TREATMENT3(self.long_chaine)
                            break
            else:  pass

            if self.left != self.rigth:  self.active_key = True
            elif self.left == self.rigth and str_ in [')', '}', ']', '"', "'"]: self.active_key = False
            elif self.left == self.rigth and str_ not in [')', '}', ']', '"', "'"]:
                self.active_key = False
                node = 'None'
            else: pass 

            if   self.active_key is True:
                node = ""
                self.string += str_
                self.string_inter += str_

                if self.block_segmentation:
                    if self.block_segmentation[ 0 ][ -1 ] == ')':
                        if self.string_inter[ 0 ] != '[':
                            self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                            break
                        else: pass
                    else:
                        self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                        break
                else:  pass
            elif self.active_key is False :
                if not node:

                    self.count += 1
                    self.string_inter += str_

                    if self.count <= 1:
                        self.string += str_
                        self.block_segmentation.append( self.string_inter )
                        self.string_inter = ''

                        if i != len( self.master ) - 1:
                            self.chaine = self.master[ i + 1 : ]
                            self.chaine, self.error = CS.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( self.chaine, name="cython" )
                            if self.error is not "": pass
                            else:
                                if str_ == ')':
                                    if self.chaine[ 0 ] not in ['.', '[']:
                                        self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                        break
                                    else: pass
                                elif str_ in [ ']', '"', "'", '}' ]:
                                    if self.name[ 0 ] not in [ '.' ]:
                                        self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                        break
                                    else: pass
                                else: pass
                        else:
                            if self.dot_count == 0:
                                if   str_ in [ ')' ] and self.string[ 0 ] not in [ '(' ]:
                                    func, self.error = DOT_DOT( self.string, self.data_base, self.line ).CHECK_SYNTAX()
                                    if self.error is None: self.var_attribute.append( func )
                                    else: break
                                elif str_ in [ ')' ] and self.string[ 0 ] in [ '(' ]    :
                                    self.string, self.error = CS.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( self.string, name="cython" )
                                    if self.var_attribute:
                                        func, self.error = DOT_DOT(self.string, self.data_base, self.line).CHECK_SYNTAX( )
                                        if not self.error:
                                            if self.var_attribute[ -1 ][ 'function_name' ] is not None: self.var_attribute.append( func )
                                            else:
                                                self.error = FFE.ERRORS(self.line).ERROR0(self.master)
                                                break
                                        else: break
                                    else: self.var_attribute.append( self.string )
                                else:
                                    self.string, self.error = CS.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( self.string, name="cython" )
                                    if self.var_attribute:
                                        func, self.error = DOT_DOT(self.string, self.data_base, self.line).CHECK_SYNTAX( True )
                                        if not self.error:
                                            if self.var_attribute:
                                                if self.var_attribute[ -1 ]['function_name'] is None:
                                                    if self.string[ -1 ] == ')': self.var_attribute.append(func)
                                                    else:
                                                        self.error = FFE.ERRORS( self.line ).ERROR0( self.master)
                                                        break
                                                else: self.var_attribute.append(func)
                                            else: self.var_attribute.append(func)
                                        else: break
                                    else: self.var_attribute.append( self.string )
                            else:
                                self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                break
                    else:
                        if self.count == 2:
                            self.string += str_
                            self.string_inter_ = self.block_segmentation[ 0 ]

                            if self.string_inter_[ 0 ] in ['('] and self.string_inter_[ -1 ] in [ ')' ]:
                                if self.string_inter[ 0 ] in [ '[' ] and self.string_inter[ -1 ] in [ ']' ]:
                                    if i == len( self.master ) - 1:
                                        if self.dot_count == 0:
                                            func, self.error = DOT_DOT(self.string, self.data_base, self.line).CHECK_SYNTAX(  True)####
                                            if not self.error:
                                                self.var_attribute.append( func )
                                                self.string         = ''
                                                self.string_inter   = ''
                                            else: break
                                        else:
                                            self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                            break
                                    else:
                                        self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                        break
                                else:
                                    self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                    break
                            else:
                                self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                break
                        else:
                            self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                            break

                    self.initialize[ 0 ]    = None
                    self.left               = 0
                    self.rigth              = 0
                    self.str_id             = False
                    self.str_id_            = False
                    self.key_bracket        = False
                    self.chaine             = ""
                else:
                    self.string += str_
                    if self.string:
                        self.count              = 0
                        self.block_segmentation = []
                    else: pass

                    if i < len( self.master ) - 1:
                        if str_ == '.':
                            try:
                                self.string, self.error  = CS.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( self.string[: - 1], name="cython" )

                                if  not self.error:
                                    if self.string[ -1 ] in [ ')' ]:
                                        if self.dot_count in [0, 1]: 
                                            self.chaine = self.master[ i + 1 : ]
                                            self.chaine, self.error = CS.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( self.chaine, name="cython" )
                                            if self.chaine[ 0 ] in self.accepted_chars:
                                                func, self.error = DOT_DOT( self.string, self.data_base, self.line).CHECK_SYNTAX()
                                                if not self.error:
                                                    self.var_attribute.append( func )
                                                    self.string = ''
                                                else: break
                                            else:
                                                self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                break 
                                        else:
                                            self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                            break
                                    elif self.string[ -1 ] in [ '"', "'", ']', '}' ]:
                                        start, end  = START_END( self.string[-1] )

                                        if self.string[ 0 ] == start :
                                            if self.dot_count in [0, 1]: 
                                                self.chaine = self.master[ i + 1 : ]
                                                self.chaine, self.error = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( 
                                                                                        self.chaine, name="cython" )
                                                if self.chaine[ 0 ] in self.accepted_chars:
                                                    func, self.error = DOT_DOT( self.string, self.data_base, self.line).CHECK_SYNTAX( False )
                                                    if not self.error:
                                                        self.var_attribute.append( func )
                                                        self.string = ''
                                                    else:break
                                                else:
                                                    self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                    break
                                            else:
                                                self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                break
                                        else:
                                            self.error = FFE.ERRORS( self.line ).ERROR0( self.string )
                                            break
                                    else:
                                        before = self.string
                                        after  = self.master[ i + 1 : ]
                                        after, self.error = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( after,
                                                                                 name="cython" )
                                        if not self.error:
                                            if before[ 0 ] in [ str(x) for x in range(10)]:
                                                if before[ -1 ] in [ str(x) for x in range(10)]:
                                                    if after[ 0 ] in [ str(x) for x in range(10)]:
                                                        if self.dot_count <= 2: 
                                                            self.dot_count += 1
                                                            self.string += '.'
                                                        else:
                                                            self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                            break

                                                    elif after[ 0 ] in ['e', 'E']:
                                                        try:
                                                            if after[ 1 ] in [str(x) for x in range(10)]:
                                                                if self.dot_count <= 2: 
                                                                    self.dot_count += 1
                                                                    self.string += '.'
                                                                else:
                                                                    self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                                    break
                                                            else:
                                                                self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                                break
                                                        except IndexError:
                                                            self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                            break
                                                    else:
                                                        self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                        break
                                                else:
                                                    self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                    break
                                            elif before[ 0 ] in self.accepted_chars:
                                                if after[ 0 ] in self.accepted_chars:
                                                    if self.dot_count == 0:
                                                        func, self.error = DOT_DOT( self.string, self.data_base,
                                                                                    self.line).CHECK_SYNTAX( False )
                                                        if not self.error:
                                                            self.var_attribute.append( func )
                                                            self.string = ''
                                                        else: break
                                                    else:
                                                        self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                        break
                                                else:
                                                    self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                    break
                                            else:
                                                self.error = self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                break
                                        else:
                                            if after[ 0 ] in [str(x) for x in range(10)]:
                                                if self.dot_count <= 2: 
                                                    if not self.var_attribute:
                                                        self.dot_count += 1
                                                        self.string += '.'
                                                    else:
                                                        self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                        break
                                                else:
                                                    self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                    break
                                            else:
                                                self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                break
                                else:
                                    if self.master[ i + 1 ] in [str(x) for x in range(10)]:
                                        if self.dot_count <= 2: 
                                            if not self.var_attribute:
                                                self.dot_count += 1
                                                self.string += '.'
                                            else:
                                                self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                                break
                                        else:
                                            self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                            break
                                    else:
                                        self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                        break
                            except IndexError:
                                self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                                break
                        else: pass
                    if self.var_attribute:
                        if type( self.var_attribute[ -1 ] ) == type( dict() ):
                            self.string, self.error = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( self.string, name="cython" )
                            func, self.error = DOT_DOT( self.string, self.data_base, self.line ).CHECK_SYNTAX( False )
                            if not self.error:
                                self.var_attribute.append( func )
                            else: break
                        else:
                            self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                            break
                    else:
                        self.string, self.error = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( self.string, name="cython" )
                        self.var_attribute.append( self.string )
        
        
        if not self.error:
            final_value, self.error = FINAL_TREATMENT(self.var_attribute, self.data_base, self.line ).FINAL( self.master )
        else: final_value = {}

        return final_value, self.error

cdef class DOT_DOT:
    cdef public:
        str master 
        dict data_base 
        unsigned long long int line 
   
    cdef:
        unsigned long long int index, right, left
        str string, error, new_string, chaine
        bint key 
        dict function_store

    def __cinit__(self, master, data_base, line ):
        self.master             = master
        self.data_base          = data_base
        self.line               = line 
        self.error              = ""
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
        self.new_string         = ""
        self.chaine             = ""

    cdef CHECK_SYNTAX(self, bint list_ = False):
        cdef:
            unsigned long long int i
            str str_

        self.master, self.error = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( self.master, name="cython" )
        
        if not self.error:
            try:
                if self.master[ 0 ] not in ['"', "'", '[', '{']:
                    for i, str_ in enumerate( self.master ):
                        if str_ in [ '(' ]:
                            self.key = True
                            break
                        else: self.string += str_

                    if list_ is True:
                        for i, str_ in enumerate( self.master ):
                            self.left, self.right = self.left + str_.count('(') , self.right + str_.count(')')
                            if self.left !=  self.right: pass
                            else:
                                if str_ in [ '[' ]:
                                    self.index = i
                                    break
                                else: pass

                        self.new_string = self.master[ self.index : ]
                        self.new_string, self.error         = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( 
                                                                                self.new_string, name="cython" )
                        if not self.error:
                            self.function_store['data_list']    = self.new_string
                            if self.key is True:
                                self.string, self.error = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( 
                                                                                    self.string, name="cython" )
                                if not self.error:
                                    self.function_store['function_name']    = self.string
                                    self.chaine, self.error                 = CS.STRING_ANALYSE(self.data_base, 
                                                            self.line).DELETE_SPACE( self.master[ : self.index], name="cython" )
                                    if not self.error: self.function_store['expression']       = self.chaine
                                    else: pass
                                else: self.error = FFE.ERRORS( self.line ).ERROR0( self.master )
                            else:
                                self.string, self.error = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( 
                                                            self.string[: self.index], name="cython" )
                                if not self.error:
                                    self.function_store['function_name']    = self.string
                                    self.chaine, self.error                 = CS.STRING_ANALYSE(self.data_base, 
                                                                                self.line).DELETE_SPACE(self.master[: self.index], name="cython")
                                    if not self.error :self.function_store['expression']       = self.chaine
                                    else: pass
                                else: self.error = FFE.ERRORS(self.line).ERROR0(self.master)
                        else:pass
                    else:
                        self.string, self.error = CS.STRING_ANALYSE(self.data_base, 
                                                        self.line).DELETE_SPACE( self.string, name="cython" )
                        if not self.error:
                            self.function_store['function_name']        = self.string
                            self.master, self.error                     = CS.STRING_ANALYSE(self.data_base, 
                                                                            self.line).l.DELETE_SPACE( self.master, name="cython" )
                            if not self.error :self.function_store['expression']           = self.master
                            else: pass
                        else:
                            self.function_store['expression'] = self.master
                            self.error = ""
                else: self.function_store[ 'expression' ] = self.master
            except IndexError: pass
        else: pass

        return self.function_store, self.error

cdef class FINAL_TREATMENT:
    cdef public :
        list master
        dict data_base 
        unsigned long long int line 
    
    cdef:
        str error, string
        list upper, lower, function_expression
        dict _return_, _key_
        unsigned long long int count, _count_c_

    def __cinit__(self, master, data_base, line):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.error              = ""
        self.string             = ""
        self.count              = 0
        self._count_c_          = 0
        self.upper              = CS.STRING_ANALYSE( self.data_base, self.line ).UPPER_CASE()
        self.lower              = CS.STRING_ANALYSE( self.data_base, self.line ).LOWER_CASE()
        self.accepted_chars     = self.upper+self.lower
        self._return_           = dict()
        self._key_              = dict(s=None)
        self.function_expression= []

    cdef FINAL(self, str main_string):
        cdef :
            char str_
            unsigned long int i
            str name 
        
        self._return_           = {
            'names'             : [],
            'numeric'           : None,
            'add_params'        : [],
            'expressions'       : [],
            'type'              : None
        }

        if len( self.master ) == 1:
            if type( self.master[ 0 ] ) == type( str() ):
                self.string = self.master[ 0 ]

                if   self.string[ 0 ] in [ '.' ] + [ str(x) for x in range(10) ]:
                    for i, str_ in enumerate( self.string ):
                        if not self.error :
                            if str_ in self.accepted_chars:
                                if str_ in [ 'e', 'E' ] :
                                    if self.count <= 1:
                                        self.count += 1
                                        if i < len( self.string ) - 1:  pass
                                        else:
                                            if self.count > 1:
                                                self.error = FFE.ERRORS(self.line).ERROR0(main_string)
                                                break
                                            else: pass
                                    else:
                                        self.error = FFE.ERRORS( self.line ).ERROR0( main_string )
                                        break
                                elif str_ in [ 'j' ]:
                                    if self._count_c_ <= 1:
                                        self._count_c_ += 1
                                        self._key_['s'] = 'complex'
                                        if i < len( self.string ) - 1:  pass
                                        else:
                                            if self._count_c_ > 1:
                                                self.error = FFE.ERRORS(self.line).ERROR0(main_string)
                                                break
                                            else: pass
                                    else:
                                        self.error = FFE.ERRORS( self.line ).ERROR0( main_string )
                                        break
                                else:
                                    self.error = FFE.ERRORS(self.line).ERROR0( main_string )
                                    break
                            else: pass
                        else: break

                    if not self.error:
                        if self._key_['s'] is None:
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
                self._return_[ 'expressions' ]      = self.master[ 0 ] [ 'expression' ]
                self._return_[ 'add_params' ]       = self.master[ 0 ] [ 'data_list' ]
                self._return_['type']               = 'function'

                name, self.error  =  CS.STRING_ANALYSE( self.data_base, self.line ).CHECK_NAME( self.master[ 0 ] [ 'function_name' ], 
                                                                                                        name="cython" )
                if not self.error: self._return_[ 'names' ]        = [ name ]
                else: self.error = FFE.ERRORS( self.line ).ERROR1( main_string )

        else:
            for i in range(len(self.master)):
                self.function_expression    = [ self.master[i][ 'expression' ] ]
                self._return_[ 'add_params' ].append( self.master[i][ 'data_list' ] )

                if self.master[i][ 'function_name' ] != None:
                    name, self.error = CS.STRING_ANALYSE( self.data_base, self.line ).CHECK_NAME( self.master[i][ 'function_name' ], name="cython" )
                    if not self.error:
                        if i == 0: self._return_[ 'type' ] = 'class'
                        else: pass
                    else: break
                else:
                    if len( self.master ) == 2:
                        self.name = None
                        if i == 0:
                            if self.master[i][ 'expression' ][ 0 ] in ['['] and self.master[i][ 'expression' ][ -1 ] in [']']:
                                self._return_[ 'type' ] = 'list'
                            elif self.master[i][ 'expression' ][ 0 ] in ['{'] and self.master[i][ 'expression' ][ -1 ] in ['}']:
                                self._return_[ 'type' ] = 'dictionnary'
                            elif self.master[i][ 'expression' ][ 0 ] in ['('] and self.master[i][ 'expression' ][ -1 ] in [')']:
                                self._return_[ 'type' ] = 'tuple'
                            elif self.master[i][ 'expression' ][ 0 ] in ['"'] and self.master[i][ 'expression' ][ -1 ] in ['"']:
                                self._return_[ 'type' ] = 'string'
                            elif self.function_expression[ 0 ] in ["'"] and self.function_expression[ -1 ] in ["'"]:
                                self._return_[ 'type' ] = 'string'
                        else: pass
                    else:
                        self.error = FFE.ERRORS( self.line ).ERROR0( main_string )
                        break

                if not self.error:
                    self._return_[ 'names' ].append( name )

                    if ')' == self.function_expression[ 0 ][ -1 ]:
                        self._return_[ 'expressions' ].append( self.master[i][ 'expression' ] )
                    else:
                        self.function_expression = self.function_expression[ 0 ]
                        self._return_[ 'expressions' ].append( self.function_expression )
                else:
                    self.error = FFE.ERRORS( self.line ).ERROR1( self.master[i][ 'function_name' ] )
                    break

        return self._return_, self.error
    
                                        