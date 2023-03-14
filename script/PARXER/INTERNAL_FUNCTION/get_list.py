import                              numpy as np
from script                         import control_string
from script.LEXER                   import particular_str_selection
from script.LEXER                   import main_lexer
from script.LEXER                   import check_if_affectation
from script.PARXER                  import numerical_value
from src.classes.Lists              import Lists
from src.classes                    import error as er
from script.PARXER.LEXER_CONFIGURE  import numeric_lexer
from script.LEXER.FUNCTION          import main
from script.STDIN.LinuxSTDIN        import bm_configure as bm
try:
    from CythonModules.Windows      import fileError as fe 
except ImportError:
    from CythonModules.Linux        import fileError as fe 


class LIST:
    def __init__(self, master: dict, data_base: dict, line: int):
        self.line                       = line
        self.master                     = master
        self.data_base                  = data_base

        self.control                    = control_string.STRING_ANALYSE(self.data_base, self.line)
        self.selection                  = particular_str_selection
        self.lexer                      = main_lexer
        self.numeric                    = numerical_value
        self.affectation                = check_if_affectation
        self.variables                  = self.data_base[ 'variables' ][ 'vars' ]

    def LIST(self):
        self.error                      = None
        self.type                       = self.master[ 'type' ]
        self.main_dict                  = self.master[ 'numeric' ][ 0 ]
        self._return_                   = []

        self.string     = self.main_dict[ 1: -1]
        self.string, self.error = self.control.DELETE_SPACE( self.string )
        if self.error is None:
            self.value, self.error = self.selection.SELECTION( self.string, self.string, self.data_base,
                                                              self.line ).CHAR_SELECTION( ',' )

            if self.error is None:
                for _value_ in self.value:
                    self.true_value, self.error = self.control.DELETE_SPACE( _value_ )
                    if self.error is None:
                        self.check_dot, self.error = self.selection.SELECTION(self.true_value, self.true_value,
                                                                self.data_base,self.line).CHAR_SELECTION( ':' )
                        if self.error is None:
                            if len( self.check_dot )   == 1:
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
                                                    self._return_.append( self.final_val[ 0 ] )
                                                else: break
                                            else:
                                                self.error = ERRORS( self.line ).ERROR0( self.main_dict )
                                                break
                                        else: break
                                    else:
                                        self.operator = self.dict_value[ 'operator' ]
                                        self.error = ERRORS( self.line ).ERROR1(self.main_dict, self.operator )
                                        break
                                else: break

                            elif len( self.check_dot ) == 2:
                                self.new_list = []
                                for w, _sub_value_ in enumerate( self.check_dot):
                                    self._sub_value_, self.error = self.control.DELETE_SPACE( _sub_value_ )
                                    if self.error is None:
                                        self.number, self.error = numeric_lexer.NUMERCAL_LEXER( self._sub_value_,
                                                                    self.data_base, self.line ).LEXER( self.main_dict )
                                        if self.error is None:
                                            self.check_dot[ w ] = self.number
                                            self.new_list.append( self._sub_value_ )
                                        else:break
                                    else:break
                                if self.error is None:
                                    if type( self.check_dot[ 1 ]) == type( int()):
                                        if type( self.check_dot[ 0 ] ) == type( int()):
                                            if self.check_dot[ 0 ] < self.check_dot[ 1 ]:
                                                if self.check_dot[ 1 ] <= 10:
                                                    for w in range( self.check_dot[ 0 ], self.check_dot[ 1 ]):
                                                        self._return_.append( w )
                                                else:
                                                    self._return_ = range( self.check_dot[ 0 ], self.check_dot[ 1 ] )
                                            else:
                                                lower   = self.new_list[ 1 ]
                                                bigger  = self.new_list[ 0 ]
                                                if self.check_dot[ 0 ] == self.check_dot[ 1 ]:
                                                    self.error = ERRORS(self.line).ERROR16(lower, bigger)
                                                    break
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR14( lower, bigger )
                                                    break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR10(self.new_list[ 0 ])
                                            break
                                    else:
                                        self.error = self.error = ERRORS( self.line ).ERROR10(self.new_list[ 1 ])
                                        break

                                else: break

                            elif len( self.check_dot ) == 3:
                                self.new_list = []
                                for w, _sub_value_ in enumerate(self.check_dot):
                                    self._sub_value_, self.error = self.control.DELETE_SPACE(_sub_value_)
                                    if self.error is None:
                                        self.number, self.error = numeric_lexer.NUMERCAL_LEXER(self._sub_value_,
                                                                self.data_base,self.line).LEXER( self.main_dict )

                                        if self.error is None:

                                            self.check_dot[w] = self.number
                                            self.new_list.append(self._sub_value_)
                                        else:break
                                    else:break

                                if self.error is None:
                                    if type( self.check_dot[ 2 ]) == type( int()):
                                        if type( self.check_dot[ 1 ] ) == type( int()):
                                            if type( self.check_dot[ 0 ] ) == type( int()):
                                                if self.check_dot[ 0 ] < self.check_dot[ 1 ]:
                                                    if self.check_dot[ 2 ] < self.check_dot[ 1 ]:
                                                        if self.check_dot[ 2 ] > 0:
                                                            first   = self.check_dot[ 0 ]
                                                            second  = self.check_dot[ 1 ]
                                                            third   = self.check_dot[ 2 ]

                                                            if int( (second - first) / third ) <= 10:
                                                                for w in range( first, second, third ):
                                                                    self._return_.append( w )
                                                            else:
                                                                self._return_ = range( first, second, third )
                                                        else:
                                                            self.error = ERRORS( self.line ).ERROR17()
                                                            break
                                                    else:
                                                        lower   = self.new_list[ 1 ]
                                                        bigger  = self.new_list[ 2 ]

                                                        if self.check_dot[ 1 ] == self.check_dot[ 2 ]:
                                                            self.error = ERRORS(self.line).ERROR16(lower, bigger)
                                                            break
                                                        else:
                                                            self.error = ERRORS(self.line).ERROR14(lower, bigger)
                                                            break

                                                else:
                                                    lower   = self.new_list[ 1 ]
                                                    bigger  = self.new_list[ 0 ]
                                                    if self.check_dot[ 1 ] == self.check_dot[ 2 ]:
                                                        self.error = ERRORS(self.line).ERROR16(lower, bigger)
                                                        break
                                                    else:
                                                        self.error = ERRORS( self.line ).ERROR14( lower, bigger )
                                                        break
                                            else:
                                                self.error = ERRORS(self.line).ERROR10( self.new_list[ 0 ] )
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR10( self.new_list[ 1 ] )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR10(self.new_list[ 2 ])
                                        break

                                else:break

                            else:
                                self.error = ERRORS( self.line ).ERROR15( _value_ )
                                break

                        else:break
                    else:
                        self.error = ERRORS( self.line ).ERROR0( self.main_dict )
                        break
            else: self.error = self.error

        else:
            self.error      = None
            self._return_   = self._return_

        return self._return_, self.error

    def MAIN_LIST(self, main_string: str):
        self.error                  = None
        self.numeric                = self.master[ 'numeric' ]
        self._return_               = []
        self.historyOfFunctions     = []
        self.listFunctions          = [ 'empty', 'clear', 'copy', 'remove', 'init', 'index', 'count', 'sorted', 'add', 'insert', 'random', 'enumerate',
                                        'size', 'round', 'rand', 'choice', 'to_array' ]
        if self.numeric is not None:
            self.list_values, self.info, self._all_data_, self.error = LIS_OPTIONS( self.numeric, self.master,
                                                                        self.data_base, self.line ).OPTION( )

            if self.error is None: self._return_ = self.list_values
            else: pass
        else: 
            self._names_        = self.master[ 'names' ]
            self.expressions    = self.master[ 'expressions' ]
            self.params         = self.master[ 'add_params' ]
            
            if self._names_[ 0 ] is None:
                if len( self._names_ ) == 2:
                    self.main_expression = {'numeric': [self.expressions[ 0 ] ], 'type': 'list' }
                    self.list_values, _, _, self.error = LIS_OPTIONS([self.expressions[ 0 ] ], self.main_expression, self.data_base, self.line ).OPTION( )
           
                    if self.error is None:
                        if self._names_[ 1 ] in self.listFunctions:
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
                                    self._return_, self.error = Lists.LIST( self.data_base, self.line, self.list_values,
                                                                        self.name, self.dictionary[ 'functions' ]).LIST( 'list.', main_string)
                                    if self.error is None:
                                        if self.params[ 1 ] is None : pass
                                        else: 
                                            self._return_, _, self.error = LIS_OPTIONS( [ self.master ], self.master, self.data_base, 
                                                                    self.line ).ARGUMENT_LIST( self._return_, self.params[ 1 ], function = True )
                                    else: pass                                                       
                                else: pass    
                            else: self.error = er.ERRORS( self.line ).ERROR22( self._names_[ 1 ], 'list()' )
                        else: self.error = er.ERRORS( self.line ).ERROR22( self._names_[ 1 ], 'list()' )
                    else:  pass
                else: self.error = ERRORS( self.line ).ERROR0( main_string )
            else: self.error = ERRORS( self.line ).ERROR0( main_string )
            
        return self._return_, self.error

    def VAR_NAMES(self, main_string: str, global_type:str = 'variables'):
        self.error          = None
        self.numeric        = self.master[ 'numeric' ]
        self._return_       = None
        self.info           = None
        self._all_data_     = None

        if self.numeric is not None:
            self._return_, self.info, self._all_data_, self.error = LIS_OPTIONS(self.numeric, self.master,
                                                        self.data_base, self.line).OPTION( global_type = global_type )
        else: pass

        return self._return_, self.info, self._all_data_, self.error

