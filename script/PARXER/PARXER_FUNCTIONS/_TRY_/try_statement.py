
from script                                         import control_string
from script.STDIN.WinSTDIN                          import stdin
from script.PARXER.PARXER_FUNCTIONS._TRY_           import end_except_finaly_else
from script.PARXER.PARXER_FUNCTIONS._UNLESS_        import unless_statement
from script.PARXER.PARXER_FUNCTIONS._SWITCH_        import switch_statement
from script.PARXER.PARXER_FUNCTIONS._IF_            import if_statement
from script.PARXER.PARXER_FUNCTIONS._BEGIN_COMMENT_ import comment
from script.PARXER.PARXER_FUNCTIONS._IF_            import if_statement
from script.PARXER.LEXER_CONFIGURE                  import lexer_and_parxer
from script.LEXER.FUNCTION                          import main
from script.STDIN.LinuxSTDIN                        import bm_configure as bm
try:
    from CythonModules.Windows                      import fileError as fe 
except ImportError:
    from CythonModules.Linux                        import fileError as fe 

class EXTERNAL_TRY_STATEMENT:
    def __init__(self, master:any, data_base:dict, line:int):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_par                = lexer_and_parxer

    def TRY_STATEMENT(self, tabulation : int = 1):
        self.error                  = None
        self.locked_error           = []
        self.get_errors             = []
        self.active_calculations    = True
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_finally          = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'try' ]
        self.color                  = bm.fg.rbg(255, 80, 0 )
        ke                          = bm.fg.rbg(255, 255, 0 )
        self.before                 = end_except_finaly_else.CHECK_VALUES( self.data_base ).BEFORE()
        self.finally_key            = False
        self.except_key             = False
        self._finally_key_          = False

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            self.line       += self.if_line

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.line ).STDIN({ '0': ke, '1': self.color }, self.tabulation )
                if self.error is None:
                    if self.active_tab is True:

                        self.get_block, self.value, self.error = end_except_finaly_else.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )
   
                        if self.get_block   == 'begin:'  :
                            self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                            self.store_value.append(self.normal_string)

                            self.error1 = comment.COMMENT_STATEMENT(self.master,
                                        self.data_base, self.line).COMMENT( self.tabulation + 1)

                            if self.error is None:
                                if self.error1 is None:
                                    #################################################
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    ################################################

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.error = self.error1
                                    self.locked_error.append(self.error)
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                        self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append(self._error_)
                            else:
                                self.locked_error.append(self.error)
                                self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                    self.before_init, self.after, self.error)
                                self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                self.get_errors.append(self._error_)

                        elif self.get_block == 'if:'     :
                            
                            self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                            self.store_value.append(self.normal_string)

                            self.error1 = if_statement.INTERNAL_IF_STATEMENT( self.master,
                                        self.data_base, self.line ).IF_STATEMENT( self.value, self.tabulation + 1)

                            if self.error is None:
                                if self.error1 is None:
                                    #################################################
                                    self.history.append( 'if' )
                                    self.space = 0
                                    ################################################

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.error = self.error1 
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(self.before_init,
                                                                                                    self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )
                            else:
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init,self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )
                                    
                        elif self.get_block == 'try:'    :
                            self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                            self.store_value.append(self.normal_string)

                            self._finally_key_, self.error1 = INTERNAL_TRY_STATEMENT ( self.master,
                                        self.data_base, self.line ).TRY_STATEMENT( self.tabulation + 1)

                            if self.error is None:
                                if self.error1 is None:
                                    self.space = 0
                                    self.history.append( 'try' )

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        self.error = True
                                        self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                        self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                            self.before, self.after, self.error)
                                        self.error = None

                                else:
                                    self.error = self.error1
                                    if self._finally_key_ is not True:
                                        self.locked_error.append( self.error )
                                        self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                        self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(self.before,
                                                                                            self.after, self.error)
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append( self._error_ )
                                        self._finally_key_ = False
                                        
                                    else:
                                        self.locked_error.append( self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append( self._error_ )
                            else:
                                if self._finally_key_ is not True:
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(self.before,
                                                                                        self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )
                                    self._finally_key_ = False
                                    
                                else:
                                    self.locked_error.append( self.error )
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )

                        elif self.get_block == 'unless:' :
                            self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                            self.store_value.append(self.normal_string)

                            self.error1 = unless_statement.INTERNAL_UNLESS_STATEMENT( self.master,
                                        self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1)

                            if self.error is None:
                                if self.error1 is None:
                                    self.history.append( 'unless' )
                                    self.space = 0

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before_init, self.after, self.error)
                                            self.error = None
                                else:
                                    self.error = self.error1
                                    self.locked_error.append(self.error)
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                        self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append(self._error_)
                            else:
                                self.locked_error.append(self.error)
                                self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                    self.before_init, self.after, self.error)
                                self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                self.get_errors.append(self._error_)

                        elif self.get_block == 'switch:' :
                            self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                            self.store_value.append(self.normal_string)

                            self.error1 = switch_statement.SWITCH_STATEMENT( self.master,
                                        self.data_base, self.line ).SWITCH( self.value, self.tabulation + 1)

                            if self.error is None:
                                if self.error1 is None:
                                    self.history.append( 'switch' )
                                    self.space = 0

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors:  pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.error = self.error1
                                    self.locked_error.append(self.error)
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                        self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append(self._error_)
                            else:
                                self.locked_error.append(self.error)
                                self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                    self.before_init, self.after, self.error)
                                self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                self.get_errors.append(self._error_)

                        elif self.get_block == 'empty'   :
                            if self.space <= 2:  self.space += 1
                            else:
                                self.error = ERRORS( self.line ).ERROR4()
                                break

                        elif self.get_block == 'any'     :
                            self.before_init = end_except_finaly_else.CHECK_VALUES( self.data_base ).BEFORE()
                            self.store_value.append( self.normal_string )

                            self.error1 = self.lex_par.LEXER_AND_PARXER( self.value, self.data_base,
                                                            self.line ).ANALYZE( _id_ = 1, _type_ = 'conditional')
                            if self.error is None:
                                if self.error1 is None:
                                    self.space = 0

                                    if self.active_calculations is True:  pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors:  pass
                                    else:
                                        
                                        self.error = True
                                        self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                        self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                        self.before_init, self.after, self.error)
                                        self.error = None

                                else:
                                    self.error = self.error1 
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init,self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )
                            else:
                                self.locked_error.append( self.error )
                                self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                        self.before_init,self.after, self.error)
                                self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                self.get_errors.append( self._error_ )
                       
                    else:
                        self.get_block, self.value, self.error = end_except_finaly_else.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'    :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]

                                    if self.except_key is False and self.finally_key is False:
                                        self.error = ERRORS( self.line ).ERROR5()
                                        break
                                    else:
                                        break

                                else:
                                    self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                    break

                            elif self.get_block == 'except:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'except' )
                                        self.bool_value         = self.value
                                        self.store_value        = []
                                        self.except_key         = True

                                        if type( self.value ) == type( str()):
                                            if self.get_errors:
                                                if self.value in self.get_errors:
                                                    self.idd = self.get_errors.index( self.value )
                                                    del self.get_errors[ self.idd ]
                                                    del self.locked_error[ self.idd ]

                                                    self.active_calculations = True
                                                else:
                                                    self.active_calculations = False
                                            else:
                                                self.active_calculations = True

                                        else:
                                            for _error_ in self.value:
                                                if self.get_errors:
                                                    if _error_ in self.get_errors:
                                                        self.idd = self.get_errors.index( _error_ )
                                                        del self.get_errors[ self.idd ]
                                                        del self.locked_error[ self.idd ]
                                                        self.active_calculations = True
                                                    else:
                                                        self.active_calculations = False
                                                else:
                                                    self.active_calculations = True

                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR1( 'finally' )
                                    break

                            elif self.get_block == 'finally:':
                                if self.index_finally < 1:
                                    if self.store_value:
                                        self.index_finally         += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append( 'finally' )
                                        self.active_calculations    = True
                                        self.finally_key            = True

                                        if self.get_errors:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                                self.before, self.after, self.error)
                                            self.error = None
                                        else:
                                            pass

                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                        break

                                else:
                                    self.error = ERRORS( self.line ).ERROR3( 'finally' )
                                    break

                            elif self.get_block == 'empty'   :
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
                        self.get_block, self.value, self.error = end_except_finaly_else.EXTERNAL_BLOCKS(self.string,
                                            self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'    :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]

                                    if self.except_key is True or self.finally_key is True:
                                        break
                                    elif self.except_key is True and self.finally_key is True:
                                        break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR5()
                                        break

                                else:
                                    self.error = ERRORS( self.line ).ERROR2(self.history[ -1 ] )
                                    break

                            elif self.get_block == 'except:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'except' )
                                        self.bool_value     = self.value
                                        self.store_value    = []
                                        self.except_key     = True

                                        if type(self.value) == type(str()):
                                            if self.get_errors:
                                                if self.value in self.get_errors:
                                                    self.idd = self.get_errors.index( self.value )
                                                    del self.get_errors[ self.idd ]
                                                    del self.locked_error[ self.idd ]

                                                    self.active_calculations = True
                                                else: self.active_calculations = False
                                            else: self.active_calculations = True

                                        else:
                                            for _error_ in self.value:
                                                if self.get_errors:
                                                    if _error_ in self.get_errors:
                                                        self.idd = self.get_errors.index( _error_ )
                                                        del self.get_errors[ self.idd ]
                                                        del self.locked_error[ self.idd ]

                                                        self.active_calculations = True
                                                    else: self.active_calculations = False
                                                else: self.active_calculations = True

                                    else:
                                        self.error = ERRORS(self.line).ERROR2(self.history[-1])
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR1( 'finally' )
                                    break

                            elif self.get_block == 'finally:':
                                if self.index_finally < 1:
                                    if self.store_value:
                                        self.index_finally += 1
                                        self.key_else_activation = True
                                        self.store_value = []
                                        self.history.append( 'finally' )
                                        self.active_calculations    = True
                                        self.finally_key            = True

                                        if self.get_errors:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                                self.before, self.after, self.error)
                                            self.error = None
                                        else:
                                            pass

                                    else:
                                        self.error = ERRORS(self.line).ERROR2( self.history[ -1 ] )
                                        break

                                else:
                                    self.error = ERRORS(self.line).ERROR3( 'finally' )
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

        if self.error is None:
            if self.get_errors:
                self.error = self.locked_error[0]
                if self.finally_key is False:
                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(self.before, self.after, self.error)
                else: self._finally_key_ = self.finally_key 
            else: pass
        else: pass

        ############################################################################

        return self._finally_key_, self.error

