from script                     import control_string
from script.LEXER               import particular_str_selection
from script.LEXER               import main_lexer
from script.LEXER               import check_if_affectation
from script.PARXER              import numerical_value
from script.STDIN.WinSTDIN      import stdin
from script.STDIN.LinuxSTDIN    import bm_configure as bm
from script.LEXER.FUNCTION      import main

from script.PARXER.INTERNAL_FUNCTION                import get_list
from script.PARXER.PARXER_FUNCTIONS.CLASSES         import classInit
try:
    from CythonModules.Windows                      import fileError as fe 
except ImportError:
    from CythonModules.Linux                        import fileError as fe 


class DICTIONARY:
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

    def DICT(self):
        self.error              = None
        self.type               = self.master[ 'type' ]
        self.main_dict          = self.master[ 'numeric' ][ 0 ]
        self._return_           = {}
        self.check_name         = []

        self.string             = self.main_dict[1 : -1]
        self.string, self.error = self.control.DELETE_SPACE( self.string )
        if self.error is None:
            self.value, self.error = self.selection.SELECTION( self.string, self.string, self.data_base,
                                                            self.line ).CHAR_SELECTION( ',' )
            if self.error is None:
                for i, _val_ in enumerate( self.value ):
                    self.new_string, self.error  = self.control.DELETE_SPACE( _val_ )
                    if self.error is None:
                        self.sub_value, self.error = self.selection.SELECTION(self.new_string, self.new_string,
                                                                self.data_base, self.line).CHAR_SELECTION( ':' )
                        if self.error is None:
                            if len( self.sub_value ) == 2:
                                self.name           = self.sub_value[ 0 ]
                                self.init_value     = self.sub_value[ 1 ]

                                if self.name:
                                    if self.init_value:
                                        self.name, self.error = self.control.DELETE_SPACE( self.name )
                                        if self.error is None:
                                            self.name, self.error = self.control.CHECK_NAME( self.name, True )
                                            if self.error is None:
                                                if not self.check_name:
                                                    self.check_name.append( self.name )
                                                else:
                                                    if self.name in self.check_name:
                                                        self.error = ERRORS( self.line ).ERROR5(self.main_dict, self.name)
                                                        break
                                                    else:
                                                        self.check_name.append( self.name )
                                                if self.error is None:
                                                    self.domain, self.error = self.affectation.AFFECTATION(self.init_value,
                                                                self.init_value, self.data_base,self.line ).DEEP_CHECKING()
                                                    if self.error is None:
                                                        if 'operator' in list( self.domain.keys() ):
                                                            self.operators = self.domain[ 'operator' ]
                                                            self.error = ERRORS( self.line ).ERROR1( self.main_dict, self.operators)
                                                            break
                                                        else:
                                                            self.lex, self.error = self.lexer.FINAL_LEXER(self.init_value,
                                                                self.data_base, self.line).FINAL_LEXER(self.domain, _type_=None)

                                                            if self.error is None:
                                                                self.all_data = self.lex[ 'all_data' ]

                                                                if self.all_data is not None:
                                                                    self.final_val, self.error = self.numeric.NUMERICAL(self.lex,
                                                                                self.data_base, self.line).ANALYSE( self.master )
                                                                    if self.error is None:
                                                                        self._return_[ self.name ] = self.final_val[ 0 ]
                                                                    else:
                                                                        self.error = self.error
                                                                        break
                                                                else:
                                                                    self.error = ERRORS( self.line ).ERROR0( self.main_dict )
                                                                    break
                                                            else:
                                                                self.error = self.error
                                                                break
                                                    else:
                                                        self.error = self.error
                                                        break
                                                else:
                                                    self.error = self.error
                                                    break

                                            else:
                                                self.error = self.error
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( self.main_dict )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR3( self.main_dict, 'value', 'keyword', self.name)
                                        break
                                else:
                                    if self.init_value:
                                        self.error = ERRORS(self.line).ERROR3(self.main_dict, 'keyword', 'value', self.init_value)
                                        break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( self.main_dict )
                                        break

                            else:
                                self.error = ERRORS( self.line ).ERROR2( self.main_dict, self.sub_value[ 0 ] )
                                break
                        else:
                            self.error = self.error
                            break
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.main_dict )
                        break
            else:
                self.error = self.error

        else:
            self.error      =  None
            self._return_   = {}

        return self._return_, self.error

    def MAIN_DICT(self, main_string: str):

        self.error              = None
        self.numeric            = self.master[ 'numeric' ]
        self._return_           = []
        self.historyOfFunctions = []
        self.dictFunctions      = [ 'empty', 'get', 'clear', 'copy', 'remove', 'init'] 

        if self.numeric is not None:
            self.dict_values, self.error = DICTIONARY( self.master, self.data_base, self.line ).DICT()
            if self.error is None:
                self._return_ = self.dict_values
            else:
                self.error = self.error

        else:
            self._names_        = self.master[ 'names' ]
            self.expressions    = self.master[ 'expressions' ]
            self.params         = self.master[ 'add_params' ]
            
            if self._names_[ 0 ] is None:
                if len( self._names_ ) == 2:
                    self.main_expression = {'numeric' : [ self.expressions[ 0 ] ], 'type' : 'dictionnary' }
                    self.dict_values, self.error = DICTIONARY(self.main_expression, self.data_base, self.line ).DICT()
                    if self.error is None:
                        if self._names_[ 1 ] in self.dictFunctions:
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
                                    self._return_, self.error = classInit.DICTIONARY( self.data_base, self.line, self.dict_values,
                                                                        self.name, self.dictionary[ 'functions' ]).DICT( 'dictionary', main_string)
                                    if self.error is None:
                                        if self.params[ 1 ] is None : pass
                                        else: 
                                            self._return_, _, self.error = get_list.LIS_OPTIONS( [ self.master ], self.master, self.data_base, 
                                                                    self.line ).ARGUMENT_LIST( self._return_, self.params[ 1 ], function = True )
                                    else: pass                                                       
                                else: pass    
                            
                            else: self.error = classInit.ERRORS( self.line ).ERROR22( self._names_[ 1 ], 'dictionary()' )
                        else: self.error = classInit.ERRORS( self.line ).ERROR22( self._names_[ 1 ], 'dictionry()' )
                    else: pass
                else:  self.error = ERRORS( self.line ).ERROR0( main_string )
            else: self.error = ERRORS( self.line ).ERROR0( main_string )

        return self._return_, self.error

