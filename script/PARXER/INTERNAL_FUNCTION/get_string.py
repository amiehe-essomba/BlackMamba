from script                         import control_string
from script.LEXER                   import particular_str_selection
from script.LEXER                   import main_lexer
from script.LEXER                   import check_if_affectation
from script.PARXER                  import numerical_value
from script.STDIN.WinSTDIN          import stdin
from script.PARXER.LEXER_CONFIGURE  import numeric_lexer
from script.STDIN.LinuxSTDIN        import bm_configure as bm
from script.LEXER.FUNCTION          import main
from script.PARXER.INTERNAL_FUNCTION                import get_list
from script.PARXER.PARXER_FUNCTIONS.CLASSES         import classInit 
try:
    from CythonModules.Windows                      import fileError as fe 
except ImportError:
    from CythonModules.Linux                        import fileError as fe 


class STRING:
    def __init__(self, master: any, data_base : any, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base

        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.selection          = particular_str_selection
        self.lexer              = main_lexer
        self.numeric            = numerical_value
        self.affectation        = check_if_affectation
        self.variables          = self.data_base['variables']['vars']
        self.numeric_lex        = numeric_lexer

    def STRING(self):
        self.error              = None
        self.type               = self.master[ 'type' ]
        self.main_dict          = self.master[ 'numeric' ][ 0 ]
        self._return_           = ''
        self.check_name         = []
        self.internal_value     = False

        self.string             = self.main_dict[1 : -1]
        self.all_string, self.string_data, self.string_info, self.error = STRING( self.string, self.data_base,
                                                        self.line ).LOOKING_IF_BRACKET()
        if not self.string_data:
            self._return_ = str( self.string )
        else:
            for i, string in enumerate( self.string_data ):
                self._string_ , self.error = self.control.DELETE_SPACE( string[ 1 : -1 ] )
                if self.error is None:
                    self.final_val, self.error = self.numeric_lex.NUMERCAL_LEXER(self._string_, self.data_base,
                                                                self.line ).LEXER( string )
                    if self.error is None:
                        self.string_data[ i ] = str( self.final_val )
                    else:
                        self.error = self.error
                        break
                else:
                    self.error = None
                    self.string_data[ i ] = ''

            self.index_str      = 0
            self.index_data     = 0

            for i, str_ in enumerate( self.string_info ):
                if str_ == 'string':
                    self.index_str += 1
                    self._return_ += self.all_string[ self.index_str - 1]
                else:
                    self.index_data += 1
                    self._return_ += self.string_data[ self.index_data - 1]

        if self.error is None:
            self.all_string, self.string_data, self.string_info, self.error = STRING( self._return_, self.data_base,
                                                        self.line ).LOOKING_IF_BRACKET('[', ']')

            if self.error is None:
                if not self.string_data:
                    self._return_ = self._return_
                else:
                    self.internal_value = True
                    for i, string in enumerate(self.string_data):
                        self._string_, self.error = self.control.DELETE_SPACE( self.string )
                        if self.error is None: pass
                        else: pass
            else: pass
        else: pass

        return self._return_, self.internal_value, self.error

    def MAIN_STRING(self, main_string: str):
        self.error              = None
        self.numeric            = self.master[ 'numeric' ]
        self._return_           = ''
        self.historyOfFunctions = []
        self.strFunctions       = [ 'upper', 'lower', 'capitalize', 'empty', 'enumerate', 'split', 'join', 'format', 'index', 'rstrip', 'lstrip',
                                    'count', 'endwith', 'startwith', 'replace', 'size']
        self.subStrFunctions    = ['upper', 'lower', 'capitalize']
        self.asSubStrFunctions  = ['split', 'isEMPTY', 'enumerate']
                
        if self.numeric is not None:
            self.string_values, self.key, self.error = STRING(self.master, self.data_base, self.line).STRING()
            if self.error is None: self._return_ = self.string_values
            else: pass
        else:
            self._names_        = self.master[ 'names' ]
            self.expressions    = self.master[ 'expressions' ]
            self.params         = self.master[ 'add_params' ]

            if self._names_[ 0 ] is None:
                if len( self._names_ ) == 2:
                    self.main_expression = {'numeric': [self.expressions[ 0 ] ], 'type': 'string' }
                    self.dict_values, _, self.error = STRING(self.main_expression, self.data_base, self.line).STRING()

                    if self.error is None:
                        if self._names_[ 1 ] in self.strFunctions:
                            if self._names_[ 1 ] != self.expressions[ 1 ]:
                                self.historyOfFunctions.append( self._names_[ 1 ] )
                                self.expression         = 'def '+self.expressions[ 1 ]+ ':'
                                self.dictionary         = {
                                'functions'             : [],
                                'func_names'            : []
                                }
                                self.lexer, self.normal_expression, self.error = main.MAIN( self.expression, self.dictionary,
                                                                            self.line ).MAIN( def_key = 'indirect' )
                                if self.error is None: 
                                    self.name = self._names_[ 1 ]
                                    self._return_, self.error = classInit.STRING( self.data_base, self.line, self.dict_values,
                                                                        self.name, self.dictionary[ 'functions' ]).STR( 'string', main_string)
                                    if self.error is None:
                                        if self.params[ 1 ] is None : pass
                                        else: 
                                            self._return_, _, self.error = get_list.LIS_OPTIONS( [ self.master ], self.master, self.data_base, 
                                                                    self.line ).ARGUMENT_LIST( self._return_, self.params[ 1 ], function = True )
                                    else: pass                                                       
                                else: pass    
                            
                            else: self.error = classInit.ERRORS( self.line ).ERROR22( self._names_[ 1 ] )
                        else: self.error = classInit.ERRORS( self.line ).ERROR22( self._names_[ 1 ] )
                    else:  pass
                else: self.error = ERRORS( self.line ).ERROR0( main_string )
            else: self.error = ERRORS( self.line ).ERROR0( main_string )
        
        return  self._return_, self.error

    def LOOKING_IF_BRACKET(self, start: str = '{', end: str = '}'):
        self.active_key         = None
        self.l                  = 0
        self.r                  = 0
        self.bracket            = [start, end ]
        self.string_storage     = []
        self.data_storage       = []
        self.error              = None
        self.string1            = ''
        self.string2            = ''
        self.count              = []

        for i, str_, in enumerate( self.master ):
            self.l, self.r = self.l + str_.count( start ), self.r + str_.count( end )
            if self.l != self.r:
                self.active_key = True
            elif self.l == self.r and str_ == self.bracket[ 1 ] :
                 self.active_key = False
            elif self.l == self.r and str_ != self.bracket[ 1 ] :
                self.active_key = None

            if self.active_key == True:
                self.string1 += str_
            elif self.active_key == False:
                self.string1 += str_
                self.data_storage.append(self.string1)
                self.string1 = ''

                if self.string2:
                    self.string_storage.append( self.string2 )
                    self.count.append( 'string' )
                    self.string2 = ''
                else:
                    self.string2 = ''

                self.count.append( 'dict' )

                self.active_key = None
                self.l          = 0
                self.r          = 0

            else:
                self.string1 = ''
                self.string2 += str_
                if i != len( self.master ) - 1:
                    pass
                else:
                    self.string_storage.append( self.string2 )
                    self.count.append( 'string' )

        return self.string_storage, self.data_storage, self.count, self.error

class FORMAT:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.data_base      = data_base
        self.master         = master
        self.control        = control_string.STRING_ANALYSE(self.data_base, self.line)
        self.selection      = particular_str_selection
        self.numeric        = numerical_value
        self.affectation    = check_if_affectation
        self.lexer          = main_lexer
        self.numeric_lex    = numeric_lexer

    def STRING_FORMAT(self, main_string: str):
        self.error          = None
        self.real           = ['f', 'd', 'e']
        self.space          = ['x']
        self.integer        = ['i']
        self.complex        = ['g']
        self.string         = ['a']
        self.type           = 'default'
        self.list           = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'x']

        self.string = self.master[ 1 : -1 ]
        self.string,self.error = self.control.DELETE_SPACE( self.string )
        if self.error is None:
            self.data, self.error = self.selection.SELECTION( self.string, self.string, self.data_base,
                                                              self.line ).CHAR_SELECTION( ';' )
            if self.error is None:
                for i, string in enumerate( self.data ):
                    self._string_, self.error = self.control.DELETE_SPACE( string )
                    if self.error is None:
                        self._sub_string_, self.error = self.selection.SELECTION(self._string_, self._string_,
                                                            self.data_base, self.line).CHAR_SELECTION( '.' )
                        if len( self._sub_string_ ) == 1:
                            if self._string_ in self.list:
                                pass
                        elif len( self._sub_string_ ) == 2:
                            self.char_, self.error = self.control.DELETE_SPACE( self._sub_string_[ 0 ])
                            if self.error is None:
                                self._int_, self.error = self.control.DELETE_SPACE( self._sub_string_[ 1 ] )
                                if self.error is None:
                                    self.final_val, self.error = self.numeric_lex.NUMERCAL_LEXER( self._int_,
                                                                self.data_base, self.line).LEXER( self._string_ )
                                    if self.error is None:
                                        self._integer_ = self.final_val
                                    else:
                                        self.error = self.error
                                        break
                                else:
                                    self.error = ERRORS( self.line ).ERROR0( self._string_)
                                    break
                            else:
                                self.error = ERRORS( self.line ).ERROR0( self._string_ )
                                break
                        else:
                            self.error = ERRORS( self.line ).ERROR0( self._string_ )
                            break
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.master )
                        break
            else:
                self.error = self.error
        else:
            self.error = None
            self.type = self.type

