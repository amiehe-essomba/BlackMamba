from script                             import control_string
from CythonModules.Windows.LEXER.seg    import num
from CythonModules.Windows.LEXER.seg    import segError as SE
from CythonModules.Windows.LEXER.seg    import subString

cdef class SEGMENTATION:
    cdef public:
        str master , long_chaine
        dict data_base 
        unsigned long long int line  

    cdef :
        str error 
        unsigned long int left, right
        str string, string_in_true 
        list storage_value, initialize
        bint str_id, str_id_, key_bracket, active_key, if_key_is_true

    def __cinit__(self,
        master      ,        # concatenate main string after checking tabulation and comment line
        long_chaine ,        # non-concatenate main string after checking tabulation and comment line
        data_base   ,        # data base
        line        ,        # current line
        ):

        # main string
        self.master         = master
        # self.main string
        self.long_chaine    = long_chaine
        # current line 
        self.line           = line
        # data base
        self.data_base      = data_base
        # error
        self.error          = ''
        # last right bracket
        self.right          = 0
        # firt left bracket
        self.left           = 0
        # string
        self.string         = ''
        # string used in True block
        self.string_in_true = ''
        self.str_id         = False 
        # id string, used to compte ['"', "'"] when self.id it's False i start counting of left
        #   .the left value takes 1 as a value and self.id takes True values and i start counting the rigth values
        #   .however the max left and right is 1, it means that for this you cannot have more than 1 ['"' or "'"]
        self.str_id_        = False
        # initialization bracket research
        self.initialize     = [ None ]
        # storing list
        self.storage_value  = []
        # key bracket it means that you cannot have right bracket before letf bracket
        # [, {, ( come before '), }, ] else self.key_bracket stays None and you get an error
        self.key_bracket    = False
        # when left braket was detected
        self.active_key     = False
        # if left and rigth bracket was found
        self.if_key_is_true = False

    cdef tuple TREATEMENT(self,
        unsigned long int _id_   ,  # _id_ value for indentations
        str color                   # color used for the blocks
        ):

        cdef:
            signed long long int i 
            str str_, char1, char2, char3, char4, char5, str__
            str Open, Close
            list list_of_string = ['[','(','{', '"', "'"]    
            signed int _idd_     
            bint transform
            unsigned long int count  
        
        try:
            try:
                # removing right and left space
                self.master , self.error        = control_string.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( self.master, 'cython' )   
                # removing right and left space
                self.long_chaine, self.error    = control_string.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( self.long_chaine, 'cython' )      
            except TypeError: pass

            if not self.error :

                for i, str_ in enumerate( self.long_chaine ):
                    if str_ in subString.SUB_STRING( '', self.data_base, self.line ).chars:

                        if str_ in list_of_string:

                            if str_ == '('  : char1 = str_.index( '(' )
                            else            : char1 = int( num.NUMBER().number )

                            if  str_ == '[' : char2 = str_.index( '[' )
                            else            : char2 = int( num.NUMBER().number )

                            if  str_ == '{' : char3 = str_.index( '{' )
                            else            : char3 = int( num.NUMBER().number )

                            if  str_ == '"' : char4 = str_.index( '"' )
                            else            : char4 = int( num.NUMBER().number )

                            if str_ == "'"  : char5 = str_.index("'")
                            else            : char5 = int( num.NUMBER().number )

                            if self.initialize[ 0 ] is None:
                                if char1 < char2 and char1 < char3 and char1 < char4 and char1 < char5: self.initialize[ 0 ] = '('
                                if char2 < char1 and char2 < char3 and char2 < char4 and char2 < char5: self.initialize[ 0 ] = '['
                                if char3 < char1 and char3 < char2 and char3 < char4 and char3 < char5: self.initialize[ 0 ] = '{'
                                if char4 < char1 and char4 < char2 and char4 < char3 and char4 < char5: self.initialize[ 0 ] = '"'
                                if char5 < char1 and char5 < char2 and char5 < char3 and char5 < char4: self.initialize[ 0 ] = "'"
                                self.key_bracket = True
                            else: pass

                        else:
                            if str_ in [']', ')', '}'] and self.key_bracket is False:
                                Open = num.NUMBER().OPENING( str_ )                   
                                self.error = SE.ERROR( self.line ).ERROR_TREATMENT2( self.long_chaine, str_ )
                                break
                            else: pass

                        if self.initialize [ 0 ] is not None :
                            if self.initialize[0]   == '(':
                                self.left, self.right = self.left + str_.count( '(' ), self.rigth + str_.count( ')' )

                            if self.initialize[ 0 ] == '[':
                                self.left, self.right = self.left + str_.count( '[' ), self.rigth + str_.count( ']' )

                            if self.initialize[ 0 ] == '{':
                                self.left, self.right = self.left + str_.count( '{' ), self.rigth + str_.count( '}' )

                            if self.initialize[ 0 ] == '"':
                                if self.str_id == False:
                                    self.left               = 1
                                    self.right              = 0
                                    self.str_id             = True
                                else:
                                    if self.right <= 1:
                                        self.right  = self.right + str_.count( '"' )
                                        self.left   = self.left
                                    else:
                                        self.error = SE.ERROR( self.line ).ERROR_TREATMENT3( self.long_chaine )
                                        break

                            if self.initialize[ 0 ] == "'":
                                if self.str_id_ == False:
                                    self.left               = 1
                                    self.right              = 0
                                    self.str_id_            = True
                                else:
                                    if self.right <= 1:
                                        self.right  = self.rigth + str_.count( "'" )
                                        self.left   = self.left
                                    else:
                                        self.error = SE.ERROR( self.line ).ERROR_TREATMENT3( self.long_chaine )
                                        break
                        else: pass

                        if self.left != self.right  : self.active_key = True
                        else                        : self.active_key = False

                        if self.active_key is True :
                            self.string         += str_
                            self.string_in_true += str_

                            if i == len( self.long_chaine ) - 1:
                                self.if_key_is_true = True

                                if self.initialize[ 0 ] not in ['"', "'"]:
                                    if ( self.left - self.right ) == 1:
                                        self.store, self.error = SEGMENTATION( self.master, self.long_chaine, self.data_base,
                                                        self.line ).STRING_IN_TRUE_BLOCK(self.string_in_true, self.string )

                                        if not self.error:
                                            self.new_str, self.error = subString.SUB_STRING( self.initialize[ 0 ], self.data_base,
                                                                                self.line ).SUB_STR( _id_, color, self.store )

                                            if not self.error:
                                                self.string += self.new_str
                                            else: break
                                        else: break
                                    else:
                                        self.error = SE.ERROR( self.line ).ERROR_TREATMENT4( self.long_chaine, self.initialize[ 0 ] )
                                        break
                                else: pass
                            else: pass
                        else:
                            if self.if_key_is_true is False  : self.string = self.string +  str_
                            else                             : self.if_key_is_true = False


                            ################################################################################################
                            # initialization part                                                                          #
                            # even if self.active_key didn't take True value it's important to make that initialization    #
                            # to be sure that we are going with the good initial paremeters .                              #
                            ################################################################################################

                            self.initialize[ 0 ]    = None
                            self.left               = 0
                            self.right              = 0
                            self.str_id             = False
                            self.str_id_            = False
                            self.key_bracket        = False
                            self.string_in_true     = ''
                    else:
                        if str_ in [ '\t' ]     : self.string += ' '
                        elif str_ in [ '\n' ]   : self.string += '{}\n'.format( '' )
                        else:
                            self.error = SE.ERROR( self.line ).ERROR7( self.long_chaine, str_ )
                            break
            
            else: pass 

            if not self.error:
                for str_ in [ '[', '(', '{' ]:
                    if str_ in self.string:
                        Close           = subString.SUB_STRING(str_, self.data_base, self.line).GET_CLOSE()     
                        self.left       = self.string.count( str_ )                                   
                        self.right      = self.string.count( Close )                                  

                        if self.left == self.right: pass
                        else:
                            if self.string[0] not in ['"', "'"]:
                                if self.left > self.right:
                                    self.error  = SE.ERROR( self.line ).ERROR_TREATMENT1( self.string, str_ )
                                    break
                                else:
                                    self.error  = SE.ERROR( self.line ).ERROR_TREATMENT2( self.string, Close )
                                    break
                            else: pass
                    else: pass

                if not self.error:
                    for str_ in [']', ')', '}']:
                        if str_ in self.string:
                            Open            = num.NUMBER().OPENING( str_ )                                  
                            self.left       = self.string.count( Open )                            
                            self.right      = self.string.count( str_ )                                 

                            if self.left == self.right: pass
                            else:
                                if self.string[0] not in ['"', "'"]:
                                    if self.left > self.right:
                                        self.error = SE.ERROR( self.line ).ERROR_TREATMENT1( self.string, Open )
                                        break
                                    else:
                                        self.error = SE.ERROR( self.line ).ERROR_TREATMENT2( self.string, str_ )
                                        break
                                else: pass
                        else: pass

                    if not self.error:
                        str__          = ""
                        _idd_          = -1
                        transform      = False

                        if ( self.string[ 0 ] == "'" )  and ( self.string[ -1 ]== "'" ) :
                            self.string     = '"' + self.string[ 1 : -1 ] + '"'
                            transform  = True
                        else: pass

                        for str_ in ['"', "'"]:
                            if str_ in  self.string :
                                str__ = str_
                                _idd_ = self.string.index( str__ )
                                break
                            else: pass

                        if str__ :
                            count = self.string.count( str__ )
                            if count % 2 == 0: pass
                            else:
                                if _idd_ == 0: self.error = SE.ERROR( self.line ).ERROR_TREATMENT1( self.string, str__ )
                                else: self.error = SE.ERROR( self.line ).ERROR_TREATMENT2( self.string, str__ )
                        else: pass
                    else: pass
                else: pass
            else: pass
        except IndexError: pass

        return self.string, self.error

    cdef tuple STRING_IN_TRUE_BLOCK(self,  str string  , str main_string ):
        cdef:
            list storage = []
            unsigned int i
            str str_, String = "", test_string

        for i, str_ in enumerate( string ):
            String        += str_

            if i != len( string ) - 1:
                if str_ in [ ',' ]:
                    try:  test_string, self.error = control_string.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( String[ 1 : -1 ], 'cython' )
                    except TypeError: pass
                         
                    if not  self.error :
                        storage.append( String )
                        String = ''
                    else:
                        self.error = SE.ERROR( self.line ).ERROR5( main_string )
                        break
                else: pass
            else:
                if str_ in [ ',' ]:
                    try:  test_string, self.error = control_string.STRING_ANALYSE( self.data_base, self.line ).DELETE_SPACE( String[ 1 : -1 ], 'cython' )
                    except TypeError: pass

                    if  not self.error:  storage.append( String )
                    else:
                        self.error = SE.ERROR( self.line ).ERROR5( main_string )
                        break
                else: storage.append( String )

        return storage, self.error