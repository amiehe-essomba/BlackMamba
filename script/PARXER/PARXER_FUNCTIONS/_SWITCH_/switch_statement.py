from script                                     import control_string
from script.STDIN.WinSTDIN                      import stdin
from script.PARXER.PARXER_FUNCTIONS._SWITCH_    import end_case_default
from script.PARXER.LEXER_CONFIGURE              import lexer_and_parxer
from script.LEXER.FUNCTION                      import main
from script.STDIN.LinuxSTDIN                    import bm_configure as bm
try:
    from CythonModules.Windows                  import fileError as fe 
except ImportError:
    from CythonModules.Linux                    import fileError as fe

class SWITCH_STATEMENT:
    def __init__(self, master, data_base, line):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def SWITCH(self, main_values:any, tabulation : int = 0):
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = [ 'swtich' ]
        self.index_else             = 0
        self.if_line                = 0

        ############################################################################
        self.main_value             = main_values
        self.bool_value             = ''
        self.boolean_store          = []
        self.key_else_activation    = None
        self.data_activation        = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'switch' ]
        self.color                  = bm.fg.red_L
        ke                          = bm.fg.rbg(255,255,0)
        self.before                 = end_case_default.CHECK_VALUES( self.data_base ).BEFORE()

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            self.line       += self.if_line

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.line ).STDIN({ '0': ke, '1': self.color }, self.tabulation )
                if self.error is None:
                    if self.active_tab is True:

                        self.get_block, self.value, self.error = end_case_default.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )

                        if self.error  is None:

                            if self.get_block == 'empty':
                                if self.space <= 2:
                                    self.space += 1
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break

                            elif self.get_block == 'any':
                                self.store_value.append( self.normal_string )
                                if self.data_activation is True:
                                    if self.bool_value is True:
                                        self.error = self.lex_par.LEXER_AND_PARXER( self.value, self.data_base,
                                                                self.line ).ANALYZE( _id_ = 1, _type_ = 'conditional')
                                        if self.error is None:
                                            self.space = 0
                                        else:
                                            self.error = self.error
                                            break
                                    else:
                                        self.error = main.SCANNER( self.value, self.data_base,
                                                        self.line).SCANNER(_id_ = 1, _type_ = 'conditional', _key_=True)
                                        if self.error is None:
                                            self.space = 0
                                        else:
                                            break

                                else:
                                    self.error = ERRORS( self.line ).ERROR6()
                                    break

                            else:
                                self.error = ERRORS( self.line ).ERROR4()
                                break

                        else:
                            self.error = self.error
                            break

                    else:
                        self.get_block, self.value, self.error = end_case_default.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'     :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    del self.boolean_store[ : ]

                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                    break

                            elif self.get_block == 'case:'    :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'case' )
                                        self.store_value        = []
                                        self.data_activation    = True
                                        self.bool_key           = None
                                        self.bool_value = CASE_TREATMENT( self.main_value, self.value, self.data_base,
                                                                                                self.line ).CASE( )
                                        for _bool_ in self.boolean_store:
                                            if _bool_ is True:
                                                self.bool_key = True
                                                break
                                            else:
                                                self.bool_key = False

                                        if self.bool_key is True:
                                            self.bool_value = False
                                        else:
                                            self.bool_value = self.bool_value

                                        self.boolean_store.append(self.bool_value)

                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR1( 'default' )
                                    break

                            elif self.get_block == 'default:' :
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
                                                else:
                                                    self.bool_key = False

                                            if self.bool_key is True:
                                                self.bool_value = False
                                            else:
                                                self.bool_value = True

                                        else:
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR5( 'case' )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR3( 'default' )
                                    break

                            elif self.get_block == 'empty'    :
                                if self.space <= 2:
                                    self.space += 1
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break

                            else:
                                self.error = ERRORS( self.line ).ERROR4()
                                break

                        else:
                            self.error = self.error
                            break

                else:
                    if self.tabulation == 1:
                        self.error = self.error
                        break

                    else:
                        self.get_block, self.value, self.error = end_case_default.EXTERNAL_BLOCKS(self.string,
                                            self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )

                        if self.error is None:
                            if self.get_block   == 'end:'    :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    del self.boolean_store[ : ]

                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR2(self.history[ -1 ] )
                                    break

                            elif self.get_block == 'case:'   :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'case' )
                                        self.store_value        = []
                                        self.data_activation    = True
                                        self.bool_key           = None

                                        self.bool_value = CASE_TREATMENT(self.main_value, self.value, self.data_base,
                                                                                                self.line).CASE()
                                        for _bool_ in self.boolean_store:
                                            if _bool_ is True:
                                                self.bool_key = True
                                                break
                                            else:
                                                self.bool_key = False

                                        if self.bool_key is True:
                                            self.bool_value = False
                                        else:
                                            self.bool_value = self.bool_value

                                        self.boolean_store.append( self.bool_value )

                                    else:
                                        self.error = ERRORS(self.line).ERROR2( self.history[ -1 ])
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR1( 'default' )
                                    break

                            elif self.get_block == 'default:':
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
                                                    self.bool_value = True
                                                    break
                                                else:
                                                    self.bool_key = False

                                            if self.bool_key is True:
                                                self.bool_value = False
                                            else:
                                                self.bool_value = True
                                        else:
                                            self.error = ERRORS(self.line).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR5( 'case' )
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR3( 'default' )
                                    break

                            elif self.get_block == 'empty'   :
                                if self.space <= 2:
                                    self.space += 1
                                else:
                                    self.error = ERRORS(  self.line ).ERROR4()
                                    break

                            else:
                                self.error = ERRORS( self.line ).ERROR4()
                                break

                        else:
                            self.error = self.error
                            break

            except KeyboardInterrupt:
                self.error = ERRORS( self.line ).ERROR4()
                break

        self.after      = end_case_default.CHECK_VALUES( self.data_base ).AFTER()
        self.error      = end_case_default.CHECK_VALUES( self.data_base ).UPDATE( self.before, self.after, self.error )

        return self.error

