from script.LEXER                       import segmentation
from script                             import control_string
from script.LEXER.error.CythonWIN       import affectationError as AE
from CythonModules.Windows.LEXER.seg    import num
from CythonModules.Windows.LEXER.seg    import segError

cdef class ATTRIBUTES:
    cdef public:
        str master
        dict data_base
        unsigned long int line 
    cdef:
        unsigned long long int number
        unsigned long int left, rigth
        list initialize
        bint active_key
        str error, string, chaine, value
        bint str_id, str_id_, key_bracket
        list var_attribute
    
    def __cinit__(self, master, data_base, line):
        self.master         = master
        self.data_base      = data_base
        self.line           = line
        self.left           = 0
        self.rigth          = 0
        self.initialize     = [None]
        self.active_key     = False
        self.error          = ""
        self.string         = ""
        self.str_id         = False
        self.str_id_        = False
        self.key_bracket    = False
        self.chaine         = ""
        self.var_attribute  = []
        self.number         = int(num.NUMBER().number)
        self.value          = ""

    cdef CHAR_SELECTION(self):
        cdef :
            unsigned long long int i
            str str_
            list list_of_chars = ['[', '(', '{', '"', "'"]
            unsigned long long int char1, char2, char3, char4, char5 

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
                                    self.error = segError.ERROR(self.line).ERROR_TREATMENT3( self.master )
                                    break
                    else:  pass

                    if self.left != self.rigth: self.active_key = True
                    else:  self.active_key = False

                    if self.active_key is  True: self.string += str_
                    else:
                        self.string += str_
                        if i != len( self.master ) - 1: 
                            if str_ in  [ ',' ]:
                                self.value, self.error = control_string.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE( self.string[ : -1 ], name="cython" )
                                if not self.error :
                                    self.var_attribute.append(self.value)
                                    self.string = ""
                                else:
                                    self.error = AE.ERRORS(self.line).ERROR7( self.master )
                                    break
                            else: pass
                        else:
                            if str_ not in [ ',' ]:
                                self.value, self.error = control_string.STRING_ANALYSE(self.data_base, self.line).DELETE_SPACE(self.string, name="cython")
                                self.var_attribute.append( self.value )
                            else:
                                self.error = AE.ERRORS(self.line).ERROR6( self.master, ',' )
                                break

                        self.initialize[0]      = None
                        self.left               = 0
                        self.rigth              = 0
                        self.str_id             = False
                        self.str_id_            = False
                        self.key_bracket        = False
            else: pass
        except IndentationError: pass

        return self.var_attribute, self.error