class DICT_FUNCTION:
    def __init__(self, master: any, data_base: any, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.selection          = particular_str_selection

    def GET(self, main_string: str):

        self.error          = None
        self._return_       = None
        self.lists          = [ 'items', 'keys', 'values', 'id' ]
        self.string         = self.master[4 : -1 ]

        self.string, self.error = self.control.DELETE_SPACE( self.string )

        if self.error is None:
            self.names, self.error = self.selection.SELECTION( self.string, self.string, self.data_base,
                                                               self.line).CHAR_SELECTION( ',' )
            if self.error is None:
                check = []
                self.len  = len( self.names )
                for name in self.names:
                    name, self.error = self.control.DELETE_SPACE( name )
                    if not check:
                        check.append( name )
                    else:
                        if name in check:
                            self.error = ERRORS( self.line ).ERROR6(self.master, name )
                            break
                        else:
                            check.append( name )

                if self.error is None:
                    self.names = check[ : ]
                    for name in self.names:
                        if name in self.lists :
                            pass
                        else:
                            self.error = ERRORS( self.line ).ERROR7( name )
                            break
                    if self.error is None:
                        self._return_ = self.names
                    else:
                        self.error = self.error
                else:
                    self.error = self.error

            else:
                self.error = self.error

        else:
            self.error = ERRORS( self.line ).ERROR4( main_string, self.master)

        return self._return_, self.error

class KEYS:
    def __init__(self, master:any, key: str):
        self.key            = key
        self.master         = master

    def KEY(self):
        self._return_       = None

        if self.key == 'items':
            self._return_ = self.master.items()
        elif self.key == 'keys':
            self._return_ = list( self.master.keys() )
        elif self.key == 'values':
            values = []
            for item,  value in self.master.items():
                value.append( values )
            self._return_ = value

        else:
            pass

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
        error = '{}line: {}{}'.format(self.cyan, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str, char: str):
        error = '{}due to {}<< {} >>. {}line: {}{}'.format(self.white, self.red, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR2(self, string: str, char:str):
        error = '{}the keyword of value {}<< {} >> {}is not defined. {}line: {}{}'.format(self.white, self.magenta, char, self.yellow,
                                                                                          self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR3(self, string: str, char1: str = 'keyword', char2:str='value', char: str = None):
        error = '{}{} {}is not defined for the {}{} {}<< {} >>. {}line: {}{}'.format(self.red, char, self.white, self.green, char2, self.magenta, char,
                                                                                self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR4(self, string: str, char: str):
        error = '{}due to the fact that {}<< {} >> {}is {}EMPTY. {}line: {}{}'.format(self.white, self.red, char, self.white, self.yellow,
                                                                                                    self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{} invalid syntax in {}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR5(self, string: str, char: str):
        error = '{}keyword {}<< {} >> {}is repeated. {}line: {}{}'.format(self.red, self.blue, char, self.yellow, self.white, self.yellow, self.line)
        self.error =fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR6(self, string: str, char: str):
        error = '{}argument {}<< {} >> {}is repeated. {}line: {}{}'.format(self.white, self.magenta, char, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white,  string) + error

        return self.error+self.reset

    def ERROR7(self, char: str, func = 'get( )'):
        error = '{}<< {} >>. {}line: {}{}'.format(self.red, char,  self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError').Errors()+'{}<< {} >> {}has not attributed '.format(self.cyan, func, self.white) + error

        return self.error+self.reset
