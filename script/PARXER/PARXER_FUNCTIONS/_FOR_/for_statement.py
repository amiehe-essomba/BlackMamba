from script                                             import control_string
from script.STDIN.WinSTDIN                              import stdin
import cython
from script.PARXER.PARXER_FUNCTIONS._FOR_               import end_for_else
from script.PARXER.LEXER_CONFIGURE                      import lexer_and_parxer
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_if
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_try
from script.PARXER.PARXER_FUNCTIONS._FOR_               import for_unless
from script.LEXER.FUNCTION                              import main
from script.PARXER                                      import parxer_assembly
from script.STDIN.LinuxSTDIN                            import bm_configure as bm
try:
    from CythonModules.Windows                          import fileError as fe 
except ImportError:
    from CythonModules.Linux                            import fileError as fe


class EXTERNAL_FOR_STATEMENT:
    def __init__(self, master:any, data_base:dict, line:int):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def FOR_STATEMENT(self, tabulation : int = 1, _type_ : str = 'loop'):
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
        self.color                  = bm.fg.rbg(255, 255, 0)
        self.loop_for               = []
        ke                          = bm.fg.rbg(255, 255, 0)

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            self.line       += self.if_line

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.line ).STDIN({ '0': ke, '1': self.color }, self.tabulation )
                if self.error is None:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = end_for_else.INTERNAL_BLOCKS( self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1, function = _type_ )

                        if self.error  is None:

                            if self.get_block   == 'if:'            :
                                self.store_if_values    = []
                                self.store_if_values.append( (self.normal_string, True) )
                                self.if_values, self.error = for_if.INTERNAL_IF_STATEMENT( self.master,
                                        self.data_base, self.line ).IF_STATEMENT( self.value, self.tabulation + 1, _type_=_type_ )

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'if' )
                                    self.store_if_values.append( self.if_values )

                                    self.loop_for.append( {'if' : self.store_if_values, 'value' : self.value,
                                    'tabulation' : (self.tabulation + 1) } )

                                    self.store_if_values = []
                                else:break 
                            
                            elif self.get_block == 'unless:'        :
                                self.store_if_values    = []
                                self.store_if_values.append( (self.normal_string, True) )
                                self.if_values, self.error = for_unless.INTERNAL_UNLESS_STATEMENT( self.master,
                                        self.data_base, self.line ).UNLESS_STATEMENT( self.tabulation + 1 )

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'unless' )
                                    self.store_if_values.append( self.if_values )

                                    self.loop_for.append( {'unless' : self.store_if_values, 'value' : self.value,
                                    'tabulation' : (self.tabulation + 1) } )

                                    self.store_if_values = []
                                else: break

                            elif self.get_block == 'try:'           :
                                self.store_if_values    = []
                                self.store_if_values.append( ( self.normal_string, True ) )
                                self.try_values, self.error = for_try.INTERNAL_TRY_STATEMENT( self.master,
                                        self.data_base, self.line ).TRY_STATEMENT( self.tabulation + 1 )

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'try' )
                                    self.store_if_values.append( self.try_values )

                                    self.loop_for.append( {'try' : self.store_if_values, 'value' : self.value,
                                    'tabulation' : (self.tabulation + 1) } )

                                    self.store_if_values = []
                                else:break

                            elif self.get_block == 'empty'          :
                                if self.space <= 2:
                                    self.space += 1
                                    self.loop_for.append( {'empty' : (self.normal_string, True), 'value': None,
                                                          'tabulation' : (self.tabulation + 1) } )
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break

                            elif self.get_block == 'any'            :
                                self.store_value.append( self.normal_string )
                                self._lexer_, self.error = self.lex_par.MAIN(self.value, self.data_base,
                                                                    self.line).MAIN_LEXER( _id_=1, _type_='loop' )
                                if self.error is None:
                                    self.loop_for.append( {'any' : (self.value, True), 'value' : None,
                                                           'tabulation' : (self.tabulation + 1),
                                                           'lex' : self._lexer_} )
                                    self.space  = 0
                                else:break

                        else:break

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
                                    self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                    break

                            elif self.get_block == 'else:' :
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.store_value            = []
                                        self.history.append( 'else' )
                                        self.loop_for.append( (self.normal_string, False) )

                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                        break

                                else:
                                    self.error = ERRORS( self.line ).ERROR3( 'else' )
                                    break

                            elif self.get_block == 'empty' :
                                if self.space <= 2:
                                    self.space += 1
                                    self.loop_for.append( (self.normal_string, False ))
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break

                            else:
                                self.error = ERRORS( self.line ).ERROR4()
                                break
                        else:break

                else:
                    if self.tabulation == 1: break
                    else:
                        self.get_block, self.value, self.error = end_for_else.EXTERNAL_BLOCKS(self.string,
                                            self.normal_string, self.data_base, self.line).BLOCKS( self.tabulation )

                        if self.error is None:
                            if   self.get_block == 'end:'  :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop_for.append( (self.normal_string, False ))

                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR2(self.history[ -1 ] )
                                    break

                            elif self.get_block == 'else:' :
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.store_value            = []
                                        self.history.append( 'else' )
                                        self.loop_for.append( (self.normal_string, False ))

                                    else:
                                        self.error = ERRORS(self.line).ERROR2(self.history[-1])
                                        break
                                else:
                                    self.error = ERRORS(self.line).ERROR3( 'else' )
                                    break

                            elif self.get_block == 'empty' :
                                if self.space <= 2:
                                    self.space += 1
                                    self.loop_for.append((self.normal_string, False))
                                else:
                                    self.error = ERRORS(  self.line ).ERROR4()
                                    break

                            else:
                                self.error = ERRORS( self.line ).ERROR4()
                                break
                        else:break

            except KeyboardInterrupt:
                self.error = ERRORS( self.line ).ERROR4()
                break

        ############################################################################

        return {'for' : self.loop_for},  self.tabulation, self.error

