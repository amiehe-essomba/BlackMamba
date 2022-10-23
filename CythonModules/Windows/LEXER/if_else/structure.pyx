from script                                     import control_string   as CS
from script.LEXER.error.CythonWIN               import affectationError as AE
from CythonModules.Windows.LEXER.seg            import num
from CythonModules.Windows.LEXER.seg            import segError
from CythonModules.Windows.LEXER.particular     import particular_str_selection as PSS 
from CythonModules.Windows.LEXER.logical        import logicalError as LE


cdef class IF_ELSE:
    cdef public:
        str master, long_chaine
        dict data_base
        unsigned long int line 
    cdef:
        unsigned long long int number
        unsigned long int left, rigth
        list initialize
        bint active_key, if_key_is_true
        str error, string, chaine
        bint str_id, str_id_, key_bracket
        list  var_attribute
    
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
        self.string         = ""
        self.if_key_is_true = False
        self.str_id         = False
        self.str_id_        = False
        self.key_bracket    = False
        self.chaine         = ""
        self.var_attribute  = []
        self.number         = int(num.NUMBER().number)

    cpdef STRUCTURE(self, unsigned long int ID):
        cdef :
            unsigned long long int i, Len
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
                    if str_ not in [' ']:
                        if i < len( self.master ) - 1: self.string += str_    
                        else:
                            self.var_attribute.append( self.string )
                            self.var_attribute.append( str_ )
                    elif str_ == ':':
                        self.var_attribute.append( self.string )
                        self.var_attribute.append( str_ )
                        self.string = ""
                    else: 
                        if self.string: 
                            self.var_attribute.append( self.string )
                            self.var_attribute.append( str_ )
                        else: pass 
                        self.string = ""
                    
                    self.initialize[0]      = None
                    self.left               = 0
                    self.rigth              = 0
                    self.str_id             = False
                    self.str_id_            = False
                    self.key_bracket        = False

        else: pass 
        
        self.var_attribute, self.error = IF_ELSE(self.master, self.long_chaine, self.data_base, self.line).STRUC( self.var_attribute, ID )
        
        return self.var_attribute, self.error
    
    cdef STRUC(self, list data, signed long int ID):
        cdef :
            unsigned long int i
            list struc = []
            list index = []
            list _return_ = []
            str string1="", string2="", s1="", s2="", str_, end="", ss1="", ss2=""
            bint key = False
            unsigned int dot = 0

            functions   = ['if', 'unless', 'for', 'while', 'else']
            bad_Funcs   = ['class', 'def', 'switch', 'begin', 'until', 
                            'elif', 'case', 'default', 'except', 'finally',
                            'save', 'with', 'open', 'close', 'from', 'module', 
                            'load', 'as', 'func']

        for i in range(len(data)):
            if data[i] in functions:
                if not struc: 
                    if data[ i ] in functions[ : -1]:
                        struc.append(data[ i ])
                        index.append( i )
                    else: 
                        self.error = LE.ERRORS(self.line).ERROR0(self.master)
                        break
                else:
                    if struc[ 0 ] in ['if', 'unless']:
                        if len(struc) <= 2:
                            if data[ i ] == 'else': 
                                struc.append(data[ i ])
                                index.append( i )
                            else: 
                                self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                break
                        else: 
                            self.error = LE.ERRORS(self.line).ERROR0(self.master)
                            break 
                    else:
                        self.error = LE.ERRORS(self.line).ERROR0(self.master)
                        break
            elif data[ i ] == ':' :
                if dot == 0:  dot = i
                else:
                    self.error = LE.ERRORS(self.line).ERROR0(self.master)
                    break

        if not self.error:
            if data[ 0 ] not in bad_Funcs:
                if struc:
                    if data[ -1 ] == ':':
                        try:
                            if   len(struc) == 2:
                                if data[ 0 ] not in functions:
                                    key = True
                                    for str_ in data[ : index[ 0 ]]:
                                        s1 += str_
                                    for str_ in data[index[ 1 ] + 1 : -1]:
                                        s2 += str_
                                    for str_ in data[index[ 0 ] + 1: index[1]]:
                                        ss1 += str_
                                    s1, self.error = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( s1, name="cython" )
                                    if not self.error:
                                        s2, self.error = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( s2, name="cython" )
                                        if not self.error:
                                            string1 = 't'*(ID-1) + struc[0] + ' ' + ss1 + ' ' + ':'
                                            string2 = 't'*(ID-1) + struc[1] + ' ' + ':'
                                            end     = 't'*(ID-1) + "end:"
                                            s1, s2  = 't'*ID+s1, 't'*ID+s2
                                            _return_.append((string1, True))
                                            _return_.append([(s1, True), (string2, False), (s2, True), (end, False)])
                                        else: self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                    else: self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                else: self.error = LE.ERRORS(self.line).ERROR0(self.master)
                            elif len(struc) == 1:
                                if struc[ 0 ] in ['if', 'unless']:
                                    if data[ 0 ] not in functions[ : -1]:
                                        key = True
                                        for str_ in data[ : index[ 0 ]]:
                                            s1 += str_
                                        for str_ in data[index[ 0 ] + 1: -1]:
                                            ss1 += str_
                                        s1, self.error = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( s1, name="cython" )
                                        if not self.error:
                                            end     = 't'*(ID-1) + "end:"
                                            string1 = 't'*(ID-1) + struc[ 0 ] + ' ' + ss1 + ' ' + ':'
                                            s1      = 't'*ID+s1
                                            _return_.append((string1, True))
                                            _return_.append([(s1, True), (end, False)])
                                        else: self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                    else: self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                else: self.error = LE.ERRORS(self.line).ERROR0(self.master)
                            else: self.error = LE.ERRORS(self.line).ERROR0(self.master)
                        except IndexError : self.error = LE.ERRORS(self.line).ERROR0(self.master)
                    else:
                        if len(struc) == 1:
                            if dot != 0:
                                try:
                                    if struc[ 0 ] in functions[ : -1]:
                                        for str_ in data[1 : dot]:
                                            s11 += str_ 
                                        for str_ in data[dot + 1 : ]:
                                            s1 += str_ 
                                        
                                        s1, self.error = CS.STRING_ANALYSE(self.data_base, self.line ).DELETE_SPACE( s1, name="cython" )
                                        if not self.error:
                                            string1 = 't'*(ID-1) + struc[ 0 ] + ' ' + ss1 + ' ' + ':'
                                            end     = 't'*(ID-1) + "end:"
                                            s1      = 't'*ID+s1
                                            _return_.append((string1, True))
                                            _return_.append([(s1, True), (string2, False), (s2, True), (end, False)])
                                        else: self.error = LE.ERRORS(self.line).ERROR0(self.master)
                                except IndexError: self.error = LE.ERRORS(self.line).ERROR0(self.master)
                            else: self.error = LE.ERRORS(self.line).ERROR0(self.master)
                        else: self.error = LE.ERRORS(self.line).ERROR0(self.master)
                else: pass 
            else: pass
        else: pass

        if not _return_: return [self.master], self.error 
        else:            return _return_, self.error 



