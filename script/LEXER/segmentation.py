import  sys, os, re
from script.STDIN.LinuxSTDIN                import control_string
from script.STDIN.WinSTDIN                  import stdin
from script.LEXER                           import checking_if_backslash
from script.STDIN.LinuxSTDIN                import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS._IF_    import IfError
from CythonModules.Windows                  import fileError    as fe 
from IDE.EDITOR                             import string_to_chr 

ne = bm.fg.red_L
ie = bm.fg.blue_L
ae = bm.fg.cyan_L
te = bm.fg.magenta_M
ke = bm.fg.rbg(255,255,0)
ve = bm.fg.rbg(0,255,0)
se = bm.fg.rbg(255,255,0)
we = bm.fg.rbg(255,255,255)

class SEGMENTATION:
    def __init__(self,
                    master      : str,          # concatenate main string after checking tabulation and comment line
                    long_chaine : str,          # non-concatenate main string after checking tabulation and comment line
                    data_base   : dict,         # data base
                    line        : int           # current line
                 ):
        self.master         = master
        self.long_chaine    = long_chaine
        self.line           = line
        self.data_base      = data_base
        self.analyze        = control_string.STRING_ANALYSE( self.data_base, self.line )   # string analyses

    def TREATEMENT(self,
                        _id_    : int,          # _id_ value for indentations
                        color   : str           # color used for the blocks
                   ):

        self.left                   = 0         # firt left bracket
        self.rigth                  = 0         # last right bracket
        self.initialize             = [ None ]  # initialization bracket research
        self.active_key             = None      # when left braket was detected
        self.string                 = ''        # string
        self.string_in_true         = ''        # string used in True block
        self.storage_value          = []        # storing list
        self.error                  = None      # error
        self.if_key_is_true         = None      # if left and rigth bracket was found
        self.str_id                 = False     # id string, used to compte ['"', "'"] when self.id it's False i start counting of left
                                                #   .the left value takes 1 as a value and self.id takes True values and i start counting the rigth values
                                                #   .however the max left and right is 1, it means that for this you cannot have more than 1 ['"' or "'"]
        self.str_id_                = False
        self.key_bracket            = None      # key bracket it means that you cannot have right bracket before letf bracket
                                                # [, {, ( come before '), }, ] else self.key_bracket stays None and you get an error
        try:
            self.master , self.error        = self.analyze.DELETE_SPACE( self.master )           # removing right and left space
            self.long_chaine, self.error    = self.analyze.DELETE_SPACE( self.long_chaine )      # removing right and left space
        
            if self.error is None:

                for i, str_ in enumerate( self.long_chaine ):
                    if str_ in SUB_STRING( '', self.data_base, self.line ).chars:

                        if str_ in [ '[', '(', '{', '"', "'" ]:

                            if str_ == '('  : char1 = str_.index( '(' )
                            else            : char1 = int( NUMBER().number )

                            if  str_ == '[' : char2 = str_.index( '[' )
                            else            : char2 = int( NUMBER().number )

                            if  str_ == '{' : char3 = str_.index( '{' )
                            else            : char3 = int( NUMBER().number )

                            if  str_ == '"' : char4 = str_.index( '"' )
                            else            : char4 = int( NUMBER().number )

                            if str_ == "'"  : char5 = str_.index("'")
                            else            : char5 = int( NUMBER().number )

                            if self.initialize[ 0 ] is None:

                                if char1 < char2 and char1 < char3 and char1 < char4 and char1 < char5:
                                    self.initialize[ 0 ] = '('

                                if char2 < char1 and char2 < char3 and char2 < char4 and char2 < char5:
                                    self.initialize[ 0 ] = '['

                                if char3 < char1 and char3 < char2 and char3 < char4 and char3 < char5:
                                    self.initialize[ 0 ] = '{'

                                if char4 < char1 and char4 < char2 and char4 < char3 and char4 < char5:
                                    self.initialize[ 0 ] = '"'

                                if char5 < char1 and char5 < char2 and char5 < char3 and char5 < char4:
                                    self.initialize[ 0 ] = "'"

                                self.key_bracket = True

                            else: self.initialize = self.initialize

                        else:
                            if str_ in [']', ')', '}'] and self.key_bracket is None:
                                self.open = NUMBER().OPENING( str_ )                        # if srtr_ = '(' so, self.open = ')'
                                self.error = ERROR( self.line ).ERROR_TREATMENT2( self.long_chaine, str_ )
                                break
                            else: pass

                        if self.initialize [ 0 ] is not None :
                            if self.initialize[0] == '(' :
                                self.left, self.rigth = self.left + str_.count( '(' ), self.rigth + str_.count( ')' )

                            if self.initialize[ 0 ] == '[':
                                self.left, self.rigth = self.left + str_.count( '[' ), self.rigth + str_.count( ']' )

                            if self.initialize[ 0 ] == '{':
                                self.left, self.rigth = self.left + str_.count( '{' ), self.rigth + str_.count( '}' )

                            if self.initialize[ 0 ] == '"':
                                if self.str_id == False:
                                    self.left               = 1
                                    self.rigth              = 0
                                    self.str_id             = True
                                else:
                                    if self.rigth <= 1:
                                        self.rigth  = self.rigth + str_.count( '"' )
                                        self.left   = self.left
                                    else:
                                        self.error = ERROR( self.line ).ERROR_TREATMENT3( self.long_chaine )
                                        break

                            if self.initialize[ 0 ] == "'":
                                if self.str_id_ == False:
                                    self.left               = 1
                                    self.rigth              = 0
                                    self.str_id_            = True
                                else:
                                    if self.rigth <= 1:
                                        self.rigth  = self.rigth + str_.count( "'" )
                                        self.left   = self.left
                                    else:
                                        self.error = ERROR( self.line ).ERROR_TREATMENT3( self.long_chaine )
                                        break
                        else: pass

                        # condition to make self.active_key True
                        if self.left != self.rigth  : self.active_key = True
                        else                        : self.active_key = False

                        if self.active_key == True :

                            self.string         += str_
                            self.string_in_true += str_

                            if i == len( self.long_chaine ) - 1 :
                                self.if_key_is_true = True

                                if self.initialize[ 0 ] not in ['"', "'"]:
                                    if ( self.left - self.rigth ) == 1:
                                        self.store, self.error = SEGMENTATION( self.master, self.long_chaine, self.data_base,
                                                        self.line ).STRING_IN_TRUE_BLOCK(self.string_in_true, self.string )

                                        if self.error is None:
                                            self.new_str, self.error = SUB_STRING( self.initialize[ 0 ], self.data_base,
                                                                                self.line ).SUB_STR( _id_, color, self.store )

                                            if self.error is None:
                                                self.string += self.new_str
                                            else: break
                                        else: break
                                    else:
                                        self.error = ERROR( self.line ).ERROR_TREATMENT4( self.long_chaine, self.initialize[ 0 ] )
                                        break
                                else: pass
                            else: pass
                        else:
                            if self.if_key_is_true is None  : self.string = self.string +  str_
                            else                            : self.if_key_is_true = None


                            ################################################################################################
                            # initialization part                                                                          #
                            # even if self.active_key didn't take True value it's important to make that initialization    #
                            # to be sure that we are going with the good initial paremeters .                              #
                            ################################################################################################

                            self.initialize[ 0 ]    = None
                            self.left               = 0
                            self.rigth              = 0
                            self.str_id             = False
                            self.str_id_            = False
                            self.key_bracket        = None
                            self.string_in_true     = ''
                    else:
                        if str_ in [ '\t' ]     : self.string += ' '
                        elif str_ in [ '\n' ]   : self.string += '{}\n'.format( '' )
                        else:
                            self.error = ERROR( self.line ).ERROR7( self.long_chaine, str_ )
                            break
            else: pass

            if self.error is None:
                self.error = STR( self.string, self.line).STR()
                
                """
                for str_ in [ '[', '(', '{' ]:
                    if str_ in self.string:
                        self.close      = SUB_STRING(str_, self.data_base, self.line).GET_CLOSE()     # if str_ = [, so self.close = ]
                        self.left       = self.string.count( str_ )                                   # left counting
                        self.right      = self.string.count( self.close )                             # right counting

                        if self.left == self.right: pass
                        else:
                            print(self.string[0], self.string )
                            if self.string[0] not in ["'", '"']:
                                if self.left > self.right:
                                    self.error  = ERROR( self.line ).ERROR_TREATMENT1( self.string, str_ )
                                    break
                                else:
                                    self.error  = ERROR( self.line ).ERROR_TREATMENT2( self.string, self.close )
                                    break
                            else: pass
                    else: pass
               
                if self.error is None:
                    for str_ in [']', ')', '}']:
                        if str_ in self.string:
                            self.open       = NUMBER().OPENING( str_ )                                  # if str_ = ( so, self.open = )
                            self.left       = self.string.count( self.open )                            # left counting
                            self.right      = self.string.count( str_ )                                 # right counting

                            if self.left == self.right: pass
                            else:
                                if self.string[0] not in ['"', "'"]:
                                    if self.left > self.right:
                                        self.error = ERROR( self.line ).ERROR_TREATMENT1( self.string, self.open )
                                        break
                                    else:
                                        self.error = ERROR( self.line ).ERROR_TREATMENT2( self.string, str_ )
                                        break
                                else: pass
                        else: pass
                """
                
                if self.error is None:
                    self.str__          = None
                    self._idd_          = None
                    self.transform      = False

                    if ( self.string[ 0 ] == "'" )  and ( self.string[ -1 ]== "'" ) :
                        self.string     = '"' + self.string[ 1 : -1 ] + '"'
                        self.transform  = True
                    else: pass

                    for str_ in ['"', "'"]:
                        if str_ in  self.string :
                            self.str__ = str_
                            self._idd_ = self.string.index( self.str__ )
                            break
                        else: pass

                    if self.str__ is not None:
                        self.count = self.string.count( self.str__ )
                        if self.count % 2 == 0: pass
                        else:
                            if self._idd_ == 0: self.error = ERROR( self.line ).ERROR_TREATMENT1( self.string, self.str__ )
                            else: self.error = ERROR( self.line ).ERROR_TREATMENT2( self.string, self.str__ )
                    else: pass
                else: pass
            else: pass
            #else: pass
        except IndexError: pass

        return self.string, self.error

    def STRING_IN_TRUE_BLOCK(self,
                                string      : str,
                                main_string : str
                             ):

        self.storage        = []
        self.str            = ''
        self.error          = None

        for i, str_ in enumerate( string ):
            self.str        += str_

            if i != len( string ) - 1:
                if str_ in [ ',' ]:
                    self.test_string, self.error = self.analyze.DELETE_SPACE( self.str[ 1 : -1 ] )
                    if self.error is None:
                        self.storage.append( self.str )
                        self.str = ''
                    else:
                        self.error = ERROR( self.line ).ERROR5( main_string )
                        break
                else: pass
            else:
                if str_ in [ ',' ]:
                    self.test_string, self.error = self.analyze.DELETE_SPACE( self.str[ 1 : -1 ] )
                    if self.error is None:
                        self.storage.append( self.str )
                    else:
                        self.error = ERROR( self.line ).ERROR5( main_string )
                        break
                else: self.storage.append( self.str )

        return self.storage, self.error

