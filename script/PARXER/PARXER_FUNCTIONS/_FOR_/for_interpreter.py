from script                                             import control_string
from script.STDIN.WinSTDIN                              import stdin
import cython
from script.PARXER.PARXER_FUNCTIONS._FOR_               import end_for_else
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.PARXER.PARXER_FUNCTIONS._IF_                import if_inter
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import unless_interpreter as ui
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_try
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_statement
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:
    from CythonModules.Windows                          import fileError as fe 
except ImportError:
    from CythonModules.Linux                            import fileError as fe


class EXTERNAL_FOR_STATEMENT:
    def __init__(self, 
                master      :any, 
                data_base   :dict, 
                line        :int
                ):
        
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def FOR_STATEMENT(self, 
                    tabulation  : int   = 1, 
                    loop_list   : list  = [], 
                    _type_      : str   = 'loop',
                    loop        : bool  = False
                    ):
        
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_else             = 0
        self.if_line                = 0

        ############################################################################

        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'for' ]
        self.loop_for               = []

        ############################################################################
        self.loop_list              = loop_list
        self.next_line              = 0
        ############################################################################
        
        if self.loop_list:
            for j, _string_ in enumerate( self.loop_list ):
                self.if_line    += 1
                self.line       += 1

                if _string_:
                    if j >= self.next_line:
                        k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)                   
                        self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                            self.line ).STDIN_FOR_INTERPRETER( k, _string_ )
                        
                        if self.error is None:
                            if self.active_tab is True:
                                self.get_block, self.value, self.error = end_for_else.INTERNAL_BLOCKS( self.string,
                                                self.normal_string, self.data_base, self.line ).BLOCKS( k + 1, loop = loop, function = _type_ )
                                
                                if self.error  is None:

                                    if self.get_block   == 'if:'            :
                                        self.next_line              = j+1
                                        self.store_if_values        = []
                                        self.store_if_values.append( (self.normal_string, True) )
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = if_inter.INTERNAL_IF_STATEMENT(self.master,
                                                                self.data_base, self.line).IF_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('if')
                                                self.space      = 0
                                                self.store_if_values.append( self._values_ )
                                                self.loop_for.append( {'if' : self.store_if_values, 'value' : self.value,
                                                                    'tabulation' : k } )
                                                self.store_if_values = []
                                            else: break
                                        else: 
                                            self.error = if_inter.ERRORS( self.line ).ERROR4()
                                            break

                                    elif self.get_block == 'unless:'        :
                                        self.store_if_values    = []
                                        self.store_if_values.append( (self.normal_string, True) )
                                        self.next_line              = j+1
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = ui.INTERNAL_UNLESS_STATEMENT(self.master,
                                                                self.data_base, self.line).UNLESS_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('unless')
                                                self.space      = 0
                                                self.store_if_values.append( self._values_ )
                                                self.loop_for.append( {'unless' : self.store_if_values, 'value' : self.value,
                                                                    'tabulation' : k } )
                                                self.store_if_values = []
                                            else: break
                                        else: 
                                            self.error = if_inter.ERRORS( self.line ).ERROR4()
                                            break
                                        
                                    elif self.get_block == 'for:'           :
                                        self.store_if_values    = []
                                        self.store_if_values.append( (self.normal_string, True) )
                                        self.next_line              = j+1
                                   
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self._, self.error = INTERNAL_FOR_STATEMENT(self.master,
                                                                self.data_base, self.line).FOR_STATEMENT( k, self.NewLIST,  _type_ = _type_, loop = loop )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('unless')
                                                self.space      = 0
                                                self.store_if_values.append( self._values_ )
                                                self.loop_for.append( {'for' : self.store_if_values, 'value' : self.value,
                                                                    'tabulation' : k } )
                                                self.store_if_values = []
                                            else: break
                                        else: 
                                            self.error = if_inter.ERRORS( self.line ).ERROR4()
                                            break

                                    elif self.get_block == 'empty'          :
                                        if self.space <= 2:
                                            self.space += 1
                                            self.loop_for.append( {'empty' : (self.normal_string, True), 'value': None,
                                                                'tabulation' : k } )
                                        else:
                                            self.error = for_statement.ERRORS( self.line ).ERROR4()
                                            break

                                    elif self.get_block == 'any'            :
                                        self.store_value.append( self.normal_string )
                                        self._lexer_, self.error = self.lex_par.MAIN(self.value, self.data_base,
                                                                            self.line).MAIN_LEXER( _id_=1, _type_='loop' )
                                        if self.error is None:
                                            self.loop_for.append( {'any' : (self.value, True), 'value' : None,
                                                                'tabulation' : k, 'lex' : self._lexer_} )
                                            self.space  = 0
                                        else:
                                            self.error = self.error
                                            break

                                    ########################################################
                                    ########################################################
                                    
                                    elif   self.get_block == 'end:'         :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.loop_for.append( (self.normal_string, False) )

                                        else:
                                            self.error =  for_statement.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break
                                
                                else: break

                            else:
                                self.get_block, self.value, self.error = end_for_else.EXTERNAL_BLOCKS( self.string,
                                            self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                                if self.error is None:
                                    if   self.get_block == 'end:'  :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.loop_for.append( (self.normal_string, False) )

                                            break
                                        else:
                                            self.error =  for_statement.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break

                                    elif self.get_block == 'else:' :
                                        if self.index_else < 1:
                                            if self.store_value:
                                                self.index_else             += 1
                                                self.store_value            = []
                                                self.history.append( 'else' )
                                                self.loop_for.append( (self.normal_string, False) )

                                            else:
                                                self.error =  for_statement.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                                break

                                        else:
                                            self.error =  for_statement.ERRORS( self.line ).ERROR3( 'else' )
                                            break

                                    elif self.get_block == 'empty' :
                                        if self.space <= 2:
                                            self.space += 1
                                            self.loop_for.append( (self.normal_string, False ))
                                        else:
                                            self.error =  for_statement.ERRORS( self.line ).ERROR4()
                                            break

                                    else:
                                        self.error =  for_statement.ERRORS( self.line ).ERROR4()
                                        break
                                else: break

                        else:break   
                    else: pass
                else:
                    self.error = if_inter.ERRORS( self.line ).ERROR4()
                    break
        else:
            self.error = if_inter.ERRORS( self.line ).ERROR5('for')
        ############################################################################

        return {'for' : self.loop_for},  self.tabulation, self.error

class INTERNAL_FOR_STATEMENT:
    def __init__(self, master:any, data_base:dict, line:int):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def FOR_STATEMENT(self, 
                    tabulation  : int,
                    loop_list   : list  = [],
                    _type_      : str   = 'loop',
                    loop        : bool  = False
                    ):
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_else             = 0
        self.if_line                = 0

        ############################################################################

        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'for' ]
        self.loop_for               = []
    
        ############################################################################
        self.loop_list              = loop_list
        self.next_line              = 0
        ############################################################################

        if self.loop_list:
            for j, _string_ in enumerate( self.loop_list ):
                self.if_line    += 1
                self.line       += 1

                if _string_:
                    if j >= self.next_line:
                        k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)                   
                        self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                            self.line ).STDIN_FOR_INTERPRETER( k, _string_ )
                        
                        if self.error is None:
                            if self.active_tab is True:
                                self.get_block, self.value, self.error = end_for_else.INTERNAL_BLOCKS( self.string,
                                                self.normal_string, self.data_base, self.line ).BLOCKS( k + 1, loop = loop, function = _type_ )
                                
                                if self.error  is None:

                                    if self.get_block   == 'if:'            :
                                        self.next_line              = j+1
                                        self.store_if_values        = []
                                        self.store_if_values.append( (self.normal_string, True) )
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = if_inter.INTERNAL_IF_STATEMENT(self.master,
                                                                self.data_base, self.line).IF_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('if')
                                                self.space      = 0
                                                self.store_if_values.append( self._values_ )
                                                self.loop_for.append( {'if' : self.store_if_values, 'value' : self.value,
                                                                    'tabulation' : k } )
                                                self.store_if_values = []
                                            else: break
                                        else: 
                                            self.error = if_inter.ERRORS( self.line ).ERROR4()
                                            break

                                    elif self.get_block == 'unless:'        :
                                        self.store_if_values    = []
                                        self.store_if_values.append( (self.normal_string, True) )
                                        self.next_line              = j+1
            
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self.error = ui.INTERNAL_UNLESS_STATEMENT(self.master,
                                                                self.data_base, self.line).UNLESS_STATEMENT( k, self.NewLIST,  _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('unless')
                                                self.space      = 0
                                                self.store_if_values.append( self._values_ )
                                                self.loop_for.append( {'unless' : self.store_if_values, 'value' : self.value,
                                                                    'tabulation' : k } )
                                                self.store_if_values = []
                                            else: break
                                        else: 
                                            self.error = if_inter.ERRORS( self.line ).ERROR4()
                                            break

                                    elif self.get_block == 'for:'           :
                                        self.store_if_values    = []
                                        self.store_if_values.append( (self.normal_string, True) )
                                        self.next_line              = j+1
                                        
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            self._values_, self._, self.error = EXTERNAL_FOR_STATEMENT(self.master,
                                                                self.data_base, self.line).FOR_STATEMENT( k, self.NewLIST,  _type_ = _type_, loop = loop )
                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append('unless')
                                                self.space      = 0
                                                self.store_if_values.append( self._values_ )
                                                self.loop_for.append( {'for' : self.store_if_values, 'value' : self.value,
                                                                    'tabulation' : k } )
                                                self.store_if_values = []
                                            else: break
                                        else: 
                                            self.error = if_inter.ERRORS( self.line ).ERROR4()
                                            break

                                    elif self.get_block == 'empty'          :
                                        if self.space <= 2:
                                            self.space += 1
                                            self.loop_for.append( {'empty' : (self.normal_string, True), 'value': None,
                                                                'tabulation' : k } )
                                        else:
                                            self.error = for_statement.ERRORS( self.line ).ERROR4()
                                            break

                                    elif self.get_block == 'any'            :
                                        self.store_value.append( self.normal_string )
                                        self._lexer_, self.error = self.lex_par.MAIN(self.value, self.data_base,
                                                                            self.line).MAIN_LEXER( _id_=1, _type_='loop' )
                                        if self.error is None:
                                            self.loop_for.append( {'any' : (self.value, True), 'value' : None,
                                                                'tabulation' : k, 'lex' : self._lexer_} )
                                            self.space  = 0
                                        else:
                                            self.error = self.error
                                            break

                                    ########################################################
                                    ########################################################
                                    
                                    elif   self.get_block == 'end:'         :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.loop_for.append( (self.normal_string, False) )

                                        else:
                                            self.error =  for_statement.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break
                                
                                else: break

                            else:
                                self.get_block, self.value, self.error = end_for_else.EXTERNAL_BLOCKS( self.string,
                                            self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                                if self.error is None:
                                    if   self.get_block == 'end:'  :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            self.loop_for.append( (self.normal_string, False) )

                                            break
                                        else:
                                            self.error =  for_statement.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break

                                    elif self.get_block == 'else:' :
                                        if self.index_else < 1:
                                            if self.store_value:
                                                self.index_else             += 1
                                                self.store_value            = []
                                                self.history.append( 'else' )
                                                self.loop_for.append( (self.normal_string, False) )

                                            else:
                                                self.error =  for_statement.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                                break

                                        else:
                                            self.error =  for_statement.ERRORS( self.line ).ERROR3( 'else' )
                                            break

                                    elif self.get_block == 'empty' :
                                        if self.space <= 2:
                                            self.space += 1
                                            self.loop_for.append( (self.normal_string, False ))
                                        else:
                                            self.error =  for_statement.ERRORS( self.line ).ERROR4()
                                            break

                                    else:
                                        self.error =  for_statement.ERRORS( self.line ).ERROR4()
                                        break
                                else: break

                        else:break   
                    else: pass
                else:
                    self.error = if_inter.ERRORS( self.line ).ERROR4()
                    break
        else:
            self.error = if_inter.ERRORS( self.line ).ERROR5('for')
        ############################################################################

        return {'for' : self.loop_for},  self.tabulation, self.error