class INTERNAL_FOR_STATEMENT:
    def __init__(self, master:any, data_base:dict, line:int):
        self.line                   = line
        self.master                 = master
        self.data_base              = data_base
        self.analyze                = control_string
        self.lex_par                = lexer_and_parxer

    def IF_STATEMENT(self, tabulation: int):
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
        self.color                  = bm.fg.rbg(252, 127, 0 )
        self.loop_for               = []
        ke                          = bm.fg.rbg(255, 255, 0)

        ############################################################################

        while self.end != 'end:' :
            self.if_line    += 1
            self.line       += self.if_line

            try:
                self.string, self.normal_string, self.active_tab, self.error = self.stdin = stdin.STDIN( self.data_base,
                                            self.line ).STDIN({'0': ke, '1': self.color}, self.tabulation )

                if self.error is None:
                    if self.active_tab is True:
                        self.get_block, self.value, self.error = end_for_else.INTERNAL_BLOCKS(self.string,
                                        self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation + 1)

                        if self.error  is None:

                            if self.get_block   == 'if:'            :
                                self.store_if_values = []
                                self.store_if_values.append((self.normal_string, True))
                                self.if_values, self.error = for_if.EXTERNAL_IF_STATEMENT(self.master,
                                                            self.data_base,self.line).IF_STATEMENT(self.tabulation + 1)

                                if self.error is None:
                                    self.store_value.append(self.normal_string)
                                    self.history.append( 'if' )
                                    self.store_if_values.append(self.if_values)
                                    self.loop_for.append( {'if': self.store_if_values, 'value': self.value,
                                                          'tabulation': (self.tabulation + 1)} )
                                    self.store_if_values = []
                                else:break

                            elif self.get_block == 'unless:'        :
                                self.store_if_values    = []
                                self.store_if_values.append( (self.normal_string, True) )
                                self.if_values, self.error = for_unless.EXTERNAL_UNLESS_STATEMENT( self.master,
                                        self.data_base, self.line ).UNLESS_STATEMENT( self.tabulation + 1 )

                                if self.error is None:
                                    self.store_value.append( self.normal_string )
                                    self.history.append( 'unless' )
                                    self.store_if_values.append( self.if_values )

                                    self.loop_for.append( {'unless' : self.store_if_values, 'value' : self.value,
                                    'tabulation' : (self.tabulation + 1) } )

                                    self.store_if_values = []
                                else:break

                            elif self.get_block == 'empty'          :
                                if self.space <= 2:
                                    self.space += 1
                                    self.loop_for.append( {'empty': (self.normal_string, True), 'value': None,
                                                          'tabulation': (self.tabulation + 1)} )
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()

                            elif self.get_block == 'any'            :
                                self.store_value.append(self.normal_string)
                                self.loop_for.append({'any': (self.normal_string, True), 'value': None,
                                                      'tabulation': (self.tabulation + 1)} )
                                self.space = 0

                        else:break

                    else:
                        self.get_block, self.value, self.error = end_for_else.EXTERNAL_BLOCKS( self.string,
                                    self.normal_string, self.data_base, self.line ).BLOCKS( self.tabulation )

                        if self.error is None:
                            if self.get_block   == 'end:' :
                                if self.store_value:
                                    del self.store_value[ : ]
                                    del self.history[ : ]
                                    self.loop_for.append( (self.normal_string, False) )

                                    break
                                else:
                                    self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ])
                                    break

                            elif self.get_block == 'else:':
                                if self.index_else < 1:
                                    if self.store_value:
                                        self.index_else             += 1
                                        self.store_value            = []
                                        self.history.append('else')
                                        self.loop_for.append( (self.normal_string, False) )
                                    else:
                                        self.error = ERRORS( self.line ).ERROR2( self.history[ -1 ] )
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR3( 'else' )
                                    break

                            elif self.get_block == 'empty':
                                if self.space <= 2:
                                    self.space += 1
                                    self.loop_for.append( (self.normal_string, False) )
                                else:
                                    self.error = ERRORS( self.line ).ERROR4()
                                    break

                            else:
                                self.error = ERRORS( self.line ).ERROR4()
                                break

                        else:break

                else:
                    self.get_block, self.value, self.error = end_for_else.EXTERNAL_BLOCKS(self.string,
                                self.normal_string, self.data_base,self.line).BLOCKS( self.tabulation )

                    if self.error is None:
                        if self.get_block   == 'end:' :
                            if self.store_value:
                                del self.store_value[ : ]
                                del self.history[ : ]
                                self.loop_for.append( (self.normal_string, False) )

                                break
                            else:
                                self.error = ERRORS(self.line).ERROR2(self.history[ -1 ])
                                break

                        elif self.get_block == 'else:':
                            if self.index_else < 1:
                                if self.store_value:
                                    self.index_else             += 1
                                    self.store_value            = []
                                    self.history.append( 'else' )
                                    self.loop_for.append( (self.normal_string, False) )
                                else:
                                    self.error = ERRORS(self.line).ERROR2(self.history[ -1 ])
                                    break
                            else:
                                self.error = ERRORS(self.line).ERROR3( 'else' )
                                break

                        elif self.get_block == 'empty':
                            if self.space <= 2:
                                self.space += 1
                                self.loop_for.append((self.normal_string, False))
                            else:
                                self.error = ERRORS(self.line).ERROR4()
                                break

                        else:
                            self.error = ERRORS( self.line ).ERROR4()
                            break

                    else:break

            except KeyboardInterrupt:
                self.error = ERRORS( self.line ).ERROR4()
                break

        ############################################################################

        return {'for': self.loop_for }, self.tabulation, self.error

