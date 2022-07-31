from script                             import control_string
from script.LEXER                       import particular_str_selection
from script.PARXER.LEXER_CONFIGURE      import numeric_lexer
from script.PARXER.PRINT                import show_data
from script.STDIN.LinuxSTDIN            import bm_configure as bm
try:
    from CythonModules.Windows          import fileError as fe 
except ImportError:
    from CythonModules.Linux            import fileError as fe

class PRINT:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.selection          = particular_str_selection
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_par            = numeric_lexer

    def PRINT(self, key : bool = False):
        self.error              = None
        self.normal_string      = 'print ' + self.master
        self.list_of_values     = None

        self.master, self.error = self.control.DELETE_SPACE( self.master )
        if self.error is None:
            if self.master[ 0 ] == '*':
                self.master, self.error = self.control.DELETE_SPACE( self.master[1 : ])
                if self.error is None:
                    self.list_of_values, self.error = self.selection.SELECTION( self.master, self.master,
                                                                        self.data_base, self.line).CHAR_SELECTION( ',' )

                    if self.error is None:
                        for i, value in enumerate( self.list_of_values ):
                            self.value, self.error = self.control.DELETE_SPACE( value )
                            if self.error is None:
                                self.value, self.error = self.lex_par.NUMERCAL_LEXER( self.value, self.data_base,
                                                                                        self.line).LEXER( self.value )
                                if self.error is None:
                                    self.list_of_values[ i ] = self.value
                                else: break
                            else:
                                self.error = ERRORS( self.line ).ERROR0( self.normal_string )
                                break

                        if self.error is None:
                            if key is False:
                                if self.data_base[ 'loading' ] is False:
                                    PRINT_PRINT( self.list_of_values , self.data_base ).PRINT_PRINT( key = key)
                                else:self.data_base[ 'loading' ] = False
                            else: pass
                        else: pass
                    else: pass
                else: self.error = ERRORS( self.line ).ERROR0( self.normal_string )
            else: self.error = ERRORS( self.line ).ERROR1( self.normal_string, self.master )
        else: self.error = ERRORS( self.line ).ERROR0( self.normal_string )

        return self.list_of_values, self.error

class PRINT_PRINT:
    def __init__(self, master: any, data_base: dict):
        self.master         = master
        self.data_base      = data_base
        self.orange         = bm.fg.rbg(252, 127, 0 )
        self.cyan           = bm.fg.cyan_L
        self.red            = bm.fg.red_L
        self.green          = bm.fg.green_L
        self.yellow         = bm.fg.yellow_L
        self.magenta        = bm.fg.magenta_M
        self.white          = bm.fg.white_L
        self.blue           = bm.fg.blue_L
        self.reset          = bm.init.reset

    def PRINT_PRINT(self, key:bool = False, loop : bool = False):
        self.build_string   = ''
        self.__string__     = '{}[{} result{} ]{} : {}'.format(self.blue, self.orange, self.blue, self.white, self.reset)

        for i, value in enumerate( self.master ):
            if i < len( self.master ) - 1:
                self.build_string += show_data.SHOW(value, self.data_base, bool).PRINT() + '  '
            else: self.build_string += show_data.SHOW(value, self.data_base, bool).PRINT()

        self.build_string = self.__string__ + self.build_string

        if loop is False:
            if key is False: print( '{}\n'.format( self.build_string+bm.init.reset ) )
            else: pass
        
        else:
            
            if key is False: print( self.build_string+bm.init.reset )
            else: pass

class ERRORS:
    def __init__(self, line):
        self.line           = line
        self.cyan           = bm.fg.cyan_L
        self.red            = bm.fg.red_L
        self.green          = bm.fg.green_L
        self.yellow         = bm.fg.yellow_L
        self.magenta        = bm.fg.magenta_M
        self.white          = bm.fg.white_L
        self.blue           = bm.fg.blue_L
        self.reset          = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'invalid syntax in {}<< {} >> '.format(self.cyan, string) + error
        return self.error+self.reset

    def ERROR1(self, string: str, char:str):
        error = '{}<< * >> {}was not defined {}at beginning {}of {}<< {} >>. {}line: {}{}'.format(self.green, self.white, self.magenta, self.yellow,
                                                                                        self.cyan, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'invalid syntax in {}<< {} >> '.format(self.cyan, string) + error
        return self.error+self.reset