class INTERNAL_TRY_STATEMENT:
    def __init__(self, master:any, data_base:dict, line:int):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_par                = lexer_and_parxer

    def TRY_STATEMENT(self, tabulation:int):
        self.error                  = None
        self.locked_error           = []
        self.get_errors             = []
        self.active_calculations    = True
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_finally          = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'try' ]
        self.color                  = bm.fg.rbg(255, 150, 0 )#bm.fg.rbg(0, 255, 255 )
        ke                          = bm.fg.rbg(255, 255, 0 )
        self.before                 = end_except_finaly_else.CHECK_VALUES( self.data_base ).BEFORE()
        self.finally_key            = False
        self.except_key             = False
        self._finally_key_          = False

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            self.line       += self.if_line

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.line ).STDIN({'0': ke, '1': self.color}, self.tabulation )

                if self.error is None:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = end_except_finaly_else.INTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1)

                        if   self.get_block == 'begin:' :
                            self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                            self.store_value.append(self.normal_string)

                            self.error1 = comment.COMMENT_STATEMENT(self.master,
                                                self.data_base, self.line).COMMENT( self.tabulation + 1)

                            if self.error is None:
                                if self.error1 is None:
                                    #################################################
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    ################################################

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.error = self.erro1 
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init,self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )
                            else:
                                self.locked_error.append(self.error)
                                self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                    self.before_init, self.after, self.error)
                                self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                self.get_errors.append(self._error_)

                        elif self.get_block == 'if:'    :
                            self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                            self.store_value.append(self.normal_string)

                            self.error1 = if_statement.EXTERNAL_IF_STATEMENT(  self.master,
                                    self.data_base, self.line).IF_STATEMENT( self.value, self.tabulation + 1)

                            if self.error is None:
                                if self.error1 is None:
                                    #################################################
                                    self.history.append( 'if' )
                                    self.space = 0
                                    ################################################

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.error = self.error1
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init,self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )
                            else:
                                self.locked_error.append(self.error)
                                self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                    self.before_init, self.after, self.error)
                                self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                self.get_errors.append(self._error_)

                        elif self.get_block == 'try:'   :
                            self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                            self.store_value.append(self.normal_string)

                            self._finally_key_, self.error1 = EXTERNAL_TRY_STATEMENT ( self.master,
                                        self.data_base, self.line ).TRY_STATEMENT( self.tabulation + 1)

                            if self.error is None:
                                if self.error1 is None:
                                    self.space = 0
                                    self.history.append( 'try' )

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        self.error = True
                                        self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                        self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                        self.before, self.after, self.error)
                                        self.error = None

                                else:
                                    self.error = self.erro1 
                                    if self._finally_key_ is not True:
                                        self.locked_error.append( self.error )
                                        self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                        self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(self.before,
                                                                                            self.after, self.error)
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append( self._error_ )
                                        self._finally_key_ = None
                                    else:
                                        self.locked_error.append( self.error )
                                        self._error_ = end_except_finaly_else.GET_ERROR(self.error, self.data_base,
                                                                                        self.line ).ERROR()
                                        self.get_errors.append( self._error_ )
                            else:
                                if self._finally_key_ is not True:
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(self.before,
                                                                                        self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )
                                    self._finally_key_ = None
                                else:
                                    self.locked_error.append( self.error )
                                    self._error_ = end_except_finaly_else.GET_ERROR(self.error, self.data_base,
                                                                                    self.line ).ERROR()
                                    self.get_errors.append( self._error_ )

                        elif self.get_block == 'unless:':
                            self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                            self.store_value.append(self.normal_string)

                            self.error1 = unless_statement.EXTERNAL_UNLESS_STATEMENT( self.master,
                                        self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1)

                            if self.error is None:
                                if self.error1 is None:
                                    #################################################
                                    self.history.append( 'unless' )
                                    self.space = 0
                                    ################################################

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors:  pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.error = self.error1
                                    self.locked_error.append(self.error)
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                        self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append(self._error_)
                            else:
                                self.locked_error.append(self.error)
                                self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                    self.before_init, self.after, self.error)
                                self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                self.get_errors.append(self._error_)

                        elif self.get_block == 'switch:':
                            self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                            self.store_value.append(self.normal_string)

                            self.error1 = switch_statement.SWITCH_STATEMENT(self.master,
                                                self.data_base, self.line).SWITCH(self.value, self.tabulation + 1)
                            
                            if self.error is None:
                                if self.error1 is None:
                                    #################################################
                                    self.history.append( 'switch' )
                                    self.space = 0
                                    ################################################

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors:  pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.error = self.error1
                                    self.locked_error.append(self.error)
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                        self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append(self._error_)
                            else:
                                self.locked_error.append(self.error)
                                self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                    self.before_init, self.after, self.error)
                                self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                self.get_errors.append(self._error_)

                        elif self.get_block == 'empty'  :
                            if self.space <= 2: self.space += 1
                            else:
                                self.error = ERRORS( self.line ).ERROR4()

                        elif self.get_block == 'any'    :
                            self.before_init = end_except_finaly_else.CHECK_VALUES( self.data_base ).BEFORE()
                            self.store_value.append( self.normal_string )

                            self.error1 = self.lex_par.LEXER_AND_PARXER(self.value, self.data_base,
                                                    self.line).ANALYZE(_id_ = 1, _type_ = 'conditional')
                            
                            if self.error is None:
                                if self.error1 is None:
                                    self.space = 0
                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init, self.after, self.error)
                                            self.error = None
                                else:
                                    self.error = self.error1
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append(self._error_)
                            else:
                                self.locked_error.append(self.error)
                                self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                    self.before_init, self.after, self.error)
                                self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                self.get_errors.append(self._error_)

                    else:
                        self.get_block, self.value, self.error = end_except_finaly_else.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )
            
                        if self.error is None:
                            if   self.get_block == 'end:'    :
                                if self.store_value:
                                    del self.store_value[:]
                                    del self.history[:]

                                    if self.except_key is False and self.finally_key is False:
                                        self.error = ERRORS(self.line).ERROR5()
                                        break
                                    else: break

                                else:
                                    self.error = ERRORS(self.line).ERROR2(self.history[-1])
                                    break

                            elif self.get_block == 'except:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append('except')
                                        self.bool_value = self.value
                                        self.store_value = []
                                        self.except_key = True

                                        if type(self.value) == type(str()):
                                            if self.get_errors:
                                                if self.value in self.get_errors:
                                                    self.idd = self.get_errors.index(self.value)
                                                    del self.get_errors[self.idd]
                                                    del self.locked_error[self.idd]

                                                    self.active_calculations = True
                                                else:  self.active_calculations = False
                                            else: self.active_calculations = True

                                        else:
                                            for _error_ in self.value:
                                                if self.get_errors:
                                                    if _error_ in self.get_errors:
                                                        self.idd = self.get_errors.index(_error_)
                                                        del self.get_errors[self.idd]
                                                        del self.locked_error[self.idd]
                                                        self.active_calculations = True
                                                    else: self.active_calculations = False
                                                else: self.active_calculations = True

                                    else:
                                        self.error = ERRORS(self.line).ERROR2(self.history[-1])
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR1('finally')
                                    break

                            elif self.get_block == 'finally:':
                                if self.index_finally < 1:
                                    if self.store_value:
                                        self.index_finally += 1
                                        self.key_else_activation = True
                                        self.store_value = []
                                        self.history.append('finally')
                                        self.active_calculations = True
                                        self.finally_key = True

                                        if self.get_errors:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before, self.after, self.error)
                                            self.error = None
                                        else:  pass
                                    else:
                                        self.error = ERRORS(self.line).ERROR2(self.history[-1])
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR3('finally')
                                    break
                            
                            elif self.get_block == 'empty'   :
                                if self.space <= 2: self.space += 1
                                else:
                                    self.error = ERRORS(self.line).ERROR4()
                                    break
                            
                            else:
                                self.error = ERRORS(self.line).ERROR4()
                                break
                        else: pass
                else:
                    self.get_block, self.value, self.error = end_except_finaly_else.EXTERNAL_BLOCKS(self.string,
                                self.normal_string, self.data_base,self.line).BLOCKS( self.tabulation )
            
                    if self.error is None:
                        if   self.get_block == 'end:'    :
                            if self.store_value:
                                del self.store_value[:]
                                del self.history[:]

                                if self.except_key is False and self.finally_key is False:
                                    self.error = ERRORS(self.line).ERROR5()
                                    break
                                else: break
                            else:
                                self.error = ERRORS(self.line).ERROR2(self.history[-1])
                                break

                        elif self.get_block == 'except:' :
                            if self.key_else_activation == None:
                                if self.store_value:
                                    self.history.append( 'except' )
                                    self.bool_value = self.value
                                    self.store_value = []
                                    self.except_key = True
                                 
                                    if type(self.value) == type(str()):
                                        #self.value, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.value ).initError() )
                                        if self.get_errors:
                                            if self.value in self.get_errors:
                                                self.idd = self.get_errors.index(self.value)
                                                del self.get_errors[self.idd]
                                                del self.locked_error[self.idd]

                                                self.active_calculations = True
                                            else: self.active_calculations = False
                                        else:self.active_calculations = True

                                    else:
                                        for _error_ in self.value:
                                            if self.get_errors:
                                                if _error_ in self.get_errors:
                                                    self.idd = self.get_errors.index(_error_)
                                                    del self.get_errors[self.idd]
                                                    del self.locked_error[self.idd]
                                                    self.active_calculations = True
                                                else:
                                                    self.active_calculations = False
                                            else:
                                                self.active_calculations = True

                                else:
                                    self.error = ERRORS(self.line).ERROR2(self.history[-1])
                                    break
                            else:
                                self.error = ERRORS(self.line).ERROR1('finally')
                                break

                        elif self.get_block == 'finally:':
                            if self.index_finally < 1:
                                if self.store_value:
                                    self.index_finally += 1
                                    self.key_else_activation = True
                                    self.store_value = []
                                    self.history.append('finally')
                                    self.active_calculations = True
                                    self.finally_key = True

                                    if self.get_errors:
                                        self.error = True
                                        self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                        self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                            self.before, self.after, self.error)
                                        self.error = None
                                    else:
                                        pass

                                else:
                                    self.error = ERRORS(self.line).ERROR2(self.history[-1])
                                    break

                            else:
                                self.error = ERRORS(self.line).ERROR3('finally')
                                break

                        elif self.get_block == 'empty'   :
                            if self.space <= 2:
                                self.space += 1
                            else:
                                self.error = ERRORS(self.line).ERROR4()
                                break
                       
                        else:
                            self.error = ERRORS(self.line).ERROR4()
                            break
                    else: break

            except KeyboardInterrupt:
                self.error = ERRORS(self.line).ERROR4()
                break

        if self.error is None:
            if self.get_errors:
                self.error = self.locked_error[ 0 ]
                if self.finally_key is False:
                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(self.before, self.after,
                                                                                            self.error)
                else: self._finally_key_ = self.finally_key
            else: pass
        else: pass

        ############################################################################

        return self._finally_key_ , self.error

