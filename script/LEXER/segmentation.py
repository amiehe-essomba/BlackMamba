import  sys, os, re
from colorama                   import Fore
from script                     import control_string
from script.STDIN.WinSTDIN      import stdin
from script.LEXER               import checking_if_backslash
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS._IF_ import IfError
try:
    from CythonModules.Windows  import fileError as fe 
except ImportError:
    from CythonModules.Linux    import fileError as fe 

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

    def SUB_STR(self, _id_: int, color: str, storage):
        self.string         = ''                                                                                        # concateante string
        self.normal_string  = ''                                                                                        # non-concatenate string
        self.error          =  None                                                                                     # error got during de precess
        self.string_line    = 0                                                                                         # line inside while loop
        self.space          = 0                                                                                         # max lines under the last string
        self.close          = SUB_STRING(self.first_char, self.data_base, self.line).GET_CLOSE()                        # the closing opening bracket
        self.storage        = storage[ : ]                                                                              # a storing list
        self.len_storage    = len( self.storage )
        self.key_break      = False
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

        sys.stdout.write(bm.clear.line(2))
        sys.stdout.write(bm.move_cursor.LEFT(1000))
        sys.stdout.write(bm.string().syntax_highlight(name=self.input))
        sys.stdout.flush()

        while self.normal_string != self.first_char :
            try:
                self.char = bm.read().readchar()
                if self.char not in {10, 13}:
                    self.input      = self.input[: self.index] + chr(self.char) + self.input[self.index:]
                    self.mainString = self.mainString[: self.mainIndex] + chr(self.char) + self.mainString[  self.mainIndex:]
                    self.index      += 1
                    self.mainIndex  += 1
                else:
                    self.string_line += 1
                    sys.stdout.write(bm.move_cursor.LEFT(pos=1000))
                    self.clear_input = self.mainString
                    if self.clear_input:
                        ####################################################################
                        self.string, self.active_tab, self.error = self.analyze.BUILD_CON(string=self.clear_input,  tabulation=_id_)
                        if self.error is None:
                            self.normal_string = self.analyze.BUILD_NON_CON( string=self.clear_input, tabulation=_id_ )
                            self._ = stdin.STDIN(data_base=self.data_base, line=self.line).ENCODING(string=self.clear_input)
                            if (self._ - _id_) == 0:
                                self.input = self.input[: self.length] + bm.words(string=self.mainString, color=color).final()
                            else:
                                self.error = ERROR( self.string_line ).ERROR9()
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
                self._keyboard_ = bm.bg.red_L + bm.fg.white_L + "KeyboardInterrupt" + bm.init.reset
                print(self._keyboard_)
                self.error = IfError.ERRORS(self.string_line).ERROR4()
                break
            except EOFError:  break
            except TypeError:
                self._end_of_file_ = bm.bg.red_L + bm.fg.white_L + "EOFError" + bm.init.reset
                print(self._end_of_file_)
                self.error = IfError.ERRORS(self.string_line).ERROR4()
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