class LIS_OPTIONS:
    def __init__(self, master: str, main_master: any, data_base: any, line: int):
        self.line           = line
        self.data_base      = data_base
        self.master         = master[ 0 ]
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.main_master    = main_master
        self.lexer          = numeric_lexer

    def OPTION(self, global_type:str = 'values'):

        self.error          = None
        self.name           = ''
        self.idd            = None
        self._return_       = None
        self.info           = None
        self.all_data       = None

        for i, str_ in enumerate( self.master ):
            if str_ not in [ '[' ]:
                self.name += str_
            else:
                self.idd = i
                break

        if self.idd == 0:
            self._return_, self.error = LIST( self.main_master, self.data_base, self.line ).LIST()
        else:
            self.name, self.error = self.control.DELETE_SPACE( self.name )
            if self.error is None:
                self.name, self.error = self.control.CHECK_NAME( self.name )
                if self.error is None:
                    self.true_name  = self.name
                    self.list       = self.master[ self.idd : ]
                    self.list, self.error = self.control.DELETE_SPACE( self.list )
                    if self.error is None:
                        self.data, self.error = self.lexer.NUMERCAL_LEXER(self.true_name, self.data_base,
                                                                              self.line).LEXER(self.master)
                        if self.error is None:
                            self._return_, self.options, self.error = LIS_OPTIONS(self.master, self.main_master,
                                    self.data_base, self.line).ARGUMENT_LIST(self.data, self.list,
                                                                             self.name, global_type)
                            if self.error is None:
                                self.info       = self.options
                                self.all_data   = self.data
                            else: pass
                        else: pass
                    else:  self.error = ERRORS( self.line ).ERROR0( self.line )
                else: self.error = self.error
            else: self.error = ERRORS( self.line ).ERROR0( self.master )

        return self._return_, self.info, self.all_data, self.error

    def ARGUMENT_LIST(self, object1: any,  object2: str, name:str = '', globa_type: str = 'values', function : bool = False):

        self.error          = None
        self.type           = type( object1 )
        self.logical        = ['.eq.', '.ne.', '.le.', '.ge.', '.lt.', '.gt.']
        self.logical_exp    = ['.or.', '.and.']
        self.operator       = []
        self.value_split    = []

        self.value = object2[1 : -1]
        self.value, self.error = self.control.DELETE_SPACE( self.value )
        if self.error is None:
            self.all_value, self.error = particular_str_selection.SELECTION( self.value, self.value, self.data_base,
                                                                            self.line ).CHAR_SELECTION( ',' )
            if self.error is None:
                for i, value in enumerate( self.all_value):
                    self._value_, self.error = self.control.DELETE_SPACE( value )
                    self.type = type( object1 )
                    if self.error is None:
                        self.dot, self.error = particular_str_selection.SELECTION( self._value_, self._value_, self.data_base,
                                                                                   self.line).CHAR_SELECTION( ':' )
                        if self.error is None:
                            if   len( self.dot ) == 1:
                                for op in self.logical:
                                    self._operator_, self.error = particular_str_selection.SELECTION(
                                        self._value_, self._value_,
                                        self.data_base, self.line).CHAR_SELECTION( op )

                                    if   len( self._operator_ ) == 1: pass
                                    elif len( self._operator_ ) == 2:
                                        if function is False:
                                            self.operator.append(OPERATOR_TRANSFORMATION( op ).TRANSFORMATION())
                                            self.value_split.append( self._operator_ )
                                        else:
                                            self.error = ERRORS( self.line ).ERROR0( object2 )
                                            break
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( value )
                                        break

                                if self.error is None:
                                    if self.operator:
                                        if len(self.operator) == 1:
                                            self.value_split = self.value_split[0]
                                            self.sub_name, self.error = self.control.DELETE_SPACE(self.value_split[ 0 ] )

                                            if self.error is None:
                                                if self.sub_name == name:
                                                    self._num_, self.error = numeric_lexer.NUMERCAL_LEXER(
                                                        self.value_split[1],
                                                        self.data_base, self.line).LEXER(object2)
                                                    if self.error is None:
                                                        if type(object1) in [ type( list() ), type( tuple() ),
                                                                              type( range( 1 ) ), type( str()) ]:
                                                            self.list_value, self.num, self.error = numerical_value.FINAL_VALUE(object1, self.data_base, self.line, 
                                                                                                    self.operator[0]).GET_DATA(self._num_, False)
                                                            if self.error is None:
                                                                object1 = self.list_value
                                                                self.all_value[i] = self.num
                                                                self.operator = []
                                                                self.value_split = []
                                                            else: break
                                                        else:
                                                            self.error = ERRORS(self.line).ERROR9(object1)
                                                            break
                                                    else: break
                                                else:
                                                    self.error = ERRORS(self.line).ERROR13(name, self.sub_name)
                                                    break
                                            else: break
                                        else:
                                            self.error = ERRORS(self.line).ERROR0(value)
                                            break
                                    else:
                                        self.num, self.error = numeric_lexer.NUMERCAL_LEXER(self._value_,
                                                                        self.data_base, self.line).LEXER( object2 )
                                        if self.error is None:
                                            self.all_value[ i ] = self.num
                                            _type_ = type( self.num )
                                            if   _type_ == type( int() )    :
                                                if self.type in [ type( list() ), type( tuple() ), type( range(1)),
                                                                  type(str()), type(np.array([0])) ]:
                                                    if self.num < len( object1 ):
                                                        try:
                                                            object1 = object1[ self.num ]
                                                        except IndexError:
                                                            if self.type == type( list() ):
                                                                self.error = ERRORS(self.line).ERROR8()
                                                                break
                                                            else:
                                                                self.error = ERRORS(self.line).ERROR8('tuple')
                                                                break
                                                    else:
                                                        if self.type == type( list() ):
                                                            self.error = ERRORS( self.line ).ERROR8( )
                                                            break
                                                        else:
                                                            self.error = ERRORS( self.line ).ERROR8( 'tuple')
                                                            break
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR9( object1 )
                                                    break
                                            elif _type_ == type( str() )    :
                                                if self.type == type( dict() ):
                                                    if self.num in list( object1.keys() ):
                                                        object1 = object1[ self.num ]
                                                        if type( object1 ) == type( str() ):
                                                            object1 = "'" + object1 + "'"
                                                        else: pass
                                                    else:
                                                        if globa_type == 'values':
                                                            self.error = ERRORS( self.line ).ERROR12( object1, self.num )
                                                            break
                                                        else:
                                                            if i == len( self.all_value ) - 1: pass
                                                            else:
                                                                self.error = ERRORS(self.line).ERROR12( object1,
                                                                                            self.all_value[ i - 2 ] )
                                                                break
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR10( value, 'a dictionary()' )
                                                    break
                                            else:
                                                self.error = ERRORS( self.line ).ERROR11( value )
                                                break
                                        else: break
                                else: break
                            elif len( self.dot ) == 2:
                                for j in range( 2 ):
                                    self._name_, self.error = self.control.DELETE_SPACE(self.dot[ j ])
                                    if self.error is None:
                                        self.dot[ j ] = self._name_
                                    else:
                                        self.error = ERRORS( self.line ).ERROR0( object2 )
                                        break

                                if self.error is None:
                                    self.first              = None
                                    self.case               = None
                                    self.second             = None

                                    if   self.dot[ 0 ] == '_' and self.dot[ 1 ] != '_':
                                        self.first = self.dot[ 1 ]
                                        self.case       = '1'
                                    elif self.dot[ 0 ] != '_' and self.dot[ 1 ] == '_':
                                        self.first = self.dot[ 0 ]
                                        self.case       = '2'
                                    elif self.dot[ 0 ] == '_' and self.dot[ 1 ] == '_':
                                        self.first = '0'
                                        self.case       = '3'
                                    elif self.dot[ 0 ] != '_' and self.dot[ 1 ] != '_':
                                        self.first  = self.dot[ 0 ]
                                        self.second = self.dot[ 1 ]
                                        self.case       = '4'
                                    else:
                                        self.error = ERRORS( self.error ).ERROR0( object2 )
                                        break

                                    self.num1, self.error = numeric_lexer.NUMERCAL_LEXER( self.first,
                                                                    self.data_base, self.line).LEXER( object2 )
                                    if self.error is None:
                                        if self.second is not None:
                                            self.num2, self.error = numeric_lexer.NUMERCAL_LEXER( self.second,
                                                                        self.data_base, self.line).LEXER( object2 )
                                            if self.error is None: pass
                                            else: break
                                        else: pass

                                        _type_1 = type( self.num1 )
                                        if _type_1 == type( int() ) :
                                            if self.type in [ type( list() ), type( tuple()), type( range( 1 ) ),
                                                              type(str()) , type( np.array([0]) ) ]:
                                                self.len = len( object1 )

                                                if self.case ==   '1':
                                                    if self.num1 >= 0:
                                                        if self.num1 <= self.len :
                                                            self.dot[ 0 ] = 0
                                                            self.dot[ 1 ] = self.num1
                                                        else:
                                                            if self.type == type( list() ):
                                                                self.error = ERRORS( self.line ).ERROR8()
                                                                break
                                                            elif self.type == type(np.array([0])):
                                                                self.error = ERRORS(self.line).ERROR8('ndarray')
                                                                break
                                                            else:
                                                                self.error = ERRORS(self.line).ERROR8('tuple')
                                                                break
                                                    else:
                                                        if self.num1 >= -self.len :
                                                            self.dot[ 0 ] = - self.len
                                                            self.dot[ 1 ] = self.num1
                                                        else:
                                                            if self.type == type( list() ):
                                                                self.error = ERRORS(self.line).ERROR8()
                                                                break
                                                            elif self.type == type(np.array([0])):
                                                                self.error = ERRORS(self.line).ERROR8('ndarray')
                                                                break
                                                            else:
                                                                self.error = ERRORS(self.line).ERROR8('tuple')
                                                                break
                                                elif self.case == '2':
                                                    if self.num1 >= 0:
                                                        if self.num1 <= self.len:
                                                            self.dot[ 0 ] = self.num1
                                                            self.dot[ 1 ] = self.len
                                                        else:
                                                            if self.type == type(list()):
                                                                self.error = ERRORS(self.line).ERROR8()
                                                                break
                                                            elif self.type == type(np.array([0])):
                                                                self.error = ERRORS(self.line).ERROR8('ndarray')
                                                                break
                                                            else:
                                                                self.error = ERRORS(self.line).ERROR8('tuple')
                                                                break
                                                    else:
                                                        if self.num1 <= -1:
                                                            if self.num1 == -1:
                                                                self.dot[ 0 ] = self.len - 1
                                                                self.dot[ 1 ] = self.len
                                                            else:
                                                                if self.len + self.num1 >= 0:
                                                                    self.dot[ 0 ] = self.len + self.num1
                                                                    self.dot[ 1 ] = self.len
                                                                else:
                                                                    self.dot[ 0 ] = 0
                                                                    self.dot[ 1 ] = self.len
                                                        else:
                                                            if self.type == type(list()):
                                                                self.error = ERRORS(self.line).ERROR8()
                                                                break
                                                            elif self.type == type(np.array([0])):
                                                                self.error = ERRORS(self.line).ERROR8('ndarray')
                                                                break
                                                            else:
                                                                self.error = ERRORS(self.line).ERROR8('tuple')
                                                                break
                                                elif self.case == '3':
                                                    self.dot[ 0 ] = 0
                                                    self.dot[ 1 ] = self.len
                                                elif self.case == '4':
                                                    _type_2 = type( self.num2 )
                                                    if _type_2 == type( int() ):
                                                        if abs( self.num2 ) <= self.len:
                                                            if self.num1 <= self.num2:
                                                                if self.num1 < self.len:
                                                                    self.dot[ 0 ] = self.num1
                                                                    self.dot[ 1 ] = self.num2
                                                                else:
                                                                    if self.type == type( list() ):
                                                                        self.error = ERRORS(self.line).ERROR8()
                                                                        break
                                                                    else:
                                                                        self.error = ERRORS( self.line ).ERROR8('tuple')
                                                                        break
                                                            elif self.num1 >  self.num2:
                                                                self.dot[0] = self.num1
                                                                self.dot[1] = self.num2
                                                            else:
                                                                if self.type == type( list() ):
                                                                    self.error = ERRORS(self.line).ERROR8()
                                                                    break
                                                                else:
                                                                    self.error = ERRORS(self.line).ERROR8('tuple')
                                                                    break
                                                        else:
                                                            if self.type == type( list() ):
                                                                self.error = ERRORS(self.line).ERROR8()
                                                                break
                                                            else:
                                                                self.error = ERRORS(self.line).ERROR8('tuple')
                                                                break
                                                    else:
                                                        self.error = ERRORS( self.line ).ERROR10(self.second)
                                                        break

                                                if self.error is None:
                                                    try:
                                                        if object1:
                                                            try:
                                                                object1 = object1[self.dot[0] : self.dot[1]]
                                                                self.all_value[ i ] = [ x for x in range(self.dot[0], self.dot[1])]
                                                            except IndexError:
                                                                if self.type == type( list() ):
                                                                    self.error = ERRORS(self.line).ERROR8()
                                                                    break
                                                                elif self.type == type( np.array([0]) ):
                                                                    self.error = ERRORS(self.line).ERROR8('ndarray')
                                                                    break
                                                                else:
                                                                    self.error = ERRORS(self.line).ERROR8('tuple')
                                                                    break
                                                        else:
                                                            if self.type == type(list()):
                                                                self.error = ERRORS(self.line).ERROR8()
                                                                break
                                                            elif self.type == type(np.array([0])):
                                                                self.error = ERRORS(self.line).ERROR8('ndarray')
                                                                break
                                                            else:
                                                                self.error = ERRORS(self.line).ERROR8('tuple')
                                                                break
                                                    except ValueError:
                                                        if object1.all():
                                                            try:
                                                                object1 = object1[self.dot[0]: self.dot[1]]
                                                                self.all_value[i] = [x for x in range(self.dot[0], self.dot[1])]
                                                            except IndexError:
                                                                self.error = ERRORS(self.line).ERROR8('ndarray')
                                                        else:
                                                            self.error = ERRORS(self.line).ERROR8('ndarray')
                                                            break
                                                else: break
                                            else:
                                                self.error = ERRORS( self.line ).ERROR9( value )
                                                break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR10( self.first )
                                            break
                                    else:  break
                                else: break
                            else:
                                self.error = ERRORS( self.line ).ERROR0( value )
                                break
                        else:
                            self.error = ERRORS( self.line ).ERROR0( object2 )
                            break
                    else:
                        self.error = ERRORS( self.line ).ERROR0( object2 )
                        break
            else: self.error = ERRORS( self.line ).ERROR0( object2 )
        else: self.error = ERRORS( self.line ).ERROR0( self.master )

        return object1, self.all_value, self.error

