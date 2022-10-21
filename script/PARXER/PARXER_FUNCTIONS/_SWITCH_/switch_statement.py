import cython
from script                                     import control_string
from script.PARXER.LEXER_CONFIGURE              import lexer_and_parxer
from script.PARXER.PARXER_FUNCTIONS._SWITCH_    import case
from updatingDataBase                           import updating
from statement                                  import InternalStatement    as IS
from statement                                  import externalSwitch       as ES
from script.PARXER.PARXER_FUNCTIONS._SWITCH_    import switchError          as sE

@cython.cclass
class SWITCH_LOOP_STATEMENT:
    def __init__(self, 
                master      : any,
                data_base   : dict,
                line        : int
                ) -> None:

        # current line
        self.line                   = line
        # can take any value
        self.master                 = master
        # main data base
        self.data_base              = data_base
        # controling string
        self.analyze                = control_string.STRING_ANALYSE(self.data_base, self.line)
        # loading lexer_and_parxer
        self.lex_par                = lexer_and_parxer

    @cython.cfunc
    def SWITCH(self,
        main_values     : any,
        tabulation      : int   = 1, 
        loop_list       : any   = None, 
        _type_          : str   = 'conditional', 
        keyPass         : bool  = False
        ) -> str :

        ##############################################################################
        self.error                  = None              # error
        self.string                 = ''                # concatenated string
        self.normal_string          = ''                # normal string
        self.end                    = ''                # break switch statement
        self.store_value            = []                # storing value
        self.main_value             = main_values       # main values
        self.index_else             = 0                 # index for controling the default case
        self.if_line                = 0                 # counting line
        self.break_                 = None              # break loop for
        self.data_activation        = None              # activating data calculation

        ############################################################################

        self.key_else_activation    = None              # when default is already activated case one cannot be used
        self.space                  = 0                 # space
        self.active_tab             = None              # activating indentation
        self.tabulation             = tabulation        # indentation used
        self.history                = [ 'switch' ]      # history of commands
        self.store_value            = [ 'swtich' ]      # storing value
        self.before                 = updating.UPDATE( data_base=self.data_base ).BEFORE() # values before running switch
        self.loop_list              = loop_list         # input of values containing history of commands
        self.next_line              = None              # next line
        self.boolean_store          = []                # storing boolean values

        ############################################################################
        self.keyPass                = keyPass           # is pass function  was used
        self.max_emtyLine           = 5                 # max empty line for space variable
        ############################################################################

        if self.keyPass is False:
            for j, _string_ in enumerate( self.loop_list ):
                if j != self.next_line :
                    self.if_line                        += 1
                    #self.line                           += 1
                    self.normal_string, self.active_tab = _string_
                    self.string                         = self.normal_string
                    
                    if self.normal_string:
                        if self.active_tab is True:
                            self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string,
                                normal_string=self.normal_string, data_base=self.data_base, line=self.if_line).BLOCKS(
                                tabulation=self.tabulation + 1, function=_type_, interpreter=True)

                            if self.error  is None:
                                # empty line
                                if   self.get_block == 'empty'   :
                                    # condition for space line
                                    if self.space <= self.max_emtyLine: 
                                        self.space += 1
                                        self.store_value.append(self.normal_string)
                                    else:
                                        self.error = sE.ERRORS( self.line ).ERROR4()
                                        break
                                # computing values
                                elif self.get_block == 'any'     :
                                    self.store_value.append(self.normal_string)
                                    if self.data_activation is True:
                                        if self.bool_value is True:
                                            if self.data_base[ 'pass' ] is None:
                                                # running lexer and parxer
                                                self.error = self.lex_par.LEXER_AND_PARXER( self.value, self.data_base,
                                                                self.line ).ANALYZE( _id_ = 1, _type_ = _type_)
                                                if self.error is None:
                                                    # initialization of value
                                                    self.space  = 0
                                                    self.break_ = True
                                                    break
                                                else: break
                                            else: pass
                                        else: pass
                                    else:
                                        self.error = sE.ERRORS( self.if_line ).ERROR6()
                                        break
                            else: break
                        else:
                            self.get_block, self.value, self.error = ES.EXTERNAL_BLOCKS(string=self.string,
                                    normal_string=self.normal_string,   data_base=self.data_base,
                                    line=self.if_line).BLOCKS(  tabulation=self.tabulation, function=_type_, interpreter=True)

                            if self.error is None:
                                # break loop for when "end" is detected
                                if   self.get_block == 'end:'       :
                                    if self.store_value:
                                        del self.store_value[ : ]
                                        del self.history[ : ]
                                        del self.boolean_store[ : ]
                                        if self.tabulation == 1:  self.data_base['pass'] = None 
                                        else: pass
                                        break
                                    else:
                                        self.error = sE.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                        break
                                # case block
                                elif self.get_block == 'case:'      :
                                    if self.key_else_activation == None:
                                        if self.store_value:
                                            self.history.append( 'case' )
                                            self.store_value        = []
                                            self.data_activation    = True
                                            self.bool_key           = None
                                            # checking value
                                            self.bool_value = case.CASE_TREATMENT( main_master=self.main_value, master=self.value ).CASE( )
                                            for _bool_ in self.boolean_store:
                                                if _bool_ is True:
                                                    self.bool_key = True
                                                    break
                                                else: self.bool_key = False

                                            if self.bool_key is True:  self.bool_value = False
                                            else: self.bool_value = self.bool_value

                                            self.boolean_store.append(self.bool_value)
                                            
                                            self.data_base[ 'pass' ]    = None
                                            self.keyPass                = False

                                        else:
                                            self.error = sE.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = sE.ERRORS( self.line ).ERROR1( 'default' )
                                        break
                                # default case
                                elif self.get_block == 'default:'   :
                                    if self.index_else < 1:
                                        if self.data_activation is True:
                                            if self.store_value:
                                                self.index_else             += 1
                                                self.key_else_activation    = True
                                                self.store_value            = []
                                                self.history.append( 'default' )
                                                self.bool_key               = None
                                                
                                                for _bool_ in self.boolean_store:
                                                    if _bool_ is True:
                                                        self.bool_key = True
                                                        break
                                                    else: self.bool_key = False

                                                if self.bool_key is True: self.bool_value = False
                                                else: self.bool_value = True
                                                
                                                self.data_base[ 'pass' ]    = None
                                                self.keyPass                = False
                                            else:
                                                self.error = sE.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                                break
                                        else:
                                            self.error = sE.ERRORS( self.line ).ERROR5( 'case' )
                                            break
                                    else:
                                        self.error = sE.ERRORS( self.line ).ERROR3( 'default' )
                                        break
                                # empty line
                                elif self.get_block == 'empty'      :
                                    if self.space <= self.max_emtyLine: self.space += 1
                                    else:
                                        self.error = sE.ERRORS( self.line ).ERROR4()
                                        break
                                else:
                                    self.error = sE.ERRORS( self.line ).ERROR4()
                                    break
                            else: break
                    else: pass
                else:
                    self.if_line        += 1
                    self.line           += 1
                    self.next_line      = None
            
            self.after      = updating.UPDATE( data_base=self.data_base ).AFTER()
            self.error      = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, after=self.after, error=self.error )
        else: pass

        ############################################################################
        return self.error
