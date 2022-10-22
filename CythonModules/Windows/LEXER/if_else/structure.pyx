from script.LEXER                       import segmentation
from script                             import control_string
from script.LEXER.error.CythonWIN       import affectationError as AE
from CythonModules.Windows.LEXER.seg    import num
from CythonModules.Windows.LEXER.seg    import segError
from CythonModules.Windows.LEXER.particular   import particular_str_selection as PSS

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

    cdef STRUCTURE(self, signed long int ID):
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
                        self.string += str_
                        
                        if i < len( self.master ) - 1: pass    
                        else: 
                            if self.string: self.var_attribute.append( self.string )
                            else: pass
                    else: 
                        if self.sring: 
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
        
        return self.var_attribute, self.error
    
    cdef STRUC1(self, list data, signed long int ID):
        cdef :
            unsigned long i
            list struc = []
            list index = []
            list _return_ = []
            str string1, string2, s1, s2, str_, end, ss1, ss2
            bint key = False
            unsigned int dot = 0
            string1, string2, s1, s2, end,ss1, ss2 = "", "", "", "", "", "", ""


        for i in range(len(data)):
            if data[i] in ['if', 'else']:
                if not struc: 
                    if data[i] == 'if':
                        struc.append(data[i])
                        index.append(i)
                    else: break
                else:
                    if len(struc) <= 2:
                        if data[i] == 'else': 
                            struc.append(data[i])
                            index.append(i)
                        else: break
                    else: pass 
            elif data[i] == ':' :
                if dot == 0:
                    dot = i
                else:  break

        if not self.error:
            if struc:
                index = sorted(index, reverse=True)
                if len(struc) == 2:
                    if data[0] not in ['if', 'else']:
                        key = True
                        if data[-1] == ':'
                            for str_ in data[ : index[0]]:
                                s1 += str_
                            for str_ in data[index[1]+1 : -1]:
                                s2 += str_
                            for str_ in data[index[0] + 1: index[1]]:
                                ss1 += str_
                        
                            string1 = 't'*(ID-1) + struc[0] + ' ' + ss1 + ' ' + ':'
                            string2 = 't'*(ID-1) + struc[1] + ' ' + ':'
                            end     = 't'*(ID-1) + "end:"
                            s1, s2  = 't'*ID+s1, 't'*ID+s2
                            _return_.append((string1, True))
                            _return_.append([(s1, True), (string2, False), (s2, True), (end, False)])
                        else:
                            try:
                                if data[-1][-1] == ':'
                                    for str_ in data[ : index[0]]:
                                        s1 += str_
                                    for str_ in data[index[1]+1 : -1]:
                                        s2 += str_
                                    s2 += data[-1][:-1]

                                    for str_ in data[index[0] + 1: index[1]]:
                                        ss1 += str_
                        
                                    string1 = 't'*(ID-1) + struc[0] + ' ' + ss1 + ' ' + ':'
                                    string2 = 't'*(ID-1) + struc[1] + ' ' + ':'
                                    end     = 't'*(ID-1) + "end:"
                                    s1, s2  = 't'*ID+s1, 't'*ID+s2
                                    _return_.append((string1, True))
                                    _return_.append([(s1, True), (string2, False), (s2, True), (end, False)])
                                else: pass
                            except IndexError: pass
                    else: pass
                elif len(struc) == 1:
                    key = True
                    if data[0] != 'if':
                        if data[-1] == ':':
                            for str_ in data[ : index[0]]:
                                s1 += str_
                            for str_ in data[index[0] + 1: -1]:
                                ss1 += str_
                            end     = 't'*(ID-1) + "end:"
                            string1 = 't'*(ID-1) + struc[0] + ' ' + ss1 + ' ' + ':'
                            _return_.append((string1, True))
                            _return_.append([(s1, True), (end, False)])
                        elif data[-1][-1] == ':'
                            for str_ in data[ : index[0]]:
                                s1 += str_
                            for str_ in data[index[0] + 1: -1]:
                                ss1 += str_
                            ss1 += data[-1][:-1]
                            end     = 't'*(ID-1) + "end:"
                            string1 = 't'*(ID-1) + struc[0] + ' ' + ss1 + ' ' + ':'
                            _return_.append((string1, True))
                            _return_.append([(s1, True), (end, False)])
                        else: pass

                    else:
                        if dot == 0: pass
                        else: pass
                else: pass
            else: pass 
        else: pass