class NUMBER:

    def __init__(self):
        self.number     = 1e10

    def OPENING(self,
                string  : str       # char value
                ):
        self.open = ''

        if   string == ']'      : self.open   = '['         # opening and closing brackets
        elif string == ')'      : self.open   = '('         # opening ans closing parentheses
        elif string == '}'      : self.open   = '{'         # ......
        elif string == '"'      : self.open   = '"'         # ......
        elif string == "'"      : self.open   = "'"         # ......

        return self.open                                    # returning value

class CHARS:
    def __init__(self):
        self.char           = ['(',')', '[',']', '{', '}', '"', "'", '+', '-', '*','/', '^', '>', '<','_',
                               '%','|', '.', '@', ',', ' ', ':', '$', '&', '#', '!', '=', ';', '?', '\{}'.format( '' )]                                    # list of accepted chars
        #self.char_num       = [ str( x ) for x in range( 10 ) ]        # numbers
        self.chars          = self.char +['0','1','2','3', '4','5','6','7','8','9']# self.char_num

class SUB_STRING:

    def __init__(self, first_char, data_base, line):
        self.first_char     = first_char                                                                                # first char before moving here                                                                               # last char before moving here
        self.data_base      = data_base                                                                                 # data base with all variables
        self.line           = line                                                                                      # line from the last while loop
        self.analyze        = control_string.STRING_ANALYSE( self.data_base, self.line )                                # string functions
        self.upper_case     = self.analyze.UPPER_CASE()                                                                 # upper cases
        self.lower_case     = self.analyze.LOWER_CASE()                                                                 # lower cases
        self.chars          = CHARS( ).chars + self.lower_case + self.upper_case                                        # authorized chars

    def SUB_STR(self, _id_: int, color: str, storage: list, term: str='orion'):
        self.term           = term
        self.string         = ''                                                                                        # concateante string
        self.normal_string  = ''                                                                                        # non-concatenate string
        self.error          =  None                                                                                     # error got during de precess
        self.string_line    = 0                                                                                         # line inside while loop
        self.space          = 0                                                                                         # max lines under the last string
        self.close          = SUB_STRING(self.first_char, self.data_base, self.line).GET_CLOSE()                        # the closing opening bracket
        self.storage        = storage[ : ]                                                                              # a storing list
        self.len_storage    = len( self.storage )
        self.key_break      = False
        self.if_line        = self.line
        #######################################################################
        self.max_emtyLine        = 5
        # set color on yellow
        self.c                   = bm.fg.rbg(255,255,0)
        if self.term == 'orion': pass 
        else: self.c             = bm.fg.rbg(255,255,255)
        # reset color
        self.reset               = bm.init.reset
        # input initialized
        self.input               = '{}... {}'.format(self.c, self.reset)
        # input main used to build the final string s
        self.main_input          = '{}... {}'.format(self.c, self.reset)
        # initial length of the input 
        self.length              = len(self.input)
        # initialisation of index associated to the input 
        self.index               = self.length
        # length of the foutth first char of input 
        self.size                = len('... ')
        # string used to handling the output that is the must inmportant string
        self.s                   = ""
        # string used for the code, 
        self.string              = ''
        # index associated to the string string value
        self.I_S                 = 0
        # initialisation of index I associated to the string s value
        self.I                   = 0    
        # history of data associated to the string  input 
        self.liste               = []
        # history of data associated to the value returns by the function readchar 
        self.get                 = []
        # initialisation of integer idd used to get the next of previous 
        # values stored in the different histories of lists 
        self.idd                 = 0
        # initialization of list associated to the string s
        self.sub_liste           = []
        # the memory contains the history of get value
        self.memory              = []
        # initilization of last
        self.last                = 0
        # initialisation of list associated to the index value
        self.tabular             = []
        # initialisation of list associated to I value
        self.sub_tabular         = []
        # initialisation of the list associated to last value
        self.last_tabular        = []
        # move cursor 
        self.remove_tab          = 0
        # storing cursor position 
        self.remove_tabular      = []
        # initialization of the list associated to string 
        self.string_tab          = []
        # initialization of associated to I_S
        self.string_tabular      = []
        ###########################################################
        # clear entire line
        sys.stdout.write(bm.clear.line(pos=0))
        #move cursor left
        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))  
        # print the input value
        sys.stdout.write(self.input)
        # save cursor position
        sys.stdout.write(bm.save.save)
        # flush
        sys.stdout.flush()
        ###########################################################

        while self.normal_string != self.first_char :
            try:
                self.char = string_to_chr.convert() 
                if self.char:
                    _ = self.char[1]
                    self.char = self.char[0]
                    if self.char is not None:
                        if self.char == 3: 
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break
                        # write char
                        elif 32 <= self.char <= 126:
                            ######################################
                            # each character has 1 as length     #   
                            # have a look on ansi char           #
                            ######################################
                            # building input   
                            self.input       = self.input[ : self.index +self.last] + chr(self.char) + self.input[ self.index+self.last : ]
                            # building s 
                            self.s           = self.s[ : self.I] + chr(self.char) + self.s[self.I : ]
                            # building string 
                            self.string      = self.string[ : self.I_S] + chr(self.char) + self.string[ self.I_S : ]
                            # increasing index of a step = 1
                            self.index       += 1
                            # increasing I of a step = 1
                            self.I           += 1
                            # increasing I_S of step = 1
                            self.I_S         += 1 
                            # storing char in get
                            self.get.append(self.char)
                        # moving cursor up, down, left, reight
                        elif self.char == 27    :
                            next1, next2 = ord( sys.stdin.read(1)), ord( sys.stdin.read(1))
                            if next1 == 91:
                                try:
                                    # move cursor to left
                                    if   next2 == 68:
                                        if self.I > 0:
                                            try:
                                                # without indentation 
                                                if 32 <= self.get[self.I-1] <= 126:
                                                    self.I     -= 1
                                                    self.index += 1
                                                    self.last  -= 2
                                                    self.I_S   -= 1
                                                # when identation is detected 
                                                elif self.get[self.I-1] == 9:
                                                    self.I     -= 4
                                                    self.index += 4
                                                    self.last  -= 8
                                                    self.I_S   -= 4
                                            except IndexError: pass
                                        else: pass
                                    # move cursor to right
                                    elif next2 == 67:
                                        if self.I < len(self.s):
                                            try:
                                                # without indentation 
                                                if 32 <= self.get[self.I] <= 126:
                                                    self.I       += 1 
                                                    self.index   -= 1
                                                    self.last    += 2
                                                    self.I_S     += 1
                                                # when identation is detected 
                                                elif self.get[self.I] == 9: 
                                                    self.I       += 4
                                                    self.index   -= 4
                                                    self.last    += 8
                                                    self.I_S     += 4
                                            except IndexError: pass
                                        else: pass
                                    # get the previous value stored in the list 
                                    elif next2 == 65: #up
                                        if self.liste:
                                            try:
                                                # idd is decreased of -1 
                                                self.idd    -= 1
                                                if len( self.liste ) >= abs( self.idd ):
                                                    # previous input 
                                                    self.input   = self.liste[ self.idd ]
                                                    # previous s
                                                    self.s       = self.sub_liste[ self.idd ]
                                                    # previous string 
                                                    self.string  = self.string_tabular[ self.idd ]
                                                    # restoring the prvious get of s 
                                                    self.get     = self.memory[ self.idd ]
                                                    # restoring cursor position in the input 
                                                    self.index   = self.tabular[ self.idd ]
                                                    # restoring cursor position in s
                                                    self.I       = self.sub_tabular[ self.idd ]
                                                    # restoring cursor position in string 
                                                    self.I_S     = self.string_tab[ self.idd ]
                                                    # restoring the value of last 
                                                    self.last    = self.last_tabular[ self.idd ]
                                                    # restoring remove_tab from index
                                                    self.remove_tab = self.remove_tabular[ self.idd ]
                                                else: self.idd += 1
                                            except IndexError: 
                                                # any changes here when local IndexError is detected 
                                                pass
                                        else: pass
                                    # get the next value stored in the list 
                                    elif next2 == 66:
                                        if self.liste:
                                            try:
                                                # idd is increased of 1
                                                self.idd     += 1
                                                # next input 
                                                if len( self.liste ) > self.idd:
                                                    self.input   = self.liste[ self.idd ]
                                                    # next s
                                                    self.s       = self.sub_liste[ self.idd ]
                                                    # next string 
                                                    self.string  = self.string_tabular[ self.idd ]
                                                    # restoring the prvious get of s 
                                                    self.get     = self.memory[ self.idd ]
                                                    # restoring cursor position in the input 
                                                    self.index   = self.tabular[ self.idd ]
                                                    # restoring cursor position in s
                                                    self.I       = self.sub_tabular[ self.idd ]
                                                    # restoring cursor position in string 
                                                    self.I_S     = self.string_tab[ self.idd ]
                                                    # restoring the value of last 
                                                    self.last    = self.last_tabular[ self.idd ]
                                                    # restoring remove_tab from index
                                                    self.remove_tab = self.remove_tabular[ self.idd ]
                                                else: self.idd -= 1
                                            except IndexError: 
                                                # any changes here when local IndexError is detected 
                                                pass
                                        else: pass
                                except IndexError: pass
                            else: pass  
                        # delecting char 
                        elif self.char in {127, 8}   :
                            # if s is not empty
                            if self.s:
                                # initialize key name of an indentation case
                                self.name = 0
                                self.key  = False
                                
                                try:
                                    # checking if I > 0
                                    if self.I-1 >=0:
                                        # new char initialized 
                                        self.char = self.get[self.I-1]
                                        # writable char
                                        if 32 <= self.get[self.I-1] <= 126:
                                            self.name = 1
                                            # delecting the value in get associated to the index I-1
                                            del self.get[self.I-1]
                                        # indentation cas 
                                        elif self.get[self.I-1] in {9}: 
                                            self.name = 1
                                            # when indentation is detected for loop is used to take into account the four value of space
                                            # it means that inden = " " * 4
                                            for i in range(4):
                                                # building input 
                                                self.input    = self.input[ : self.index + self.last - self.name] + self.input[ self.index + self.last : ]
                                                # decreasing index of -1
                                                self.index   -= 1
                                                # building s 
                                                self.s        = self.s[ : self.I - 1] + self.s[self.I : ]
                                                # decreating I of -1
                                                self.I       -= 1
                                                # delecting the value in get associated to the index I-1
                                                del self.get[self.I]
                                            
                                            # building string 
                                            self.string  = self.string[ : self.I_S-1]+self.string[ self.I_S : ]
                                            #decreasing I_S of -1
                                            self.I_S    -= 1  
                                            # set key of True
                                            self.key     = True
                                        else: pass
                                        
                                        # if key is False it means s has not indentation 
                                        if self.key is False: 
                                            # building input 
                                            self.input   = self.input[ : self.index + self.last - self.name] + self.input[ self.index + self.last : ]
                                            # decreasing index of -name with name = 1
                                            self.index  -= self.name 
                                            # building s 
                                            self.s       = self.s[ : self.I - 1] + self.s[self.I : ]
                                            # building string 
                                            self.string  = self.string[ : self.I_S - 1] + self.string[ self.I_S : ]
                                            # decreasing I and I_S of -1
                                            self.I      -= 1
                                            self.I_S    -= 1
                                        else: pass
                                    else: pass
                                except IndexError: pass  
                            else: pass
                        # indentation 
                        elif self.char == 9     :
                            self.tt = '    '
                            self.input        = self.input[ : self.index + self.last ] + str(self.tt) + self.input[ self.index + self.last : ] 
                            self.s            = self.s[ : self.I] + str(self.tt) + self.s[self.I : ]  
                            # string takes the true value of char
                            self.string       = self.string[ : self.I_S] + chr(self.char) + self.string[ self.I_S : ]
                            self.index       += 4 
                            self.I           += 4
                            self.I_S         += 1
                            
                            for i in range(4):
                                self.get.append( self.char )
                        #clear entire string
                        elif self.char == 12    :
                            # move cursor left 
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            # clear entire line 
                            sys.stdout.write(bm.clear.line(pos=0))
                            # write main_input 
                            sys.stdout.write(self.main_input)
                            # move cursor left egain 
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            
                            # initialization block
                            self.input           = self.main_input
                            self.index           = self.length
                            self.s               = ''
                            self.string          = ''
                            self.I               = 0
                            self.I_S             = 0
                            self.get             = []
                            self.idd             = 0   
                            self.last            = 0
                            self.remove_tab      = 0              
                        # move cursor at end of line 
                        elif self.char == 4     :
                            while self.I < len(self.s):
                                try:
                                    # without indentation 
                                    if 32 <= self.get[self.I] <= 126:
                                        self.I       += 1 
                                        self.index   -= 1
                                        self.last    += 2
                                        self.I_S     += 1
                                    # when identation is detected 
                                    elif self.get[self.I] == 9: 
                                        self.I       += 4
                                        self.index   -= 4
                                        self.last    += 8
                                        self.I_S     += 4
                                except IndexError: pass                    
                        # move cursor at the beginning of line 
                        elif self.char == 17    :
                            while self.I > 0:
                                try:
                                    # without indentation 
                                    if 32 <= self.get[self.I-1] <= 126:
                                        self.I     -= 1
                                        self.index += 1
                                        self.last  -= 2
                                        self.I_S   -= 1
                                    # when identation is detected 
                                    elif self.get[self.I-1] == 9:
                                        self.I     -= 4
                                        self.index += 4
                                        self.last  -= 8
                                        self.I_S   -= 4
                                except IndexError: pass                 
                        # clear entire screen and restore cursor position
                        elif self.char == 19    :
                            sys.stdout.write(bm.clear.screen(pos=2))
                            sys.stdout.write(bm.save.restore)                  
                        #End-Of-File Error
                        elif self.char == 26    :
                            self.error = IfError.ERRORS(self.if_line).ERROR4()
                            break
                        #printing and initializing of values
                        elif self.char in {10, 13}:
                            self.string_line += 1
                            self.if_line += 1
                            sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                            # print the final input with its transformations 
                            if self.term == 'orion':  print(self.main_input+bm.words(string=self.s, color=bm.fg.rbg(255,255,255)).final())
                            else: print(self.main_input+bm.fg.rbg(255,255,255)+self.s+bm.init.reset)
                            
                            # storing input 
                            self.liste.append( self.input )
                            # storing s
                            self.sub_liste.append(self.s)
                            # storing index 
                            self.tabular.append(self.index)
                            # storing I
                            self.sub_tabular.append(self.I)
                            # storing last
                            self.last_tabular.append(self.last)
                            # storing remove_tab
                            self.remove_tabular.append(self.remove_tab)
                            # storing I_S
                            self.string_tab.append(self.I_S)
                            # storing string 
                            self.string_tabular.append(self.string)
                            # storing get
                            self.memory.append(self.get)
                            
                            self.clear_input = self.string
                            if self.clear_input:
                                ####################################################################
                                self.string, self.active_tab, self.error = self.analyze.BUILD_CON(string=self.clear_input,  tabulation=_id_)
                                if self.error is None:
                                    self.normal_string = self.analyze.BUILD_NON_CON( string=self.clear_input, tabulation=_id_ )
                                    self._ = stdin.STDIN(data_base=self.data_base, line=self.line).ENCODING(string=self.clear_input)
                                    if (self._ - _id_) == 0:
                                        self.input = self.input[: self.length] + bm.words(string=self.clear_input, color=color).final()
                                    else:
                                        self.error = ERROR( self.string_line ).ERROR9()
                                        break
                                else: break

                                ######################################################################
                                if self.error is None:
                                    if self.active_tab == True :
                                        self.string             = self.string[_id_: ]                                                   # removing '\t' due to tab
                                        self.normal_string      = self.normal_string[_id_ : ]                                           # removing '\t' due to tab
                                        self.id                 = None

                                        if '#' in self.string:
                                            self.id             = self.normal_string.index('#')
                                            self.normal_string  = self.normal_string[ : self.id ]
                                            self.id             = self.string.index('#')
                                            self.string         = self.string[ : self.id ]
                                        else: pass

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
                                                                self.error = ERROR((self.line + self.string_line)).ERROR1(self.normal_string)
                                                                break
                                                            else:
                                                                if self.storage[-1][-1] in [',']:
                                                                    if str_ == self.close:
                                                                        self.error = ERROR((self.line + self.string_line)).ERROR2()
                                                                        break
                                                                    else:
                                                                        #here
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
                                                                            self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                            break
                                                                    else:
                                                                        if len(self.storage[0]) > 1:
                                                                            if str_ == self.close:
                                                                                self.storage.append(self.string_rebuild)
                                                                                self.key_break = True
                                                                                break
                                                                            else:
                                                                                self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                                break
                                                                        else:
                                                                            self.open   = NUMBER().OPENING( self.close )
                                                                            self.error = ERROR((self.line + self.string_line)).ERROR4( self.open, self.close )
                                                                            break

                                                        else:
                                                            if self.normal_string[ 0 ]  not in  [',']   :
                                                                if i < len( self.normal_string ) - 1:
                                                                    if str_ in [',']:
                                                                        self.stest_string, self.error       = self.analyze.DELETE_SPACE(
                                                                                    self.string_rebuild[: - 1])

                                                                        if self.error is None:
                                                                            if self.close in self.string_rebuild:
                                                                                self.open   = NUMBER().OPENING( self.close )
                                                                                self.left   = self.normal_string.count( self.open )
                                                                                self.right  = self.normal_string.count( self.close )
                                                                                self.idd    = self.string_rebuild.index( self.close )

                                                                                if self.left == self.right:
                                                                                    #here
                                                                                    self.storage.append(self.string_rebuild)
                                                                                    self.string_rebuild = ''
                                                                                    self.space = 0
                                                                                else:
                                                                                    self.error = ERROR((self.line + self.string_line)).ERROR0(  self.normal_string)
                                                                                    break
                                                                            else:
                                                                                #here
                                                                                self.storage.append(self.string_rebuild)
                                                                                self.string_rebuild = ''
                                                                                self.space = 0
                                                                        else:
                                                                            self.error = ERROR((self.line + self.string_line)).ERROR5(  self.normal_string)
                                                                            break
                                                                    else: pass
                                                                else:
                                                                    if str_ in [',']:
                                                                        self.stest_string, self.error = self.analyze.DELETE_RIGTH(  self.string_rebuild[: -1])
                                                                        if self.error is None:

                                                                            if self.storage[-1][-1] in [',']:
                                                                                #here
                                                                                self.storage.append(self.string_rebuild)
                                                                                self.string_rebuild = ''
                                                                                self.space = 0
                                                                            else:
                                                                                if len( self.storage ) > 1:
                                                                                    self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                                    break
                                                                                else:
                                                                                    if len( self.storage[ 0 ] ) == 1:
                                                                                        #here
                                                                                        self.storage.append(self.string_rebuild)
                                                                                        self.string_rebuild = ''
                                                                                        self.space = 0
                                                                                    else:
                                                                                        self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                                        break
                                                                        else:
                                                                            self.error = ERROR((self.line + self.string_line)).ERROR5( self.normal_string)
                                                                            break

                                                                    else:
                                                                        if str_ ==  self.close:
                                                                            self.open       = NUMBER().OPENING(self.close)
                                                                            self.left       = self.normal_string.count(self.open)
                                                                            self.right      = self.normal_string.count(self.close)

                                                                            if self.left != self.right:
                                                                                if self.storage[-1][-1] in [',']:

                                                                                    if len( self.string_rebuild ) == 1:
                                                                                        self.error = ERROR((self.line + self.string_line)).ERROR2()
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
                                                                                            self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                                            break
                                                                            else:
                                                                                if self.storage[-1][-1] in [',']:
                                                                                    #here
                                                                                    self.storage.append(self.string_rebuild)
                                                                                    self.string_rebuild = ''
                                                                                    self.space = 0
                                                                                else:
                                                                                    if len(self.storage) > 1:
                                                                                        self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                                        break

                                                                                    else:
                                                                                        if len(self.storage[0]) == 1:
                                                                                            #here
                                                                                            self.storage.append( self.string_rebuild)
                                                                                            self.string_rebuild = ''
                                                                                            self.space = 0
                                                                                        else:
                                                                                            self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                                            break

                                                                        else:
                                                                            if self.close in self.string_rebuild:
                                                                                self.open       = NUMBER().OPENING( self.close )
                                                                                self.left       = self.normal_string.count( self.open )
                                                                                self.right      = self.normal_string.count( self.close )
                                                                                self.idd        = self.string_rebuild.index(self.close)

                                                                                if self.left == self.right:
                                                                                    if self.storage[-1][-1] in [',']:
                                                                                        #here
                                                                                        self.storage.append(self.string_rebuild)
                                                                                        self.string_rebuild = ''
                                                                                        self.space = 0
                                                                                    else:
                                                                                        if len(self.storage) > 1:
                                                                                            self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                                            break
                                                                                        else:
                                                                                            if len(self.storage[0]) == 1:
                                                                                                #here
                                                                                                self.storage.append(  self.string_rebuild)
                                                                                                self.string_rebuild = ''
                                                                                                self.space = 0
                                                                                            else:
                                                                                                self.error = ERROR((self.line + self.string_line)).ERROR3()
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
                                                                                            self.error = ERROR((self.line + self.string_line)).ERROR6()
                                                                                            break
                                                                                    else:
                                                                                        if len( self.storage ) > 1:
                                                                                            self.new_string = self.string_rebuild[: self.idd]
                                                                                            self.new_string, self.error = self.analyze.DELETE_SPACE( self.new_string)
                                                                                            if self.error is None:
                                                                                                self.error = ERROR((self.line + self.string_line)).ERROR3()
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
                                                                                                    self.error = ERROR((self.line +  self.string_line)).ERROR3()
                                                                                                    break
                                                                                                else:
                                                                                                    self.error      = None
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
                                                                                    self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                                    break
                                                            else:
                                                                self.error = ERROR((self.line + self.string_line)).ERROR1(self.normal_string)
                                                                break
                                                    else:
                                                        if self.first_char not in ['"', "'"]:
                                                            self.error = ERROR( (self.line + self.string_line) ).ERROR7(  self.normal_string, str_)
                                                            break
                                                        else:  self.string_rebuild += str_

                                                if self.error is None :
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
                                            if self.space <= 5:   self.space += 1
                                            else:
                                                ############################################################################################
                                                # an error got if this condition was not sastified, if the code a value bigger than five   #
                                                # you're going to see this error on your screen                                            #
                                                ############################################################################################
                                                self.error = ERROR( (self.line + self.string_line) ).ERROR8()
                                                break

                                    else:
                                        ####################################################################################################
                                        # the error got when self.active that is not True, what does it mean excatly , it means that       #
                                        # before typing something you have to used tab, then when tab is used self.active key gave by the  #
                                        # stdin becomes True, else this value it always False.                                             #
                                        ####################################################################################################
                                        self.error = ERROR( (self.line + self.string_line) ).ERROR9( )
                                        break
                                else:  break
                            else :
                                if self.space <= self.max_emtyLine:  self.space += 1
                                else:
                                    self.error = ERROR(self.if_line).ERROR9()
                                    break
        
                            # initialization block
                            self.input           = self.main_input
                            self.index           = self.length
                            self.s               = ''
                            self.string          = ''
                            self.I               = 0
                            self.I_S             = 0
                            self.get             = []
                            self.idd             = 0   
                            self.last            = 0
                            self.remove_tab      = 0     

                        # move cursor on left
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                        # clear entire line
                        sys.stdout.write(bm.clear.line(pos=0))
                        
                        if self.term == 'orion':
                            # key word activation 
                            sys.stdout.write(self.main_input+bm.string().syntax_highlight(name=bm.words(string=self.s, color=bm.fg.rbg(255,255,255)).final()))
                        else:
                            # any activation keyword 
                            sys.stdout.write(self.main_input+bm.fg.rbg(255,255,255)+self.s+bm.init.reset)
                        # move cusror on left egain 
                        sys.stdout.write(bm.move_cursor.LEFT(pos=1000))

                        # put cursor on the right position 
                        if self.index > 0:
                            pos = len(self.s) + self.size + len(self.input) - self.index
                            sys.stdout.write(bm.move_cursor.RIGHT(pos=pos))
                        else: pass
                        sys.stdout.flush() 
                    else: pass
                else: pass
            except KeyboardInterrupt:
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break
            except TypeError:
                self.error = IfError.ERRORS(self.if_line).ERROR4()
                break

        if self.error is None :
            self.string = ''
            for str_ in self.storage[ self.len_storage : ]:  self.string += str_
        else: pass

        return self.string, self.error

    def GET_CLOSE(self):
        self.close = ''

        if   self.first_char == '[': self.close      = ']'
        elif self.first_char == '(': self.close      = ')'
        elif self.first_char == '{': self.close      = '}'
        elif self.first_char == '"': self.close      = '"'
        elif self.first_char == "'": self.close      = "'"

        return self.close

