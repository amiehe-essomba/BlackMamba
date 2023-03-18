from colorama                           import Fore
from script.LEXER                       import segmentation
from script                             import control_string
from script.LEXER.error.Cython          import affectationError as AE
from CythonModules.Linux.LEXER.seg      import segError



class SELECTION:
    def __init__(self, master: str, long_chaine: str , data_base: dict, line: int):
        self.master         = master
        self.long_chaine    = long_chaine
        self.data_base      = data_base
        self.line           = line
        self.number         = segmentation.NUMBER()
        self.string_error   = segError.ERROR(self.line)
        self.string_error_  = AE.ERRORS(self.line)
        self.str_control    = control_string.STRING_ANALYSE(self.data_base, self.line)

    def CHAR_SELECTION(self, _char_: str):

        self.left                       = 0
        self.rigth                      = 0
        self.initialize                 = [None]
        self.active_key                 = None
        self.string                     = ''
        self.string_in_true             = ''
        self.error                      = None
        self.if_key_is_true             = None
        self.str_id                     = False
        self.str_id_                    = False
        self.key_bracket                = None
        self.var_attribute              = []
        self.chaine                     = ''
        self.type_of_chaine             = ['.eq.', '.ne.', '.le.', '.ge.', '.lt.', '.gt.']

        if self.master:
            for i, str_ in enumerate( self.master ):
                if str_ in ['[', '(', '{', '"', "'"]:

                    if str_ == '(': char1 = str_.index('(')
                    else:  char1 = int(self.number.number)
                    
                    if str_ == '[': char2 = str_.index('[')
                    else: char2 = int(self.number.number)
                    
                    if str_ == '{': char3 = str_.index('{')
                    else: char3 = int(self.number.number)
                    
                    if str_ == '"': char4 = str_.index('"')
                    else: char4 = int(self.number.number)
                    
                    if str_ == "'": char5 = str_.index("'")
                    else: char5 = int(self.number.number)

                    if self.initialize[0] is None:

                        if char1 < char2 and char1 < char3 and char1 < char4 and char1 < char5: self.initialize[0] = '('
                        if char2 < char1 and char2 < char3 and char2 < char4 and char2 < char5: self.initialize[0] = '['
                        if char3 < char1 and char3 < char2 and char3 < char4 and char3 < char5: self.initialize[0] = '{'
                        if char4 < char1 and char4 < char2 and char4 < char3 and char4 < char5: self.initialize[0] = '"'
                        if char5 < char1 and char5 < char2 and char5 < char3 and char5 < char4: self.initialize[0] = "'"
                        self.key_bracket = True

                    else:  self.initialize = self.initialize

                else:
                    if str_ in [']', ')', '}'] and self.key_bracket is None:
                        self.open = self.number.OPENING(str_)
                        self.error = self.string_error.ERROR_TREATMENT2(self.long_chaine, str_)
                        break
                    else: pass

                if self.initialize[0] is not None:
                    if self.initialize[0] == '(': self.left, self.rigth = self.left + str_.count('('), self.rigth + str_.count(')')
                    if self.initialize[0] == '[': self.left, self.rigth = self.left + str_.count('['), self.rigth + str_.count(']')
                    if self.initialize[0] == '{': self.left, self.rigth = self.left + str_.count('{'), self.rigth + str_.count('}')
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
                            self.left, self.rigth   = 1, 0
                            self.str_id_            = True
                        else:
                            if self.rigth <= 1:
                                self.rigth = self.rigth + str_.count("'")
                                self.left = self.left
                            else:
                                self.error = self.string_error.ERROR_TREATMENT3(self.long_chaine)
                                break
                else:  pass

                if self.left != self.rigth: self.active_key = True
                else:  self.active_key = False

                if self.active_key == True:
                    self.string += str_
                    if i != len( self.master ) - 1:
                        pass
                    else:
                        self.error = self.string_error.ERROR0( self.master )
                        break

                else:
                    self.string += str_
                    if str_ in list( _char_ ):
                        self.chaine += str_
                        if _char_ in self.type_of_chaine:
                            if self.chaine[ 0 ] == '.':  pass
                            else:  self.chaine = ''
                        else:  pass
                    else:  pass
                    if i < len( self.master ) - 1:
                        if self.chaine == _char_:
                            try:
                                self.len = len( _char_ ) #
                                self.string, self.error  = self.str_control.DELETE_SPACE( self.string[: - self.len])
                                if  self.error is None:
                                    self.var_attribute.append( self.string )
                                    self.string = ''
                                    self.chaine = ''
                                else:
                                    if _char_ in ['-', " "]:
                                        self.var_attribute.append( self.string )
                                        self.string = ''
                                        self.error  = None
                                        self.chaine = ''
                                    else:
                                        self.error = self.string_error_.ERROR7( self.master, _char_)
                                        break

                            except IndexError:
                                if _char_ in ['-', " "]:
                                    self.var_attribute.append( self.string )
                                    self.string = ''
                                    self.error  = None
                                    self.chaine = ''
                                else:
                                    self.error = self.string_error_.ERROR7(self.master, _char_)
                                    break
                        else:  pass
                    else:
                        if self.chaine != _char_:
                            self.string, self.error = self.str_control.DELETE_SPACE(self.string)
                            self.var_attribute.append( self.string )
                            self.chaine = ''
                        else:
                            self.error = self.string_error_.ERROR6( self.master, _char_ )
                            break

                    self.initialize[0]      = None
                    self.left               = 0
                    self.rigth              = 0
                    self.str_id             = False
                    self.str_id_            = False
                    self.key_bracket        = None
        else: self.error = self.string_error.ERROR(self.long_chaine) 
        
        return self.var_attribute, self.error
