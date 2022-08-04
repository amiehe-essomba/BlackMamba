from distutils.log import error
import cython
from script.LEXER.FUNCTION                              import print_value
from script                                             import control_string
from script.STDIN.WinSTDIN                              import stdin
from script.PARXER.PARXER_FUNCTIONS._FOR_               import end_for_else
from script.PARXER.PARXER_FUNCTIONS._IF_                import end_else_elif, if_statement
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import unless_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.LEXER.FUNCTION                              import main
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:
    from CythonModules.Windows                          import fileError as fe 
except ImportError:
    from CythonModules.Linux                            import fileError as fe
    
try:  from CythonModules.Linux                          import loop_for
except ImportError: from CythonModules.Windows          import loop_for


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
        self.history                = [ 'if' ]
        self.color                  = bm.fg.rbg(255, 20, 174)
        self.before                 = end_else_elif.CHECK_VALUES( self.data_base ).BEFORE()
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
                        self.line                           += 1
                        
                        self.normal_string, self.active_tab = _string_
                        self.string                         = self.normal_string
                        
                        if self.normal_string:
                            if self.active_tab is True:
                                self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.if_line ).BLOCKS( self.tabulation + 1, function = _type_, inter = True )
                                
                                if self.error  is None:
                                    if self.get_block   == 'begin:'  :
                                        self.next_line  = j + 1
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'begin' )
                                        self.space = 0
                                        
                                        self.error = comment.COMMENT_LOOP_STATEMENT( self.master, self.data_base, 
                                                                        self.line ).COMMENT( self.tabulation + 1,  self.loop_list[ j + 1 ]) 
                                        if self.error is None: pass
                                        else: break
                                        
                                    elif self.get_block == 'if:'     :
                                        self.next_line  = j + 1
                                        self.store_value.append(self.normal_string)
                                        self.history.append('if')
                                        self.space  = 0
                                        
                                        if self.data_base[ 'pass' ] is None: pass 
                                        else: self.keyPass = True
                                        
                                        self.error = if_statement.INTERNAL_IF_LOOP_STATEMENT(self.master,
                                        self.data_base, self.line).IF_STATEMENT( self.value, self.tabulation + 1,
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
                                        
                                        self.error = try_statement.INTERNAL_TRY_FOR_STATEMENT( self.master,
                                                        self.data_base, self.line).TRY_STATEMENT( self.tabulation + 1,
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
                                            
                                        self.error = unless_statement.INTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                                    self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                    self.loop_list[ j + 1 ], _type_ = _type_, keyPass = self.keyPass )
                                        if self.error is None: pass
                                        else: break
                                                
                                    elif self.get_block == 'for:'    :
                                        self.next_line  = j + 1
                                        self.before     = end_for_else.CHECK_VALUES(self.data_base).BEFORE()
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'for' )
                                        self.space = 0
                                        
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

                                        
                                        self.error  = loop_for.LOOP( self.data_base, self.line ).LOOP( list(self.for_values_init),
                                                                                    self.var_name, True, self.loop_list[ j + 1] )
                                        if self.error is None: pass
                                        else: break
                                                
                                    elif self.get_block == 'while:'    :
                                        self.next_line  = j + 1
                                        self.store_value.append(self.normal_string)
                                        self.history.append('while')
                                        self.space  = 0
                                        
                                        if self.data_base[ 'pass' ] is None: pass 
                                        else: self.keyPass = True
                                        
                                        self.error = INTERNAL_WHILE_LOOP_STATEMENT(self.master,
                                        self.data_base, self.line).WHILE_STATEMENT( self.value, self.tabulation + 1,
                                                self.loop_list[ j + 1 ],  _type_ = _type_, keyPass = self.keyPass, main_string=main_string )
                                        if self.error is None: pass
                                        else: break
                                                
                                    elif self.get_block == 'switch:' :
                                        self.next_line  = j + 1
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'switch' )
                                        self.space = 0
                                        
                                        self.error = switch_statement.SWITCH_LOOP_STATEMENT( self.master , self.data_base,
                                                            self.line ).SWITCH( self.value, self.tabulation + 1, self.loop_list[ j + 1 ],
                                                                                _type_ = _type_, keyPass = self.keyPass)
                                        if self.error is None: pass
                                        else: break

                                    elif self.get_block == 'empty'   :
                                        if self.space <= self.max_emtyLine: self.space += 1
                                        else:
                                            self.error = ERRORS( self.line ).ERROR4()
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
                                                                    self.line).SCANNER(_id_ = 1, _type_ = _type_, _key_ = True )
                                            if self.error is None:  self.space = 0
                                            else: break
                                else: break
                            else:
                                self.get_block, self.value, self.error = end_for_else.EXTERNAL_BLOCKS(self.string,
                                            self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )

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
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break

                                    elif self.get_block == 'empty' :
                                        if self.space <= self.max_emtyLine: self.space += 1
                                        else:
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break
                                    
                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break

                                else: break
                        else: pass
                    else:
                        self.if_line        += 1
                        self.line           += 1
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
                    
                    self.bool_value, self.error = end_else_elif.MAIN_IF( main_string, self.data_base, self.line ).BOCKS( typ = 'while' )
                    if self.error is None: pass
                    else: break
                    
                else: break
     
            self.after      = end_else_elif.CHECK_VALUES( self.data_base ).AFTER()
            self.error      = end_else_elif.CHECK_VALUES( self.data_base ).UPDATE( self.before, self.after, self.error )
        else: pass
        
        ############################################################################

        return self.error

