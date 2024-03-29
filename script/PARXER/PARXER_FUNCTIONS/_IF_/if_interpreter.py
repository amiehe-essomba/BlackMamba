from script                                             import control_string
from script.PARXER.PARXER_FUNCTIONS._IF_                import end_else_elif
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import unless_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment, cmt_interpreter
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.LEXER.FUNCTION                              import main
from script.STDIN.WinSTDIN                              import stdin
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:  from CythonModules.Windows                        import fileError as fe 
except ImportError: from CythonModules.Linux            import fileError as fe


class EXTERNAL_IF_LOOP_STATEMENT:
    def __init__(self, master, data_base, line):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def IF_STATEMENT(self, bool_value: bool, tabulation : int = 1, loop_list: any = None, 
                     _type_: str = 'conditional', keyPass: bool = False):
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
        self.initLine               = self.line
        self.key                    = True
        
        ############################################################################
     
        if self.loop_list:
            for j, _string_ in enumerate( self.loop_list ):
                
                self.if_line                        += 1
                self.line                           += 1
                
                if _string_:
                    if self.next_line is None: self.key  = True 
                    else:
                        if j > self.next_line:  
                            self.key        = True 
                            self.next_line  = None
                        else: self.key = False 
                    
                    if self.key is True :
                        k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)
                        self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                    self.line ).STDIN_FOR_INTERPRETER( k, _string_ )
                        
                        if self.error is None:
                            if self.active_tab is True:
                                self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS( self.string,
                                                self.normal_string, self.data_base, self.line ).INTERPRETER_BLOCKS( k + 1, function = _type_ )
                               
                                if self.error  is None: 
                                    if self.get_block   == 'begin:'  :
                                        self.next_line              = j+1
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        if self.NewLIST:
                                            self.next_line  = len(self.NewLIST)
                                            self.error = cmt_interpreter.COMMENT_STATEMENT(self.master,
                                                                        self.data_base, self.line).COMMENT( k, self.NewLIST )

                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append( 'begin' )
                                                self.space = 0

                                            else: break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break
                                        
                                    elif self.get_block == 'if:'     :
                                        self.next_line              = j+1
                                        self.key_else_activation    = None
                                        self.index_else             = 0
                                        self.store_value.append( self.normal_string )
                                        
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(k, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        if self.NewLIST:
                                            self.next_line  += len(self.NewLIST)
                                            
                                            if self.data_base[ 'pass' ] is None: pass 
                                            else: self.keyPass = True
                                            
                                            if self.history[ -1 ] in [ 'elif', 'else' ]:
                                                if self.value is True:
                                                    self.error = INTERNAL_IF_LOOP_STATEMENT ( self.master,
                                                                self.data_base, self.line ).IF_STATEMENT( self.value, k,
                                                                            self.NewLIST,  _type_ = _type_, keyPass = self.keyPass )
                                                    if self.error is None:
                                                        self.history.append( 'if' )
                                                        self.space      = 0
                                                        self.keyPass    = False
                                                    else: break
                                                else:
                                                    self.history.append( 'if' )
                                                    self.space = 0
                                            else:
                                                self.error = INTERNAL_IF_LOOP_STATEMENT(self.master,
                                                                    self.data_base, self.line).IF_STATEMENT( self.value, k,
                                                                                self.NewLIST,  _type_ = _type_, keyPass = self.keyPass )
                                                if self.error is None:
                                                    self.store_value.append(self.normal_string)
                                                    self.history.append('if')
                                                    self.space      = 0
                                                    
                                                else: break
                                        else: 
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break
                                        
                                    elif self.get_block == 'try:'    :
                                        self.next_line = j + 1
                                        self.error = try_statement.INTERNAL_TRY_FOR_STATEMENT( self.master,
                                                self.data_base, self.line).TRY_STATEMENT( self.tabulation + 1,
                                                                                        self.loop_list[ self.next_line] )

                                        if self.error is None:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'try' )
                                            self.space = 0

                                        else: break

                                    elif self.get_block == 'unless:' :
                                        self.next_line  = j + 1
                                        if self.history[ -1 ] in [ 'else', 'elif' ]:
                                            if self.bool_value is False:
                                                self.error = unless_statement.INTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                                    self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                    self.loop_list[ j + 1 ], _type_ = _type_ )
                                                if self.error is None:
                                                    self.store_value.append( self.normal_string )
                                                    self.history.append( 'unless' )
                                                    self.space = 0
                                                else: break
                                            else:
                                                self.store_value.append( self.normal_string )
                                                self.history.append( 'unless' )
                                                self.space = 0
                                        else:
                                            self.error = unless_statement.INTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                                    self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                    self.loop_list[ j + 1 ], _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append( self.normal_string )
                                                self.history.append( 'unless' )
                                                self.space = 0
                                            else: break

                                    elif self.get_block == 'switch:' :
                                        self.error = switch_statement.SWITCH_STATEMENT( self.master,
                                                    self.data_base, self.line ).SWITCH( self.value, self.tabulation + 1)

                                        if self.error is None:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'switch' )
                                            self.space = 0

                                        else: break

                                    elif self.get_block == 'empty'   :
                                        if self.space <= 2: self.space += 1
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
                                                self.error      = main.SCANNER(self.value, self.data_base,
                                                                        self.line).SCANNER(_id_ = 1, _type_ = _type_, _key_ = True )
                                                if self.error is None:  self.space = 0
                                                else: break
                                        else:
                                            self.error = main.SCANNER(self.value, self.data_base,
                                                                    self.line).SCANNER(_id_ = 1, _type_ = _type_, _key_ = True )
                                            if self.error is None:  self.space = 0
                                            else: break
                                
                                    #################################################################
                                    #################################################################
                                    
                                    elif self.get_block == 'end:'    :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            del self.boolean_store[ : ]
                                            
                                            if self.tabulation == 1:  
                                                self.data_base['pass']  = None 
                                            else: pass
                                            break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break

                                    elif self.get_block == 'elif:'   :
                                        if self.key_else_activation == None:
                                            if self.store_value:
                                                self.history.append( 'elif' )
                                                self.bool_value         = self.value
                                                self.store_value        = []
                                                self.bool_key           = None

                                                for _bool_ in self.boolean_store:
                                                    if _bool_ == True:
                                                        self.bool_key = True
                                                        break
                                                    else: self.bool_key = False
                                                        
                                                if self.bool_key is True: self.bool_value = False
                                                else: self.bool_value = self.bool_value
                                                    
                                                self.boolean_store.append( self.bool_value )
                                                if self.keyPass is False: self.data_base[ 'pass' ] = None
                                                else: pass

                                            else:
                                                self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR1( 'else' )
                                            break

                                    elif self.get_block == 'else:'   :
                                        
                                        if self.index_else < 1:
                                            if self.store_value:
                                                self.index_else             += 1
                                                self.key_else_activation    = True
                                                self.store_value            = []
                                                self.bool_key               = None
                                                self.history.append( 'else' )
                                                
                                                for _bool_ in self.boolean_store:
                                                    if _bool_ == True:
                                                        self.bool_key = True
                                                        break
                                                    else: self.bool_key = False
                                                        
                                                if self.bool_key is True: self.bool_value = False
                                                else: self.bool_value = True
                                                
                                                if self.keyPass is False: self.data_base[ 'pass' ] = None
                                                else: pass
                                                    
                                            else:
                                                self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                                break

                                        else:
                                            self.error = ERRORS( self.line ).ERROR3( 'else' )
                                            break
                                else: break
                                
                            else:
                                
                                self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS( self.string,
                                            self.normal_string, self.data_base, self.line ).BLOCKS( k )
                            
                                if self.error is None:
                                    if   self.get_block == 'end:'  :
                                        if self.store_value:
                                            del self.store_value[ : ]
                                            del self.history[ : ]
                                            del self.boolean_store[ : ]
                                            
                                            if self.tabulation == 1:  
                                                self.data_base['pass']  = None 
                                            else: pass
                                            break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break

                                    elif self.get_block == 'elif:' :
                                        if self.key_else_activation == None:
                                            if self.store_value:
                                                self.history.append( 'elif' )
                                                self.bool_value         = self.value
                                                self.store_value        = []
                                                self.bool_key           = None
                                                
                                                for _bool_ in self.boolean_store:
                                                    if _bool_ == True:
                                                        self.bool_key = True
                                                        break
                                                    else: self.bool_key = False
                                                        
                                                if self.bool_key is True: self.bool_value = False
                                                else: self.bool_value = self.bool_value
                                                    
                                                self.boolean_store.append( self.bool_value )
                                                if self.keyPass is False: self.data_base[ 'pass' ] = None
                                                else: pass

                                            else:
                                                self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR1( 'else' )
                                            break

                                    elif self.get_block == 'else:' :
                                        
                                        if self.index_else < 1:
                                            if self.store_value:
                                                self.index_else             += 1
                                                self.key_else_activation    = True
                                                self.store_value            = []
                                                self.bool_key               = None
                                                self.history.append( 'else' )

                                                for _bool_ in self.boolean_store:
                                                    if _bool_ == True:
                                                        self.bool_key = True
                                                        break
                                                    else: self.bool_key = False
                                                        
                                                if self.bool_key is True: self.bool_value = False
                                                else: self.bool_value = True
                                                
                                                if self.keyPass is False: self.data_base[ 'pass' ] = None
                                                else: pass
                                                    
                                            else:
                                                self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR3( 'else' )
                                            break

                                    elif self.get_block == 'empty' :
                                        if self.space <= 2: self.space += 1
                                        else:
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break
                                    
                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break

                                else: break
                        else: break
                
                    else: pass
                else:pass
                
        else: self.error = ERRORS( self.line ).ERROR4()
        
        self.after      = end_else_elif.CHECK_VALUES( self.data_base ).AFTER()
        self.error      = end_else_elif.CHECK_VALUES( self.data_base ).UPDATE( self.before, self.after, self.error )

        ############################################################################
        
        return self.error

