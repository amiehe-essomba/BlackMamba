from script.LEXER                       import segmentation
from script                             import control_string
from script.LEXER.error.CythonWIN       import affectationError as AE
from CythonModules.Windows.LEXER.seg    import num
from CythonModules.Windows.LEXER.seg    import segError

cdef class SELECTION:
    cdef public:
        str master, long_chaine
        dict data_base
        unsigned long int line 
    cdef:
        unsigned long long int number
        unsigned long int left, rigth
        list initialize
        bint active_key, if_key_is_true
        str error, string_in_true, string, chaine
        bint str_id, str_id_, key_bracket
        list type_of_chaine, var_attribute
    
    def __cinit__(self, master, long_chaine, data_base, line):
        self.master         = master
        self.long_chaine    = long_chaine
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

    cdef CHAR_SELECTION(self, str _char_ = ""):
        cdef :
            unsigned long long int i, Len
            str str_, Open
            list list_of_chars = ['[', '(', '{', '"', "'"]
            unsigned long long int char1, char2, char3, char4, char5 

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

            if self.left != self.rigth: self.active_key = True
            else:  self.active_key = False

            if self.active_key is  True:
                self.string += str_
                if i != len( self.master ) - 1:  pass
                else:
                    self.error = segError.ERROR(self.line).ERROR0( self.master )
                    break
            else:
                self.string += str_
                if str_ in list( _char_ ):
                    self.chaine += str_
                    if _char_ in self.type_of_chaine:
                        if self.chaine[ 0 ] == '.':  pass
                        else:  self.chaine = ""
                    else:  pass
                else:  pass
                if i < len( self.master ) - 1:
                    if self.chaine == _char_:
                        try:
                            Len = len( _char_ ) #
                            self.string, self.error  = control_string.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( self.string[: - Len], name="cython")
                            if  not self.error:
                                self.var_attribute.append( self.string )
                                self.string = ""
                                self.chaine = ""
                            else:
                                if _char_ == '-':
                                    self.var_attribute.append( self.string )
                                    self.string = ""
                                    self.error  = ""
                                    self.chaine = ""
                                else:
                                    self.error = AE.ERRORS(self.line).ERROR7( self.master, _char_)
                                    break
                        except IndexError:
                            if _char_ == '-':
                                self.var_attribute.append( self.string )
                                self.string = ""
                                self.error  = ""
                                self.chaine = ""
                            else:
                                self.error = AE.ERRORS(self.line).ERROR7(self.master, _char_)
                                break
                    else:  pass
                else:
                    if self.chaine != _char_:
                        self.string, self.error = control_string.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE(self.string, name="cython")
                        self.var_attribute.append( self.string )
                        self.chaine = ""
                    else:
                        self.error = AE.ERRORS(self.line).ERROR6( self.master, _char_ )
                        break
                
                self.initialize[0]      = None
                self.left               = 0
                self.rigth              = 0
                self.str_id             = False
                self.str_id_            = False
                self.key_bracket        = False

        
        return self.var_attribute, self.error