class SUB_STRING_FOR_INTERPRETER:
    
    def __init__(self, first_char, data_base, line):
        self.first_char     = first_char                                                                                # first char before moving here                                                                               # last char before moving here
        self.data_base      = data_base                                                                                 # data base with all variables
        self.line           = line                                                                                      # line from the last while loop
        self.analyze        = control_string.STRING_ANALYSE( self.data_base, self.line )                                # string functions
        self.upper_case     = self.analyze.UPPER_CASE()                                                                 # upper cases
        self.lower_case     = self.analyze.LOWER_CASE()                                                                 # lower cases
        self.chars          = CHARS( ).chars + self.lower_case + self.upper_case                                        # authorized chars

    def SUB_STR(self, _id_: int, storage, MainList : list = [], lastString: str =  ''):
        
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
                                                    self.error = ERROR((self.line + self.string_line)).ERROR1(self.normal_string)
                                                    break
                                                else:
                                                    if self.storage[-1][-1] in [',']:
                                                        if str_ == self.close:
                                                            self.error = ERROR((self.line + self.string_line)).ERROR2()
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
                                                                self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                break
                                                        else:
                                                            if len(self.storage[0]) > 1:
                                                                if str_ == self.close:
                                                                    self.storage.append(self.string_rebuild)
                                                                    self.key_break  = True
                                                                    break
                                                                else:
                                                                    self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                    break
                                                            else:
                                                                self.open   = NUMBER().OPENING( self.close )
                                                                self.error = ERROR((self.line + self.string_line)).ERROR4( self.open, self.close )
                                                                break

                                            else:
                                                if self.normal_string[ 0 ]  not in  [',']   :
                                                    if i < len( self.normal_string ) - 1:
                                                        if str_ in [',']:
                                                            self.stest_string, self.error       = self.analyze.DELETE_SPACE(
                                                                        self.string_rebuild[: - 1])

                                                            if self.error is None:
                                                                if self.close in self.string_rebuild:
                                                                    self.open   = NUMBER().OPENING( self.close )
                                                                    self.left   = self.normal_string.count( self.open )
                                                                    self.right  = self.normal_string.count( self.close )
                                                                    self.idd    = self.string_rebuild.index( self.close )

                                                                    if self.left == self.right:
                                                                        self.storage.append(self.string_rebuild)
                                                                        self.string_rebuild     = ''
                                                                        self.space              = 0
                                                                    else:
                                                                        self.error = ERROR((self.line + self.string_line)).ERROR0(  self.normal_string)
                                                                        break
                                                                else:
                                                                    self.storage.append( self.string_rebuild )
                                                                    self.string_rebuild             = ''
                                                                    self.space                      = 0
                                                            else:
                                                                self.error = ERROR((self.line + self.string_line)).ERROR5(  self.normal_string)
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
                                                                        self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                        break
                                                                    else:
                                                                        if len( self.storage[ 0 ] ) == 1:
                                                                            self.storage.append(self.string_rebuild)
                                                                            self.string_rebuild = ''
                                                                            self.space = 0
                                                                        else:
                                                                            self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                            break
                                                            else:
                                                                self.error = ERROR((self.line + self.string_line)).ERROR5( self.normal_string)
                                                                break

                                                        else:
                                                            if str_ ==  self.close:
                                                                self.open       = NUMBER().OPENING(self.close)
                                                                self.left       = self.normal_string.count(self.open)
                                                                self.right      = self.normal_string.count(self.close)

                                                                if self.left != self.right:
                                                                    if self.storage[-1][-1] in [',']:

                                                                        if len( self.string_rebuild ) == 1:
                                                                            self.error = ERROR((self.line + self.string_line)).ERROR2()
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
                                                                                self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                                break
                                                                else:
                                                                    if self.storage[-1][-1] in [',']:
                                                                        self.storage.append( self.string_rebuild )
                                                                        self.string_rebuild     = ''
                                                                        self.space              = 0
                                                                    else:
                                                                        if len(self.storage) > 1:
                                                                            self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                            break

                                                                        else:
                                                                            if len(self.storage[0]) == 1:
                                                                                self.storage.append( self.string_rebuild )
                                                                                self.string_rebuild     = ''
                                                                                self.space              = 0

                                                                            else:
                                                                                self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                                break

                                                            else:
                                                                if self.close in self.string_rebuild:
                                                                    self.open       = NUMBER().OPENING( self.close )
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
                                                                                self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                                break
                                                                            else:
                                                                                if len(self.storage[0]) == 1:
                                                                                    self.storage.append(self.string_rebuild)
                                                                                    self.string_rebuild     = ''
                                                                                    self.space              = 0
                                                                                else:
                                                                                    self.error = ERROR((self.line + self.string_line)).ERROR3()
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
                                                                                self.error = ERROR((self.line + self.string_line)).ERROR6()
                                                                                break
                                                                        else:
                                                                            if len( self.storage ) > 1:
                                                                                self.new_string = self.string_rebuild[: self.idd]
                                                                                self.new_string, self.error = self.analyze.DELETE_SPACE( self.new_string)
                                                                                if self.error is None:
                                                                                    self.error = ERROR((self.line + self.string_line)).ERROR3()
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
                                                                                        self.error = ERROR((self.line +  self.string_line)).ERROR3()
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
                                                                        self.error = ERROR((self.line + self.string_line)).ERROR3()
                                                                        break
                                                else:
                                                    self.error = ERROR((self.line + self.string_line)).ERROR1(self.normal_string)
                                                    break
                                        else:
                                            if self.first_char not in ['"', "'"]:
                                                self.error = ERROR( (self.line + self.string_line) ).ERROR7(  self.normal_string, str_)
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
                                    self.error = ERROR( (self.line + self.string_line) ).ERROR8()
                                    break

                        else:
                            ####################################################################################################
                            # the error got when self.active that is not True, what does it mean excatly , it means that       #
                            # before typing something you have to used tab, then when tab is used self.active key gave by the  #
                            # stdin becomes True, else this value it always False.                                             #
                            ####################################################################################################
                            self.error = ERROR( (self.line + self.string_line) ).ERROR9( )
                            break
                    else:  break
                except KeyboardInterrupt: break
                except EOFError:  break
        else: self.error = ERROR( self.initLine ).ERROR9()
        
        if self.error is None:
            if self.loopActivation is True:
                if self.isBreak is True: pass 
                else: self.error = ERROR( self.initLine ).ERROR0( lastString  )
            else: pass
        else: pass
        
        if self.error is None :
            self.string = ''
            for str_ in self.storage[ self.len_storage : ]:
                self.string += str_
        else: pass

        return self.string, self.error

