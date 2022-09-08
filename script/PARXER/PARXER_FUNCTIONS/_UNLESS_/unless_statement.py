import cython
from script                                             import control_string
from script.STDIN.WinSTDIN                              import stdin
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.PARXER.PARXER_FUNCTIONS._IF_                import if_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_     import comment
from script.PARXER.PARXER_FUNCTIONS._TRY_               import try_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_            import switch_statement
from script.LEXER.FUNCTION                              import main
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
from statement                                          import InternalStatement as IS
from statement                                          import externalUnless as eUnless
from script.PARXER.PARXER_FUNCTIONS._UNLESS_            import UnlessError
from updatingDataBase                                   import updating
try:  from CythonModules.Linux                          import loop_for
except ImportError: from CythonModules.Windows          import loop_for

ke = bm.fg.rbg(255, 255,0)

@cython.cclass
class EXTERNAL_UNLESS_FOR_STATEMENT:
    def __init__(self, 
                master      : any,                              # any value
                data_base   : dict,                             # data base
                line        : int                               # current line
                ):
        
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    @cython.cfunc
    def UNLESS_STATEMENT(self, 
                        bool_value      : bool,                 # boolean value used to activate the calculation
                        tabulation      : int   = 0,            # tabulation
                        loop_list       : list  = [],           # all values
                        _type_          : str   = 'conditional',# type structure
                        keyPass         : bool  = False         # if pass function is detected
                        ):

        """
        :param bool_value:
        :param tabulation:
        :param loop_list:
        :param _type_:
        :param keyPass:
        :return:
        """
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.bool_value             = bool_value
        self.boolean_store          = [self.bool_value]
        self.index_else             = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'unless' ]
        self.before                 = updating.UPDATE( data_base=self.data_base ).BEFORE()
        self.loop_list              = loop_list
        self.next_line              = None

        ############################################################################
        self.keyPass                = keyPass 
        self.max_emtyLine           = 5
        ############################################################################
        
        if self.keyPass is False:
            for j, _string_ in enumerate(self.loop_list):
                if j != self.next_line:
                    self.if_line                        += 1
                    self.line                           += 1
                    self.normal_string, self.active_tab = _string_
                    self.string                         = self.normal_string

                    if self.string:
                        if self.active_tab is True:
                            self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string,
                                        normal_string=self.normal_string, data_base=self.data_base,  line=self.line).BLOCKS(
                                        tabulation=self.tabulation + 1, function=_type_, interpreter=True)

                            if self.error  is None:
                                if self.get_block   == 'begin:'     :
                                    self.next_line  = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'begin' )
                                    self.space = 0

                                    if self.bool_value is False:
                                        self.error = comment.COMMENT_LOOP_STATEMENT( master=self.master, data_base=self.data_base,
                                                                line=self.line ).COMMENT( tabulation=self.tabulation + 1,
                                                                loop_list=self.loop_list[ j + 1 ], keyPass = self.keyPass)
                                        if self.error is None: pass
                                        else: break
                                    else: pass
                                elif self.get_block == 'if:'        :
                                    self.next_line  = j + 1

                                    if self.bool_value is False:
                                        self.error = if_statement.INTERNAL_IF_LOOP_STATEMENT(  master=self.master,
                                                data_base=self.data_base, line=self.line).IF_STATEMENT( bool_value=self.value,
                                                tabulation=self.tabulation + 1,  loop_list=self.loop_list[ j + 1 ],
                                                _type_ = _type_, keyPass = self.keyPass)
                                        if self.error is None:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'if' )
                                            self.space = 0
                                        else: break
                                    else:
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'if' )
                                        self.space = 0
                                elif self.get_block == 'unless:'    :
                                    self.next_line  = j + 1
                                    if self.bool_value is False:
                                        self.error = INTERNAL_UNLESS_FOR_STATEMENT( master=self.master,
                                                            data_base=self.data_base, line=self.line ).UNLESS_STATEMENT( bool_value=self.value,
                                                            tabulation=self.tabulation + 1,
                                                            loop_list=self.loop_list[ j + 1 ], _type_ = _type_, keyPass = self.keyPass )
                                        if self.error is None:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'unless' )
                                            self.space = 0
                                        else: break
                                    else:
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'unless' )
                                        self.space = 0
                                elif self.get_block == 'try:'       :
                                    self.next_line = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'try' )
                                    self.space = 0
                                    if self.data_base[ 'pass' ] is None: pass 
                                    else: self.keyPass = True

                                    if self.bool_value is False:
                                        self.error = try_statement.INTERNAL_TRY_FOR_STATEMENT(master= self.master,
                                                data_base=self.data_base, line=self.line).TRY_STATEMENT( tabulation=self.tabulation + 1,
                                                loop_list=self.loop_list[ self.next_line], keyPass = self.keyPass, _type_ = _type_ )
                                    if self.error is None:  self.keyPass    = False
                                    else: pass
                                elif self.get_block == 'switch:'    :
                                    self.next_line  = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'begin' )
                                    self.space = 0

                                    if self.bool_value is False :
                                        self.error = switch_statement.SWITCH_LOOP_STATEMENT( master=self.master , data_base=self.data_base,
                                                        line=self.line ).SWITCH( main_values=self.value, tabulation=self.tabulation + 1,
                                                        loop_list=self.loop_list[ j + 1 ], _type_ = _type_, keyPass = self.keyPass)
                                        if self.error is None: pass
                                        else: pass
                                    else: pass
                                elif self.get_block == 'empty'      :
                                    if self.space <= self.max_emtyLine :
                                        self.space += 1
                                    else:
                                        self.error = UnlessError.ERRORS( self.line ).ERROR4()
                                        break
                                elif self.get_block == 'any'        :
                                    self.store_value.append(self.normal_string)
                                    self.space = 0
                                    if self.bool_value is True:
                                        if self.data_base[ 'pass' ] is None:
                                            self.error = self.lex_par.LEXER_AND_PARXER(master=self.value, data_base=self.data_base,
                                                                line=self.line).ANALYZE( _id_=1, _type_= _type_ )
                                            if self.error is None: pass
                                            else: break
                                        else: self.keyPass = True
                                    else: pass
                            else:  break
                        else:
                            self.get_block, self.value, self.error = eUnless.EXTERNAL_BLOCKS(string=self.string,
                                            normal_string=self.normal_string, data_base=self.data_base,
                                            line=self.line).BLOCKS( tabulation=self.tabulation)

                            if self.error is None:
                                if self.get_block   == 'end:' :
                                    if self.store_value:
                                        del self.store_value[ : ]
                                        del self.history[ : ]
                                        del self.boolean_store[ : ]
                                        break
                                    else:
                                        self.error = UnlessError.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                        break
                                elif self.get_block == 'else:':
                                    if self.index_else < 1:
                                        if self.store_value:
                                            self.index_else             += 1
                                            self.key_else_activation    = True
                                            self.store_value            = []
                                            self.bool_key               = None
                                            self.history.append('else')

                                            for _bool_ in self.boolean_store:
                                                if _bool_ == True:
                                                    self.bool_key = True
                                                    break
                                                else: self.bool_key = False

                                            if self.bool_key is True: self.bool_value = False
                                            else: self.bool_value = True
                                        else:
                                            self.error = UnlessError.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error = UnlessError.ERRORS( self.line ).ERROR3( 'else' )
                                        break
                                elif self.get_block == 'empty':
                                    if self.space <= self.max_emtyLine : self.space += 1
                                    else:
                                        self.error = UnlessError.ERRORS( self.line ).ERROR4()
                                        break
                            else: break
                    else: pass 
                else:
                    self.if_line        += 1
                    self.line           += 1
                    self.next_line      = None

            self.after = updating.UPDATE(data_base=self.data_base).AFTER()
            self.error = updating.UPDATE(data_base=self.data_base).UPDATE(before=self.before, after=self.after, error=self.error)
        else: pass 
        
        return self.error

