from CythonModules.Windows.LEXER.seg                import segError
from CythonModules.Windows.LEXER.seg                import num
from script                                         import control_string       as CS
from CythonModules.Windows.LEXER                    import Dictionary           as DIC
from CythonModules.Windows.LEXER.arr                import func_check           as FC
from CythonModules.Windows.LEXER.arr                import bracket              as BR
from CythonModules.Windows.LEXER.arr                import double_scanner       as DS
from CythonModules.Windows.LEXER.arr                import scanner              as S
from CythonModules.Windows.LEXER                    import float_or_function    as FOF
from CythonModules.Windows.LEXER.arr                import arrError             as AE
from CythonModules.Windows.LEXER.arr                import sub_checking_arr_op  as LFO

cdef class ARITHMETIC_OPERATORS:
    cdef public:
        str master 
        unsigned long long int line  
        dict data_base 

    cdef:
        str error, long_chaine
        list bool_operators, bool_operators_ , logical_operators1, logical_operators2 
        list arithmetic_operators, accpeted_chars, accpeted_chars_, upper , lower

    cdef:
        unsigned long long int number, left, rigth
        list initialize,storage_operators, storage_data, store_operators
        bint if_key_is_true
        str string_in_true, string, chaine, _string_, new_string, string_num
        str new_left_string, new_right_string
        bint str_id, str_id_, key_bracket, numerical_num, activation_operators
        list type_of_chaine, var_attribute
        dict active_key, final_value

    def __cinit__(self, master, data_base, line):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.long_chaine            = master
        self.bool_operators         = ['or', 'and', 'only']
        self.bool_operators_        = ['||', '&&', '|&|']
        self.logical_operators1     = ['not', 'in']
        self.logical_operators2     = ['==', '!=', '>=', '<=', '<', '>', '?']
        self.arithmetic_operators   = ['+', '-', '*', '/', '^', '%']
        self.upper                  = CS.STRING_ANALYSE(self.data_base, self.line ).UPPER_CASE()
        self.lower                  = CS.STRING_ANALYSE(self.data_base, self.line ).LOWER_CASE()
        self.accpeted_chars         = self.lower + self.upper + ['_', '(', '[', '{', '.', '"', "'", ' '] + [str(x) for x in range(10)]
        self.accpeted_chars_        = self.lower + self.upper + ['_', ')', ']', '}', '.', '"', '"', ' '] + [str(x) for x in range(10)]
        self.left                   = 0
        self.rigth                  = 0
        self.initialize             = [None]
        self.active_key             = dict(s=False)
        self.error                  = ""
        self.if_key_is_true         = False
        self.str_id                 = False
        self.str_id_                = False
        self.key_bracket            = False
        self.number                 = int(num.NUMBER().number)
        self.string                 = ""
        self._string_               = ""
        self.new_string             = ""
        self.new_left_string        = ""
        self.new_right_string       = ""
        self.storage_operators      = []
        self.activation_operators   = False
        self.storage_data           = []
        self.numerical_num          = False
        self.string_num             = ''
        self.final_value            = {}
        self.chaine                 = ""
        
    cdef ARITHMETIC_OPAERATORS(self):
        cdef :
            unsigned long long int Len
            signed long long int i, k
            str str_, Open, __string__
            list list_of_chars = ['[', '(', '{', '"', "'"]
            unsigned long long int char1, char2, char3, char4, char5 
            list dict_value, op1, store_data
            dict _key_, s1, _op_ = {}, dict_store = {}
        
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

                    if i != len( self.master ) - 1:
                        self.string, self.error = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( self.string, name="cython" )
                        if not self.error : pass
                        else: self.error = ""
                    else:
                        self.new_string, self.error = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( self.string, name="cython" )
                        if not self.error :
                            dict_value, self.error  = DIC.DICTIONNARY( self.new_string, self.data_base, self.line ).ANALYSES( self.master )
                            if not self.error:
                                if len( dict_value ) == 1:
                                    __string__, _key_, self.error = BR.BRACKET(self.data_base, self.line).BRACKET_ANALYSES( self.string )
                                    if not self.error :
                                        if _key_['s'] in [ False, 'tuple' ]:
                                            self.string = __string__
                                            self.error = S.CANNER( self.new_string, self.data_base, self.line).SCANNER( self.new_string )
                                            if not self.error:
                                                try:
                                                    if self.new_string[ 0 ] in ['"', "'"]: pass
                                                    else: self.new_string, self.error = BR.BRACKET( self.data_base, self.line).CHECK_CHAR( self.new_string )
                                                except IndexError: pass

                                                if not self.error:
                                                    if self.numerical_num == False:
                                                        self.error = FC.FUNC( self.master, self.data_base,
                                                                                self.line).FUNC_CHECK( self.new_string )
                                                        if not self.error:
                                                            self.final_value, self.error =  FOF.DOT( self.new_string, self.data_base,
                                                                            self.line).DOT( _char_='.')

                                                            if not self.error: self.storage_data.append( self.final_value )
                                                            else: break
                                                        else: break
                                                    else:
                                                        s1, op1, self.error = DS.SCANNER( self.new_string,
                                                            self.data_base, self.line).DOUBLE_SCAN(self.master, self.string_num)
                                                        if not self.error:
                                                            if op1:
                                                                self.storage_data.append( s1 )
                                                                self.storage_operators.append( op1 )
                                                            else: self.storage_data.append( s1 )
                                                        else: break
                                                else: break
                                            else: break
                                        elif _key_['s'] is True:
                                            self.error = S.SCANNER( __string__, self.data_base, self.line ).SCANNER( self.new_string )

                                            if not self.error :
                                                store_data, store_operators, self.error = LFO.ARITHMETIC_OPERATORS(
                                                                __string__, self.data_base,  self.line).ARITHMETIC_OPAERATORS()
                                                if not self.error:
                                                    if store_operators:
                                                        if len( store_data ) > 1:
                                                            self.storage_data.append( store_data )
                                                            self.storage_operators.append( store_operators )
                                                        else:
                                                            if len( store_operators ) <= 1 :
                                                                self.storage_data.append( store_data[ 0 ] )
                                                                self.storage_operators.append( store_operators[ 0 ] )
                                                            else:
                                                                self.storage_data.append( store_data )
                                                                self.storage_operators.append( store_operators )
                                                    else: self.storage_data.append( store_data[ 0 ] )
                                                else: break
                                            else: break
                                    else: break
                                else:
                                    self.error = AE.ERRORS( self.line ).ERROR0( self.master )
                                    break
                            else: break
                        else: self.error = ""

                    self.initialize[0]      = None
                    self.left               = 0
                    self.rigth              = 0
                    self.str_id             = False
                    self.str_id_            = False
                    self.key_bracket        = False
                else:
                    if i == 0:
                        if   str_ in ['+', '-']             :
                            self.new_string                     = self.master[1 : ]
                            self.new_string, self.error         = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( self.new_string, name="cython" )

                            if not self.error:
                                if self.new_string[ 0 ] in self.accpeted_chars:
                                    self.storage_operators.append( str_ )
                                    self.string                 = ""
                                    self.activation_operators   = True
                                else: break
                            else:
                                self.error = AE.ERRORS(self.line).ERROR2(self.master, self.new_string[0], str_)
                                break
                        elif str_ in ['*', '^', '/', '%']   :
                            self.error = AE.ERRORS(self.line).ERROR1(self.master, str_)
                            break
                        else:
                            if i == len( self.master ) - 1 :
                                if str_ in self.upper+self.lower+[str(x) for x in range(10)]:
                                    self.final_value, self.error = FOF.DOT( str_, self.data_base,  self.line).DOT( _char_='.')
                                    if not self.error:  self.storage_data.append( self.final_value )
                                    else: break
                                else:
                                    self.error = AE.ERRORS(self.line).ERROR5(self.master, str_)
                                    break
                            else: self.string += str_
                    elif i != len( self.master ) - 1:
                        if str_ in ['+', '-', '*', '/', '^', '%']:
                            try:
                                self.new_string                 = self.string
                                self.new_string, self.error     = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( self.new_string, name="cython" )
                                self.new_left_string            = self.master[: i]
                                self.new_right_string           = self.master[i + 1 : ]

                                if not self.error :
                                    if self.new_left_string[ -1 ] in self.accpeted_chars_:
                                        if self.new_right_string[ 0 ] in self.accpeted_chars:
                                            self.storage_operators.append( str_ )

                                            dict_value, self.error = DIC.DICTIONNARY( self.string, self.data_base,
                                                                        self.line).ANALYSES( self.master )
                                            if not self.error:

                                                if len( dict_value ) == 1:
                                                    __string__, _key_, self.error = BR.BRACKET(self.data_base, self.line).BRACKET_ANALYSES( self.string )

                                                    if not self.error:
                                                        if _key_['s'] is False:
                                                            self.error = S.SCANNER(self.new_string, self.data_base, self.line).SCANNER( self.new_string )
                                                            if not self.error:
                                                                self.new_string, self.error = BR.BRACKET( self.data_base, self.line).CHECK_CHAR(self.new_string, )
                                                                
                                                                if not self.error:
                                                                    if self.new_string[ -1 ] in [ 'e', 'E' ]:
                                                                        if self.new_string[ 0 ] not in ['.']+[str(x) for x in range(10)]:
                                                                            if self.numerical_num is False:
                                                                                self.error = FC.FUNC( self.master, self.data_base, self.line).FUNC_CHECK(
                                                                                                        self.new_string, end = False)
                                                                                if not self.error:
                                                                                    self.final_value, self.error = FOF.DOT(  self.new_string, self.data_base,
                                                                                                                self.line).DOT(_char_='.')
                                                                                    if not self.error:
                                                                                        self.storage_data.append( self.final_value )
                                                                                        self.string         = ''
                                                                                        self.new_string     = ''
                                                                                    else: break
                                                                                else: break
                                                                            else:
                                                                                _op_ = {'s' : None}
                                                                                if self.storage_operators: _op_['s'] = self.storage_operators[-1]
                                                                                else: pass
                                                                                
                                                                                s1, op1, self.error = DS.SCANNER( self.new_string, self.data_base, self.line
                                                                                                    ).DOUBLE_SCAN(self.master, self.string_num)

                                                                                if not self.error:
                                                                                    if op1:
                                                                                        self.storage_data.append( s1 )
                                                                                        self.storage_operators.append( op1 )
                                                                                        if _op_["s"] is None: pass
                                                                                        else: self.storage_operators.append( _op_['s'])
                                                                                    else: self.storage_data.append(self.new_string)

                                                                                    self.string         = ''
                                                                                    self.numerical_num  = False
                                                                                    self.string_num     = ''
                                                                                    self.new_string     = ''

                                                                                else: break
                                                                        else:
                                                                            if self.new_string[ 0 ] == '.':
                                                                                if len( self.new_string ) <= 2:
                                                                                    self.error = AE.ERRORS( self.line ).ERROR0(self.master )
                                                                                    break
                                                                                else:
                                                                                    if self.new_string[ 1 ] != '.': pass
                                                                                    else:
                                                                                        self.error = AE.ERRORS(self.line).ERROR0( self.master)
                                                                                        break
                                                                            else: pass

                                                                            if not self.error:
                                                                                if str_ in [ '+', '-' ]:
                                                                                    self.string         = self.new_string+str_
                                                                                    self.string_num     = self.new_string+str_
                                                                                    del self.storage_operators[ -1 ]
                                                                                    self.numerical_num  = True
                                                                                else:
                                                                                    self.error = AE.ERRORS( self.line ).ERROR0( self.master )
                                                                                    break
                                                                            else: break
                                                                    else:
                                                                        if self.numerical_num is False:
                                                                            self.error = FC.FUNC(self.master, self.data_base, self.line).FUNC_CHECK(
                                                                                                self.new_string, end=False )
                                                                            if not self.error:
                                                                                self.final_value, self.error = FOF.DOT( self.new_string, self.data_base, self.line
                                                                                                        ).DOT( _char_='.')
                                                                                if not self.error:
                                                                                    self.storage_data.append( self.final_value )
                                                                                    self.string         = ''
                                                                                    self.new_string     = ''
                                                                                else: break
                                                                            else: break
                                                                        else:
                                                                            _op_['s'] = None
                                                                            if self.storage_operators: _op_['s'] = self.storage_operators[ -1 ]
                                                                            else: pass
                                                                            
                                                                            s1, op1, self.error = DS.SCANNER( self.new_string, self.data_base, self.line
                                                                                            ).DOUBLE_SCAN( self.master, self.string_num )

                                                                            if not self.error:
                                                                                if op1:
                                                                                    self.storage_data.append( s1 )
                                                                                    self.storage_operators.append( op1 )
                                                                                    if _op_['s'] is None: pass
                                                                                    else: self.storage_operators.append( _op_['s'] )
                                                                                else:  self.storage_data.append( s1)
                                                                                self.string         = ''
                                                                                self.new_string     = ''
                                                                                self.string_num     = ''
                                                                                self.numerical_num  = False
                                                                            else: break
                                                                else: break
                                                            else: break
                                                        else:
                                                            _op_['s'] = self.storage_operators[ -1 ]
                                                            del self.storage_operators[ -1 ]

                                                            self.error = S.SCANNER(__string__, self.data_base, self.line).SCANNER( self.new_string )

                                                            if not self.error:
                                                                store_data, self.store_operators, self.error = LFO.ARITHMETIC_OPERATORS(
                                                                            __string__, self.data_base, self.line).ARITHMETIC_OPAERATORS() 
                                                                if not self.error:
                                                                    if self.store_operators:
                                                                        if len( store_data ) > 1:
                                                                            self.storage_data.append( store_data )
                                                                            self.storage_operators.append( self.store_operators )

                                                                        else:
                                                                            if len( self.store_operators ) <= 1:
                                                                                self.storage_data.append( store_data[ 0 ] )
                                                                                self.storage_operators.append( self.store_operators[ 0 ] )
                                                                            else:
                                                                                self.storage_data.append( store_data )
                                                                                self.storage_operators.append( self.store_operators )
                                                                    else: self.storage_data.append( store_data[0] )

                                                                    self.storage_operators.append( _op_['s'] )
                                                                else: break
                                                            else: break

                                                            self.string         = ''
                                                            self.numerical_num  = False
                                                            self.new_string     = ''
                                                    else: break
                                                else:
                                                    if self.numerical_num is False :
                                                        if self.new_string[ 0 ] not in ['[', '(', '"', "'"]:
                                                            self._main_     = dict_value[ 0 ]
                                                            __string__, self.error = CS.STRING_ANALYSE(self.data_base, 
                                                                                self.line).DELETE_SPACE( dict_value[ 0 ], name="cython" )
                                                            if not self.error:
                                                                dict_store          = {
                                                                    'values'        : None,
                                                                    'operators'     : None,
                                                                    'names'         : [],
                                                                    'type'          : 'dictionnary'
                                                                }

                                                                store_data, self.store_operators, self.error = LFO.ARITHMETIC_OPERATORS( __string__, 
                                                                        self.data_base, self.line  ).ARITHMETIC_OPAERATORS()
                                                                if not self.error:
                                                                    dict_store[ 'values' ]      = store_data
                                                                    dict_store[ 'operators' ]   = self.store_operators

                                                                    for k in range(len(dict_value[ 1 : ])):

                                                                        __string__, self.error = CS.STRING_ANALYSE(self.data_base, 
                                                                                    self.line).DELETE_SPACE( dict_value[ 1 : ][k], name="cython" )
                                                                        if not self.error :
                                                                            __string__, self.error = CS.STRING_ANALYSE(self.data_base, 
                                                                                    self.line).CHECK_NAME( __string__, name="cython" )

                                                                            if not self.error: dict_store[ 'names' ].append( __string__ )
                                                                            else: break
                                                                        else:
                                                                            self.error = AE.ERRORS( self.line ).ERROR0( self.master )
                                                                            break
                                                                    if not self.error: self.storage_data.append( dict_store )
                                                                    else: break
                                                                else: break
                                                            else:
                                                                self.error = AE.ERRORS( self.line ).ERROR0( self.master )
                                                                break
                                                        else:
                                                            self.error = AE.ERRORS( self.line ).ERROR0( self.new_string )
                                                            break
                                                    else:
                                                        self.error = AE.ERRORS( self.line ).ERROR0( self.master )
                                                        break

                                                    self.string         = ''
                                                    self.new_string     = ''
                                                    self.numerical_num  = False
                                            else: break

                                            self.activation_operators       = True
                                        else:
                                            self.error = AE.ERRORS(self.line).ERROR2(self.master, self.new_right_string[0],str_)                                                                
                                            break
                                    else:
                                        self.error = AE.ERRORS(self.line).ERROR2(self.master, self.new_left_string[ -1 ], str_, pos='before')
                                        break
                                else:
                                    self.error = AE.ERRORS( self.line ).ERROR0( self.master )
                                    break
                            except IndexError:
                                self.error = AE.ERRORS( self.line ).ERROR0( self.master )
                                break
                        else: self.string  += str_
                    else:
                        if str_ in self.accpeted_chars_:
                            self.string += str_
                            self.new_string, self.error = CS.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( self.string, name="cython" )

                            if not self.error:
                                self.error = S.SCANNER( self.new_string, self.data_base,  self.line).SCANNER( self.new_string )
                                if not self.error:
                                    self.new_string, self.error == BR.BRACKET( self.data_base, self.line).CHECK_CHAR(self.new_string)

                                    store_data, self.error = DIC.DICTIONNARY(self.new_string, self.data_base,
                                                                            self.line).ANALYSES( self.master )
                                    if not self.error:
                                        if len( store_data ) == 1:
                                            if not self.error:
                                                if self.numerical_num is True:
                                                    s1, op1, self.error = DS.SCANNER( self.new_string,
                                                        self.data_base, self.line).DOUBLE_SCAN(self.master, self.string_num)

                                                    if not self.error:
                                                        if op1:
                                                            self.storage_data.append( s1 )
                                                            self.storage_operators.append( op1 )
                                                        else: self.storage_data.append( s1 )
                                                    else: break
                                                else:
                                                    self.error = FC.FUNC( self.master, self.data_base, 
                                                                    self.line ).FUNC_CHECK( self.new_string, end=False)
                                                    if not self.error:
                                                        self.final_value, self.error = FOF.DOT( self.new_string, self.data_base, 
                                                                                                self.line).DOT( _char_='.' )

                                                        if not self.error: self.storage_data.append( self.final_value )
                                                        else: break
                                                    else: break
                                            else: break
                                        else:
                                            dict_store      = {
                                                'values'    : None,
                                                'names'     : [],
                                                'operators' : None,
                                                'type'      : 'dictionnary'
                                            }
                                       
                                            if self.numerical_num is True :
                                                self.error = AE.ERRORS( self.line ).ERROR0( self.master )
                                                break
                                            else:
                                                if self.new_string[ 0 ] not in ['[', '(', '"', "'"]:
                                                    s1, op1, self.error = LFO.ARITHMETIC_OPERATORS( store_data[ 0 ],
                                                            self.data_base, self.line).ARITHMETIC_OPAERATORS()

                                                    if not self.error:
                                                        self.dict_store[ 'values' ]     = s1
                                                        self.dict_store[ 'operators' ]  = op1

                                                        for k in range(len(store_data[1:])):
                                                            __string__, self.error = CS.STRING_ANALYSE(self.data_base, 
                                                                                    self.line).DELETE_SPACE( store_data[1:][k], name="cython" )
                                                            if not self.error:
                                                                __string__, self.error = CS.STRING_ANALYSE(self.data_base, 
                                                                                    self.line).CHECK_NAME( __string__, name="cython" )

                                                                if not self.error: dict_store[ 'names' ].append( __string__ )
                                                                else: break
                                                            else:
                                                                self.error = AE.ERRORS( self.line ).ERROR0( self.master )
                                                                break
                                                        if not self.error: self.storage_data.append( dict_store )
                                                        else: break
                                                    else: break
                                                else:
                                                    self.error = AE.ERRORS( self.line ).ERROR0( self.new_string )
                                                    break
                                    else: break
                                else: break
                            else:
                                self.error = AE.ERRORS( self.line ).ERROR0( self.master )
                                break
                        else:
                            self.error = AE.ERRORS(self.line).ERROR3(self.master, str_)
                            break
        else:  self.error = AE.ERRORS( self.line ).ERROR0( self.master )

        return  self.storage_data, self.storage_operators, self.error