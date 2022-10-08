from script                     import control_string

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