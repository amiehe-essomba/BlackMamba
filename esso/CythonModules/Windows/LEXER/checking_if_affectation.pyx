from script.LEXER                           import segmentation
from script                                 import control_string
from script.LEXER.error.CythonWIN           import affectationError as AE
from CythonModules.Windows.LEXER.seg        import num
from CythonModules.Windows.LEXER.seg        import segError
from CythonModules.Windows.LEXER.particular import particular_str_selection as PSS
from CythonModules.Windows.LEXER.particular import data_transform 


cdef class AFFECTATION:
    cdef public:
        str master
        dict data_base
        unsigned long int line 
    cdef:
        unsigned long long int number
        unsigned long int left, rigth, count
        list initialize
        bint active_key, if_key_is_true
        str error, string_in_true, string, chaine
        bint str_id, str_id_, key_bracket
        list sub_symbols, operators, symbols, chars 
        dict tvar_attribute
    
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
        self.var_attribute  = {}
        self.number         = int(num.NUMBER().number)
        self.sub_symbols    = ['+', '-', '*', '/', '^', '%']
        self.operators      = ['=', '<', '>', '!', '?']
        self.symbols        = ['=', '+=', '-=', '*=', '/=', '^=', '%=']
        self.count          = 0
        self.chars          = []

    cdef DEEP_CHECKING(self, str _char_ = ""):
        cdef :

            unsigned long long int k, j_moins, j_plus
            signed long long int i, j
            str str_, Open
            list list_of_chars = ['[', '(', '{', '"', "'"]
            unsigned long long int char1, char2, char3, char4, char5 
            list final, _variable_, _attributes_ 

        try:
            self.master, self.error  = control_string.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( self.master, name="cython" )

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
                            self.error = segError.ERROR(self.line).ERROR_TREATMENT2(self.master, str_)
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
                                    self.error = segError.ERROR(self.line).ERROR_TREATMENT3(self.master)
                                    break
                        if self.initialize[0] == "'":
                            if self.str_id_ is False:
                                self.left, self.rigth   = 1, 0
                                self.str_id_            = True
                            else:
                                if self.rigth <= 1:
                                    self.rigth = self.rigth + str_.count("'")
                                else:
                                    self.error = segError.ERROR(self.line).ERROR_TREATMENT3(self.master)
                                    break
                    else:  pass

                    if self.left != self.rigth: self.active_key = True
                    else:  self.active_key = False

                    if self.active_key is True :  self.string += str_
                    else:
                        self.string +=  str_
                        if i < len(self.master) - 1:
                            if str_ in [ '=' ]:
                                j, k = i - 1, i + 1
                                try:
                                    if self.master[ j ] not in self.sub_symbols + self.operators:
                                        if self.master[ k ] != '=':
                                            if self.count < 1:
                                                self.chaine, self.error = control_string.STRING_ANALYSE(self.data_base, 
                                                                    self.line).DELETE_SPACE(self.string[: - 1], name="cython")
                                                if not self.error:
                                                    self.var_attribute['variable']      = self.chaine
                                                    self.var_attribute['operator']      = self.master[ i ]
                                                    self.count                          += 1
                                                    self.string                         = ""
                                                else:
                                                    self.error = AE.ERRORS(self.line).ERROR3(self.master)
                                                    break
                                            else:
                                                self.error = AE.ERRORS(self.line).ERROR2(self.master, self.master[i], self.var_attribute['operator'])
                                                break
                                        else: pass
                                    else:
                                        if self.master[ j ] in self.operators:  pass
                                        elif self.master[ j ] in self.sub_symbols:
                                            try:
                                                j_moins, j_plus = j - 1, k

                                                if self.master[ j_moins ] in [' ']:
                                                    if self.master[ j_plus ] in [' ']:
                                                        if self.count < 1:
                                                            self.chaine, self.error = control_string.STRING_ANALYSE(self.data_base, 
                                                                    self.line).DELETE_SPACE( self.string[ : -2], name="cython")
                                                            if not self.error:
                                                                self.var_attribute['variable']  = self.chaine
                                                                self.var_attribute['operator']  = self.master[j] + self.master[ i ]
                                                                self.count                      += 1
                                                                self.string                     = ""
                                                            else:
                                                                self.error = AE.ERRORS(self.line).ERROR3(self.master)
                                                                break
                                                        else:
                                                            self.error  = AE.ERRORS(self.line).ERROR2(self.master, self.master[j]+self.master[i],
                                                                            self.var_attribute['operator'])
                                                            break
                                                    else:
                                                        self.error = AE.ERRORS(self.line).ERROR1(self.master, self.master[ i ],self.master[ j_plus ])
                                                        break
                                                else:
                                                    self.error = AE.ERRORS(self.line).ERROR1(self.master,  self.master[ j_moins ],self.master[ j ])
                                                    break

                                            except IndexError:
                                                self.error = AE.ERRORS(self.line).ERROR0(self.master)
                                                break
                                except IndexError:
                                    self.error = AE.ERRORS(self.line).ERROR0(self.master)
                                    break
                            else: pass
                        else:
                            if str_ not in [ '=' ]:
                                self.chaine, self.error = control_string.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE(self.string, name="cython")
                                if not self.error: self.var_attribute['value'] = self.chaine
                                else: self.error = AE. ERRORS(self.line).ERROR4(self.master)
                            else: self.error = AE.ERRORS(self.line).ERROR5(self.master)
                        
                        self.initialize[ 0 ]    = None
                        self.left               = 0
                        self.rigth              = 0
                        self.str_id             = False
                        self.str_id_            = False
                        self.key_bracket        = False
            else: pass

            if not self.error:
                if 'operator' in list( self.var_attribute.keys() ):
                    self.chars.append( self.var_attribute['variable'] )
                    self.chars.append( self.var_attribute['value'] )
                
                    for i in range(len(self.chars)):
                        if not self.error:
                            final, self.error = PSS.SELECTION(self.chars[i], self.chars[i], self.data_base, self.line).CHAR_SELECTION( ',' )

                            if not self.error:
                                if i == 0:  _variable_ =  final[ : ] 
                                else: _attributes_   =  final[ : ]
                            else:  break
                        else:  break

                    if not self.error :
                        if len( self._attributes_ ) == len( self._variable_ ):
                            self.var_attribute['variable']      = _variable_
                            self.var_attribute['value']         = _attributes_
                        else:
                            if len( _attributes_ ) > len( _variable_ ): self.error = AE.ERRORS(self.line).ERROR8()
                            else:  self.error = AE.ERRORS(self.line).ERROR9()
                    else:  pass
                else:
                    final, self.error = PSS.SELECTION(self.var_attribute['value'], self.var_attribute['value'], self.data_base, 
                                                                                            self.line).CHAR_SELECTION( ',' )
              
                    if not self.error: self.var_attribute['value'] = final[ : ]
                    else:  pass
            else: pass
        except IndexError: pass

        if not self.error:  self.var_attribute, self.error = data_transform.DATA( self.var_attribute, self.master ).TRANSFORM()
        else: pass

        return self.var_attribute, self.error

