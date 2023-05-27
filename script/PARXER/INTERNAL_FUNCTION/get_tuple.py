from script                                         import control_string
from script.LEXER                                   import particular_str_selection
from script.LEXER                                   import main_lexer
from script.LEXER                                   import check_if_affectation
from script.PARXER                                  import numerical_value
from script.LEXER.FUNCTION                          import main
from script.STDIN.LinuxSTDIN                        import bm_configure as bm
from script.PARXER.INTERNAL_FUNCTION                import get_list
from src.classes.Tuples                             import Tuples
from src.classes                                    import error as er        
from CythonModules.Windows                          import fileError as fe 



class TUPLE:
    def __init__(self, master: str, data_base: dict, line: int):
        self.line                       = line
        self.master                     = master
        self.data_base                  = data_base

        self.control                    = control_string.STRING_ANALYSE(self.data_base, self.line)
        self.selection                  = particular_str_selection
        self.lexer                      = main_lexer
        self.numeric                    = numerical_value
        self.affectation                = check_if_affectation
        self.variables                  = self.data_base[ 'variables' ][ 'vars' ]

    def TUPLE(self):
        self.error                      = None
        self.type                       = self.master[ 'type' ]
        self.main_dict                  = self.master[ 'numeric' ][ 0 ]
        self._return_                   = []

        self.string     = self.main_dict[ 1: -1]
        self.string, self.error = self.control.DELETE_SPACE( self.string )

        if self.error is None:
            self.value, self.error = self.selection.SELECTION( self.string, self.string, self.data_base,
                                                        self.line).CHAR_SELECTION( ',' )
            if self.error is None:
                for _value_ in self.value:
                    self.true_value, self.error = self.control.DELETE_SPACE( _value_ )
                    if self.error is None:
                        self.check_dot, self.error = self.selection.SELECTION(self.true_value, self.true_value,
                                                                self.data_base,self.line).CHAR_SELECTION( ':' )
                        if self.error is None:
                            if len( self.check_dot ) == 1:
                                self.dict_value, self.error = self.affectation.AFFECTATION(self.true_value,
                                                            self.true_value,self.data_base, self.line ).DEEP_CHECKING()

                                if self.error is None:
                                    if 'operator' not in list( self.dict_value.keys() ):
                                        self.lex, self.error = self.lexer.FINAL_LEXER( self.string, self.data_base,
                                                                        self.line).FINAL_LEXER( self.dict_value, _type_ = None )
                                        if self.error is None:
                                            self.all_data = self.lex[ 'all_data' ]
                                            if self.all_data is not None:
                                                self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                    self.data_base,self.line).ANALYSE( self.main_dict )
                                                if self.error is None:
                                                    if type( self.final_val[ 0 ]) not in [ type( list() ), type( dict() )]:
                                                        self._return_.append( self.final_val[ 0 ] )
                                                    else:
                                                        if type( self.final_val[0] ) == type( list() ):
                                                            self.error = ERRORS( self.line ).ERROR8( 'a list' )
                                                            break
                                                        else:
                                                            self.error = ERRORS(self.line).ERROR8('a dictionary' )
                                                            break
                                                else: break
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.main_dict )
                                                break
                                        else:  break
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = ERRORS( self.line ).ERROR0(self.main_dict, self.operator )
                                        break
                                else: break
                            else:
                                self.error = ERRORS( self.line ).ERROR1( self.main_dict, ':' )
                                break
                        else:  break
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.main_dict )
                        break
            else: pass
        else:
            self.error = None
            self._return_ = tuple( self._return_ )

        return tuple( self._return_ ), self.error

    def MAIN_TUPLE(self, main_string: str):
        self.error              = None
        self.numeric            = self.master[ 'numeric' ]
        self._return_           = []
        self.historyOfFunctions = []
        self.tupleFunctions     = [ 'empty', 'init', 'enumerate', 'size', 'choice', 'index', 'count'] 

        if self.numeric is not None:
            self.tuple_values, self.error = TUPLE( self.master, self.data_base, self.line ).TUPLE()
            if self.error is None:
                self._return_ = self.tuple_values
            else: pass

        else:
            self._names_        = self.master[ 'names' ]
            self.expressions    = self.master[ 'expressions' ]
            self.params         = self.master[ 'add_params' ]

            if self._names_[ 0 ] is None:
                if len( self._names_ ) == 2:
                    self.main_expression = {'numeric': [self.expressions[ 0 ] ], 'type': 'string' }
                    self.tuple_values, self.error = TUPLE(self.main_expression, self.data_base, self.line).TUPLE()
                    
                    if self.error is None:
                        if self._names_[ 1 ] in self.tupleFunctions:
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
                                    self._return_, self.error = Tuples.TUPLE( self.data_base, self.line, self.tuple_values,
                                                                        self.name, self.dictionary[ 'functions' ]).TUPLE( 'tuple' )
                                    if self.error is None:
                                        if self.params[ 1 ] is None : pass
                                        else: 
                                            self._return_, _, self.error = get_list.LIS_OPTIONS( [ self.master ], self.master, self.data_base, 
                                                                    self.line ).ARGUMENT_LIST( self._return_, self.params[ 1 ], function = True )
                                    else: pass                                                       
                                else: pass    
                            
                            else: self.error = er.ERRORS( self.line ).ERROR22( self._names_[ 1 ], 'tuple()' )
                        else: self.error = er.ERRORS( self.line ).ERROR22( self._names_[ 1 ], 'tuple()' )
                    else:  pass
                else: self.error = ERRORS( self.line ).ERROR0( main_string )
            else: self.error = ERRORS( self.line ).ERROR0( main_string )

        return self._return_, self.error