class OPERATOR_TRANSFORMATION:
    def __init__(self, operator: str):
        self.operator       = operator
    def TRANSFORMATION(self):
        self.init_operator = None

        if   self.operator == '.eq.'            : self.init_operator = '=='
        elif self.operator == '.ne.'            : self.init_operator = '!='
        elif self.operator == '.ge.'            : self.init_operator = '>='
        elif self.operator == '.le.'            : self.init_operator = '<='
        elif self.operator == '.gt.'            : self.init_operator = '>'
        elif self.operator == '.lt.'            : self.init_operator = '<'

        return self.init_operator

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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan , string) + error

        return self.error+self.reset

    def ERROR1(self, string: str, char: str):
        error = '{}due to {}<< {} >>. {}line: {}{}'.format(self.white, self.red, char, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan , string) + error

        return self.error+self.reset

    def ERROR2(self, string: str, char:str):
        error = '{}the {}keyword {}of value {}<< {} >> {}is not defined. line: {}{}'.format(self.white, self.blue, self.yellow, self.green, char, self.white,
                                                                                                    self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan , string) + error

        return self.error+self.reset

    def ERROR3(self, string: str, char1: str = 'keyword', char2:str='value', char: str = None):
        error = '{}{} {}is not defined for the {}{} {}<< {} >>. {}line: {}{}'.format(self.red, char, self.white, self.green, char2, self.magenta, char,
                                                                                self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan , string) + error

        return self.error+self.reset

    def ERROR4(self, string: str, char: str):
        error = '{}due to the fact that {}<< {} >> {}is {}EMPTY. {}line: {}{}'.format(self.white, self.red, char, self.white, self.green,
                                                                                                    self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan , string) + error

        return self.error+self.reset

    def ERROR5(self, string: str, char: str):
        error = '{}keyword {}<< {} >> {}is repeated. {}line: {}{}'.format(self.white, self.blue, char, self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan , string) + error

        return self.error+self.reset

    def ERROR6(self, string: str, char: str):
        error = '{}argument {}<< {} >> {}is repeated. {}line: {}{}'.format(self.yellow, self.magenta, char, self.white, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> '.format(self.white, self.cyan , string) + error

        return self.error+self.reset

    def ERROR7(self, char: str, func = 'get( )'):
        error = '{}<< {} >>. {}line: {}{}'.format(self.red, char,  self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'AttributeError' ).Errors()+'{}<< {} >> {}has not attributed '.format(self.magenta, func, self.white) + error

        return self.error+self.reset

    def ERROR8(self, func = 'list', c:str = ''):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'IndexError' ).Errors()+'{}{} {}index {}out of range. '.format(self.yellow, func, self.red, self.white) + error

        return self.error+self.reset

    def ERROR9(self, string: str):
        error = '{}is not {}a list() {}a tuple(), {}a string() {}or {}a range() {}type. {}line: {}{}'.format( self.white, self.yellow,
            self.cyan, self.magenta, self.white, self.green, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR10(self, string: str, _char_ = 'an integer()' ):
        error = '{}is not {}{} {}type. {}line: {}{}'.format(self.white, self.blue, _char_, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR11(self, string: str):
        error = '{}is not {}an integer() {}or {}a string(). {}line: {}{}'.format(self.white, self.red, self.white, 
                                                                                            self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> '.format(self.cyan, string) + error

        return self.error+self.reset

    def ERROR12(self, string: str, key: str):
        error = '{}was not found in {}<< {} >>. {}line: {}{}'.format(self.white, self.magenta, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'KeyError' ).Errors()+'{}<< {} >> '.format(self.cyan, key) + error

        return self.error+self.reset

    def ERROR13(self, string: str, name: str):
        error = '{}should be {}<< {} >>. {}line: {}{}'.format(self.white, self.red, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'NameError' ).Errors()+'{}<< {} >> '.format(self.cyan, name) + error

        return self.error+self.reset

    def ERROR14(self, lower: str, bigger: str):
        error = '{}is lower than {}<< {} >>. {}line: {}{}'.format(self.white, self.green, bigger, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+ '{}<< {} >> '.format(self.cyan, lower) + error

        return self.error+self.reset

    def ERROR15(self, string: str):
        error = '{}due to  many {}<< : >>. {}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax  in {}<< {} >> '.format(self.white, self.cyan, string ) + error

        return self.error+self.reset

    def ERROR16(self, lower: str, bigger: str):
        error = '{}is egal to {}<< {} >>. {}line: {}{}'.format(self.white, self.green, bigger, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}<< {} >> '.format(self.cyan, lower) + error

        return self.error+self.reset

    def ERROR17(self, step:str='step'):
        error = '{}<< {} >> {}is zero . {}line: {}{}'.format(self.red, step, self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'DomainError' ).Errors()+'{}in {}<< range( ) >> {}function. '.format(self.white, self.cyan, self.green) + error
        return self.error+self.reset