class SEGMENTATION_FOR_INTERPRETER:
    def __init__(self,
                    master      : str,          # concatenate main string after checking tabulation and comment line
                    long_chaine : str,          # non-concatenate main string after checking tabulation and comment line
                    data_base   : dict,         # data base
                    line        : int           # current line
                 ):
        self.master         = master
        self.long_chaine    = long_chaine
        self.line           = line
        self.data_base      = data_base
        self.analyze        = control_string.STRING_ANALYSE( self.data_base, self.line )   # string analyses

    def TREATEMENT(self,
                        _id_        : int,          # _id_ value for indentations
                        MainList    : str           # Main List
                   ):
        
        self.left                   = 0         # firt left bracket
        self.rigth                  = 0         # last right bracket
        self.initialize             = [ None ]  # initialization bracket research
        self.active_key             = None      # when left braket was detected
        self.string                 = ''        # string
        self.string_in_true         = ''        # string used in True block
        self.storage_value          = []        # storing list
        self.error                  = None      # error
        self.if_key_is_true         = None      # if left and rigth bracket was found
        self.str_id                 = False     # id string, used to compte ['"', "'"] when self.id it's False i start counting of left
                                                #   .the left value takes 1 as a value and self.id takes True values and i start counting the rigth values
                                                #   .however the max left and right is 1, it means that for this you cannot have more than 1 ['"' or "'"]
        self.str_id_                = False
        self.key_bracket            = None      # key bracket it means that you cannot have right bracket before letf bracket
                                                # [, {, ( come before '), }, ] else self.key_bracket stays None and you get an error
        try:
            self.master , self.error        = self.analyze.DELETE_SPACE( self.master )           # removing right and left space
            self.long_chaine, self.error    = self.analyze.DELETE_SPACE( self.long_chaine )      # removing right and left space

            if self.error is None:

                for i, str_ in enumerate( self.long_chaine ):
                    if str_ in SUB_STRING( '', self.data_base, self.line ).chars:

                        if str_ in [ '[', '(', '{', '"', "'" ]:

                            if str_ == '('  : char1 = str_.index( '(' )
                            else            : char1 = int( NUMBER().number )

                            if  str_ == '[' : char2 = str_.index( '[' )
                            else            : char2 = int( NUMBER().number )

                            if  str_ == '{' : char3 = str_.index( '{' )
                            else            : char3 = int( NUMBER().number )

                            if  str_ == '"' : char4 = str_.index( '"' )
                            else            : char4 = int( NUMBER().number )

                            if str_ == "'"  : char5 = str_.index("'")
                            else            : char5 = int( NUMBER().number )

                            if self.initialize[ 0 ] is None:

                                if char1 < char2 and char1 < char3 and char1 < char4 and char1 < char5:
                                    self.initialize[ 0 ] = '('

                                if char2 < char1 and char2 < char3 and char2 < char4 and char2 < char5:
                                    self.initialize[ 0 ] = '['

                                if char3 < char1 and char3 < char2 and char3 < char4 and char3 < char5:
                                    self.initialize[ 0 ] = '{'

                                if char4 < char1 and char4 < char2 and char4 < char3 and char4 < char5:
                                    self.initialize[ 0 ] = '"'

                                if char5 < char1 and char5 < char2 and char5 < char3 and char5 < char4:
                                    self.initialize[ 0 ] = "'"

                                self.key_bracket = True

                            else: self.initialize = self.initialize

                        else:
                            if str_ in [']', ')', '}'] and self.key_bracket is None:
                                self.open = NUMBER().OPENING( str_ )                        # if srtr_ = '(' so, self.open = ')'
                                self.error = ERROR( self.line ).ERROR_TREATMENT2( self.long_chaine, str_ )
                                break
                            else: pass

                        if self.initialize [ 0 ] is not None :
                            if self.initialize[0] == '(' :
                                self.left, self.rigth = self.left + str_.count( '(' ), self.rigth + str_.count( ')' )

                            if self.initialize[ 0 ] == '[':
                                self.left, self.rigth = self.left + str_.count( '[' ), self.rigth + str_.count( ']' )

                            if self.initialize[ 0 ] == '{':
                                self.left, self.rigth = self.left + str_.count( '{' ), self.rigth + str_.count( '}' )

                            if self.initialize[ 0 ] == '"':
                                if self.str_id == False:
                                    self.left               = 1
                                    self.rigth              = 0
                                    self.str_id             = True
                                else:
                                    if self.rigth <= 1:
                                        self.rigth  = self.rigth + str_.count( '"' )
                                        self.left   = self.left
                                    else:
                                        self.error = ERROR( self.line ).ERROR_TREATMENT3( self.long_chaine )
                                        break

                            if self.initialize[ 0 ] == "'":
                                if self.str_id_ == False:
                                    self.left               = 1
                                    self.rigth              = 0
                                    self.str_id_            = True
                                else:
                                    if self.rigth <= 1:
                                        self.rigth  = self.rigth + str_.count( "'" )
                                        self.left   = self.left
                                    else:
                                        self.error = ERROR( self.line ).ERROR_TREATMENT3( self.long_chaine )
                                        break
                        else: pass

                        # condition to make self.active_key True
                        if self.left != self.rigth  : self.active_key = True
                        else                        : self.active_key = False

                        if self.active_key == True :

                            self.string         += str_
                            self.string_in_true += str_

                            if i == len( self.long_chaine ) - 1 :
                                self.if_key_is_true = True

                                if self.initialize[ 0 ] not in ['"', "'"]:
                                    if ( self.left - self.rigth ) == 1:
                                        self.store, self.error = SEGMENTATION( self.master, self.long_chaine, self.data_base,
                                                        self.line ).STRING_IN_TRUE_BLOCK(self.string_in_true, self.string )

                                        if self.error is None:
                                            self.new_str, self.error = SUB_STRING_FOR_INTERPRETER( self.initialize[ 0 ], self.data_base,
                                                                                self.line ).SUB_STR( _id_, self.store, MainList, self.long_chaine )

                                            if self.error is None:
                                                self.string += self.new_str
                                            else: break
                                        else: break
                                    else:
                                        self.error = ERROR( self.line ).ERROR_TREATMENT4( self.long_chaine, self.initialize[ 0 ] )
                                        break
                                else: pass
                            else: pass
                        else:
                            if self.if_key_is_true is None  : self.string = self.string +  str_
                            else                            : self.if_key_is_true = None


                            ################################################################################################
                            # initialization part                                                                          #
                            # even if self.active_key didn't take True value it's important to make that initialization    #
                            # to be sure that we are going with the good initial paremeters .                              #
                            ################################################################################################

                            self.initialize[ 0 ]    = None
                            self.left               = 0
                            self.rigth              = 0
                            self.str_id             = False
                            self.str_id_            = False
                            self.key_bracket        = None
                            self.string_in_true     = ''
                    else:
                        if str_ in [ '\t' ]     : self.string += ' '
                        elif str_ in [ '\n' ]   : self.string += '{}\n'.format( '' )
                        else:
                            self.error = ERROR( self.line ).ERROR7( self.long_chaine, str_ )
                            break
            else: pass

            if self.error is None:
                for str_ in [ '[', '(', '{' ]:
                    if str_ in self.string:
                        self.close      = SUB_STRING(str_, self.data_base, self.line).GET_CLOSE()     # if str_ = [, so self.close = ]
                        self.left       = self.string.count( str_ )                                   # left counting
                        self.right      = self.string.count( self.close )                             # right counting

                        if self.left == self.right: pass
                        else:
                            if self.left > self.right:
                                self.error  = ERROR( self.line ).ERROR_TREATMENT1( self.string, str_ )
                                break
                            else:
                                self.error  = ERROR( self.line ).ERROR_TREATMENT2( self.string, self.close )
                                break
                    else: pass

                if self.error is None:
                    for str_ in [']', ')', '}']:
                        if str_ in self.string:
                            self.open       = NUMBER().OPENING( str_ )                                  # if str_ = ( so, self.open = )
                            self.left       = self.string.count( self.open )                            # left counting
                            self.right      = self.string.count( str_ )                                 # right counting

                            if self.left == self.right: pass
                            else:
                                if self.left > self.right:
                                    self.error = ERROR( self.line ).ERROR_TREATMENT1( self.string, self.open )
                                    break
                                else:
                                    self.error = ERROR( self.line ).ERROR_TREATMENT2( self.string, str_ )
                                    break
                        else: pass

                    if self.error is None:
                        self.str__          = None
                        self._idd_          = None
                        self.transform      = False

                        if ( self.string[ 0 ] == "'" )  and ( self.string[ -1 ]== "'" ) :
                            self.string     = '"' + self.string[ 1 : -1 ] + '"'
                            self.transform  = True
                        else: pass

                        for str_ in ['"', "'"]:
                            if str_ in  self.string :
                                self.str__ = str_
                                self._idd_ = self.string.index( self.str__ )
                                break
                            else: pass

                        if self.str__ is not None:
                            self.count = self.string.count( self.str__ )
                            if self.count % 2 == 0: pass
                            else:
                                if self._idd_ == 0: self.error = ERROR( self.line ).ERROR_TREATMENT1( self.string, self.str__ )
                                else: self.error = ERROR( self.line ).ERROR_TREATMENT2( self.string, self.str__ )
                        else: pass
                    else: pass
                else: pass
            else: pass
        except IndexError: pass

        return self.string, self.error