class ERRORS:
    def __init__(self, line:int):
        self.line       = line
        self.cyan       = bm.init.bold + bm.fg.rbg(0,255,255)
        self.red        = bm.init.bold + bm.fg.rbg(255,0,0)
        self.green      = bm.init.bold + bm.fg.rbg(0,255,0)
        self.yellow     = bm.init.bold + bm.fg.rbg(255,255,0)
        self.magenta    = bm.init.bold + bm.fg.rbg(255,0,255)
        self.white      = bm.init.bold + bm.fg.rbg(255,255,255)
        self.blue       = bm.init.bold + bm.fg.rbg(0,0,255)
        self.reset      = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{} invalid syntax in {}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str, char: str):
        error = '{}due to {}<< {} >>. {}line: {}{}'.format( self.white, self.red, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR2(self, string: str, char:str):
        error = '{}the {}keyword {}of value {}<< {} >> {}is not defined. {}line: {}{}'.format( self.white, self.yellow, self.white, self.red, char, self.white,
                                                                                               self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR3(self, string: str, char1: str = 'keyword', char2:str='value', char: str = None):
        error = '{}{} {}is not defined for the {}{} {}<< {} >>. {}line: {}{}'.format(self.red, char, self.white, self.green, char2, self.magenta, char,
                                                                                self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR4(self, string: str, char: str):
        error = '{}due to the fact that {}<< {} >> {}is {}EMPTY. {}line: {}{}'.format( self.white, self.red, char, self.white, self.yellow,
                                                                                                    self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR5(self, string: str, char: str):
        error = '{}keyword {}<< {} >> {}is repeated. {}line: {}{}'.format(self.white, self.red, char, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR6(self, string: str, char: str):
        error = '{}argument {}<< {} >> {}is repeated. {}line: {}{}'.format(self.white, self.red, char, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR7(self, char: str, func = 'get( )'):
        error = '{}<< {} >>. {}line: {}{}'.format(self.red, char,  self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors()+'{}<< {} >> {}has not attributed '.format(self.cyan, func, self.white) + error

        return self.error+self.reset

    def ERROR8(self, string: str = 'a list'):
        error = '{}{}. {}line: {}{}'.format(self.yellow, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}tuple {}object cannot contain '.format(self.cyan, self.white) + error

        return self.error+self.reset