class INTERNAL_IF_LOOP_STATEMENT:
    def __init__(self, master:any, data_base:dict, line:int):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def IF_STATEMENT(self, bool_value: bool, tabulation : int, loop_list:any = None, _type_ :str = 'conditional', keyPass: bool = False):
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
        self.next_line              = None

        ############################################################################
        self.keyPass                = keyPass 
        self.isBreak                = False
        self.initLine               = self.line
        self.key                    = True
        ############################################################################
        
        if self.loop_list:
            for j, _string_ in enumerate( self.loop_list ):
                
                self.if_line                            += 1
                self.line                               += 1
                
                if _string_:
                    if self.next_line is None: self.key  = True 
                    else:
                        if j > self.next_line:   
                            self.key        = True 
                            self.next_line  = None
                        else: self.key = False 
                    
                    if self.key is True:
                        
                        k = stdin.STDIN(self.data_base, self.line ).ENCODING(_string_)
                        self.string, self.normal_string, self.active_tab, self.error =  stdin.STDIN(self.data_base,
                                                                    self.line ).STDIN_FOR_INTERPRETER( k, _string_ )
                        
                        if self.active_tab is True:
                            self.get_block, self.value, self.error = end_else_elif.INTERNAL_BLOCKS(self.string,
                                            self.normal_string, self.data_base, self.line ).INTERPRETER_BLOCKS( k+1, function = _type_)
                            
                            if self.error  is None:
                                if self.get_block   == 'begin:' :
                                    if self.bool_value is True:
                                        self.next_line              = j+1
                                        self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(self.tabulation, self.loop_list[self.next_line : ],
                                                                                                        index = 'int')
                                        if self.NewLIST:
                                            self.next_line  = len(self.NewLIST)
                                            self.error = cmt_interpreter.COMMENT_STATEMENT(self.master,
                                                                        self.data_base, self.line).COMMENT( k, self.NewLIST )

                                            if self.error is None:
                                                self.store_value.append(self.normal_string)
                                                self.history.append( 'begin' )
                                                self.space = 0

                                            else: break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR4()
                                            break
                                
                                elif self.get_block == 'if:'    :
                                    self.next_line              = j+1
                                    self.key_else_activation    = None
                                    self.index_else             = 0
                                    self.store_value.append( self.normal_string )
                                    
                                    self.NewLIST    = stdin.STDIN(self.data_base, self.line ).GROUPBY(k, self.loop_list[self.next_line : ],
                                                                                                    index = 'int')
                                    
                                    if self.NewLIST:
                                        self.next_line += len(self.NewLIST) 
                                        
                                        if self.data_base[ 'pass' ] is None: pass 
                                        else: pass
                                        
                                        if self.history[ -1 ] in [ 'else', 'elif' ]:
                                            if self.bool_value is True:
                                                if self.data_base[ 'pass' ] is None: pass 
                                                else: pass 
                                                
                                                self.error = EXTERNAL_IF_LOOP_STATEMENT(  self.master,
                                                        self.data_base, self.line).IF_STATEMENT( self.value, k ,
                                                                                            self.NewLIST, _type_ = _type_)

                                                if self.error is None:
                                                    self.history.append( 'if' )
                                                    self.space      = 0
                                                else: break
                                            else:
                                                self.history.append( 'if' )
                                                self.space = 0
                                        else:
                                            self.error  = EXTERNAL_IF_LOOP_STATEMENT( self.master,
                                                        self.data_base, self.line).IF_STATEMENT( self.value, k,
                                                                        self.NewLIST,  _type_ = _type_, keyPass = self.keyPass )
                                            if self.error is None:
                                                self.history.append( 'if' )
                                                self.space      = 0
                                            else: break
                                           
                                    else: 
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break
                                        
                                elif self.get_block == 'try:'   :
                                    self.next_line  = j + 1
                                    self.error = try_statement.EXTERNAL_TRY_FOR_STATEMENT(self.master,
                                                        self.data_base,self.line).TRY_STATEMENT(self.tabulation + 1,
                                                        self.loop_list[ self.next_line] )

                                    if self.error is None:
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'try' )
                                        self.space = 0

                                    else: break

                                elif self.get_block == 'unless:':
                                    self.next_line  = j + 1
                                    if self.history[ -1 ] in [ 'else', 'elif' ]:
                                        if self.bool_value is False:
                                            self.error = unless_statement.EXTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                                self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                self.loop_list[ j + 1 ], _type_ = _type_ )
                                            if self.error is None:
                                                self.store_value.append( self.normal_string )
                                                self.history.append( 'unless' )
                                                self.space = 0
                                            else: break
                                        else:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'unless' )
                                            self.space = 0
                                    else:
                                        self.error = unless_statement.EXTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                                                self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                self.loop_list[ j + 1 ], _type_ = _type_ )
                                        if self.error is None:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'unless' )
                                            self.space = 0
                                        else: break
                                        
                                elif self.get_block == 'switch:':
                                    self.error = switch_statement.SWITCH_STATEMENT(self.master,
                                                    self.data_base, self.line).SWITCH(self.value, self.tabulation + 1)

                                    if self.error is None:
                                        self.store_value.append(self.normal_string)
                                        self.history.append('switch')
                                        self.space = 0
                                    else: break

                                elif self.get_block == 'empty'  :
                                    if self.space <= 2:
                                        self.space += 1
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
                                            self.error = main.SCANNER(self.value, self.data_base,
                                                                self.line).SCANNER(_id_ = 1, _type_= _type_, _key_=True)
                                            if self.error is None:  self.space = 0
                                            else: break
                                    else:
                                        
                                        self.error = main.SCANNER(self.value, self.data_base,
                                                            self.line).SCANNER(_id_ = 1, _type_= _type_, _key_=True)
                                        if self.error is None:  self.space = 0
                                        else: break

                                #################################################################
                                #################################################################
                                
                                elif self.get_block == 'end:'   :
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

                                elif self.get_block == 'elif:'  :
                                    if self.key_else_activation == None:
                                        if self.store_value:
                                            self.history.append( 'elif' )
                                            self.bool_value         = self.value
                                            self.store_value        = []
                                            self.bool_key           = None

                                            for _bool_ in self.boolean_store:
                                                if _bool_ == True:
                                                    self.bool_key = True
                                                    break
                                                else:   self.bool_key = False

                                            if self.bool_key is True:   self.bool_value = False
                                            else:   self.bool_value = self.bool_value

                                            self.boolean_store.append(self.bool_value)
                                            if self.keyPass is False: self.data_base[ 'pass' ] = None
                                            else: pass

                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR1( 'else' )
                                        break

                                elif self.get_block == 'else:'  :
                                    
                                    if self.index_else < 1:
                                        if self.store_value:
                                            self.index_else             += 1
                                            self.key_else_activation    = True
                                            self.store_value            = []
                                            self.history.append('else')
                                            self.bool_key               = None

                                            for _bool_ in self.boolean_store:
                                                if _bool_ is True:
                                                    self.bool_key = True
                                                    break
                                                else:   self.bool_key = False

                                            if self.bool_key is True:   self.bool_value = False
                                            else:   self.bool_value = True
                                            
                                            if self.keyPass is False: self.data_base[ 'pass' ] = None
                                            else: pass
                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR3( 'else' )
                                        break
                            
                            else: break 

                        else:  
                           
                            self.get_block, self.value, self.error = end_else_elif.EXTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( k )
                        
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

                                elif self.get_block == 'elif:':
                                    if self.key_else_activation == None:
                                        if self.store_value:
                                            self.history.append( 'elif' )
                                            self.bool_value         = self.value
                                            self.store_value        = []
                                            self.bool_key           = None

                                            for _bool_ in self.boolean_store:
                                                if _bool_ == True:
                                                    self.bool_key = True
                                                    break
                                                else:   self.bool_key = False

                                            if self.bool_key is True:   self.bool_value = False
                                            else:   self.bool_value = self.bool_value

                                            self.boolean_store.append(self.bool_value)
                                            if self.keyPass is False: self.data_base[ 'pass' ] = None
                                            else: pass

                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR1( 'else' )
                                        break

                                elif self.get_block == 'else:':
                                    if self.index_else < 1:
                                        if self.store_value:
                                            self.index_else             += 1
                                            self.key_else_activation    = True
                                            self.store_value            = []
                                            self.history.append('else')
                                            self.bool_key               = None

                                            for _bool_ in self.boolean_store:
                                                if _bool_ is True:
                                                    self.bool_key = True
                                                    break
                                                else:   self.bool_key = False

                                            if self.bool_key is True:   self.bool_value = False
                                            else:   self.bool_value = True
                                            
                                            if self.keyPass is False: self.data_base[ 'pass' ] = None
                                            else: pass
                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR3( 'else' )
                                        break

                                elif self.get_block == 'empty':
                                    if self.space <= 2: self.space += 1
                                    else:
                                        self.error = ERRORS( self.line ).ERROR4()
                                        break

                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break
                            else : break

                    else: pass 
                else: pass
        
        else: self.error = ERRORS( self.line ).ERROR4()
        
        self.after = end_else_elif.CHECK_VALUES( self.data_base ).AFTER()
        self.error = end_else_elif.CHECK_VALUES( self.data_base ).UPDATE( self.before, self.after, self.error )

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
    
    def ERROR5(self, _str_ : str = 'if'):
        error = '{}close the opening statement {}<< {} >> . {}line: {}{}'.format(self.yellow, self.blue, _str_, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. '.format( self.white ) + error

        return self.error+self.reset