class STRING_FUNCTIONS:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line           = line
        self.data_base      = data_base
        self.master         = master
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.selection      = particular_str_selection
        self.lexer          = main_lexer
        self.numeric        = numerical_value
        self.numeric_lex    = numeric_lexer

    def FORMAT(self, function_name: str, main_string: str, key: bool = False):
        self.error          = None
        self.type_of_data   = []
        self.len            = len( function_name )
        self.expression     = self.master[ self.len :  ]
        self.expression, self.error = self.control.DELETE_SPACE( self.expression )
        self.string         = self.expression[ 1 : -1 ]
        self.string, self.error = self.control.DELETE_SPACE( self.string )

        if self.error is None:
            self.data, self.error = self.selection.SELECTION( self.string, self.string, self.data,
                                                              self.line ).CHAR_SELECTION( ',' )
            if self.error is None:
                for i, value in enumerate( self.data ):
                    self._string_, self.error = self.control.DELETE_SPACE( value )
                    if self.error is None:
                        self.final_val, self.error = self.numeric_lex.NUMERCAL_LEXER( self._string_, self.data_base,
                                                                self.line ).LEXER( value )
                        if self.error is None:
                            self.data[ i ] = self.final_val
                            self.type_of_data.append( type( self.final_val ) )

                        else:
                            self.error = self.error
                            break
                    else:
                        self.error = ERRORS( self.line ).ERROR0( main_string )
                        break
            else:
                self.error = self.error

        else:
            self.error  = None
            self.data   = None

        return self.data, self.type_of_data, self.error

class ERRORS:
    def __init__(self, line:int):
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{} invalid syntax in {}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str, char: str):
        error = '{}due to {}<< {} >>. {}line: {}{}'.format(self.white, self.red, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset
    
    def ERROR2(self, string: str, name = 'string()'): #
        error = '{}has not {}<< {} >> {}as a function. {}line: {}{}'.format(self.white, self.green, string, self.red,
                                                                             self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors()+'{}{} {}type '.format(self.cyan, name, self.yellow) + error

        return self.error+self.reset