@cython.cclass
class INTERNAL_UNLESS_FOR_STATEMENT:
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

    @cython.cfunc
    def UNLESS_STATEMENT(self, 
                        bool_value      : bool, 
                        tabulation      : int   = 0, 
                        loop_list       : list  = [],
                        _type_          : str   = 'conditional',
                        keyPass         : bool  = False
                        ):
        self.error                  = None
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.bool_value             = bool_value
        self.boolean_store          = [self.bool_value]
        self.index_else             = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'unless' ]
        self.before                 = updating.UPDATE( data_base=self.data_base ).BEFORE()
        self.loop_list              = loop_list
        self.next_line              = None

        ############################################################################
        self.keyPass                = keyPass 
        self.max_emtyLine           = 5
        ############################################################################
        
        if self.keyPass is False:
            for j, _string_ in enumerate( self.loop_list ):
                if j != self.next_line:
                    self.if_line                        += 1
                    self.line                           += 1
                    self.normal_string, self.active_tab = _string_
                    self.string                         = self.normal_string

                    if self.string:
                        if self.active_tab is True:
                            self.get_block, self.value, self.error = IS.INTERNAL_BLOCKS(string=self.string,
                                        normal_string=self.normal_string, data_base=self.data_base, line=self.line).BLOCKS(
                                        tabulation=self.tabulation + 1, function=_type_, interpreter=True)

                            if self.error  is None:
                                if self.get_block   == 'begin:'     :
                                    self.next_line  = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    if self.bool_value is False:
                                        self.error = comment.COMMENT_LOOP_STATEMENT( master=self.master, data_base=self.data_base,
                                                                line=self.line ).COMMENT( tabulation=self.tabulation + 1,
                                                                loop_list=self.loop_list[ j + 1 ], keyPass = self.keyPass)
                                        if self.error is None: pass
                                        else: break
                                    else: pass
                                elif self.get_block == 'if:'        :
                                    self.next_line  = j + 1
                                    if self.bool_value is False:
                                        self.error = if_statement.INTERNAL_IF_LOOP_STATEMENT(  master=self.master,
                                                data_base=self.data_base, line=self.line).IF_STATEMENT( bool_value=self.value,
                                                tabulation=self.tabulation + 1,  loop_list=self.loop_list[ j + 1 ],
                                                _type_ = _type_, keyPass = self.keyPass)
                                        if self.error is None:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'if' )
                                            self.space = 0
                                        else: break
                                    else:
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'if' )
                                        self.space = 0
                                elif self.get_block == 'unless:'    :
                                    self.next_line  = j + 1
                                    if self.bool_value is False:
                                        self.error = EXTERNAL_UNLESS_FOR_STATEMENT( master=self.master,
                                                data_base=self.data_base, line=self.line ).UNLESS_STATEMENT( bool_value=self.value,
                                                tabulation=self.tabulation + 1,
                                                loop_list=self.loop_list[ j + 1 ], _type_ = _type_, keyPass = self.keyPass )
                                        if self.error is None:
                                            self.store_value.append( self.normal_string )
                                            self.history.append( 'unless' )
                                            self.space = 0
                                        else: break
                                    else:
                                        self.store_value.append( self.normal_string )
                                        self.history.append( 'unless' )
                                        self.space = 0
                                elif self.get_block == 'try:'       :
                                    self.next_line = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'try' )
                                    self.space = 0
                                    if self.data_base[ 'pass' ] is None: pass
                                    else: self.keyPass = True

                                    if self.bool_value is False:
                                        self.error = try_statement.INTERNAL_TRY_FOR_STATEMENT(master= self.master,
                                                data_base=self.data_base, line=self.line).TRY_STATEMENT( tabulation=self.tabulation + 1,
                                                loop_list=self.loop_list[ self.next_line], keyPass = self.keyPass, _type_ = _type_ )
                                    if self.error is None:  self.keyPass    = False
                                    else: pass
                                elif self.get_block == 'switch:'    :
                                    self.next_line  = j + 1
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'begin' )
                                    self.space = 0

                                    if self.bool_value is False :
                                        self.error = switch_statement.SWITCH_LOOP_STATEMENT( master=self.master , data_base=self.data_base,
                                                        line=self.line ).SWITCH( main_values=self.value, tabulation=self.tabulation + 1,
                                                        loop_list=self.loop_list[ j + 1 ], _type_ = _type_, keyPass = self.keyPass)
                                        if self.error is None: pass
                                        else: pass
                                    else: pass
                                elif self.get_block == 'empty'      :
                                    if self.space <= self.max_emtyLine :
                                        self.space += 1
                                    else:
                                        self.error = UnlessError.ERRORS( self.line ).ERROR4()
                                        break
                                elif self.get_block == 'any'        :
                                    self.store_value.append(self.normal_string)
                                    self.space = 0
                                    if self.bool_value is False:
                                        if self.data_base[ 'pass' ] is None:
                                            self.error = self.lex_par.LEXER_AND_PARXER(master=self.value, data_base=self.data_base,
                                                                line=self.line).ANALYZE( _id_=1, _type_= _type_ )
                                            if self.error is None: pass
                                            else: break
                                        else: self.keyPass = True
                                    else: pass
                            else:break
                        else:
                            self.get_block, self.value, self.error = eUnless.EXTERNAL_BLOCKS(string=self.string,
                                            normal_string=self.normal_string, data_base=self.data_base,
                                            line=self.line).BLOCKS( tabulation=self.tabulation)

                            if self.error is None:
                                if self.get_block   == 'end:' :
                                    if self.store_value:
                                        del self.store_value[ : ]
                                        del self.history[ : ]
                                        del self.boolean_store[ : ]
                                        break
                                    else:
                                        self.error = UnlessError.ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                        break
                                elif self.get_block == 'else:':
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
                                        else:
                                            self.error =  UnlessError.ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                            break
                                    else:
                                        self.error =  UnlessError.ERRORS( self.line ).ERROR3( 'else' )
                                        break
                                elif self.get_block == 'empty':
                                    if self.space <= self.max_emtyLine : self.space += 1
                                    else:
                                        self.error =  UnlessError.ERRORS( self.line ).ERROR4()
                                        break
                            else: break
                    else: pass
                else:
                    self.if_line        += 1
                    self.line           += 1
                    self.next_line      = None

            self.after = updating.UPDATE(data_base=self.data_base).AFTER()
            self.error = updating.UPDATE(data_base=self.data_base).UPDATE(before=self.before, after=self.after,  error=self.error)
        else: pass 
        
        return self.error