class EXTERNAL_TRY_FOR_STATEMENT:
    def __init__(self, 
                master      :any, 
                data_base   :dict, 
                line        :int
                ):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_par                = lexer_and_parxer

    def TRY_STATEMENT(self, 
                tabulation  : int   = 1, 
                loop_list   : list  = None, 
                _type_      : str   = 'conditional'
                ):
        self.error                  = None
        self.locked_error           = []
        self.get_errors             = []
        self.active_calculations    = True
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_finally          = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'try' ]
        self.color                  = bm.fg.rbg(255, 199, 0 )
        self.before                 = end_except_finaly_else.CHECK_VALUES( self.data_base ).BEFORE()
        self.finally_key            = False
        self._finally_key_          = False
        self.except_key             = False
        self.loop_list              = loop_list
        self.next_line              = 0
        self.max_emtyLine           = 5

        ############################################################################

        for j, _string_ in enumerate( self.loop_list ):
            
            if j != self.next_line:
                self.if_line                        += 1
                self.line                           += 1
                self.normal_string, self.active_tab = _string_
                self.string                         = self.normal_string

                if self.string:
                    if self.active_tab is True:

                        self.get_block, self.value, self.error = end_except_finaly_else.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )

                        if self.error  is None:

                            if self.get_block   == 'begin:'  :
                                self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                                self.store_value.append(self.normal_string)

                                self.error = comment.COMMENT_STATEMENT(self.master,
                                            self.data_base, self.line).COMMENT( self.tabulation + 1)

                                if self.error is None:
                                    #################################################
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    ################################################

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.locked_error.append(self.error)
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                        self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append(self._error_)

                            elif self.get_block == 'if:'     :
                                self.next_line  = j + 1
                                self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                                self.store_value.append(self.normal_string)

                                self.error = if_statement.INTERNAL_IF_LOOP_STATEMENT( self.master,
                                            self.data_base, self.line ).IF_STATEMENT( self.value, self.tabulation + 1,
                                                                                    self.loop_list[ self.next_line ], _type_)

                                if self.error is None:
                                    #################################################
                                    self.history.append( 'if' )
                                    self.space = 0
                                    ################################################
                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before_init, self.after, self.error)
                                            self.error = None
                                else:
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init,self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )

                            elif self.get_block == 'try:'    :
                                
                                self.next_line  = j + 1
                                self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                                self.store_value.append( self.normal_string )

                                self._finally_key_, self.error = INTERNAL_TRY_FOR_STATEMENT( self.master,
                                            self.data_base, self.line ).TRY_STATEMENT( self.tabulation + 1,
                                                                                    self.loop_list[ self.next_line ], _type_ )
                                
                                if self.error is None:
                                    ###############################
                                    self.space = 0
                                    self.history.append( 'try' )
                                    ###############################
                                    
                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    if self._finally_key_ is not True:
                                        self.locked_error.append( self.error )
                                        self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                        self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(self.before,
                                                                                            self.after, self.error)
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append( self._error_ )

                                    else:
                                        self.locked_error.append( self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append( self._error_ )
                                            
                            elif self.get_block == 'unless:' :
                                self.next_line  = j + 1
                                self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                                self.store_value.append(self.normal_string)

                                self.error = unless_statement.INTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                            self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                                        self.loop_list[ self.next_line ])

                                if self.error is None:
                                    #################################
                                    self.history.append( 'unless' )
                                    self.space = 0
                                    #################################
                                    
                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.locked_error.append(self.error)
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                        self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append(self._error_)

                            elif self.get_block == 'switch:' :
                                self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                                self.store_value.append(self.normal_string)

                                self.error = switch_statement.SWITCH_STATEMENT( self.master,
                                            self.data_base, self.line ).SWITCH( self.value, self.tabulation + 1)

                                if self.error is None:
                                    #################################
                                    self.history.append( 'switch' )
                                    self.space = 0
                                    #################################

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.locked_error.append(self.error)
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                        self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append(self._error_)

                            elif self.get_block == 'empty'   :
                                if self.space <= self.max_emtyLine : self.space += 1
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break

                            elif self.get_block == 'any'     :
                                self.before_init = end_except_finaly_else.CHECK_VALUES( self.data_base ).BEFORE()
                                self.store_value.append( self.normal_string )

                                self.error = self.lex_par.LEXER_AND_PARXER( self.value, self.data_base,
                                                                self.line ).ANALYZE( _id_ = 1, _type_ = _type_)
                                if self.error is None:
                                    self.space = 0

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init,self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )

                        else: break
                    else:
                        self.get_block, self.value, self.error = end_except_finaly_else.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'    :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]

                                    if self.except_key is False and self.finally_key is False:
                                        self.error = ERRORS( self.line ).ERROR5()
                                        break
                                    else: break

                                else:
                                    self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                    break
                            elif self.get_block == 'except:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'except' )
                                        self.bool_value         = self.value
                                        self.store_value        = []
                                        self.except_key         = True

                                        if type( self.value ) == type( str()):
                                            if self.get_errors:
                                                if self.value in self.get_errors:
                                                    self.idd = self.get_errors.index( self.value )
                                                    del self.get_errors[ self.idd ]
                                                    del self.locked_error[ self.idd ]

                                                    self.active_calculations = True
                                                else: self.active_calculations = False
                                            else: self.active_calculations = True

                                        else:
                                            for _error_ in self.value:
                                                if self.get_errors:
                                                    if _error_ in self.get_errors:
                                                        self.idd = self.get_errors.index( _error_ )
                                                        del self.get_errors[ self.idd ]
                                                        del self.locked_error[ self.idd ]
                                                        self.active_calculations = True
                                                    else: self.active_calculations = False
                                                else: self.active_calculations = True

                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR1( 'finally' )
                                    break
                            elif self.get_block == 'finally:':
                                if self.index_finally < 1:
                                    if self.store_value:
                                        self.index_finally         += 1
                                        self.key_else_activation    = True
                                        self.store_value            = []
                                        self.history.append( 'finally' )
                                        self.active_calculations    = True
                                        self.finally_key            = True

                                        if self.get_errors:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                                self.before, self.after, self.error)
                                            self.error = None
                                        else:  pass
                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR3( 'finally' )
                                    break
                            elif self.get_block == 'empty'   :
                                if self.space <= self.max_emtyLine : self.space += 1
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
            if self.get_errors:
                self.error = self.locked_error[ 0 ]
                if self.finally_key is False :# and self._finally_key_ is None:
                    self.after = end_except_finaly_else.CHECK_VALUES( self.data_base ).AFTER()
                    self.error = end_except_finaly_else.CHECK_VALUES( self.data_base ).UPDATE( self.before, self.after,
                                                                                            self.error )
                else: self._finally_key_ = self.finally_key
            else: pass
        else:pass

        ############################################################################
        return self._finally_key_, self.error