@cython.cclass
class INTERNAL_WHILE_LOOP_STATEMENT:
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
                    tabulation      : int, 
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
        self.history                = [ 'if' ]
        self.color                  = bm.fg.magenta_M
        self.before                 = end_else_elif.CHECK_VALUES( self.data_base ).BEFORE()
        self.loop_list              = loop_list
        self.next_line              = 0

        ############################################################################
        self.keyPass                = keyPass 
        self.key                    = False
        self.max_emtyLine           = 5
        ############################################################################

        if self.keyPass is False:
            while self.bool_value:
                for j, _string_ in enumerate( self.loop_list ):
                    
                    if self.next_line == 0: self.key = True 
                    else:
                        if self.next_line != j: self.key = True 
                        else: self.key = False 
                    
                    if self.key == True:
                        
                        self.if_line                        += 1
                        self.line                           += 1
                        
                        self.normal_string, self.active_tab     = _string_
                        self.string                             = self.normal_string

                        if self.string :
                            if self.active_tab is True:
                                self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.if_line ).BLOCKS( self.tabulation + 1, function = _type_, inter = True )
                            
                                if self.error  is None:
                                    if self.get_block   == 'begin:' :
                                        self.next_line  = j + 1
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'begin' )
                                        self.space = 0
                                        
                                        if self.history[ -1 ] in ['else', 'elif']:
                                            if self.bool_value is True :
                                                self.error = comment.COMMENT_LOOP_STATEMENT( self.master, self.data_base, 
                                                                                self.line ).COMMENT( self.tabulation + 1,  self.loop_list[ j + 1 ]) 
                                                if self.error is None: pass
                                                else: pass
                                            else: pass
                                        else: 
                                            self.error = comment.COMMENT_LOOP_STATEMENT( self.master, self.data_base, 
                                                                            self.line ).COMMENT( self.tabulation + 1,  self.loop_list[ j + 1 ]) 
                                            if self.error is None: pass
                                            else: break

                                    elif self.get_block == 'if:'    :
                                        self.next_line  = j + 1
                                        self.store_value.append(self.normal_string)
                                        self.history.append('if')
                                        self.space  = 0
                                        
                                        if self.data_base[ 'pass' ] is None: pass 
                                        else: self.keyPass = True
                                        
                                        self.error = if_statement.EXTERNAL_IF_LOOP_STATEMENT(self.master,
                                        self.data_base, self.line).IF_STATEMENT( self.value, self.tabulation + 1,
                                                                                    self.loop_list[ j + 1 ],  _type_ = _type_, keyPass = self.keyPass )
                                        if self.error is None: pass
                                        else: break
                                      
                                    elif self.get_block == 'while:' :
                                        self.next_line  = j + 1
                                        self.store_value.append(self.normal_string)
                                        self.history.append('while')
                                        self.space  = 0
                                        
                                        if self.data_base[ 'pass' ] is None: pass 
                                        else: self.keyPass = True
                                        
                                        self.error = EXTERNAL_WHILE_LOOP_STATEMENT(self.master,
                                        self.data_base, self.line).WHILE_STATEMENT( self.value, self.tabulation + 1,
                                                self.loop_list[ j + 1 ],  _type_ = _type_, keyPass = self.keyPass, main_string=main_string )
                                        if self.error is None: pass
                                        else: break
                                            
                                    elif self.get_block == 'try:'   :
                                        self.next_line = j + 1
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'try' )
                                        self.space = 0
                                        
                                        if self.data_base[ 'pass' ] is None: pass 
                                        else: self.keyPass = True
                                        
                                        
                                        self.error = try_statement.EXTERNAL_TRY_FOR_STATEMENT( self.master,
                                                        self.data_base, self.line).TRY_STATEMENT( self.tabulation + 1,
                                                                        self.loop_list[ self.next_line], keyPass = self.keyPass, _type_ = _type_ )
                                        if self.error is None: pass
                                        else: break

                                    elif self.get_block == 'unless:':
                                        
                                        self.error = unless_statement.EXTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                                self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                self.loop_list[ j + 1 ], _type_ = _type_, keyPass = self.keyPass )
                                        if self.error is None: pass
                                        else: break
                                                
                                    elif self.get_block == 'for:'   :
                                        self.next_line  = j + 1
                                        self.before     = end_for_else.CHECK_VALUES(self.data_base).BEFORE()
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'for' )
                                        self.space = 0
                                        
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

                                        self.error  = loop_for.LOOP( self.data_base, self.line ).LOOP( list(self.for_values_init),
                                                                                self.var_name, True, self.loop_list[ j + 1] )
                                        if self.error is None: pass
                                        else: break
                                                
                                    elif self.get_block == 'switch:':
                                        self.next_line  = j + 1
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'switch' )
                                        self.space = 0
                                        
                                        self.error = switch_statement.SWITCH_LOOP_STATEMENT( self.master , self.data_base,
                                                            self.line ).SWITCH( self.value, self.tabulation + 1, 
                                                                        self.loop_list[ j + 1 ], _type_ = _type_, keyPass = self.keyPass )
                                        if self.error is None: pass
                                        else: break

                                    elif self.get_block == 'empty'  :
                                        if self.space <= self.max_emtyLine:  self.space += 1
                                        else:   
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break

                                    elif self.get_block == 'any'    :
                                        self.store_value.append( self.normal_string )
                                        if self.bool_value is True:
                                            if self.data_base[ 'pass' ] is None:
                                                self.error = self.lex_par.LEXER_AND_PARXER(self.value, self.data_base,
                                                            self.line ).ANALYZE( _id_ = 1, _type_ = _type_ )
                                                if self.error is None:  
                                                    self.space  = 0
                                                    self.break_ = True
                                                else: break
                                            else:
                                                self.keyPass    = True
                                                self.error      = main.SCANNER(self.value, self.data_base,
                                                                    self.line).SCANNER(_id_ = 1, _type_= _type_, _key_=True)
                                                if self.error is None:  self.space = 0
                                                else: break
                                        else:
                                            self.error = main.SCANNER(self.value, self.data_base,
                                                                self.line).SCANNER(_id_ = 1, _type_= _type_, _key_=True)
                                            if self.error is None:  self.space = 0
                                            else: break
                                else: break 
                            else:
                                self.get_block, self.value, self.error = end_for_else.EXTERNAL_BLOCKS(self.string,
                                            self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )
                            
                                if self.error is None:
                                    if self.get_block   == 'end:' :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            del self.boolean_store[ : ]
                                            
                                            if self.tabulation == 1:  self.data_base['pass'] = None 
                                            else: pass

                                            break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break

                                    elif self.get_block == 'empty':
                                        if self.space <= self.max_emtyLine: self.space += 1
                                        else:
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break

                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break

                                else : break
                        else: pass
                    else:
                        self.if_line        += 1
                        self.line           += 1
                        #self.next_line      = None
                
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
                        
                    self.bool_value, self.error = end_else_elif.MAIN_IF( main_string, self.data_base, self.line ).BOCKS( typ = 'while' )
                    if self.error is None: pass
                    else: break
                    
                else: break
                
            self.after = end_else_elif.CHECK_VALUES( self.data_base ).AFTER()
            self.error = end_else_elif.CHECK_VALUES( self.data_base ).UPDATE( self.before, self.after, self.error )
        else: pass

        ############################################################################

        return self.error

class ERRORS:
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

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,
                                                                                                       self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str = 'else'):
        error = '{}is already defined. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. {}<< {} >> {}block '.format(self.white,
                                                                                self.cyan, string, self.green) + error
        return self.error+self.reset

    def ERROR2(self, string):
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format(self.green, self.white, self.cyan, string, self.green,
                                                                                             self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax '.format( self.white ) + error

        return self.error+self.reset

    def ERROR3(self, string: str = 'else'):
        error = 'due to {}many {}<< {} >> {}blocks. {}line: {}{}'.format(self.green, self.cyan, string, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax '.format( self.white ) + error

        return self.error+self.reset

    def ERROR4(self):
        self.error =  fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                    self.white, self.yellow, self.line )
        return self.error+self.reset