@cython.cclass
class NEXT_ANALYZE:
    def __init__(self, master: str, data_base : dict, line : int):
        self.line               = line
        self.data_base          = data_base
        self.master             = master
        self.main               = main
        
    @cython.cfunc
    def SUB_ANALYZE(self, _id_:int = 1, _type_:any = None, _lexer_ : dict = None):
        self.error          = None
        #self.lexer          = _lexer_
        self.lexer, self.string, self.error = self.main.MAIN(self.master, self.data_base, self.line).MAIN(_id_, _type_, True)
        if self.error is None:
            self.error = parxer_assembly.ASSEMBLY(self.lexer, self.data_base, self.line).ASSEMBLY( self.master, True )
        else: pass

        return self.error

    @cython.cfunc
    def SUB_SUB_ANALYZE(self, _lexer_ : dict = None):
        self.lexer          = _lexer_
        self.error = parxer_assembly.ASSEMBLY(self.lexer, self.data_base, self.line).ASSEMBLY( self.master, True )
        
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
        self.error =  fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format( self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str = 'else'):
        error = '{}is already defined. line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. {}<< {} >> {}block '.format(self.white, self.cyan, string, self.green) + error

        return self.error+self.reset

    def ERROR2(self, string):
        error = '{}no values {}in the previous statement {}<< {} >> {}block. {}line: {}{}'.format(self.green, self.white, self.cyan, string, self.green,
                                                                                             self.white, self.yellow, self.line)
        self.error =  fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax. '.format(self.white) + error

        return self.error+self.reset

    def ERROR3(self, string: str = 'else'):
        error = '{}due to {}many {}<< {} >> {}blocks. {}line: {}{}'.format(self.redd, self.white, self.cyan, string, self.green, 
                                                                           self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax '.format(self.white) + error

        return self.error+self.reset

    def ERROR4(self):
        self.error = fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                                        self.white, self.yellow, self.line )
        return self.error+self.reset