class INTERNAL_TRY_FOR_STATEMENT:
    def __init__(self, 
                master      : any, 
                data_base   : dict, 
                line        : int
                ):
        
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_par                = lexer_and_parxer

    def TRY_STATEMENT(self, 
                tabulation  :int, 
                loop_list   :list, 
                _type_      : str   = 'conditional'):
        
        self.error                  = None
        self.locked_error           = []
        self.get_errors             = []
        self.active_calculations    = True
        self.string                 = ''
        self.normal_string          = ''
        self.end                    = ''
        self.store_value            = []
        self.index_finally          = 0
        self.if_line                = 0

        ############################################################################

        self.key_else_activation    = None
        self.space                  = 0
        self.active_tab             = None
        self.tabulation             = tabulation
        self.history                = [ 'try' ]
        self.color                  = bm.fg.rbg(0, 255, 255 )
        self.before                 = end_except_finaly_else.CHECK_VALUES( self.data_base ).BEFORE()
        self.finally_key            = False
        self._finally_key_          = False
        self.except_key             = False
        self.loop_list              = loop_list
        self.next_line              = 0
        self.max_emtyLine           = 5

        ############################################################################

        for j, _string_ in enumerate( self.loop_list ):

            if j != self.next_line:
                self.if_line                        += 1
                self.line                           += 1
                self.normal_string, self.active_tab = _string_
                self.string                         = self.normal_string

                if self.string:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = end_except_finaly_else.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1 )

                        if self.error  is None:
                            if self.get_block   == 'begin:' :
                                self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                                self.store_value.append( self.normal_string )

                                self.error = comment.COMMENT_STATEMENT(self.master,
                                                    self.data_base, self.line).COMMENT( self.tabulation + 1)

                                if self.error is None:
                                    #################################################
                                    self.history.append( 'begin' )
                                    self.space = 0
                                    ################################################

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init,self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )

                            elif self.get_block ==   'if:'  :
                                self.next_line  = j + 1
                                self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                                self.store_value.append(self.normal_string)

                                self.error = if_statement.EXTERNAL_IF_LOOP_STATEMENT(  self.master,
                                        self.data_base, self.line).IF_STATEMENT( self.value, self.tabulation + 1,
                                                                                self.loop_list[ self.next_line], _type_ )

                                if self.error is None:
                                    #################################################
                                    self.history.append( 'if' )
                                    self.space = 0
                                    ################################################
                                    
                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init,self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )

                            elif self.get_block == 'try:'   :
                                self.next_line  = j + 1
                                
                                self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                                self.store_value.append(self.normal_string)

                                self._finally_key_, self.error = EXTERNAL_TRY_FOR_STATEMENT( self.master,
                                            self.data_base, self.line ).TRY_STATEMENT( self.tabulation + 1,
                                                                                    self.loop_list[ self.next_line ], _type_ )
                                if self.error is None:
                                    ################################
                                    self.space = 0
                                    self.history.append( 'try' )
                                    ################################
                                    
                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    if self._finally_key_ is not True:
                                        self.locked_error.append( self.error )
                                        self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                        self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(self.before,
                                                                                            self.after, self.error)
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append( self._error_ )
                                        
                                    else:
                                        self.locked_error.append( self.error )
                                        self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                        self.get_errors.append( self._error_ )
                                                
                            elif self.get_block == 'unless:':
                                self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                                self.store_value.append(self.normal_string)

                                self.error = unless_statement.EXTERNAL_UNLESS_FOR_STATEMENT( self.master,
                                            self.data_base, self.line ).UNLESS_STATEMENT( self.value, self.tabulation + 1,
                                                                                        self.loop_list[ self.next_line])

                                if self.error is None:
                                    #################################################
                                    self.history.append( 'unless' )
                                    self.space = 0
                                    ################################################
                                    
                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.locked_error.append(self.error)
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                        self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append(self._error_)

                            elif self.get_block == 'switch:':
                                self.before_init = end_except_finaly_else.CHECK_VALUES(self.data_base).BEFORE()
                                self.store_value.append(self.normal_string)

                                self.error = switch_statement.SWITCH_STATEMENT(self.master,
                                                self.data_base, self.line).SWITCH(self.value, self.tabulation + 1)

                                if self.error is None:
                                    #################################################
                                    self.history.append( 'switch' )
                                    self.space = 0
                                    ################################################

                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before_init, self.after, self.error)
                                            self.error = None

                                else:
                                    self.locked_error.append(self.error)
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                        self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append(self._error_)

                            elif self.get_block == 'empty'  :
                                if self.space <= self.max_emtyLine : self.space += 1
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()

                            elif self.get_block == 'any'    :
                                self.before_init = end_except_finaly_else.CHECK_VALUES( self.data_base ).BEFORE()
                                self.store_value.append( self.normal_string )

                                self.error = self.lex_par.LEXER_AND_PARXER(self.value, self.data_base,
                                                        self.line).ANALYZE(_id_ = 1, _type_ = _type_)

                                if self.error is None:
                                    self.space = 0
                                    if self.active_calculations is True: pass
                                    elif self.active_calculations is False:
                                        if not self.get_errors: pass
                                        else:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                        self.before_init, self.after, self.error)
                                            self.error = None
                                else:
                                    self.locked_error.append( self.error )
                                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                                            self.before_init, self.after, self.error)
                                    self._error_, _ = self.analyze.DELETE_SPACE( fe.FileErrors( self.error ).initError() )
                                    self.get_errors.append( self._error_ )

                        else: break
                    else:
                        self.get_block, self.value, self.error = end_except_finaly_else.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'    :
                                if self.store_value:
                                    del self.store_value[:]
                                    del self.history[:]

                                    if self.except_key is False and self.finally_key is False:
                                        self.error = ERRORS(self.line).ERROR5()
                                        break
                                    else: break
                                else:
                                    self.error = ERRORS(self.line).ERROR2(self.history[-1])
                                    break
                            elif self.get_block == 'except:' :
                                if self.key_else_activation == None:
                                    if self.store_value:
                                        self.history.append( 'except' )
                                        self.bool_value     = self.value
                                        self.store_value    = []
                                        self.except_key     = True

                                        if type( self.value ) == type( str() ):
                                            if self.get_errors:
                                                if self.value in self.get_errors:
                                                    self.idd = self.get_errors.index( self.value )
                                                    del self.get_errors[ self.idd ]
                                                    del self.locked_error[ self.idd ]

                                                    self.active_calculations = True
                                                else: self.active_calculations = False
                                            else: self.active_calculations = True

                                        else:
                                            for _error_ in self.value:
                                                if self.get_errors:
                                                    if _error_ in self.get_errors:
                                                        self.idd = self.get_errors.index( _error_ )
                                                        del self.get_errors[ self.idd ]
                                                        del self.locked_error[ self.idd ]
                                                        self.active_calculations = True
                                                    else: self.active_calculations = False
                                                else: self.active_calculations = True

                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR1('finally')
                                    break
                            elif self.get_block == 'finally:':
                                if self.index_finally < 1:
                                    if self.store_value:
                                        self.index_finally += 1
                                        self.key_else_activation = True
                                        self.store_value = []
                                        self.history.append('finally')
                                        self.active_calculations = True
                                        self.finally_key = True

                                        if self.get_errors:
                                            self.error = True
                                            self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                                            self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(
                                                self.before, self.after, self.error)
                                            self.error = None
                                        else: pass
                                    else:
                                        self.error = ERRORS(self.line).ERROR2(self.history[-1])
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR3('finally')
                                    break
                            elif self.get_block == 'empty'   :
                                if self.space <= self.max_emtyLine: self.space += 1
                                else:
                                    self.error = ERRORS(self.line).ERROR4()
                                    break
                            else:
                                self.error = ERRORS(self.line).ERROR4()
                                break
                        else:  break
                else: pass
            else:
                self.if_line        += 1
                self.line           += 1
                self.next_line      = None

        if self.error is None:
            if self.get_errors:
                self.error = self.locked_error[ 0 ]
                if self.finally_key is False:
                    self.after = end_except_finaly_else.CHECK_VALUES(self.data_base).AFTER()
                    self.error = end_except_finaly_else.CHECK_VALUES(self.data_base).UPDATE(self.before, self.after,
                                                                                            self.error)
                else: self._finally_key_ = self.finally_key
            else: pass
        else:pass

        ############################################################################
        
        return self._finally_key_, self.error

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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str = 'finally'):
        error = '{}is already defined. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. {}<< {} >> {}block '.format(self.white, self.cyan, 
                                                                                                string, self.white) + error
        return self.error+self.reset

    def ERROR2(self, string):
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format( self.green, self.white,
                                                            self.cyan, string, self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. '.format(self.white) + error

        return self.error+self.reset

    def ERROR3(self, string: str = 'finally'):
        error = ' {}<< {} >> {}blocks. {}line: {}{}'.format(self.cyan, string, self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax due to many '.format(self.white) + error
        return self.error+self.reset

    def ERROR4(self):
        self.error = fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format( self.red, 
                                                                                            self.white, self.yellow, self.line)
        return self.error+self.reset

    def ERROR5(self):
        error = '{}<< except >> {}or {}<< finally >> {}statement blocks. {}line: {}{}'.format(self.cyan, self.white, self.red, self.white,
                                                                                       self.white, self.yellow, self.line)
        self.error =fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax. no '.format(self.white) + error
        return self.error+self.reset