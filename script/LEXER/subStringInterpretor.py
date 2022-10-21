from script                             import control_string
from script.STDIN.WinSTDIN              import stdin
from CythonModules.Windows.LEXER.seg    import segError as SE
from CythonModules.Windows.LEXER.seg    import num

class SUB_STRING:
    
    def __init__(self, first_char: str , data_base: dict , line: int):
        self.first_char     = first_char                                                                                # first char before moving here                                                                               # last char before moving here
        self.data_base      = data_base                                                                                 # data base with all variables
        self.line           = line                                                                                      # line from the last while loop
        self.analyze        = control_string.STRING_ANALYSE( self.data_base, self.line )                                # string functions
        self.upper_case     = self.analyze.UPPER_CASE()                                                                 # upper cases
        self.lower_case     = self.analyze.LOWER_CASE()                                                                 # lower cases
        self.chars          = CHARS( ).chars + self.lower_case + self.upper_case                                        # authorized chars

    def SUB_STR(self, _id_: int, storage, MainList : list = [], lastString: str =  '', name : str = 'python'):
        
        self.string         = ''                                                                                        # concateante string
        self.normal_string  = ''                                                                                        # non-concatenate string
        self.error          =  None                                                                                     # error got during de precess
        self.string_line    = 0                                                                                         # line inside while loop
        self.space          = 0                                                                                         # max lines under the last string
        self.close          = SUB_STRING(self.first_char, self.data_base, self.line).GET_CLOSE()                        # the closing opening bracket
        self.storage        = storage[ : ]                                                                              # a storing list
        self.len_storage    = len( self.storage )
        self.key_break      = False                                                                                     # key used to break while loop
        self.isBreak            = False
        self.loopActivation     = False
        self.initLine           = self.line
        
        if MainList:
            self.NewLIST                = stdin.STDIN(self.data_base, self.line ).FOR_STRING(_id_, MainList)
            
            for x, _string_ in enumerate( self.NewLIST ):
                try:
                    self.string_line    += 1
                    self.loopActivation = True
                                                                                         
                    self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                            (self.line + self.string_line)).STDIN_FOR_INTERPRETER( _id_, _string_ )   
                    if self.error is None:
                        if self.active_tab == True :
                            self.string             = self.string[_id_: ]                                                   # removing '\t' due to tab
                            self.normal_string      = self.normal_string[_id_ : ]                                           # removing '\t' due to tab
                            
                            try:
                                self.string_rebuild             = ''                                                        # rebuilding string by using self.normal_string
                                self.string, self.error         = control_string.STRING_ANALYSE(self.data_base,
                                                    (self.line + self.string_line)).DELETE_SPACE(self.string)               # removing left and right space on string
                                self.normal_string, self.error  = control_string.STRING_ANALYSE(self.data_base,
                                                    (self.line + self.string_line)).DELETE_SPACE(self.normal_string)        # removing left and right space on string
                                if self.error is None:
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
                                                            self.storage.append( self.string_rebuild )
                                                            self.string_rebuild     = ''
                                                            self.space              = 0
                                                    else:
                                                        if len( self.storage ) > 1:
                                                            if str_ == self.close:
                                                                self.storage.append(self.string_rebuild)
                                                                self.key_break  = True
                                                                break
                                                            else:
                                                                self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                break
                                                        else:
                                                            if len(self.storage[0]) > 1:
                                                                if str_ == self.close:
                                                                    self.storage.append(self.string_rebuild)
                                                                    self.key_break  = True
                                                                    break
                                                                else:
                                                                    self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                    break
                                                            else:
                                                                self.open   = num.NUMBER().OPENING( self.close )
                                                                self.error = SE.ERROR((self.line + self.string_line)).ERROR4( self.open, self.close )
                                                                break

                                            else:
                                                if self.normal_string[ 0 ]  not in  [',']   :
                                                    if i < len( self.normal_string ) - 1:
                                                        if str_ in [',']:
                                                            self.stest_string, self.error       = self.analyze.DELETE_SPACE(
                                                                        self.string_rebuild[: - 1])

                                                            if self.error is None:
                                                                if self.close in self.string_rebuild:
                                                                    self.open   =  num.NUMBER().OPENING( self.close )
                                                                    self.left   = self.normal_string.count( self.open )
                                                                    self.right  = self.normal_string.count( self.close )
                                                                    self.idd    = self.string_rebuild.index( self.close )

                                                                    if self.left == self.right:
                                                                        self.storage.append(self.string_rebuild)
                                                                        self.string_rebuild     = ''
                                                                        self.space              = 0
                                                                    else:
                                                                        self.error = SE.ERROR((self.line + self.string_line)).ERROR0(  self.normal_string)
                                                                        break
                                                                else:
                                                                    self.storage.append( self.string_rebuild )
                                                                    self.string_rebuild             = ''
                                                                    self.space                      = 0
                                                            else:
                                                                self.error = SE.ERROR((self.line + self.string_line)).ERROR5(  self.normal_string)
                                                                break
                                                        else: pass
                                                    else:
                                                        if str_ in [',']:
                                                            self.stest_string, self.error = self.analyze.DELETE_RIGTH(  self.string_rebuild[: -1])
                                                            if self.error is None:

                                                                if self.storage[-1][-1] in [',']:
                                                                    self.storage.append( self.string_rebuild )
                                                                    self.string_rebuild     = ''
                                                                    self.space              = 0
                                                                else:
                                                                    if len( self.storage ) > 1:
                                                                        self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                        break
                                                                    else:
                                                                        if len( self.storage[ 0 ] ) == 1:
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
                                                                self.open       =  num.NUMBER().OPENING(self.close)
                                                                self.left       = self.normal_string.count(self.open)
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
                                                                            #self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                            #break
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
                                                                        self.storage.append( self.string_rebuild )
                                                                        self.string_rebuild     = ''
                                                                        self.space              = 0
                                                                    else:
                                                                        if len(self.storage) > 1:
                                                                            self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                            break

                                                                        else:
                                                                            if len(self.storage[0]) == 1:
                                                                                self.storage.append( self.string_rebuild )
                                                                                self.string_rebuild     = ''
                                                                                self.space              = 0

                                                                            else:
                                                                                self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                                break

                                                            else:
                                                                if self.close in self.string_rebuild:
                                                                    self.open       =  num.NUMBER().OPENING( self.close )
                                                                    self.left       = self.normal_string.count( self.open )
                                                                    self.right      = self.normal_string.count( self.close )
                                                                    self.idd        = self.string_rebuild.index(self.close)

                                                                    if self.left == self.right:
                                                                        if self.storage[-1][-1] in [',']:
                                                                            self.storage.append( self.string_rebuild )
                                                                            self.string_rebuild     = ''
                                                                            self.space              = 0

                                                                        else:
                                                                            if len(self.storage) > 1:
                                                                                self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                                break
                                                                            else:
                                                                                if len(self.storage[0]) == 1:
                                                                                    self.storage.append(self.string_rebuild)
                                                                                    self.string_rebuild     = ''
                                                                                    self.space              = 0
                                                                                else:
                                                                                    self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                                    break

                                                                    else:
                                                                        if self.storage[-1][-1] in [',']:
                                                                            self.new_string = self.string_rebuild[: self.idd]
                                                                            self.new_string, self.error = self.analyze.DELETE_SPACE( self.new_string)
                                                                            if self.error is None:
                                                                                self.storage.append(self.string_rebuild)
                                                                                self.key_break = True
                                                                                break

                                                                            else:
                                                                                self.error = SE.ERROR((self.line + self.string_line)).ERROR6()
                                                                                break
                                                                        else:
                                                                            if len( self.storage ) > 1:
                                                                                self.new_string = self.string_rebuild[: self.idd]
                                                                                self.new_string, self.error = self.analyze.DELETE_SPACE( self.new_string)
                                                                                if self.error is None:
                                                                                    self.error = SE.ERROR((self.line + self.string_line)).ERROR3()
                                                                                    break
                                                                                else:
                                                                                    self.error      = None
                                                                                    self.storage.append(self.string_rebuild)
                                                                                    self.key_break  = True
                                                                                    break

                                                                            else:
                                                                                if len(self.storage[0]) == 1:
                                                                                    self.storage.append(self.string_rebuild)
                                                                                    self.key_break = True
                                                                                    break

                                                                                else:
                                                                                    self.stest_string, self.error = self.analyze.DELETE_SPACE(
                                                                                        self.string_rebuild[: self.idd])

                                                                                    if self.error is None:
                                                                                        self.error = SE.ERROR((self.line +  self.string_line)).ERROR3()
                                                                                        break
                                                                                    else:
                                                                                        self.error      = None
                                                                                        self.key_break  = True
                                                                                        self.storage.append(self.string_rebuild)
                                                                                        break

                                                                else:
                                                                    if self.storage[-1][-1] in [',']:
                                                                        self.storage.append( self.string_rebuild )
                                                                        self.string_rebuild     = ''
                                                                        self.space              = 0

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

                                    if self.error is None :
                                        ############################################################################################
                                        # self.key_break helps us to get out of < for > loop when self.error is None and then      #
                                        # we break < while> without any problem to get the final string set in this part           #
                                        ############################################################################################
                                        if self.key_break == True: 
                                            self.isBreak                    = True
                                            self.data_base['globalIndex']   = x+self.data_base['starter']
                                            break
                                        else: pass
                                    else: break
                                else: self.error = None
                            except IndexError:
                                ###############################################
                                # i've limited the number of lines to 5       #
                                ###############################################
                                if self.space <= 5:   self.space += 1
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
                except KeyboardInterrupt: break
                except EOFError:  break
        else: self.error = SE.ERROR( self.initLine ).ERROR9()
        
        if self.error is None:
            if self.loopActivation is True:
                if self.isBreak is True: pass 
                else: self.error =SE. ERROR( self.initLine ).ERROR0( lastString  )
            else: pass
        else: pass
        
        if self.error is None :
            self.string = ''
            for str_ in self.storage[ self.len_storage : ]:
                self.string += str_
        else: pass

        if name == 'cython':
            if self.error is None: self.error = ""
            else: pass 
        else: pass 
        
        return self.string, self.error
    
class CHARS:
    def __init__(self):
        self.char   = ['(',')', '[',']', '{', '}', '"', "'", '+', '-', '*','/', '^', '>', '<','_',
                               '%','|', '.', '@', ',', ' ', ':', '$', '&', '#', '!', '=', ';', '?', '\{}'.format( '' )]                                    
        self.chars  = self.char +['0','1','2','3', '4','5','6','7','8','9']