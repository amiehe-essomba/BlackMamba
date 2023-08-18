from distutils.log import error
import cython
from script.LEXER.FUNCTION                              import print_value
from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._IF_                import if_statement
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import unless_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.LEXER.FUNCTION                              import main
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS.WHILE               import whileError as WEr
from updatingDataBase                                   import updating
from statement                                          import InternalStatement as IS
from CythonModules.Windows                              import loop_for
from statement.comment                                  import externalCmt
from statement                                          import mainStatement        as MS


@cython.cclass
class EXTERNAL_WHILE_LOOP_STATEMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def WHILE_STATEMENT(self,
                    bool_value      : bool, 
                    tabulation      : int   = 1, 
                    loop_list       : any   = None, 
                    _type_          : str   = 'loop', 
                    keyPass         : bool  = False,
                    main_string     : str   = ''
                    ):
        
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.bool_value             = bool_value
        self.boolean_store          = [ self.bool_value ]
        self.index_else             = 0
        self.if_line                = 0
        self.break_                 = None

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'while' ]
        self.color                  = bm.fg.rbg(255, 20, 174)
        self.before                 = updating.UPDATE( data_base=self.data_base ).BEFORE()
        self.loop_list              = loop_list
        self.next_line              = None

        ############################################################################
        self.keyPass                = keyPass 
        self.max_emtyLine           = 5
        ############################################################################

        if self.keyPass is False:
            while self.bool_value:
                for j, _string_ in enumerate( self.loop_list ):
                    if j != self.next_line :
                        self.if_line                        += 1
                        self.normal_string, self.active_tab = _string_
                        self.string                         = self.normal_string
                        
                        if self.normal_string:
                            if self.active_tab is True:
                                self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string, normal_string=self.normal_string,
                                                data_base=self.data_base, line=self.if_line).BLOCKS(tabulation = self.tabulation + 1,
                                                function = _type_, interpreter = True)

                                if self.error  is None:
                                    if self.get_block   == 'begin:'  :
                                        self.next_line  = j + 1
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'begin' )
                                        self.space = 0
                                        
                                        self.error = comment.COMMENT_LOOP_STATEMENT( self.master, self.data_base, 
                                                                        self.if_line ).COMMENT( self.tabulation + 1,  self.loop_list[ j + 1 ])
                                        if self.error is None: pass
                                        else: break
                                    elif self.get_block == 'if:'     :
                                        self.next_line  = j + 1
                                        self.store_value.append(self.normal_string)
                                        self.history.append('if')
                                        self.space  = 0
                                        
                                        if self.data_base[ 'pass' ] is None: pass 
                                        else: self.keyPass = True
                                        
                                        self.error = if_statement.EXTERNAL_IF_LOOP_STATEMENT(self.master,
                                        self.data_base, self.if_line).IF_STATEMENT( self.value, self.tabulation + 1,
                                                                                    self.loop_list[ j + 1 ],  _type_ = _type_, keyPass = self.keyPass )
                                        if self.error is None: pass
                                        else: break
                                    elif self.get_block == 'try:'    :
                                        self.next_line = j + 1
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'try' )
                                        self.space = 0
                                        
                                        if self.data_base[ 'pass' ] is None: pass 
                                        else: self.keyPass = True
                                        
                                        self.error = try_statement.EXTERNAL_TRY_FOR_STATEMENT( self.master,
                                                        self.data_base, self.if_line).TRY_STATEMENT( self.tabulation + 1,
                                                                        self.loop_list[ self.next_line], keyPass = self.keyPass, _type_ = _type_ )
                                        if self.error is None: pass
                                        else: break
                                    elif self.get_block == 'unless:' :
                                        
                                        self.next_line  = j + 1
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'unless' )
                                        self.space = 0
                                        
                                        if self.data_base[ 'pass' ] is None: pass 
                                        else: self.keyPass = True
                                            
                                        self.error = unless_statement.EXTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                                    self.data_base, self.if_line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                    self.loop_list[ j + 1 ], _type_ = _type_, keyPass = self.keyPass )
                                        if self.error is None: pass
                                        else: break
                                    elif self.get_block == 'for:'    :
                                        self.next_line  = j + 1
                                        self.before     = updating.UPDATE( data_base=self.data_base ).BEFORE()
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'for' )
                                        self.space      = 0
                                        
                                        self.var_name       = self.value[ 'variable' ]
                                        self.for_values_init= self.value[ 'value' ]
                                        self.variables      = self.data_base['variables']['vars'].copy()
                                        self._values_       = self.data_base['variables']['values'].copy()
                                        
                                        if self.var_name in self.variables:
                                            self.idd = self.variables.index( self.var_name )
                                            self._values_[ self.idd ] = self.for_values_init[ 0 ]
                                            self.data_base[ 'variables' ][ 'values' ] = self._values_
                                        else:
                                            self.variables.append( self.var_name )
                                            self._values_.append( self.for_values_init[ 0 ] )
                                            self.data_base[ 'variables' ][ 'values' ]   = self._values_
                                            self.data_base[ 'variables' ][ 'vars' ]     = self.variables

                                        self.error  = loop_for.LOOP( self.data_base, self.if_line ).LOOP( list(self.for_values_init),
                                                                                    self.var_name, True, self.loop_list[ j + 1] )
                                        if self.error is None: pass
                                        else: break
                                    elif self.get_block == 'while:'  :
                                        self.next_line  = j + 1
                                        self.store_value.append(self.normal_string)
                                        self.history.append('while')
                                        self.space  = 0
                                        
                                        if self.data_base[ 'pass' ] is None: pass 
                                        else: self.keyPass = True
                                        self.error = EXTERNAL_WHILE_LOOP_STATEMENT(self.master,
                                        self.data_base, self.if_line).WHILE_STATEMENT( self.value, self.tabulation + 1,
                                                self.loop_list[ j + 1 ],  _type_ = _type_, keyPass = self.keyPass, main_string=main_string )
                                        if self.error is None: pass
                                        else: break
                                    elif self.get_block == 'switch:' :
                                        self.next_line  = j + 1
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'switch' )
                                        self.space = 0
                                        
                                        self.error = switch_statement.SWITCH_LOOP_STATEMENT( self.master , self.data_base,
                                                            self.if_line ).SWITCH( self.value, self.tabulation + 1, self.loop_list[ j + 1 ],
                                                                                _type_ = _type_, keyPass = self.keyPass)
                                        if self.error is None: pass
                                        else: break
                                    elif self.get_block == 'empty'   :
                                        if self.space <= self.max_emtyLine: self.space += 1
                                        else:
                                            self.error = WEr.ERRORS( self.if_line ).ERROR4()
                                            break
                                    elif self.get_block == 'any'     :
                                        self.store_value.append(self.normal_string)
                                        if self.bool_value is True:
                                            if self.data_base[ 'pass' ] is None:
                                                self.error = self.lex_par.LEXER_AND_PARXER( self.value, self.data_base,
                                                                self.line ).ANALYZE( _id_ = 1, _type_ = _type_)
                                                if self.error is None:  
                                                    self.space  = 0
                                                    self.break_ = True
                                                else: break
                                            else: 
                                                self.keyPass    = True
                                                self.error      = main.SCANNER(self.value, self.data_base,
                                                                        self.line).SCANNER(_id_ = 1, _type_ = _type_, _key_ = True )
                                                if self.error is None:  self.space = 0
                                                else: break
                                        else:
                                            self.error = main.SCANNER(self.value, self.data_base,
                                                                    self.if_line).SCANNER(_id_ = 1, _type_ = _type_, _key_ = True )
                                            if self.error is None:  self.space = 0
                                            else: break
                                else: break
                            else:
                                self.get_block, self.value, self.error = externalCmt.EXTERNAL_BLOCKS(
                                                    normal_string=self.normal_string, data_base=self.data_base,
                                                    line=self.if_line).BLOCKS(tabulation=self.tabulation)

                                if self.error is None:
                                    if   self.get_block == 'end:'  :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            del self.boolean_store[ : ]
                                            if self.tabulation == 1:  self.data_base['pass'] = None 
                                            else: pass
                                            break
                                        else:
                                            self.error = WEr.ERRORS( self.if_line ).ERROR2( self.history[ -1 ])
                                            break
                                    elif self.get_block == 'empty' :
                                        if self.space <= self.max_emtyLine: self.space += 1
                                        else:
                                            self.error = WEr.ERRORS( self.if_line ).ERROR4()
                                            break
                                    else:
                                        self.error = WEr.ERRORS( self.if_line ).ERROR4()
                                        break
                                else: break
                        else: pass
                    else:
                        self.if_line        += 1
                        self.next_line      = None
                
                if self.error is None:
                    if self.data_base[ 'print' ] is not None:
                        self.list_of_values = self.data_base[ 'print' ]
                        for i, value in enumerate( self.list_of_values ):
                            if i < len( self.list_of_values ) - 1:
                                print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False, loop = True )
                            else:
                                print_value.PRINT_PRINT( value, self.data_base ).PRINT_PRINT( key = False )             
                    else: pass
                    
                    self.data_base['print'] = []
                    
                    self.bool_value, self.error = MS.MAIN(master = main_string, data_base=self.data_base,
                                line=self.line).MAIN(typ = 'while', opposite = False, interpreter = True, function = 'loop')
                    if self.error is None: pass
                    else: break
                else: break
            self.after      = updating.UPDATE( data_base=self.data_base ).AFTER()
            self.error      = updating.UPDATE( data_base=self.data_base ).UPDATE( before=self.before, after=self.after, error=self.error )
        else: pass
        ############################################################################

        return self.error


