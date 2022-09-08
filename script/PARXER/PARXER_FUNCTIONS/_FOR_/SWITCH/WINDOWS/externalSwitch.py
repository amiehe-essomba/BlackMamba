from script.LEXER.FUNCTION                              import main
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switchError as sE
from script                                             import control_string
from statement                                          import InternalStatement as IS
from statement                                          import externalSwitch as ES

class EXTERNAL_SWITCH:
    def __init__(self, 
            master      : str,              
            data_base   : dict,             
            line        : int ,
            history     : list,
            store_value : list,
            space       : int,    
            case_block  : dict
            ):
        
        # main string
        self.master             = master
        # current line in the IDE
        self.line               = line
        # data base 
        self.data_base          = data_base
        # history of command 
        self.history            = history
        # canceling def when any command was not typed
        self.store_value        = store_value
        # counting empty line 
        self.space              = space
        #canceling def 
        self.def_cancel         = False
        #contriling string
        self.analyse            = control_string.STRING_ANALYSE(self.data_base, self.line)
        # else block 
        self.case_block         = case_block

    def SWITCH(self, 
            any_value       : any,                  # can take any values
            loop            : list,                 # loop for storing values
            tabulation      : int   = 1,            # tabular for indentation . default value = 1
            _type_          : str   = 'conditional' # type of struction 
            ) -> tuple:
        
        ############################################################################
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.index_else             = 0
        self.if_line                = self.line

        ############################################################################
        self.bool_value             = ''
        self.boolean_store          = []
        self.key_else_activation    = self.case_block['key_else_activation']
        self.data_activation        = self.case_block['data_activation']
        self.active_tab             = None
        self.tabulation             = tabulation
        self.max_emtyLine           = 5
        self.loop                   = loop
        self.switch_break           = False
        ############################################################################

        for i in range(1): 
            # concatening string and extraction of string concatenated , tabulation for and indensation and error        
            self.string, self.active_tab, self.error = self.analyse.BUILD_CON(string=self.master,
                                                                        tabulation=self.tabulation)
            if self.error is None:
                # build normal string 
                self.normal_string = self.analyse.BUILD_NON_CON(string=self.master, tabulation=self.tabulation)

                # when indentation is True
                if self.active_tab is True:

                    self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                            data_base=self.data_base, line=self.if_line).BLOCKS(tabulation = self.tabulation + 1, function = _type_,
                                                                                interpreter = False)

                    if self.error  is None:
                        # empty line 
                        if   self.get_block == 'empty'  :
                            self.store_value.append(self.normal_string)
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.loop.append( (self.normal_string, True) )
                            else:
                                self.error = sE.ERRORS( self.if_line).ERROR4()
                                break
                        # checking value 
                        elif self.get_block == 'any'    :
                            self.store_value.append( self.normal_string )
    
                            if self.data_activation is True:
                                self.space = 0
                                self.error = main.SCANNER( self.value, self.data_base,  self.line).SCANNER(_id_ = 1,
                                                                                _type_ = _type_, _key_=True)
                                if self.error is None:  self.loop.append( (self.normal_string, True) )
                                else: break
                            else:
                                self.error = sE.ERRORS( self.if_line ).ERROR6()
                                break
                        else:
                            self.error = sE.ERRORS( self.if_line ).ERROR4()
                            break          
                    else:  break
                else:
                    self.get_block, self.value, self.error = ES.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                data_base=self.data_base, line=self.if_line).BLOCKS(tabulation=self.tabulation,  function=_type_, interpreter=False)

                    if self.error is None:
                        # break switch statement
                        if   self.get_block == 'end:'     :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                del self.boolean_store[ : ]
                                self.loop.append( (self.normal_string, False) )
                                self.switch_break = True
                                break
                            else:
                                self.error = sE.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                break
                        # case block
                        elif self.get_block == 'case:'    :
                            if self.key_else_activation == None:
                                if self.store_value:
                                    self.history.append( 'case' )
                                    self.store_value        = []
                                    self.data_activation    = True
                                    self.bool_key           = None
                                    self.loop.append( (self.normal_string, False) )
                                    
                                else:
                                    self.error = sE.ERRORS( self.if_line ).ERROR2( self.history[ -1 ] )
                                    break
                            else:
                                self.error = sE.ERRORS( self.if_line ).ERROR1( 'default' )
                                break
                        # default block 
                        elif self.get_block == 'default:' :
                            if self.index_else < 1:
                                if self.data_activation is True:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append( 'default' )
                                        self.bool_key               = None
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = sE.ERRORS( self.if_line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = sE.ERRORS( self.if_line ).ERROR5( 'case' )
                                    break
                            else:
                                self.error = sE.ERRORS( self.if_line ).ERROR3( 'default' )
                                break
                        # empty line 
                        elif self.get_block == 'empty'    :
                            if self.space <= self.max_emtyLine: 
                                self.loop.append( (self.normal_string, False) )
                                self.space += 1
                            else:
                                self.error = sE.ERRORS( self.if_line ).ERROR4()
                                break
                        else:
                            self.error = sE.ERRORS( self.if_line ).ERROR4()
                            break
                    else:  break
            else:
                if self.tabulation == 1:  break
                else:
                    # if tabulation is false ( not indentation)
                    self.error = None
                    self.normal_string = self.analyse.BUILD_NON_CON(string=self.master,tabulation=self.tabulation)
                    
                    self.get_block, self.value, self.error = ES.EXTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                                    data_base=self.data_base, line=self.if_line).BLOCKS(tabulation=self.tabulation,
                                                    function=_type_, interpreter=False)

                    if self.error is None:
                        # break switch satelment
                        if self.get_block   == 'end:'    :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                del self.boolean_store[ : ]
                                self.loop.append( (self.normal_string, False) )
                                self.switch_break = True
                                break
                            else:
                                self.error = sE.ERRORS( self.if_line ).ERROR2(self.history[ -1 ] )
                                break
                        # case block
                        elif self.get_block == 'case:'   :
                            if self.key_else_activation == None:
                                if self.store_value:
                                    self.history.append( 'case' )
                                    self.store_value        = []
                                    self.data_activation    = True
                                    self.bool_key           = None
                                    self.loop.append( (self.normal_string, False) )

                                else:
                                    self.error = sE.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                    break
                            else:
                                self.error = sE.ERRORS( self.if_line ).ERROR1( 'default' )
                                break
                        # default block
                        elif self.get_block == 'default:':
                            if self.index_else < 1:
                                if self.data_activation is True:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append( 'default' )
                                        self.bool_key               = None
                                        self.loop.append( (self.normal_string, False) )

                                    else:
                                        self.error = sE.ERRORS( self.if_line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = sE.ERRORS( self.if_line ).ERROR5( 'case' )
                                    break
                            else:
                                self.error = sE.ERRORS( self.if_line ).ERROR3( 'default' )
                                break
                        # empty line 
                        elif self.get_block == 'empty'   :
                            if self.space <= self.max_emtyLine:
                                self.space += 1
                                self.loop.append( (self.normal_string, False) )
                            else:
                                self.error = sE.ERRORS(  self.if_line ).ERROR4()
                                break
                        else:
                            self.error = sE.ERRORS( self.if_line ).ERROR4()
                            break
                    else: break

        ###############################################################################
        self.case_block['key_else_activation']  = self.key_else_activation
        self.case_block['data_activation']      = self.data_activation
        ###############################################################################
        
        return self.loop, self.switch_break, self.error

