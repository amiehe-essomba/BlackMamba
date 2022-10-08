import  sys
from script.STDIN.WinSTDIN              import stdin
from script.STDIN.LinuxSTDIN            import bm_configure as bm
from CythonModules.Windows.LEXER.seg    import segErrror as SE
from CythonModules.Windows.LEXER.seg    import num
from CythonModules.Windows.LEXER.seg    import characters
from script                             import control_string


cdef class SUB_STRING:
    cdef public:
        str first_char
        dict data_base
        unsigned long int line 
    
    cdef :
        str error, chars, upper_case, lower_case
        unsigned int space, string_line
        str string, normal_string, close, string_rebuild
        list storage
        unsigned long long int len_storage
        str c, input, length,  mainString , Open, new_string
        unsigned long int mainIndex, max_emtyLine, index, sub_length
        bint active_tab, key_bracket
        int left, right

    def __init__(self, first_char, data_base, line):

        # first char before moving here 
        self.first_char     = first_char 
        # data base with all variables                                                                                                                                                             # last char before moving here
        self.data_base      = data_base      
        # current line                                                                            
        self.line           = line     
        # line inside while loop
        self.string_line    = 0           
        # space                                                                               
        self.space          = 0 
        # error got during de precess  
        self.error          = ''  
        # upper case                             
        self.upper_case     = self.analyze.UPPER_CASE()            
        # lower cases
        self.lower_case     = self.analyze.LOWER_CASE()   
        # authorized chars                                                              
        self.chars          = characters.CHARS() + self.lower_case + self.upper_case    
        # concateante string
        self.string         = ''   
        # non-concatenate string                                                                                     
        self.normal_string  = ''  
        # the closing opening bracket                                                                                      
        self.close          = SUB_STRING(self.first_char, self.data_base, self.line).GET_CLOSE() 
        # a storing list                                                                         
        self.storage        = []                                                                             
        self.len_storage    = 0
        self.key_break      = False
        self.active_tab     = False
        self.string_rebuild = ''
        self.Open           = ''
        self.left           = 0
        self.right          = 0
        self.new_string     = ""

        #######################################################################
        self.c              = bm.fg.rbg(0, 255, 255)
        self.input          = '{}... {}'.format(self.c, bm.init.reset)
        self.length         = len(self.input)
        self.index          = self.length
        self.sub_length     = len('{}{}'.format(self.c, bm.init.reset))
        self.mainString     = ''
        self.mainIndex      = 0
        self.max_emtyLine   = 5
        #######################################################################

    cdef tuple SUB_STR(self, unsigned long int _id_, str color, list storage):
        
        cdef :
            int sub_char, idd, i
            str str_, _end_of_file_, _keyboard_

        ######################################################
        self.storage        = storage[ : ]                                                                              
        self.len_storage    = len( storage )
        ######################################################
        
        sys.stdout.write(bm.clear.line(2))
        sys.stdout.write(bm.move_cursor.LEFT(1000))
        sys.stdout.write(bm.string().syntax_highlight(name=self.input))
        sys.stdout.flush()

        while self.normal_string != self.first_char :
            try:
                sub_char  = bm.read().readchar()
                if sub_char  not in {10, 13}:
                    self.input      = self.input[: self.index] + chr(sub_char ) + self.input[self.index:]
                    self.mainString = self.mainString[: self.mainIndex] + chr(sub_char ) + self.mainString[  self.mainIndex:]
                    self.index      += 1
                    self.mainIndex  += 1
                else:
                    self.string_line += 1
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                  
                    if self.mainStringt:
                        ####################################################################
                        self.string, self.active_tab, self.error = control_string.STRING_ANALYSE( self.data_base, self.line 
                                ).BUILD_CON(string=self.mainString,  tabulation=_id_, name = 'cython')
                        if self.error is None:
                            self.normal_string = control_string.STRING_ANALYSE( self.data_base, self.line 
                                ).BUILD_NON_CON( string=self.clear_input, tabulation=_id_ )
                            self._ = stdin.STDIN(data_base=self.data_base, line=self.line).ENCODING(string=self.mainString)
                            if (self._ - _id_) == 0:
                                self.input = self.input[: self.length] + bm.words(string=self.mainString, color=color).final()
                            else:
                                self.error = SE.ERROR( self.string_line ).ERROR9()
                                break
                        else: break

                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        sys.stdout.write(bm.move_cursor.UP(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(self.input)
                        sys.stdout.flush()
                        sys.stdout.write(bm.move_cursor.DOWN(1))
                        sys.stdout.write(bm.clear.line(2))
                        sys.stdout.write(bm.move_cursor.LEFT(1000))

                        ######################################################################
                        if not self.error:
                            if self.active_tab is True :
                                self.string             = self.string[ _id_ : ]                                                   
                                self.normal_string      = self.normal_string[ _id_ : ]                                           
                                idd                     = 0

                                if '#' in self.string:
                                    idd                 = self.normal_string.index('#')
                                    self.normal_string  = self.normal_string[ : idd ]
                                    idd                 = self.string.index('#')
                                    self.string         = self.string[ : idd ]
                                else: pass

                                try:
                                    self.string_rebuild             = ""             
                                    # rebuilding string by using self.normal_string                                           
                                    self.string, self.error         = control_string.STRING_ANALYSE(self.data_base,
                                                        (self.line + self.string_line)).DELETE_SPACE(self.string, "cython")     
                                    # removing left and right space on string         
                                    self.normal_string, self.error  = control_string.STRING_ANALYSE(self.data_base,
                                                        (self.line + self.string_line)).DELETE_SPACE(self.normal_string, "cython")        
                                    if not self.error :
                                        ################################################################################################
                                        # when i got string from the < stdin > i make some verifications before storing it in          #
                                        # self.storage, if the conditions set here were not respected we got an error in function of   #
                                        # the mistakes, i used the <for> loop to check the syntax of each string defined  here         #
                                        # because of the < stdin > we have a lot of input strings .                                    #
                                        # the separtors used here to pass of a line to an another one is the comma < , >               #
                                        ################################################################################################
                                        for i, str_ in enumerate( self.normal_string ):
                                            ############################################################################################
                                            # in first of all i check here if the all the chars are accpeted by the code it means that #
                                            # i set a data_base where all accpeted chars are stored then if you a set non accept char  #
                                            # you will get an error.                                                                   #
                                            ############################################################################################

                                            if str_ in self.chars:
                                                self.string_rebuild += str_
                                                if len( self.normal_string ) == 1 :
                                                    if str_ in [ ',' ]:
                                                        self.error = SE.ERROR((self.line + self.string_line)).ERROR1(self.normal_string)
                                                        break
                                                    else:
                                                        if self.storage[-1][-1] in [',']:
                                                            if str_ == self.close:
                                                                self.error = SE.ERROR((self.line + self.string_line)).ERROR2()
                                                                break
                                                            else:
                                                                #this part need to be updated
                                                                self.storage.append( self.string_rebuild )
                                                                self.string_rebuild     = ''
                                                                self.space              = 0
                                                        else:
                                                            if len( self.storage ) > 1:
                                                                if str_ == self.close:
                                                                    self.storage.append(self.string_rebuild)
                                                                    self.key_break = True
                                                                    break
                                                                else:
                                                                    self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                    break
                                                            else:
                                                                if len(self.storage[0]) > 1:
                                                                    if str_ == self.close:
                                                                        self.storage.append(self.string_rebuild)
                                                                        self.key_break = True
                                                                        break
                                                                    else:
                                                                        self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                        break
                                                                else:
                                                                    self.Open   = num.NUMBER().OPENING( self.close )
                                                                    self.error = SE.ERROR((self.line + self.string_line)).ERROR4( self.Open, self.close )
                                                                    break
                                                else:
                                                    if self.normal_string[ 0 ]  not in  [',']   :
                                                        if i < len( self.normal_string ) - 1:
                                                            if str_ in [',']:
                                                                self.stest_string, self.error       = control_string.STRING_ANALYSE(self.data_base,
                                                                        (self.line + self.string_line)).DELETE_SPACE(  self.string_rebuild[: - 1], 'cython')

                                                                if self.error is None:
                                                                    if self.close in self.string_rebuild:
                                                                        self.open   = num.NUMBER().OPENING( self.close )
                                                                        self.left   = self.normal_string.count( self.open )
                                                                        self.right  = self.normal_string.count( self.close )
                                                                        idd         = self.string_rebuild.index( self.close )
                                                                    
                                                                        if self.left == self.right:
                                                                            #this part need to be updated
                                                                            self.storage.append(self.string_rebuild)
                                                                            self.string_rebuild = ''
                                                                            self.space = 0
                                                                        else:
                                                                            self.error = SE.ERROR((self.line + self.string_line)).ERROR0(  self.normal_string)
                                                                            break
                                                                    else:
                                                                        #this part need to be updated
                                                                        self.storage.append(self.string_rebuild)
                                                                        self.string_rebuild = ''
                                                                        self.space = 0
                                                                else:
                                                                    self.error = SE.ERROR((self.line + self.string_line)).ERROR5(  self.normal_string)
                                                                    break
                                                            else: pass
                                                        else:
                                                            if str_ in [',']:
                                                                self.stest_string, self.error = control_string.STRING_ANALYSE(self.data_base,
                                                                        (self.line + self.string_line)).DELETE_RIGTH(  self.string_rebuild[: -1], "cython")
                                                                if not self.error:

                                                                    if self.storage[-1][-1] in [',']:
                                                                        #this part need to be updated
                                                                        self.storage.append(self.string_rebuild)
                                                                        self.string_rebuild = ''
                                                                        self.space = 0
                                                                    else:
                                                                        if len( self.storage ) > 1:
                                                                            self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                            break
                                                                        else:
                                                                            if len( self.storage[ 0 ] ) == 1:
                                                                                #this part need to be updated
                                                                                self.storage.append(self.string_rebuild)
                                                                                self.string_rebuild = ''
                                                                                self.space = 0
                                                                            else:
                                                                                self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                                break
                                                                else:
                                                                    self.error = SE.ERROR((self.line + self.string_line)).ERROR5( self.normal_string)
                                                                    break

                                                            else:
                                                                if str_ ==  self.close:
                                                                    self.Open       = num.NUMBER().OPENING(self.close)
                                                                    self.left       = self.normal_string.count(self.Open)
                                                                    self.right      = self.normal_string.count(self.close)

                                                                    if self.left != self.right:
                                                                        if self.storage[-1][-1] in [',']:

                                                                            if len( self.string_rebuild ) == 1:
                                                                                self.error = SE.ERROR((self.line + self.string_line)).ERROR2()
                                                                                break
                                                                            else:
                                                                                self.storage.append(self.string_rebuild)
                                                                                self.key_break = True
                                                                                break
                                                                        else:
                                                                            if len(self.storage) > 1:
                                                                                self.storage.append(self.string_rebuild)
                                                                                self.key_break = True
                                                                                break
                                                                               
                                                                            else:
                                                                                if len( self.storage[0] ) == 1 :
                                                                                    self.storage.append(self.string_rebuild)
                                                                                    self.key_break = True
                                                                                    break
                                                                                else:
                                                                                    self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                                    break
                                                                    else:
                                                                        if self.storage[-1][-1] in [',']:
                                                                            self.storage.append(self.string_rebuild)
                                                                            self.string_rebuild = ''
                                                                            self.space = 0
                                                                        else:
                                                                            if len(self.storage) > 1:
                                                                                self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                                break

                                                                            else:
                                                                                if len(self.storage[0]) == 1:
                                                                                    #here
                                                                                    self.storage.append( self.string_rebuild)
                                                                                    self.string_rebuild = ''
                                                                                    self.space = 0
                                                                                else:
                                                                                    self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                                    break

                                                                else:
                                                                    if self.close in self.string_rebuild:
                                                                        self.Open       = num.NUMBER().OPENING( self.close )
                                                                        self.left       = self.normal_string.count( self.Open )
                                                                        self.right      = self.normal_string.count( self.close )
                                                                        idd             = self.string_rebuild.index(self.close)

                                                                        if self.left == self.right:
                                                                            if self.storage[-1][-1] in [',']:
                                                                                #here
                                                                                self.storage.append(self.string_rebuild)
                                                                                self.string_rebuild = ''
                                                                                self.space = 0
                                                                            else:
                                                                                if len(self.storage) > 1:
                                                                                    self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                                    break
                                                                                else:
                                                                                    if len(self.storage[0]) == 1:
                                                                                        #here
                                                                                        self.storage.append(  self.string_rebuild)
                                                                                        self.string_rebuild = ''
                                                                                        self.space = 0
                                                                                    else:
                                                                                        self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                                        break

                                                                        else:
                                                                            if self.storage[-1][-1] in [',']:
                                                                                self.new_string = self.string_rebuild[: idd]
                                                                                self.new_string, self.error = control_string.STRING_ANALYSE(self.data_base,
                                                                                        (self.line + self.string_line)).DELETE_SPACE( self.new_string, "cython")
                                                                                if self.error is None:
                                                                                    self.storage.append(self.string_rebuild)
                                                                                    self.key_break = True
                                                                                    break

                                                                                else:
                                                                                    self.error = SE.ERROR((self.line + self.string_line)).ERROR6()
                                                                                    break
                                                                            else:
                                                                                if len( self.storage ) > 1:
                                                                                    self.new_string = self.string_rebuild[: idd]
                                                                                    self.new_string, self.error = control_string.STRING_ANALYSE(self.data_base,
                                                                                        (self.line + self.string_line)).DELETE_SPACE( self.new_string, "cython")
                                                                                    if self.error is None:
                                                                                        self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                                        break
                                                                                    else:
                                                                                        self.error      = ""
                                                                                        self.storage.append(self.string_rebuild)
                                                                                        self.key_break  = True
                                                                                        break

                                                                                else:
                                                                                    if len(self.storage[0]) == 1:
                                                                                        self.storage.append(self.string_rebuild)
                                                                                        self.key_break = True
                                                                                        break

                                                                                    else:
                                                                                        self.stest_string, self.error = control_string.STRING_ANALYSE(self.data_base,
                                                                                            (self.line + self.string_line)).DELETE_SPACE(
                                                                                            self.string_rebuild[: idd], "cython")

                                                                                        if self.error is None:
                                                                                            self.error = SE.ERROR((self.line +  self.string_line)).ERROR3()
                                                                                            break
                                                                                        else:
                                                                                            self.error      = ""
                                                                                            self.key_break  = True
                                                                                            self.storage.append(self.string_rebuild)
                                                                                            break

                                                                    else:
                                                                        if self.storage[-1][-1] in [',']:
                                                                            #here
                                                                            self.storage.append(self.string_rebuild)
                                                                            self.string_rebuild = ''
                                                                            self.space = 0
                                                                        else:
                                                                            self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                            break
                                                    else:
                                                        self.error = SE.ERROR((self.line + self.string_line)).ERROR1(self.normal_string)
                                                        break
                                            else:
                                                if self.first_char not in ['"', "'"]:
                                                    self.error = SE.ERROR( (self.line + self.string_line) ).ERROR7(  self.normal_string, str_)
                                                    break
                                                else:  self.string_rebuild += str_
                                        if not self.error :
                                            ############################################################################################
                                            # self.key_break helps us to get out of < for > loop when self.error is None and then      #
                                            # we break < while> without any problem to get the final string set in this part           #
                                            ############################################################################################
                                            if self.key_break == True: break
                                            else: pass
                                        else: break
                                    else: self.error = None
                                except IndexError:
                                    ###############################################
                                    # i've limited the number of lines to 5       #
                                    ###############################################
                                    if self.space <= self.max_emtyLine:   self.space += 1
                                    else:
                                        ############################################################################################
                                        # an error got if this condition was not sastified, if the code a value bigger than five   #
                                        # you're going to see this error on your screen                                            #
                                        ############################################################################################
                                        self.error = SE.ERROR( (self.line + self.string_line) ).ERROR8()
                                        break
                            else:
                                ####################################################################################################
                                # the error got when self.active that is not True, what does it mean excatly , it means that       #
                                # before typing something you have to used tab, then when tab is used self.active key gave by the  #
                                # stdin becomes True, else this value it always False.                                             #
                                ####################################################################################################
                                self.error = SE.ERROR( (self.line + self.string_line) ).ERROR9( )
                                break
                        else:  break
                    else :
                        if self.space <= self.max_emtyLine:  self.space += 1
                        else:
                            self.error = SE.ERROR(self.if_line).ERROR9()
                            break

                    self.input      = '{}... {}'.format(self.c, bm.init.reset)
                    self.index      = self.length
                    self.mainString = ''
                    self.mainIndex  = 0

                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                sys.stdout.write(bm.clear.line(pos=0))
                sys.stdout.write(bm.string().syntax_highlight(name=self.input))
                sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                if self.index > 0:  sys.stdout.write(bm.move_cursor.RIGHT(pos=self.index - self.sub_length))
                else:  pass
                sys.stdout.flush()

            except KeyboardInterrupt:
                _keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(_keyboard_)
                self.error = SE.ERRORS(self.string_line).ERROR9()
                break
            except EOFError:  break
            except TypeError:
                _end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                print(_end_of_file_)
                self.error = SE.ERRORS(self.string_line).ERROR9()
                break

        ####################################################################################
        if not self.error :
            self.string = ''
            for str_ in self.storage[ self.len_storage : ]:  self.string += str_
        else: pass
        ####################################################################################

        return self.string, self.error

    cdef str GET_CLOSE(self):
        self.close = ''

        if   self.first_char == '[': self.close      = ']'
        elif self.first_char == '(': self.close      = ')'
        elif self.first_char == '{': self.close      = '}'
        elif self.first_char == '"': self.close      = '"'
        elif self.first_char == "'": self.close      = "'"

        return self.close

