class SWITCH_LOOP_STATEMENT:
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

    def SWITCH(self,
                    main_values     : any,
                    tabulation      : int   = 1, 
                    loop_list       : any   = None, 
                    _type_          : str   = 'conditional', 
                    keyPass         : bool  = False
                    ):
        
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.main_value             = main_values
        self.index_else             = 0
        self.if_line                = 0
        self.break_                 = None
        self.data_activation        = None

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'switch' ]
        self.store_value            = [ 'swtich' ]
        self.before                 = end_case_default.CHECK_VALUES( self.data_base ).BEFORE()
        self.loop_list              = loop_list
        self.next_line              = None
        self.boolean_store          = []

        ############################################################################
        self.keyPass                = keyPass 
        self.max_emtyLine           = 5
        ############################################################################
    
        for j, _string_ in enumerate( self.loop_list ):
         
            if j != self.next_line :
                self.if_line                        += 1
                self.line                           += 1
                
                self.normal_string, self.active_tab = _string_
                self.string                         = self.normal_string
                
                if self.normal_string:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = end_case_default.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.if_line ).BLOCKS( self.tabulation + 1 )
                        
                        if self.error  is None:
                            if self.get_block == 'empty'   :
                                if self.space <= self.max_emtyLine: 
                                    self.space += 1
                                    self.store_value.append(self.normal_string)
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break

                            elif self.get_block == 'any'     :
                                self.store_value.append(self.normal_string)
                                if self.data_activation is True:
                                    if self.bool_value is True:
                                        if self.data_base[ 'pass' ] is None:
                                            self.error = self.lex_par.LEXER_AND_PARXER( self.value, self.data_base,
                                                            self.line ).ANALYZE( _id_ = 1, _type_ = _type_)
                                            if self.error is None:  
                                                self.space  = 0
                                                self.break_ = True
                                            else: break
                                        else: pass
                                    else: pass
                                else:
                                    self.error = ERRORS( self.if_line ).ERROR6()
                                    break
                        else: break
                    else:
                        self.get_block, self.value, self.error = end_case_default.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.if_line ).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'       :
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

                            elif self.get_block == 'case:'      :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'case' )
                                        self.store_value        = []
                                        self.data_activation    = True
                                        self.bool_key           = None
                                 
                                        self.bool_value = CASE_TREATMENT( self.main_value, self.value, self.data_base,
                                                                                self.line ).CASE( )
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
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR1( 'default' )
                                    break

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
                                            self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR5( 'case' )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR3( 'default' )
                                    break

                            elif self.get_block == 'empty'      :
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
        
        self.after      = end_case_default.CHECK_VALUES( self.data_base ).AFTER()
        self.error      = end_case_default.CHECK_VALUES( self.data_base ).UPDATE( self.before, self.after, self.error )

        ############################################################################

        return self.error

class CASE_TREATMENT:
    def __init__(self, main_master:any, master:any, data_base:dict, line:int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.main_master        = main_master

    def CASE(self):
        self.error              = None
        self.type               = type( self.master )
        self._return_           = None

        if self.type != type( tuple() ):
            if self.main_master == self.master :
                self._return_ = True
            else:
                self._return_ = False
        else:
            for value in self.master :
                if value == self.main_master:
                    self._return_ = True
                    break
                else:
                    self._return_ = False

        return  self._return_

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

    def ERROR1(self, string: str = 'default'):
        error = '{}is already defined. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. {}<< {} >> {}block '.format(self.white,
                                                                                self.cyan, string, self.green) + error
        return self.error+self.reset

    def ERROR2(self, string):
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format(self.green, self.white, self.cyan, string, self.green,
                                                                                             self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax '.format( self.white ) + error

        return self.error+self.reset

    def ERROR3(self, string: str = 'default'):
        error = 'due to {}many {}<< {} >> {}blocks. {}line: {}{}'.format(self.green, self.cyan, string, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax '.format( self.white ) + error

        return self.error+self.reset

    def ERROR4(self):
        self.error =  fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                    self.white, self.yellow, self.line )
        return self.error+self.reset

    def ERROR5(self, string:str = 'case'):
        error = '{}is not defined. {}line: {}{}'.format(self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. {}<< {} >> {}block '.format(self.white, self.cyan, 
                                                                                                            string, self.white) + error

        return self.error+self.reset

    def ERROR6(self):
        error = '{}or {}<< default >> {}statement blocks. {}line: {}{}'.format( self.white, self.cyan, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. no {}<< case >> '.format(self.white, self.red ) + error

        return self.error+self.reset