class STR:
    def __init__(self, master: str, line: int):
        self.master         = master
        self.line           = line  
        
    def STR(self):
        op = ['[', '{', '(']
        close = [']', '}', ')']
        quote = ['"', "'"]
        key = {"main":None, 'sub_main':None}
        index = 'closed'
        to1, to2, to3 = 0, 0, 0
        tc1, tc2, tc3 = 0, 0, 0
        self.error = None
        
        if self.master: pass 
        else:
            for i, s in enumerate(self.master):
                if s in quote: 
                    if key['main'] is None: 
                        key['main']=s
                        index = "opened"
                    else:
                        if s == key['main']: 
                            if key['sub_main'] is None:
                                key['main'] = None
                                index = 'closed'
                            else: 
                                self.error  = ERROR( self.line ).ERROR_TREATMENT1( self.master, key['sub_main'], key['main'] )
                                break
                        else:
                            if key['sub_main'] is None: key['sub_main'] = s 
                            else: key['sub_main'] = None
                else:
                    if index == 'opened':
                        if s in op:
                            if s == '[': to1 += 1
                            elif s == '(': to2 +=1
                            else: to3 =+ 1
                        elif s in close:
                            if s == ']': tc1 += 1
                            elif s == ')': tc2 +=1
                            else: tc3 =+ 1
                        else: pass 
                    else:
                        if to1 == tc1: tc1, to1 = 0, 0
                        else:
                            if to1 > tc1:
                                self.error  = ERROR( self.line ).ERROR_TREATMENT1( self.master, '[' )
                                break
                            else:
                                self.error  = ERROR( self.line ).ERROR_TREATMENT2( self.master, ']')
                                break
                        
                        if to2 == tc2: tc2, to2 = 0, 0
                        else:
                            if to2 > tc2:
                                self.error  = ERROR( self.line ).ERROR_TREATMENT1( self.master, '(')
                                break
                            else:
                                self.error  = ERROR( self.line ).ERROR_TREATMENT2( self.master, ')')
                                break
                        
                        if to3 == tc3: tc3, to3 = 0, 0
                        else: 
                            if to3 > tc3:
                                self.error  = ERROR( self.line ).ERROR_TREATMENT1( self.master, '{' )
                                break
                            else:
                                self.error  = ERROR( self.line ).ERROR_TREATMENT2( self.master, '}')
                                break 
        return self.error       
                  
class ERROR:
    def __init__(self, line: int):
        self.line       = line
        self.cyan       = bm.fg.cyan_L
        self.red        = bm.fg.red_L
        self.green      = bm.fg.green_L
        self.yellow     = bm.fg.yellow_L
        self.magenta    = bm.fg.magenta_M
        self.white      = bm.fg.white_L
        self.blue       = bm.fg.blue_L
        self.reset      = bm.init.reset

    def ERROR0(self, string: str ):
        error = ' {}line: {}{}'.format( self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>.'.format(self.white, self.cyan, string)+error

        return self.error+self.reset

    def ERROR1(self, string: str ):
        error       = '{}due to {}<< , >> {}at the beginning. {}line: {}{}'.format(self.white, self.red, self.yellow, 
                                                                                   self.white, self.yellow,self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax, in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR2(self):
        error       = '{}<< , >> {}on the previous line. {}line: {}{}'.format(self.red, self.yellow, 
                                                                              self.white,self.yellow, (self.line-1) )
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax, due to '.format(self.white) + error

        return self.error+self.reset

    def ERROR3(self):
        error       = '{}<< , >> {}was not set on the previous line. {}line: {}{}'.format(self.red, self.yellow,
                                                                                          self.white, self.yellow, (self.line - 1) )
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax '.format(self.white) + error

        return self.error+self.reset

    def ERROR4(self, _open_: str, _close_: str):
        error       = '{}<< {} {} >> {}line: {}{}'.format(self.blue, _open_,  _close_, 
                                                          self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax, due no value inside '.format(self.white) + error

        return  self.error+self.reset

    def ERROR5(self, string: str):
        error       = '{}due to {}no value {}before {}<< , >>. {}line: {}{}'.format(ke, ve, ke, ne, we, ke, self.line )
        self.error  = '{}{} : invalid syntax in {} << {} >>, '.format(ke,'SyntaxError', ae, string) + error

        return self.error+self.reset

    def ERROR6(self):
        error       = '{}<< , >> {} at the end on the previous line. line: {}{}'.format(self.red, self.white, self.yellow, (self.line - 1))
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax, due to '.format(self.white) + error

        return  self.error+self.reset

    def ERROR7(self, mains_tring: str, sub_string: str):

        error = '{}due to bad {}char, {}<< {} >>. {}line: {}{}'.format(self.white, self.red, self.green, sub_string, 
                                                                       self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, mains_tring) + error

        return self.error+self.reset

    def ERROR8(self):
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}syntax error, {}EMPTY {}value was detected. {}line : {}{}'.format(self.white,
                                                    self.green, self.yellow, self.white, self.yellow, self.line)

        return  self.error+self.reset

    def ERROR9(self):
        self.error = fe.FileErrors( 'IndentationError' ).Errors() + '{}unexpected an indented block. {}line : {}{}'.format(self.yellow, 
                                                self.white, self.yellow, self.line)

        return self.error+self.reset

    def ERROR_TREATMENT1(self, string: str, _open_: str):
        error       = '{}close {}the {}opening {}<< {} >>. {}line: {}{}'.format(self.green, self.white, self.red, self.blue,
                                                                        _open_, self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR_TREATMENT2(self, string: str, _close_: str):
        error       = '{}open {}<< {} >> {}before {}closing. {}line: {}{}'.format(self.green, self.blue, _close_, self.white, self.red, 
                                                                                  self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR_TREATMENT3(self, string: str):
        error       = '{}due to, too much  {}<< " >> {}characters. {}line: {}{}'.format(self.white, self.red, self.yellow,
                                                                                self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR_TREATMENT4(self, string: str, _open_: str):
        error       = '{}due to many {}opening {}<< {} >>. {}line: {}{}'.format(self.white, self.green, self.red, _open_, 
                                                                                self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR_TREATMENT5(self, string: str, close1: str, close2: str):
        error       = '{}close {}<< {} >> {}before {}closing {}{}. {}line: {}{}'.format(self.green, self.blue, close1, self.white, self.red, self.yellow, close2,
                                                                                  self.white, self.yellow, self.line)
        self.error  = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

