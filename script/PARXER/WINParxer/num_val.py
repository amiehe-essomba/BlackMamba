from colorama       import Fore, init, Back, Style
import numpy
import pandas       as pd
from script         import control_string
from script.LEXER   import particular_str_selection
from script.MATHS   import arithemtic_operations, mathematics

import cython
try:  from CythonModules.Linux                      import NumeriCal
except ImportError:  from CythonModules.Windows     import NumeriCal

from script.PARXER.INTERNAL_FUNCTION                import get_dictionary
from script.PARXER.INTERNAL_FUNCTION                import get_list
from script.PARXER.INTERNAL_FUNCTION                import get_string
from script.PARXER.INTERNAL_FUNCTION                import get_none
from script.PARXER.INTERNAL_FUNCTION                import get_boolean
from script.PARXER.INTERNAL_FUNCTION                import get_tuple
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS       import functions as func
from script.PARXER.PARXER_FUNCTIONS.CLASSES         import classInit 
from script.STDIN.LinuxSTDIN                        import bm_configure as bm
try:
    from CythonModules.Windows                      import fileError as fe 
except ImportError:
    from CythonModules.Linux                        import fileError as fe

ne = Fore.LIGHTRED_EX
ie = Fore.LIGHTBLUE_EX
ae = Fore.CYAN
te = Fore.MAGENTA
ke = Fore.LIGHTYELLOW_EX
ve = Fore.LIGHTGREEN_EX
se = Fore.YELLOW
we = Fore.LIGHTWHITE_EX
me = Fore.LIGHTCYAN_EX
le = Fore.RED
be = Fore.BLUE
ge = Fore.GREEN

@cython.cclass
class NUMERICAL:
    def __init__(self, master: dict, data_base: dict, line: int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base

        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.selection          = particular_str_selection
        self.chars              = self.control.LOWER_CASE()+self.control.UPPER_CASE()+['_']

        self.main_value         = self.master[ 'all_data' ]
        self.variables          = self.data_base[ 'variables' ][ 'vars' ]
        self._values_           = self.data_base[ 'variables' ][ 'values' ]
        self._if_egal_          = self.master[ 'if_egal' ]
        self.maths_operation    = arithemtic_operations

    @cython.cfunc
    def ANALYSE(self, main_string: str, loop : bool = False):
        global main__main
        self.error                  = None
        self.numeric                = []
        self.active_key             = None
        self.index                  = None
        self.sum                    = ''

        #print( self.master )
        if self.main_value is not None:

            self.values                 = self.main_value[ 'value' ]
            self.boolean_operator       = self.main_value[ 'bool_operator' ]
            self.logical_operator       = self.main_value[ 'logical_operator' ]
            self.arithmetic_operator    = self.main_value[ 'arithmetic_operator' ]
            main__main                  = main_string
            self.numeric                = []

            if loop is False:
                self.numeric, self.error = NUMERICAL(self.master, self.data_base,
                                    self.line).BOOLEAN_CHECK( self.values, self.arithmetic_operator, self.logical_operator,
                                                                                              self.boolean_operator, main_string)
                
                #self.numeric, self.error = NUMERICAL(self.master, self.data_base,
                #                                    self.line).ARITHMETIC_CHECK(self.values, self.arithmetic_operator)
            else:
                self.numeric, self.error = NUMERICAL(self.master, self.data_base,
                                                     self.line).ARITHMETIC_CHECK(self.values, self.arithmetic_operator)


            return self.numeric, self.error

        else:  return None, None

    @cython.cfunc
    def NUEMERICAL_CHECK(self, values: dict ):
        self.values                 = values
        self.numeric                = None
        self.error                  = None

        if 'values' in list( self.values.keys() ):

            self._ar_op_            = self.values[ 'operators' ]
            self.firt_part          = self.values[ 'values' ][ 0 ]
            self.second_part        = self.values[ 'values' ][ 1 ]
            self.key                = False
            self._val_1_, self.error = self.selection.SELECTION(self.firt_part, self.firt_part,
                                                               self.data_base, self.line).CHAR_SELECTION('.')
            if self.error is None:
                if len( self._val_1_ ) == 1:
                    self.key        = False
                elif len( self._val_1_ ) == 2:
                    self.key        = True
                else:
                    self.error      = ERRORS( self.line ).ERROR1( self.firt_part )

                if self.error is None :
                    self._val_1     = self.firt_part
                    self._val_2     = self.second_part[ 0 ]

                    if type( self._val_2 ) == type( dict() ):
                        self.type       = self._val_2[ 'type' ]
                        self.var        = self._val_2[ 'numeric' ][ 0 ]

                        if self.type is None:
                            if self.variables:
                                if self.var in self.variables:
                                    self.index          = self.variables.index( self.var )
                                    self.numeric2       = self._values_[ self.index ]

                                    if type( self.numeric2 ) in [ type( int() ), type( complex() )]:
                                        self.numeric2   = self.numeric2
                                        self.numeric1   = self._val_1
                                        self.__type__   = type( self.numeric2 )
                                        self.string = self.numeric1 + self._ar_op_[ 0 ] + str( self.numeric2 )

                                        if self.__type__ in [ type( int())]:
                                            try:
                                                if self.key == False:
                                                    self.numeric = float( self.string )
                                                elif self.key == True:
                                                    self.numeric = float( self.string )
                                            except (SyntaxError, ValueError):
                                                if self.key == False:
                                                    self.error = ERRORS( self.line ).ERROR4( self.string, 'a float' )
                                                elif self.key == True:
                                                    self.error = ERRORS(self.line).ERROR4(self.string, 'a float' )
                                            except OverflowError:
                                                self.error = ERRORS(self.line).ERROR9( 'float' )
                                        else:
                                            try:
                                                self.numeric = complex( self.string )
                                                self.numeric, self.error = COMPLEX_ANALYZE(self.numeric,
                                                                                            self.line).COMPLEX()
                                            except (SyntaxError, ValueError):
                                                    self.error = ERRORS(self.line).ERROR4(self.string, 'a complex' )
                                            except OverflowError:
                                                self.error = ERRORS(self.line).ERROR9( 'complex' )

                                    else:
                                        self.error = ERRORS( self.line ).ERROR3( self.var )
                                else:
                                    self.error = ERRORS( self.line ).ERROR2( self.var )
                            else:
                                self.error = ERRORS( self.line ).ERROR2( self.var )

                        elif self.type == 'numeric':
                            self._val_2_, self.error = self.selection.SELECTION(self.var, self.var,
                                                            self.data_base, self.line).CHAR_SELECTION( '.' )
                            if self.error is None:
                                if len( self._val_2_ ) == 1:
                                    try:
                                        self.numeric2 = int( float( self.var ))
                                    except SyntaxError:
                                        self.error = ERRORS( self.line ).ERROR4( self.var )

                                    if self.error is None:
                                        self.numeric2   = str( self.numeric2 )
                                        self.numeric1   = self._val_1
                                        self.string     = self.numeric1 + self._ar_op_[0] + self.numeric2

                                        try:
                                            if self.key == False:
                                                self.numeric = float( self.string)
                                            elif self.key == True:
                                                self.numeric = float( self.string )
                                        except ( ValueError, SyntaxError):
                                            if self.key == False:
                                                self.error = ERRORS( self.line ).ERROR4( self.string, 'a float' )
                                            elif self.key == True:
                                                self.error = ERRORS(self.line).ERROR4(self.string, 'a float')
                                    else:
                                        self.error = self.error
                                else:
                                    self.error = ERRORS( self.line ).ERROR1( self.var )#self._val_2 )

                            else:
                                self.error = self.error

                        elif self.type == 'complex':
                            try:
                                self.numeric2 = complex( self.var )
                                self.numeric2, self.error = COMPLEX_ANALYZE(self.numeric2, self.line).COMPLEX()
                            except (ValueError, SyntaxError):
                                self.error = ERRORS( self.line ).ERROR4(self.var, 'a complex')

                            if self.error is None:
                                self.numeric2 = str(self.numeric2)
                                self.numeric1 = self._val_1
                                self.string = self.numeric1 + self._ar_op_[0] + self.numeric2

                                try:
                                    self.numeric = complex( self.string )
                                    self.numeric, self.error = COMPLEX_ANALYZE(self.numeric, self.line).COMPLEX()
                                except ( ValueError, SyntaxError ):
                                    self.error = ERRORS( self.line ).ERROR4( self.string, 'a complex')
                            else:
                                self.error = self.error

                    elif type( self._val_2 ) == type( list() ):
                        self.sign           = self._ar_op_[ 0 ]
                        self.operators      = self._ar_op_[ 1 : ]
                        self.num, self.error = NUMERICAL( self.master, self.data_base,
                                                self.line).ARITHMETIC_DEEP_CHECKING_INIT( self._val_2, self.operators )
                        if self.error is None:
                            if self.sign == '+':
                                self.numeric = self.num[ 0 ]
                            else:
                                self.numeric = self.sign + self.num[ 0 ]
                        else:
                            self.error = self.error

                else:
                    self.error = self.error
            else:
                self.error = self.error

        else:
            self._val_                  = self.values[ 'numeric' ][ 0 ]
            self._type_                 = self.values[ 'type' ]
            if self._type_ in [ None, 'numeric']:
                if self._val_[ 0 ] in self.chars:
                    self.__val__, self.error = self.control.CHECK_NAME( self._val_ )
                    if self.error is None:
                        self._val_ = self.__val__
                    else:
                        if self._val_ in [ '_int_', '_float_', '_complex_', '_string_' ]: self.error = None
                        else: pass

                    if self.error is None:
                        if self.variables:
                            if self._val_ in self.variables:
                                self.index      = self.variables.index( self._val_ )
                                self.numeric    = self._values_[ self.index ]
                            else: self.error = ERRORS( self.line ).ERROR2( self._val_ )
                        else: self.error = ERRORS( self.line ).ERROR2( self._val_ )
                    else: self.error = self.error

                else:
                    self._val__, self.error = self.selection.SELECTION(self._val_, self._val_,
                                                                       self.data_base, self.line).CHAR_SELECTION('.')
                    if self.error is None:
                        if len(self._val__) == 1:
                            self.key = False
                        elif len(self._val__) == 2:
                            self.key = True
                        else:
                            self.error = ERRORS( self.line ).ERROR1( self._val_ )

                        if self.error is None:

                            try:
                                if self.key == False:
                                    if 'e' in self._val_:
                                        self.numeric = float( self._val_ )
                                    elif 'E' in self._val_:
                                        self.numeric = float( self._val_ )
                                    else:
                                        self.numeric = int( float(self._val_) )

                                elif self.key == True :
                                    self.numeric = float( self._val_)

                            except SyntaxError:
                                if self.key == False:
                                    self.error = ERRORS( self.line ).ERROR4( self._val_ )
                                elif self.key == True:
                                    self.error = ERRORS( self.line ).ERROR4( self._val_, 'a float' )

                            except ValueError:
                                if self.key == False:
                                    self.error = ERRORS( self.line ).ERROR4( self._val_ )
                                elif self.key == True:
                                    self.error = ERRORS( self.line ).ERROR4( self._val_, 'a float' )

                            except OverflowError:
                                self.error = ERRORS( self.line ).ERROR9( 'float')
                        else:
                            self.error = self.error
                    else:
                        self.error = self.error

            else:
                try:
                    self.numeric = complex( self._val_ )
                    self.numeric, self.error = COMPLEX_ANALYZE( self.numeric, self.line ).COMPLEX()

                except (ValueError, SyntaxError):
                    self.error = ERRORS( self.line ).ERROR4(self._val_, 'a complex')
                except OverflowError:
                    self.error = ERRORS(self.line).ERROR9( 'complex' )

        return self.numeric, self.error

    @cython.cfunc
    def ARITHMETIC_CHECK(self, values: list, arithmetic: list, main_string: str=""):
        self.values                     = values
        self.arithmetic_operator        = arithmetic
        self.numeric                    = []
        self.calculations               = []
        self.error                      = None

        for i, op in enumerate( self.arithmetic_operator ):
            if op is None:
                try:
                    self.get_values             = self.values[ i ][ 0 ]
                    self.type                   = self.get_values[ 'type' ]

                    self._return_, self.error   = TYPE( self.master, self.get_values, self.data_base, self.line,
                                                                                    self.type ).TYPE( main__main )
                    if self.error is None:
                        self.numeric.append( self._return_ )
                    else:  break
                except IndexError: 
                    self.error = ERRORS( self.line).ERROR0(main_string)
                    break

            else:
                if len( self.values[ i ] ) > len( op ):
                    self.len_val                        = len( self.values[ i ] )
                    for j in range( self.len_val ):
                        self._get_values_               = self.values[ i ][ j ]
                        self.type                       = self._get_values_[ 'type' ]
                        self._return_, self.error       = TYPE( self.master, self._get_values_, self.data_base,
                                                                            self.line, self.type ).TYPE( main__main )
                        if self.error is None:
                            if j != self.len_val - 1:
                                self.calculations.append( [ self._return_ ] )
                                self.calculations.append( op[ j ] )
                            else:
                                self.calculations.append( [ self._return_ ] )
                        else:
                            self.error = self.error
                            break

                    if self.error is None:
                        self.history_of_op              = ''
                        for string in self.calculations:
                            if type( string ) == type( str() ):
                                self.history_of_op += string
                            else:
                                pass

                        self.__values__, self.error       = mathematics.MAGIC_MATH_BASE( self.calculations, self.data_base,
                                                                    self.history_of_op, self.line ).MATHS_OPERATIONS()
                        if self.error is None:
                            self.numeric.append( self.__values__ )
                            self.calculations = []

                        else:
                            self.error = self.error
                            break
                    else:
                        self.error = self.error
                        break

                elif len( self.values[ i ] ) == len( op ):

                    if type( op[ 0 ] ) == type( list() ):
                        self.sign       = '+'
                    else:
                        if len( op ) == 1:
                            self.sign   = op[ 0 ]
                        else:
                            key = False
                            for _op_ in op:
                                if type( _op_ ) == type( list( ) ):
                                    key = True
                                    break
                            if key == False:
                                self.sign = op[ 0 ]
                            else:
                                self.sign = ''

                    if self.sign in [ '-' ]:  self.calculations.append( self.sign )
                    else: pass

                    self.len_val = len( self.values[ i ] )

                    if len( op ) == 1:
                        
                        self._get_values_ = self.values[ i ][ 0 ]

                        try:
                            self.type                   = self._get_values_[ 'type' ]
                            self._return_, self.error   = TYPE( self.master, self._get_values_, self.data_base, self.line,
                                                                              self.type ).TYPE( main__main )
                            if self.error is None:
                                self.calculations.append( [ self._return_ ] )
                                self.history_of_op      = ''
                                for string in self.calculations:
                                    if type( string ) == type( str() ):
                                        self.history_of_op += string
                                    else:
                                        pass

                                self.__values__, self.error = mathematics.MAGIC_MATH_BASE( self.calculations,
                                                    self.data_base, self.history_of_op, self.line ).MATHS_OPERATIONS()

                                if self.error is None:
                                    self.numeric.append( self.__values__ )
                                    self.calculations = []
                                else:
                                    self.error = self.error
                                    break

                            else:
                                self.error = self.error
                                break

                        except TypeError :
                            
                            self._return_, self.error   = ARRITHMETIC_DEEP_CHECKING( self.master, self._get_values_,
                                                            op[ 0 ], self.data_base, self.line ).INIT( main__main )
                            if self.error is None:
                                self.calculations.append( [ self._return_[ 0 ] ])
                                self.history_of_op      = ''

                                for string in self.calculations:
                                    if type( string ) == type( str() ):
                                        self.history_of_op += string
                                    else:
                                        pass

                                self.__values__, self.error = mathematics.MAGIC_MATH_BASE( self.calculations,
                                                    self.data_base, self.history_of_op, self.line ).MATHS_OPERATIONS()

                                if self.error is None:
                                    self.numeric.append( self.__values__ )
                                    self.calculations = []
                                else:
                                    self.error = self.error
                                    break
                            else:
                                self.error = self.error
                                break

                    else:
                        for j in range( self.len_val ):
                            self._get_values_ = self.values[ i ][ j ]

                            if type( self._get_values_ ) == type( dict() ) :
                                self.type = self._get_values_[ 'type' ]
                                self._return_, self.error = TYPE( self.master, self._get_values_, self.data_base, self.line,
                                                            self.type ).TYPE( main__main )
                                if self.error is None:
                                    if j != self.len_val - 1:
                                        try:
                                            self.calculations.append( [ self._return_ ] )
                                            if self.calculations[ 0 ] == '-':
                                                self.calculations.append( op[ j + 1 ] )
                                            else:
                                                self.calculations.append(op[ j ]) ### here
                                        except TypeError:
                                            self.calculations.append( [ self._return_ ] )
                                            self.calculations.append( op[ j ] )
                                    else:
                                        self.calculations.append( [ self._return_ ] )
                                else: break
                                
                            else:
                                self._return_, self.error = ARRITHMETIC_DEEP_CHECKING(self.master, self._get_values_,
                                                             op[ j ], self.data_base, self.line).INIT( main__main )
                        
                                if self.error is None :
                                    if j != self.len_val - 1:
                                        try:
                                            self.calculations.append( [ self._return_[ 0 ] ] )
                                            self.calculations.append( op[ j + 1 ] )
                                        except TypeError:
                                            self.calculations.append( [ self._return_[ 0 ] ] )
                                            self.calculations.append( op[ j ] )

                                    else:  self.calculations.append( [ self._return_[ 0 ] ] )
                                else:  break

                        if self.error is None:
                            self.history_of_op          = ''
                            for string in self.calculations:
                                if type( string ) == type( str() ):
                                    self.history_of_op += string
                                else: pass
                        
                            self.__values__, self.error = mathematics.MAGIC_MATH_BASE(self.calculations,
                                                self.data_base,self.history_of_op, self.line) .MATHS_OPERATIONS()

                            if self.error is None:
                                self.numeric.append( self.__values__ )
                                self.calculations = []
                            else:
                                self.error = self.error
                                break
                        else:
                            self.error = self.error
                            break

                else:
                    self.sign               = ''
                    self.operators          = op[ : ]
                    self._get_values_       = self.values[ i ]

                    self._return_, self.error = ARRITHMETIC_DEEP_CHECKING(self.master, self._get_values_,
                                                        self.operators, self.data_base, self.line).INIT( main__main )
                    if self.error is None:
                        self.history_of_op  =  ''
                        self.calculations.append( [ self._return_[ 0 ] ] )
                        for string in self.calculations:
                            if type( string ) == type( str() ):
                                self.history_of_op += string
                            else:  pass

                        self.__values__, self.error = mathematics.MAGIC_MATH_BASE(self.calculations,
                                            self.data_base, self.history_of_op, self.line).MATHS_OPERATIONS()

                        if self.error is None:
                            self.numeric.append( self.__values__[ 0 ] )
                            self.calculations = []
                        else: break
                    else: break
       
        return  self.numeric, self.error
    
    @cython.cfunc
    def LOGICAL_CHECK(self, values: list, arithmetic: list, logical: list, main_string: str=""):
        self.error                  = None
        self.arithmetic_operator    = arithmetic
        self.logical_operator       = logical
        self.values                 = values
        self.numeric                = []
        self._return_               = None

        for i, l_op in enumerate( self.logical_operator ):
            if l_op is None:
                self.get_values = [ self.values[ i ] ]
                self.ar_op      = [ self.arithmetic_operator[ i ] ]
                self.num, self.error = NUMERICAL( self.master, self.data_base,
                                            self.line ).ARITHMETIC_CHECK( self.get_values, self.ar_op, main_string )
                if self.error is None:  self.numeric.append( self.num[ 0 ] )
                else:  break

            else:
                if self.data_base['irene'] is None: pass
                else: self.data_base['irene'] = None

                self._num_  = []
                self.get_values = self.values[ i ]

                for j in range( len( self.get_values ) ):
                    self._get_values_ = self.get_values[ j ]
                    
                    if type( self._get_values_ ) == type( dict() ):  self._get_values_   = [[ self._get_values_ ]]
                    else:  self._get_values_   = [ self._get_values_ ]

                    self.ar_op              = [ self.arithmetic_operator[ i ][ j ] ]
                    self.num, self.error    = NUMERICAL(self.master, self.data_base,
                                                     self.line).ARITHMETIC_CHECK( self._get_values_, self.ar_op, main_string )
                    if self.error is None:  self._num_.append( self.num[ 0 ] )
                    else:  break

                if self.error is None:  self.numeric.append( self._num_)
                else: break

        if self.error is None:
            self._return_, self.error = FINAL_VALUE( self.numeric, self.data_base, self.line, self.logical_operator).FINAL_VALUE()
        else: pass

        return self._return_, self.error

    @cython.cfunc
    def BOOLEAN_CHECK(self, values: list, arithmetic: list, logical: list, boolean: list, main_string: str = ""):
        self.error                      = None
        self.arithmetic_operator        = arithmetic
        self.logical_operator           = logical
        self.bool_operator              = boolean
        self.values                     = values
        self.numeric                    = []

        for i, b_op in enumerate( self.bool_operator ):
            if b_op is None:
                self.get_values         = [ self.values[ i ] ]
                self.l_op               = [ self.logical_operator[ i ] ]
                self.ar_op              = [ self.arithmetic_operator[ i ] ]
                
                self.num, self.error    = NUMERICAL( self.master, self.data_base,
                                                  self.line ).LOGICAL_CHECK(self.get_values, self.ar_op, self.l_op, main_string )
                if self.error is None:  self.numeric.append( self.num )
                else:  break

            else:
                if self.data_base['irene'] is None: pass
                else: self.data_base['irene'] = None

                self._num_          = []
                self.get_values     = self.values[ i ]
                self.l_op           = self.logical_operator[ i ]
                self.ar_op          = self.arithmetic_operator[ i ]
                self.len            = len( self.values[ i ])

                for j in range( self.len ):
                    self._get_values_   = self.get_values[ j ]
                    self._l_op_         = self.l_op[ j ]
                    self._ar_op_        = self.ar_op[ j ]

                    if self._ar_op_ is None:  self._ar_op_    = [[ self._ar_op_ ]]
                    else: self._ar_op_    = [ self._ar_op_ ]
                    
                    if self._l_op_ is None:  self._l_op_     = [[ self._l_op_ ]]
                    else:  self._l_op_     = [ self._l_op_ ]

                    if type( self._get_values_ ) == type( dict() ):  self._get_values_   = [ [ self._get_values_ ] ]
                    else:  self._get_values_   = [ self._get_values_ ]

                    self.num, self.error = NUMERICAL( self.master, self.data_base,
                                            self.line).LOGICAL_CHECK( self._get_values_, self._ar_op_, self._l_op_, main_string)
                    if self.error is None:  self._num_.append( self.num )
                    else: break
                    
                if self.error is None:
                    self._num_ = FINAL_VALUE( self._num_, self.data_base, self.line, None ).BOOLEAN_OPERATION( b_op )
                    self.numeric.append( self._num_ )
                else: break

        return self.numeric, self.error

    @cython.cfunc
    def ARITHMETIC_DEEP_CHECKING_INIT(self, values: list, operators: list ):
        self.error          = None
        self.sum            = ''
        self.numeric        = []
        self.operators      = operators
        self._get_values_   = values
        self.index          = []

        self.sub_len_val    = len( self._get_values_ )
        self.sub_len_op     = len( self.operators )

        if self.sub_len_val > self.sub_len_op:
            for k, sub_values in enumerate( self._get_values_ ):
                if type( sub_values ) == type( dict() ):
                    self.sub_values     = sub_values

                    self.type = sub_values[ 'type' ]
                    self.num, self.error = TYPE( self.master, self.sub_values, self.data_base, self.line,
                                                                                    self.type ).TYPE( main__main )

                    if self.error is None:
                        if k != self.sub_len_val - 1:
                            self.sum += str( self.num ) + self.operators[ k ]

                        else:
                            self.sum += str( self.num )
                    else:
                        self.error = self.error
                        break

                else:
                    self.sub_values = sub_values
                    self.num, self.error = NUMERICAL(self.master, self.data_base,
                                        self.line).ARITHMETIC_DEEP_CHECKING( self.sub_values, self.operators[ 0 ][ k ])
                    if self.error is None:
                        if k != self.sub_len_val - 1:
                            self.sum += str( self.num[ 0 ] ) + self.operators[ k ]

                        else:
                            self.sum += str( self.num[ 0 ] )

                    else:
                        self.error = self.error
                        break

            if self.error is None:

                self._sum_, self.error = self.maths_operation.MAGIC_MATH_BASE( self.sum, self.data_base,
                                                            self.line ).MATHS_OPERATIONS()
                if self.error is None:
                    self.numeric.append( str( self._sum_ ) )
                    self.sum = ''
                else:
                    self.error = self.error

            else:
                self.error = self.error

        else:
            if type( self.operators[ 0 ] ) == type( list() ):
                self.sign                   = '+'
                self.operators              = self.operators
            else:
                self.sign                   = self.operators[ 0 ]
                self.operators              = self.operators[1 : ]

            for k, sub_values in enumerate( self._get_values_ ):
                self.sub_values             = sub_values
                if type( self.sub_values ) == type( dict() ):
                    self.type               = self.sub_values[ 'type' ]
                    self.num, self.error    = TYPE( self.master, self.sub_values, self.data_base, self.line,
                                                                                    self.type ).TYPE( main__main )

                    if self.error is None:
                        if k != self.sub_len_val - 1:
                            if not self.index:
                                self.sum += str( self.num ) + self.operators[ k + 1 ]
                            else:
                                self.sum += str( self.num ) + self.operators[ k + self.index[ -1 ] + 1]
                        else:
                            self.sum += str( self.num )
                    else:
                        self.error = self.error
                        break

                else:
                    self.num        = ''
                    if type( self.operators[ k ] ) == type( list()):
                        self.num, self.error = NUMERICAL(self.master, self.data_base,
                                        self.line).ARITHMETIC_DEEP_CHECKING( self.sub_values, self.operators[ k ])
                    else:
                        self.idd    = 0
                        for s, _op_ in enumerate( self.operators[k : ] ):
                            if type( _op_ ) == type( list() ):
                                self.idd = s
                                break
                            else:
                                pass
                        self.index.append( self.idd )
                        self.num, self.error = NUMERICAL(self.master, self.data_base,
                                    self.line).ARITHMETIC_DEEP_CHECKING(self.sub_values, self.operators[k + self.idd ])

                    if self.error is None:
                        self.key    = True
                        if k != self.sub_len_val - 1:
                            try:
                                self.sum += str( self.num[ 0 ] ) + self.operators[ k + 1 ]
                            except TypeError:
                                self.sum += str( self.num[ 0 ] ) + self.operators[ k + 2 ]
                        else:
                            self.sum += str( self.num[ 0 ] )
                    else:
                        self.error = self.error
                        break

            if self.error is None:
                if self.sign == '+':
                    self.sum = self.sum
                else:
                    self.sum = self.sign + self.sum
                print(self.sum)
                self._sum_, self.error = self.maths_operation.MAGIC_MATH_BASE( self.sum, self.data_base,
                                                                self.line ).MATHS_OPERATIONS()
                if self.error is None:
                    self.numeric.append( str( self._sum_ ) )
                    self.sum = ''
                else:
                    self.error = self.error

            else:
                self.error = self.error

        return self.numeric, self.error

    @cython.cfunc
    def ARITHMETIC_DEEP_CHECKING(self, values: list, operators: list):
        self.error          = None
        self.sum            = ''
        self.numeric        = []
        self.operators      = operators
        self._get_values_   = values

        self.sub_len_val    = len( self._get_values_ )
        self.sub_len_op     = len( self.operators )

        if self.sub_len_val > self.sub_len_op:
            for k, sub_values in enumerate(self._get_values_):
                if type( sub_values ) == type( dict() ):
                    self.type = sub_values[ 'type' ]
                    self.sub_values = sub_values
                    self.num, self.error = TYPE( self.master, self.sub_values, self.data_base, self.line,
                                                                                self.type ).TYPE( main__main )

                    if self.error is None:

                        if k != self.sub_len_val - 1:
                            self.sum += str( self.num ) + self.operators[ k ]
                        else:

                            self.sum += str( self.num )
                    else:
                        self.error = self.error
                        break

                else:
                    self.num, self.error = NUMERICAL( self.master, self.data_base,
                                            self.line ).ARITHMETIC_DEEP_CHECKING_INIT( sub_values, self.operators[ k ])
                    if self.error is None:
                        if k != self.sub_len_val - 1:
                            self.sum += str( self.num[ 0 ] ) + self.operators[ k ]
                        else:
                            self.sum += str( self.num[ 0 ] )
                    else:
                        self.error = self.error
                        break

            if self.error is None:
                self._sum_, self.error = self.maths_operation.MAGIC_MATH_BASE (self.sum, self.data_base,
                                                                              self.line ).MATHS_OPERATIONS()
                if self.error is None:
                    self.numeric.append( str( self._sum_ ) )
                    self.sum = ''
                else:
                    self.error = self.error

            else:
                self.error = self.error

        elif self.sub_len_val == self.sub_len_op:
            if type(  self.operators[ 0 ] ) == type( list()):
                self.sign       = ''
            else:
                self.sign       = self.operators[ 0 ]
                self.operators  = self.operators[ 1 : ]
                self.sum        = self.sign

            for k, sub_values in enumerate( self._get_values_ ):
                if type( sub_values ) == type( dict() ):
                    self.type = sub_values[ 'type' ]
                    self.sub_values = sub_values

                    self.num, self.error = TYPE( self.master, self.sub_values, self.data_base, self.line,
                                                                                    self.type ).TYPE( main__main )

                    if self.error is None:
                        if k != self.sub_len_val - 1:
                            self.sum += str( self.num ) + self.operators[ k ]
                        else:
                            self.sum += str( self.num )
                    else:
                        self.error = self.error
                        break

                else:
                    self.num, self.error = NUMERICAL(self.master, self.data_base,
                                        self.line).ARITHMETIC_DEEP_CHECKING_INIT(sub_values, self.operators[ k ])
                    if self.error is None:

                        if k != self.sub_len_val - 1:
                            self.sum += str( self.num[ 0 ] ) + self.operators[ k ]
                        else:
                            self.sum += str( self.num[ 0 ] )
                    else:
                        self.error = self.error
                        break

            if self.error is None:
                self._sum_, self.error = self.maths_operation.MAGIC_MATH_BASE ( self.sum, self.data_base,
                                                                                        self.line ).MATHS_OPERATIONS()
                if self.error is None:
                    self.numeric.append( str( self._sum_ ) )
                    self.sum    = ''
                else:
                    self.error  = self.error

            else:
                self.error = self.error

        else:
            if type( self.operators[ 0 ] ) == type( list() ):
                self.sign       = '+'
                self.operators  = self.operators[ : ]
            else:
                self.sign       = self.operators[ 0 ]
                self.operators  = self.operators[ 1 : ]

            for k, sub_values in enumerate( self._get_values_ ):
                if type( sub_values ) == type( dict() ):
                    self.sub_values         = sub_values
                    self.type               = self.sub_values[ 'type' ]
                    self.num, self.error    = TYPE( self.master, self.sub_values, self.data_base, self.line,
                                                                                self.type ).TYPE( main__main )

                    if self.error is None:
                        if k != self.sub_len_val - 1:
                            try:
                                self.sum += str( self.num ) + self.operators[ k + 2 ]
                            except TypeError:
                                self.sum += str( self.num ) + self.operators[ k + 1 ]
                            except IndexError:
                                self.sum += str( self.num ) + self.operators[ k ]
                        else:
                            self.sum += str( self.num )
                    else:
                        self.error = self.error
                        break

                else:
                    self.sub_values = sub_values
                    self.num, self.error = NUMERICAL(self.master, self.data_base,
                                        self.line).ARITHMETIC_DEEP_CHECKING_INIT(self.sub_values, self.operators[ k ])

                    if self.error is None:
                        if k != self.sub_len_val - 1:
                            try:
                                self.sum += str( self.num[ 0 ] ) + self.operators[ k + 1 ]
                            except TypeError:
                                self.sum += str( self.num[ 0 ] ) + self.operators[ k + 2 ]
                        else:
                            self.sum += str( self.num[ 0 ] )
                    else:
                        self.error = self.error
                        break

            if self.error is None:
                if self.sign == '+':
                    self.sum = self.sum
                else:
                    self.sum = self.sign + self.sum

                self._sum_, self.error = self.maths_operation.MAGIC_MATH_BASE(self.sum, self.data_base,
                                                                              self.line).MATHS_OPERATIONS()
                if self.error is None:
                    self.numeric.append( str( self._sum_ ) )
                    self.sum    = ''
                else:
                    self.error  = self.error

            else:
                self.error = self.error

        return self.numeric, self.error

class DICT:
    def __init__(self, master:list, data_base:dict, line:int):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.variables      = self.data_base[ 'variables' ][ 'vars' ]
        self._values_       = self.data_base[ 'variables' ][ 'values' ]
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def DICT_CHECK(self, main_string : str ):
        self.error          = None
        self.key_names      = self.master[ 'names' ]
        self._val_          = self.master[ 'values' ][ 0 ]
        self.list_keys      = list( self._val_.keys() )
        self.type           = self._val_[ 'type' ]
        
        try:
            self.main_dict      = self._val_[ 'numeric' ][ 0 ]
            self._return_       = None
            self.dict_type      = None

            if   self.type is None          :
                if self.variables:
                    self.main_dict, self.error = self.control.CHECK_NAME( self.main_dict, True )
                    if self.error is None:
                        if self.main_dict in self.variables:
                            self.index = self.variables.index( self.main_dict )
                            self.main_dict_value    = self._values_[ self.index ]

                            if type( self.main_dict_value ) == type( dict() ):
                                for j, keys in enumerate( self.key_names ):
                                    if keys in list( self.main_dict_value.keys() ):
                                        self.main_dict_value = self.main_dict_value[ keys ]
                                        if j != len( self.key_names ) - 1:
                                            if type( self.main_dict_value ) == type( dict() ): pass
                                            else:
                                                self.error = ERRORS( self.line).ERROR3( self.main_dict_value, 'a dictionary()')
                                                break
                                        else:  pass
                                    else:
                                        self.error = ERRORS( self.line ).ERROR5( self.main_dict_value.keys(), keys )
                                        break

                                if self.error is None:
                                    self._return_   = self.main_dict_value
                                    self.dict_type  = type( self._return_ )
                                else: pass

                            else: self.error = ERRORS( self.line ).ERROR3( self.main_dict, 'a dictionary()')

                        else:  self.error = ERRORS( self.line ).ERROR2( self.main_dict )

                    else: pass
                else:
                    self.main_dict, self.error = self.control.CHECK_NAME(self.main_dict)
                    if self.error is None:  self.error = ERRORS( self.line ).ERROR2( self.main_dict )
                    else: pass

            elif self.type == 'dictionnary' :
                self.input = {'numeric': [ self.main_dict ], 'type': 'dictionnary' }
                self._return_, self.error = get_dictionary.DICTIONARY(self.input, self.data_base,
                                                                            self.line ).MAIN_DICT( main_string )
                if self.error is None:
                    self.names = list( self._return_.keys() )
                    for i, keys in enumerate( self.key_names ):
                        if keys in self.names:
                            self._return_ = self._return_[ keys ]
                            if i == len( self.key_names ) - 1:  pass
                            else:
                                if type( self._return_ ) == type( dict() ):
                                    self.names = list( self._return_.keys() )
                                else:
                                    self.error = ERRORS( self.line ).ERROR3( self._return_, 'a dictionary()')
                                    break
                        else:
                            self.error = ERRORS( self.line ).ERROR5( self._return_, keys)
                            break

                else: pass

            elif self.type == 'list'        :
                self.input = {'numeric': [ self.main_dict ], 'type': 'list'}
                self._return_, self.error = get_list.LIST(self.input, self.data_base,
                                                                    self.line).MAIN_LIST(main_string)
                if self.error is None:
                    if type( self._return_) == type( dict()) :
                        self.names = list( self._return_.keys() )
                        for i, keys in enumerate( self.key_names ):
                            if keys in self.names:
                                self._return_ = self._return_[ keys ]
                                if i == len(self.key_names) - 1:  pass
                                else:
                                    if type(self._return_) == type(dict()):
                                        self.names = list(self._return_.keys())
                                    else:
                                        self.error = ERRORS(self.line).ERROR3(self._return_, 'a dictionary()')
                                        break

                            else:
                                self.error = ERRORS(self.line).ERROR5(self._return_, keys)
                                break
                    else: self.error = ERRORS( self.line ).ERROR3( self._return_, 'a dictionary()')
                else: pass

            elif self.type == 'numeric'     :
                self.error = ERRORS( self.line ).ERROR0( main_string )

            elif self.type == 'class'       :
                
                self.num, _ , e, self.error = classInit.CLASS_TREATMENT( self._val_ , self.data_base,
                                                  self.line ).TREATMENT( )
                if self.error is None:
                    if not  _ :
                        self._return_ = self.num
                        if self.master[ 'add_params' ][ 1 ] is None: pass 
                        else:
                            self.num, self.error = func.FUNCTION_TREATMENT( self.master, self.data_base,
                                                    self.line ).TOTAL_TREATMENT( self._return_, typ = 'class' )
                            if self.error is None: 
                                self._return_ = self.num 
                                if type( self._return_ ) == type( dict() ):
                                    self.names = list( self._return_.keys() )
                                    for i, keys in enumerate( self.key_names ):
                                        if keys in self.names:
                                            self._return_ = self._return_[ keys ]
                                            if i == len( self.key_names ) - 1: pass
                                            else:
                                                if type( self._return_ ) == type( dict() ): self.names = list( self._return_.keys() )
                                                else:
                                                    self.error = ERRORS( self.line ).ERROR3( self._return_, 'a dictionary()')
                                                    break
                                        else:
                                            self.error = ERRORS( self.line ).ERROR5( self._return_, keys)
                                            break
                                else: self.error = ERRORS( self.line ).ERROR3( self._return_, 'a dictionary()')
                            else: pass
                    else:
                        self.error                              = _[ 0 ]
                        self.data_base[ 'no_printed_values' ]   = []
                else: self.error = self.error
            
            else: pass
            
            if type( self._return_ ) == type( str() ): return self._return_ , self.error#'"'+self._return_+'"', self.error
            else: return self._return_ , self.error

        except TypeError:
            
            if   self.type == 'function'    :
                self.num, _, e, self.error = func.FUNCTION_TREATMENT( self._val_, self.data_base,
                                                  self.line ).TREATMENT( main_string, self._val_ )
                if self.error is None:
                    if not  _ :
                        self._return_ = self.num
                        if self._val_[ 'add_params' ] is None: pass 
                        else:
                            self.num, self.error = func.FUNCTION_TREATMENT( self._val_, self.data_base,
                                                    self.line ).TOTAL_TREATMENT( self._return_ )
                            if self.error is None: self._return_ = self.num 
                            else: pass
                    else:
                        self.error = _[ 0 ]
                        self.data_base[ 'no_printed_values' ] = []
                else: pass
            
                if self.error is None:
                    if type( self._return_ ) == type( dict() ):
                        self.names = list( self._return_.keys() )
                        for i, keys in enumerate( self.key_names ):
                            if keys in self.names:
                                self._return_ = self._return_[ keys ]
                                if i == len( self.key_names ) - 1: pass
                                else:
                                    if type( self._return_ ) == type( dict() ):
                                        self.names = list( self._return_.keys() )
                                    else:
                                        self.error = ERRORS( self.line ).ERROR3( self._return_, 'a dictionary()')
                                        break
                            else:
                                self.error = ERRORS( self.line ).ERROR5( self._return_, keys)
                                break
                    else: self.error = ERRORS( self.line ).ERROR3( self._return_, 'a dictionary()')
                else: pass

                if type( self._return_ ) == type( str() ): return self._return_ , self.error#'"'+self._return_+'"', self.error
                else: return self._return_ , self.error 
                
            elif self.type == 'class'       : 
                self.num, _ , e, self.error = classInit.CLASS_TREATMENT( self._val_ , self.data_base,
                                                  self.line ).TREATMENT( )
                if self.error is None:
                    if not  _ :
                        self._return_ = self.num
                        if self._val_[ 'add_params' ][ 1 ] is None: pass 
                        else:
                            self.num, self.error = func.FUNCTION_TREATMENT( self._val_, self.data_base,
                                                    self.line ).TOTAL_TREATMENT( self._return_, typ = 'class' )
                            if self.error is None:  self._return_ = self.num 
                            else: pass
                    else:
                        self.error                              = _[ 0 ]
                        self.data_base[ 'no_printed_values' ]   = []
                else: pass
                
                if self.error is None: 
                    if type( self._return_ ) == type( dict() ):
                        self.names = list( self._return_.keys() )
                        for i, keys in enumerate( self.key_names ):
                            if keys in self.names:
                                self._return_ = self._return_[ keys ]
                                if i == len( self.key_names ) - 1: pass
                                else:
                                    if type( self._return_ ) == type( dict() ): self.names = list( self._return_.keys() )
                                    else:
                                        self.error = ERRORS( self.line ).ERROR3( self._return_, 'a dictionary()')
                                        break
                            else:
                                self.error = ERRORS( self.line ).ERROR5( self._return_, keys)
                                break
                    else: self.error = ERRORS( self.line ).ERROR3( self._return_, 'a dictionary()')
                else: pass 
                
                if type( self._return_ ) == type( str() ): return self._return_ , self.error#'"'+self._return_+'"', self.error
                else: return self._return_ , self.error
                            
            else: return None, None

    def VAR_NAMES(self, main_string : str ) :

        self.error              = None
        self.key_names          = self.master['names']
        self._val_              = self.master['values'][0]
        self.list_keys          = list(self._val_.keys())
        self.type               = self._val_['type']
        self.main_dict          = self._val_['numeric'][0]
        self._return_           = None
        self.dict_type          = None
        self._name_             = None
        self.info               = None

        if self.type is None            :
            if self.variables:
                self.main_dict, self.error = self.control.CHECK_NAME(self.main_dict, True)
                if self.error is None:
                    if self.main_dict in self.variables:
                        self._name_ = self.main_dict
                        self.index = self.variables.index(self.main_dict)
                        self.main_dict_value = self._values_[self.index]

                        if type(self.main_dict_value) == type(dict()):
                            for j, keys in enumerate(self.key_names):
                                if keys in list(self.main_dict_value.keys()):
                                    self.main_dict_value = self.main_dict_value[ keys ]
                                    if j != len(self.key_names) - 1:
                                        if type(self.main_dict_value) == type(dict()): pass
                                        else:
                                            self.error = ERRORS(self.line).ERROR3(self.main_dict_value, 'a dictionary()')                               
                                            break
                                    else: pass
                                else:
                                    if j == len( self.key_names ) - 1: pass
                                    else:
                                        self.error = ERRORS( self.line ).ERROR5( self.main_dict_value, self.key_names[j - 2 ])
                                        break

                            if self.error is None:
                                self._return_ = self.main_dict_value
                                self.dict_type = type(self._return_)
                            else: pass 
                        else: self.error = ERRORS(self.line).ERROR3(self.main_dict, 'a dictionary()')
                    else: self.error = ERRORS(self.line).ERROR2(self.main_dict)
                else: pass
            else:
                self.main_dict, self.error = self.control.CHECK_NAME(self.main_dict)
                if self.error is None: self.error = ERRORS(self.line).ERROR2(self.main_dict)
                else: pass

        elif self.type == 'dictionnary' :
            self.idd            = None
            self.string         = ''
            for i, str_ in enumerate( self.main_dict ):
                if str_ in ['[', '(', '{', '$']:
                    self.idd = i
                    break
                else: self.string += str_

            if self.idd != 0:
                self.string, self.error = self.control.DELETE_SPACE( self.string )
                if self.error is None:
                    self._name_, self.error = self.control.CHECK_NAME( self.string )
                    if self.error is None:
                        self.input = {'numeric': [self.main_dict], 'type': 'dictionnary'}
                        self._return_, self.error = get_dictionary.DICTIONARY(self.input, self.data_base,
                                                                              self.line).MAIN_DICT(main_string)
                        if self.error is None:
                            self.names = list(self._return_.keys())
                            for i, keys in enumerate(self.key_names):
                                if keys in self.names:
                                    self._return_ = self._return_[ keys ]
                                    if i == len(self.key_names) - 1: pass
                                    else:
                                        if type(self._return_) == type(dict()):
                                            self.names = list(self._return_.keys())
                                        else:
                                            self.error = ERRORS(self.line).ERROR3(self._return_, 'a dictionary()')
                                            break

                                else:
                                    if i == len( self.key_names ) - 1: pass
                                    else:
                                        self.error = ERRORS( self.line ).ERROR5( self._return_, self.key_names[  i - 2 ])
                                        break

                        else: pass
                    else: pass
                else: self.error = ERRORS( self.line ).ERROR0( self.main_dict )
            else:
                self.string, self.error = self.control.DELETE_SPACE( self.string )
                if self.error is None:
                    self._name_, self.error = self.control.CHECK_NAME( self.string )
                else:
                    self.error = ERRORS( self.line ).ERROR0( self.main_dict )

        elif self.type == 'list'        :
            self.idd        = None
            self.string     = ''
            for i, str_ in enumerate( self.main_dict ):
                if str_ in ['[', '(', '{', '$']:
                    self.idd = i
                    break
                else: self.string += str_

            if self.idd != 0:
                self._name_, self.error = self.control.DELETE_SPACE( self.string )
                if self.error is None:
                    self._name_, self.error  =self.control.CHECK_NAME( self._name_ )
                    if self.error is None:
                        self.input = {'numeric': [self.main_dict], 'type': 'list'}
                        self._return_, self.info, self.data, self.error = get_list.LIST(self.input, self.data_base,
                                                                                        self.line).VAR_NAMES( main_string )
                        if self.error is None:
                            if type( self._return_ ) == type( dict() ):
                                self.names = list(self._return_.keys())
                                for i, keys in enumerate( self.key_names ):
                                    if keys in self.names:
                                        self._return_ = self._return_[ keys ]
                                        if i == len(self.key_names) - 1: pass
                                        else:
                                            if type(self._return_) == type(dict()):
                                                self.names = list(self._return_.keys())
                                            else:
                                                self.error = ERRORS(self.line).ERROR3(self._return_, 'a dictionary()')
                                                break

                                    else:
                                        if i == len( self.key_names ) - 1: pass
                                        else:
                                            self.error = ERRORS(self.line).ERROR5(self._return_, self.key_names[ i - 2 ])
                                            break
                            else: self.error = ERRORS( self.line ).ERROR3( self._return_, 'a dictionary()')
                        else: pass
                    else: pass
                else: self.error = ERRORS(self.line).ERROR0(self.main_dict)
            else:
                self.string, self.error = self.control.DELETE_SPACE( self.string )
                if self.error is None:
                    self._name_, self.error = self.control.CHECK_NAME( self.string )
                else:
                    self.error = ERRORS( self.line ).ERROR0( self.main_dict )

        elif self.type == 'numeric'     : 
            self.error = ERRORS(self.line).ERROR0(main_string)
        
        else: pass

        return self._name_, self.key_names, self.info,  self.error

@cython.cclass
class TYPE:
    def __init__(self, main_master: dict, master: dict, data_base: dict, line: int, type: str):
        self.type               = type
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.main_master        = main_master

    def TYPE(self, main_string: str, name : str = 'python'):
        self.error              = None
        self._return_           = None

        if   self.type in [ 'numeric', None, 'complex' ]:
            #self.num, self.error = NUMERICAL( self.main_master, self.data_base,
            #                                 self.line).NUEMERICAL_CHECK( self.master )
            self.num, self.error = NumeriCal.NUMERICAL( self.master, self.data_base, self.line ).CHECK()
            if self.error is None:
                self._return_ = self.num
            else:
                if self.error : pass
                else:
                    self._return_ = self.num
                    self.error = None
        elif self.type in [ 'dictionnary' ]             :
            
            if type( self.master ) == type( dict() ):
                self.lists = list( self.master.keys() )
                if 'values' not in self.lists:
                    self.num, self.error = get_dictionary.DICTIONARY(self.master, self.data_base,
                                                                     self.line).MAIN_DICT( main_string )
                else:
                    #print( self.type,'@@', self.master)
                    self.num, self.error = DICT(self.master, self.data_base,
                                                self.line).DICT_CHECK( main_string )
                if self.error is None:
                    self._return_ = self.num
                else:
                    self.error = self.error
            else:
                pass
        elif self.type in [ 'list' ]                    :
            if type( self.master ) == type( dict() ):
                self.lists = list( self.master.keys() )
                if 'values' not in self.lists:
                    self.num, self.error = get_list.LIST(self.master, self.data_base,
                                                         self.line).MAIN_LIST( main_string )
                    if self.error is None:
                        self._return_ = self.num
                    else: pass
                else: self.error = ERRORS( self.line ).ERROR0( main_string )

            else: pass
        elif self.type in [ 'tuple' ]                   :
            if type( self.master ) == type( dict() ):
                self.lists = list( self.master.keys() )
                if 'values' not in self.lists:
                    self.num, self.error = get_tuple.TUPLE(self.master, self.data_base,
                                                           self.line).MAIN_TUPLE( main_string )
                    if self.error is None:
                        self._return_ = self.num
                    else:
                        self.error = self.error

                else:
                    self.error = ERRORS(self.line).ERROR0( main_string )

            else:
                pass
        elif self.type in [ 'string' ]                  :
            if type( self.master ) == type( dict() ):
                self.lists = list( self.master.keys() )
                if 'values' not in self.lists:
                    self.num, self.error = get_string.STRING(self.master, self.data_base,
                                                             self.line).MAIN_STRING( main_string )
                    if self.error is None: self._return_ = self.num
                    else: pass
                else: self.error = ERRORS(self.line).ERROR0( main_string )
            else:  pass
        elif self.type in [ 'none' ]                    :
            if type( self.master ) == type( dict() ):
                self.lists = list( self.master.keys() )
                if 'values' not in self.lists:
                    self.num, self.error = get_none.NONE(self.master, self.data_base,
                                                         self.line).MAIN_NONE( main_string )
                    if self.error is None:  self._return_ = self.num
                    else: pass
                else: self.error = ERRORS(self.line).ERROR0( main_string )
            else: pass
        elif self.type in [ 'boolean' ]                 :
            if type( self.master ) == type( dict() ):
                self.lists = list( self.master.keys() )
                if 'values' not in self.lists:
                    self.num, self.error = get_boolean.BOOLEAN(self.master, self.data_base,
                                                               self.line).MAIN_BOOLEAN( main_string )
                    if self.error is None:
                        self._return_ = self.num
                    else:
                        self.error = self.error

                else:
                    self.error = ERRORS(self.line).ERROR0( main_string )

            else:
                pass
        elif self.type in [ 'function' ]                :

            #print( self.master)
            self.num, _, e, self.error = func.FUNCTION_TREATMENT( self.master, self.data_base,
                                                  self.line ).TREATMENT( main_string, self.master )
            if self.error is None:
                if not  _ :
                    self._return_ = self.num
                    if self.master[ 'add_params' ] is None: pass 
                    else:
                        self.num, self.error = func.FUNCTION_TREATMENT( self.master, self.data_base,
                                                  self.line ).TOTAL_TREATMENT( self._return_, typ = 'def' )
                        if self.error is None: self._return_ = self.num 
                        else: pass
                else:
                    self.error = _[ 0 ]
                    if self.error is None: pass 
                    else: self.data_base[ 'no_printed_values' ] = []
                
                
            else: pass
        elif self.type in [ 'class' ]                   :
            
            self.num, _ , e, self.error = classInit.CLASS_TREATMENT( self.master, self.data_base,
                                                  self.line ).FINAL_TREATEMENT()#TREATMENT( )
            if self.error is None:
                if not  _ :
                    self._return_ = self.num
                    if self.master[ 'add_params' ][ -1 ] is None: pass 
                    else:
                        self.num, self.error = func.FUNCTION_TREATMENT( self.master, self.data_base,
                                                  self.line ).TOTAL_TREATMENT( self._return_, typ = 'class' )
                        if self.error is None: self._return_ = self.num 
                        else: pass
                else:
                    self.error = _[ 0 ]
                    if self.error is None: pass 
                    else: self.data_base[ 'no_printed_values' ] = []
            else: pass
        else:pass
        
        if name == 'cython':
            self._return_ = [ self._return_ ]
            if self.error is None: self.error = ""
            else: pass 
        else: pass
        
        return self._return_, self.error

class FINAL_VALUE:
    def __init__(self, master: list, data_base: dict, line: int, logical: list):
        self.master         = master
        self.logical        = logical
        self.line           = line
        self.data_base      = data_base
        self.orange         = bm.fg.rbg(252, 127, 0 )
        self.cyan           = bm.fg.cyan_L
        self.red            = bm.fg.red_L
        self.green          = bm.fg.rbg(0, 255, 0)
        self.yellow         = bm.fg.rbg(255, 255, 0)
        self.magenta        = bm.fg.magenta_M
        self.white          = bm.fg.white_L
        self.blue           = bm.fg.blue_L
        self.reset          = bm.init.reset

    def FINAL_VALUE(self, _key_=False):
        self._return_       = None
        self.error          = None
        self.number         = None

        for i, value in enumerate( self.master ):
            if self.logical[ i ] is None:
                self._return_ = value
            else:
                if   len( self.logical[ i ] ) == 1:
                    if self.logical[ i ][ 0 ] is not None:
                        if self.logical[ i ][ 0 ] not in [ '?', 'not' ]:
                            value = value
                        else:
                            value = value[ 0 ]
                        self._return_, self.error = FINAL_VALUE( value, self.data_base,  self.line, self.logical,
                                                                 ).LOGICAL_OPERATION( self.logical[ i ][ 0 ], _key_=_key_ )
                        if self.error is None:
                            self._return_ = self._return_
                        else:
                            self.error = self.error
                            break
                    else:
                        self._return_ = value[ 0 ]

                elif len( self.logical[ i ])  == 2:
                    self._op_   = None
                    for k, op in enumerate( self.logical[ i ] ):
                        if op == '?':
                            self._value_, self.error = FINAL_VALUE( value[ k ], self.data_base, self.line, self.logical
                                                            ).LOGICAL_OPERATION( self.logical[ i ][ k ],_key_=_key_  )
                            if self.error is None:
                                value[ k ] = self._value_

                            else:
                                self.error = self.error
                                break
                        else:
                            self._op_ = op

                    if self.error is None:
                        self._return_, self.error = FINAL_VALUE(value, self.data_base, self.line, self.logical
                                                                ).LOGICAL_OPERATION( self._op_, _key_=_key_  )
                    else:
                        self.error = self.error
                        break

                elif len( self.logical [ i ]) == 3:
                    self._op_       = '?'
                    self._value_    = [ value[ 0 ], value[ -1 ]]
                    for k, val in enumerate( self._value_ ):
                        self._val_, self.error = FINAL_VALUE( val, self.data_base, self.line, self.logical
                                                                ).LOGICAL_OPERATION( self._op_, _key_=_key_  )
                        if self.error is None:
                            self._value_[ k ] = self._val_
                        else:
                            self.error = self.error
                            break
                    if self.error is None:
                        self._op_ = '=='
                        self._return_, self.error = FINAL_VALUE(self._value_, self.data_base, self.line, self.logical
                                                                        ).LOGICAL_OPERATION( self._op_, _key_=_key_  )
                    else:
                        self.error = self.error
                        break

        return self._return_, self.error
    def LOGICAL_OPERATION(self, operator: str, _key_=False):
        self._return_       = None
        self.error          = None
        self.all_type       = [ type(int()), type(bool()), type(float()) ]

        try:
            if operator == '==':
                self._return_ = self.master[ 0 ] == self.master[ 1 ]
            elif operator == '>=':
                self._return_ = self.master[ 0 ] >= self.master[ 1 ]
            elif operator == '<=':
                self._return_ = self.master[ 0 ] <= self.master[ 1 ]
            elif operator == '!=':
                self._return_ = self.master[ 0 ] != self.master[ 1 ]
            elif operator == '>':
                self._return_ = self.master[ 0 ] > self.master[ 1 ]
            elif operator == '<':
                self._return_ = self.master[ 0 ] < self.master[ 1 ]
            elif operator == 'in':
                if type(self.master[ 1 ] ) in [ type( list() ), type( str( ) ), type( tuple() ) ]:
                    self._return_ = self.master[ 0 ] in self.master[ 1 ]
                else:
                    self.error = ERRORS( self.line ).ERROR6( self.master[ 1 ] )
            elif operator == 'not in':
                if type(self.master[ 1 ] ) in [ type( list() ), type( str( ) ), type( tuple() ) ]:
                    self._return_ = self.master[ 0 ] not in self.master[ 1 ]
                else:
                    self.error = ERRORS( self.line ).ERROR6( self.master[ 1 ] )

            elif operator == 'is':
                self._return_ = self.master[ 0 ] is self.master[ 1 ]
            elif operator == 'is not':
                self._return_ = self.master[ 0 ] is not self.master[ 1 ]
            elif operator == 'not':
                self._return_ = not self.master
            elif operator == '?':
                self._return_ = FINAL_VALUE( self.master, self.data_base, self.line, None ).CONVERSION()
                self.data_base['irene'] = True

        except TypeError:
            ob1 = FINAL_VALUE(self.master[ 0 ], self.data_base, self.line, None).CONVERSION()
            ob2 = FINAL_VALUE(self.master[ 1 ], self.data_base, self.line, None).CONVERSION()

            if _key_ is False:
                if operator in [ '==', '!=', '<=', '>=', '<', '>']:
                    if type( self.master[ 0 ] ) in [ type( tuple() ), type( list())]:
                            if type( self.master[ 1 ] ) in self.all_type:
                                self._return_, self.number, self.error = FINAL_VALUE(self.master[ 0 ], self.data_base,
                                                                    self.line,  operator ).GET_DATA( self.master[ 1 ] )
                            else:
                                self.error = ERRORS(self.line).ERROR7(operator, ob1, ob2)
                    else:
                        self.error = ERRORS( self.line ).ERROR7( operator, ob1, ob2 )
                else:
                    self.error = ERRORS( self.line ).ERROR7( operator, ob1, ob2 )
            else:
                if self.master[ 0 ] in self.all_type:
                    if self.master[ 1 ] in self.all_type:
                        pass
                    else:
                        self.error = ERRORS( self.line ).ERROR7( operator, ob1, ob2 )
                else:
                    self.error = ERRORS( self.line ).ERROR7( operator, ob1, ob2 )

        return self._return_, self.error
    def BOOLEAN_OPERATION(self, operator: str):
        self._return_           = None

        for i, value in enumerate( self.master ):
            if value == True:
                self.master[ i ] = 1
            elif value == False:
                self.master[ i ] = 0
            else:
                self.master[ i ] = 1

        self._return_   = self.master[ 0 ]
        self.master     = self.master[ 1 : ]

        for i, op in enumerate( operator ):
            if op == 'or':
                self._return_ += self.master[ i ]
            elif op == 'and':
                self._return_ *= self.master[ i ]

        if self._return_ != 0:
            self._return_ = True
        else:
            self._return_ = False

        return self._return_
    def CONVERSION(self):
        self._return_       = None
        self.all_Float      = [ numpy.float16, numpy.float32, numpy.float64 ]
        self.all_Int        = [ numpy.int8, numpy.int16, numpy.int32, numpy.int64 ]

        if   type( self.master ) == type( int() )       :   self._return_ = '{}{}integer(){}'.format(bm.fg.blue, self.red, bm.fg.blue)
        elif type( self.master ) == type( float() )     :   self._return_ = '{}{}float(){}'.format(bm.fg.blue, self.green, bm.fg.blue)
        elif type( self.master ) == type( bool() )      :   self._return_ = '{}{}boolean(){}'.format(bm.fg.blue, self.cyan, bm.fg.blue)
        elif type( self.master ) == type( complex() )   :   self._return_ = '{}{}complex(){}'.format(bm.fg.blue, bm.fg.cyan, bm.fg.blue)
        elif type( self.master ) == type( list() )      :   self._return_ = '{}{}list(){}'.format(bm.fg.blue, self.yellow , bm.fg.blue)
        elif type( self.master ) == type( tuple() )     :   self._return_ = '{}{}tuple(){}'.format(bm.fg.blue, self.blue, bm.fg.blue)
        elif type( self.master ) == type( dict() )      :   self._return_ = '{}{}dictionary(){}'.format( bm.fg.blue, bm.fg.rbg(186,85,211), bm.fg.blue)
        elif type( self.master ) == type( str() )       :   self._return_ = '{}{}string(){}'.format(bm.fg.blue, bm.fg.rbg(255,140,100 ), bm.fg.blue)
        elif type( self.master ) == type( range( 1 ) )  :   self._return_ = '{}{}range(){}'.format(bm.fg.blue, bm.fg.green_L, bm.fg.blue)
        elif type( self.master ) == type( None )        :   self._return_ = '{}{}none(){}'.format(bm.fg.blue, self.orange, bm.fg.blue)
        elif type( self.master ) in self.all_Float      :   self._return_ = '{}{}float(){}'.format(bm.fg.blue, self.green, bm.fg.blue)
        elif type( self.master ) in self.all_Int        :   self._return_ = '{}{}integer(){}'.format(bm.fg.blue, self.red, bm.fg.blue)
        elif type( self.master ) == type( numpy.array([1])):self._return_ = '{}{}ndarray(){}'.format(bm.fg.blue, bm.fg.rbg(255,165,0), bm.fg.blue)
        elif type( self.master ) == type( pd.DataFrame({'r':[0, 0]})) : self._return_ = '{}{}table(){}'.format(bm.fg.blue, bm.fg.rbg(204,153,255), bm.fg.blue) 
        else:  self._return_ = 'type not found'

        return self._return_+bm.init.reset
    def GET_DATA(self, object: any, out_side:bool = True):
        self._return_       = []
        self.error          = None
        self.number         = []
        self.partial_type   = [ type(list()), type(dict()), type(str()), type(tuple())]

        if self.master:
            for i, val in enumerate( self.master ):
                result = None
                try:
                    if   self.logical == '=='   : result = val ==  object
                    elif self.logical == '>='   : result = val >=  object
                    elif self.logical == '<='   : result = val <=  object
                    elif self.logical == '!='   : result = val !=  object
                    elif self.logical == '<'    : result = val <   object
                    elif self.logical == '>'    : result = val >   object

                    if result is True:
                        self.number.append( i )
                        if out_side is False: self._return_.append( True )
                        else:  self._return_.append( val )
                    else:
                        if out_side is False:  self._return_.append( False )
                        else:  pass

                except TypeError:
                    ob1 = FINAL_VALUE(val, self.data_base, self.line, None).CONVERSION()
                    ob2 = FINAL_VALUE(object, self.data_base, self.line, None).CONVERSION()
                    self.error = ERRORS( self.line ).ERROR7( self.logical, ob1, ob2)
                    break
        else:  self.error = ERRORS( self.line ).ERROR8( self.master )

        if type( self.master ) == type(list()): pass
        else:  self._return_ = tuple( self._return_ )

        return self._return_, self.number, self.error

class COMPLEX_ANALYZE:
    def __init__(self, master: complex, line:int):
        self.master         = master
        self.line           = line

    def COMPLEX(self):
        self.error          = None

        self.real = str(self.master.real)
        self.imag = str(self.master.imag)

        if self.real[ 0 ] in [ '-' ]:
            if self.real[ 1 ] not in [ 'i', 'n' ]:
                if self.imag[ 0 ] in [ '-' ]:
                    if self.imag[ 1 ] not in [ 'i', 'n' ]:
                        pass
                    else:
                        self.error = ERRORS(self.line).ERROR9('complex')
                else:
                    if self.imag[ 0 ] in [ 'i', 'n' ]:
                        self.error = ERRORS(self.line).ERROR9('complex')
                    else:
                        pass
            else:
                self.error = ERRORS(self.line).ERROR9('complex')

        else:
            if self.real[ 0 ] in [ 'i', 'n' ]:
                self.error = ERRORS(self.line).ERROR9('complex')
            else:
                if self.imag[ 0 ] in [ '-' ]:
                    if self.imag[ 1 ] not in [ 'i', 'n' ]:
                        pass
                    else:
                        self.error = ERRORS(self.line).ERROR9('complex')
                else:
                    if self.imag[ 0 ] in [ 'i', 'n' ]:
                        self.error = ERRORS(self.line).ERROR9('complex')
                    else:
                        pass

        return self.master, self.error

class ARRITHMETIC_DEEP_CHECKING:
    def __init__(self, master: any, values: list, operators: list, data_base:dict, line: int):
        self.master             = master
        self.operators          = operators
        self.data_base          = data_base
        self.line               = line
        self.values             = values

    def INIT(self, main_string: str):
        self.error              = None
        self.index              = []
        self.calculations       = []
        self.history_of_op      = ''
        self.numeric            = []

        self.length_of_values   = len( self.values )
        self.length_of_op       = len( self.operators )

        if self.length_of_values > self.length_of_op:
            for k, sub_values in enumerate( self.values ):
                self.sub_values = sub_values

                if type( self.sub_values ) == type( dict() ):
                    self.sub_values     = sub_values
                    self.type           = sub_values[ 'type' ]
                    self._return_, self.error = TYPE( self.master, self.sub_values, self.data_base, self.line,
                                                                                self.type ).TYPE( main_string )
                    if self.error is None:
                        if k != self.length_of_values - 1:
                            self.calculations.append( [ self._return_ ] )
                            self.calculations.append( self.operators[ k ] )

                        else: self.calculations.append( [ self._return_ ] )
                    else: break
                else:
                    self._return_, self.error = ARRITHMETIC_DEEP_CHECKING( self.master, self.sub_values,
                                        self.operators[ 0 ][ k ], self.data_base, self.line).INIT_INIT( main_string )

                    if self.error is None:
                        if k != self.length_of_values - 1:
                            self.calculations.append( [ self._return_[ 0 ] ] )
                            self.calculations.append(self.operators[ k ] )

                        else: self.calculations.append( [ self._return_[ 0 ] ] )
                    else: break

            if self.error is None:
                for string in self.calculations:
                    if type( string ) == type( str() ):
                        self.history_of_op += string
                    else: pass

                self._values_, self.error = mathematics.MAGIC_MATH_BASE(self.calculations, self.data_base,
                                                            self.history_of_op,self.line).MATHS_OPERATIONS()
                if self.error is None:
                    self.numeric.append( self._values_ )
                else: pass
            else: pass
        else:
            if type( self.operators[ 0 ]) == type( list() ):
                self.sign       = '+'
                self.operators  = self.operators

            else:
                self.sign       = self.operators[ 0 ]
                self.operators  = self.operators[ 1 : ]
                self.calculations.append( self.sign )

            for k, sub_values in enumerate( self.values ):
                self.sub_values     = sub_values

                if type( self.sub_values ) == type( dict() ):
                    self.type       = self.sub_values[ 'type' ]
                    self._return_, self.error = TYPE(self.master, self.sub_values, self.data_base, self.line,
                                                                                self.type).TYPE( main_string )
                    
                    if self.error is None:
                        if k != self.length_of_values - 1:
                            if not self.index:
                                try:
                                    print( self.operators[ k ], self.operators, k, self.sign )
                                    self.calculations.append( [ self._return_ ] )
                                    #self.calculations.append( self.operators[ k + 1 ])
                                    self.calculations.append( self.operators[ k ])
                                except IndexError:
                                    self.calculations.append( self.operators[ k ] )
                            else:
                                self.calculations.append( [ self._return_ ] )
                                self.calculations.append( self.operators[ k + self.index[ -1 ] + 1 ])
                        else:  self.calculations.append( [ self._return_ ] )
                    else: break

                else:
                    self._return_   = ''
                    if type( self.operators[ k ] ) == type( list() ):
                        self._return_, self.error = ARRITHMETIC_DEEP_CHECKING(self.master, self.sub_values,
                                            self.operators[ k ], self.data_base, self.line).INIT_INIT( main_string )

                    else:
                        self.idd = 0
                        for s, _op_ in enumerate( self.operators[ k : ] ):
                            if type( _op_ ) == type( list() ):
                                self.idd = s
                                break
                            else: pass

                        self.index.append( self.idd )
                        self._return_, self.error = ARRITHMETIC_DEEP_CHECKING(self.master, self.sub_values,
                                    self.operators[ k + self.idd ], self.data_base, self.line).INIT_INIT( main_string )

                    if self.error is None:
                        self.key = True
                        if k != self.length_of_values - 1:
                            try:
                                self.calculations.append( [ self._return_[ 0 ] ] )
                                self.calculations.append( self.operators[ k + 1 ] )
                            except TypeError:
                                self.calculations.append( [ self._return_[ 0 ] ] )
                                self.calculations.append( self.operators[ k + 2 ] )
                        else: self.calculations.append( [ self._return_[ 0 ] ] )
                    else: break

            if self.error is None:
                for string in self.calculations:
                    if type(string) == type(str()):
                        self.history_of_op += string
                    else:  pass
                self._values_, self.error = mathematics.MAGIC_MATH_BASE(self.calculations, self.data_base,
                                                            self.history_of_op, self.line).MATHS_OPERATIONS()

                if self.error is None: self.numeric.append( self._values_ )
                else: pass
            else: pass

        return self.numeric, self.error

    def INIT_INIT(self,main_string: str):
        self.error              = None
        self.index              = []
        self.calculations       = []
        self.history_of_op      = ''
        self.numeric            = []

        self.length_of_values   = len( self.values )
        self.length_of_op       = len( self.operators )

        if self.length_of_values > self.length_of_op:
            for k, sub_values in enumerate( self.values ):
                self.sub_values = sub_values

                if type( sub_values ) == type( dict() ):
                    self.type   = sub_values[ 'type' ]
                    self._return_, self.error = TYPE( self.master, self.sub_values, self.data_base, self.line,
                                                                                self.type ).TYPE( main_string )
                    if self.error is None:
                        if k != self.length_of_values - 1:
                            self.calculations.append( [ self._return_ ] )
                            self.calculations.append( self.operators[ k ])
                        else: self.calculations.append( [ self._return_ ] )
                    else: break

                else:
                    self._return_, self.error = ARRITHMETIC_DEEP_CHECKING(self.master, self.sub_values,
                                                    self.operators[ k ], self.data_base, self.line).INIT( main_string )

                    if self.error is None:
                        if k != self.length_of_values - 1:
                            self.calculations.append( [ self._return_[ 0 ] ] )
                            self.calculations.append( self.operators[ k ] )
                        else: self.calculations.append( [ self._return_[ 0 ] ] )
                    else: break

            if self.error is None:
                for string in self.calculations:
                    if type( string ) == type( str() ):
                        self.history_of_op += string
                    else: pass

                self._values_, self.error = mathematics.MAGIC_MATH_BASE(self.calculations, self.data_base,
                                                            self.history_of_op, self.line).MATHS_OPERATIONS()
                if self.error is None:
                    self.numeric.append( self._values_ )
                else: pass
            else: pass

        elif self.length_of_values == self.length_of_op:
            if type(  self.operators[ 0 ] ) == type( list() ):
                self.sign       = ''
            else:
                self.sign       = self.operators[ 0 ]
                self.operators  = self.operators[ 1 : ]
                if self.sign in [ '-' ]:
                    self.calculations.append( self.sign )
                else: pass

            for k, sub_values in enumerate( self.values ):
                self.sub_values     = sub_values

                if type( self.sub_values ) == type( dict() ):
                    self.type       = sub_values[ 'type' ]
                    self._return_, self.error = TYPE( self.master, self.sub_values, self.data_base, self.line,
                                                                                self.type ).TYPE( main_string )

                    if self.error is None:
                        if k != self.length_of_values - 1:
                            self.calculations.append( [ self._return_ ] )
                            self.calculations.append( self.operators[ k ] )
                        else: self.calculations.append( [ self._return_ ] )
                    else: break

                else:
                    self._return_, self.error = ARRITHMETIC_DEEP_CHECKING(self.master, self.sub_values,
                                    self.operators[ k ], self.data_base, self.line).INIT( main_string )

                    if self.error is None:
                        if k != self.length_of_values - 1:
                            self.calculations.append( [ self._return_[ 0 ] ] )
                            self.calculations.append( self.operators[ k ] )
                        else: self.calculations.append( [ self._return_[ 0 ] ] )
                    else: break

            if self.error is None:
                for string in self.calculations:
                    if type(string) == type(str()):
                        self.history_of_op += string
                    else: pass

                self._values_, self.error = mathematics.MAGIC_MATH_BASE(self.calculations, self.data_base,
                                                        self.history_of_op, self.line).MATHS_OPERATIONS()

                if self.error is None:
                    self.numeric.append(self._values_)
                else: pass
            else: pass

        else:
            if type( self.operators[ 0 ] ) == type( list() ):
                self.sign       = '+'
                self.operators  = self.operators[ : ]
            else:
                self.sign = self.operators[ 0 ]
                self.operators = self.operators[ 1 : ]
                if self.sign in [ '-' ]:
                    self.calculations.append( self.sign )
                else: pass

            for k, sub_values in enumerate( self.values ):
                self.sub_values             = sub_values

                if type( self.sub_values ) == type( dict() ):
                    self.type               = self.sub_values[ 'type' ]
                    self._return_, self.error    = TYPE( self.master, self.sub_values, self.data_base, self.line,
                                                                                self.type ).TYPE( main_string )

                    if self.error is None:
                        if k != self.length_of_values - 1:
                            try:
                                self.calculations.append( [ self._return_ ] )
                                self.calculations.append( self.operators[ k + 2 ] )
                            except TypeError:
                                self.calculations.append( [ self._return_ ] )
                                self.calculations.append( self.operators[k + 1] )
                            except IndexError:
                                self.calculations.append( [ self._return_ ] )
                                self.calculations.append( self.operators[ k ] )
                        else:
                            self.calculations.append( [ self._return_ ] )
                    else: break
                else:
                    self._return_, self.error = ARRITHMETIC_DEEP_CHECKING(self.master, self.sub_values,
                                                self.operators[ k ], self.data_base, self.line).INIT( main_string )

                    if self.error is None:
                        if k != self.length_of_values - 1:
                            try:
                                self.calculations.append( [ self._return_[ 0 ] ] )
                                self.calculations.append( self.operators[ k + 1 ] )
                            except TypeError:
                                self.calculations.append( [ self._return_[ 0 ] ] )
                                self.calculations.append( self.operators[ k + 2 ] )
                        else:  self.calculations.append( [ self._return_[ 0 ] ] )
                    else: break

            if self.error is None:
                for string in self.calculations:
                    if type( string ) == type( str() ):
                        self.history_of_op += string
                    else: pass

                self._values_ , self.error = mathematics.MAGIC_MATH_BASE( self.calculations, self.data_base,
                                                        self.history_of_op, self.line).MATHS_OPERATIONS()
                if self.error is None:
                    self.numeric.append( self._values_ )
                else: pass
            else: pass

        return self.numeric, self.error

class ERRORS:
    def __init__(self, line):
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

    def ERROR1(self, string: str):
        error = '{}due to {}<< . >> .{}line: {}{}'.format(self.white, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR2(self, string: str):
        error = '{}was not found. {}line: {}{}'.format(ne, we, ke, self.line)
        self.error = '{}{} : {}<< {} >> '.format(ne, 'NameError', ae, string) + error

        return self.error+self.reset

    def ERROR3(self, string: str, _char_ = 'an integer()' ):
        error = '{}is not {}{} {}type. {}line: {}{}'.format(self.white, self.red, _char_, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}<< {}{}{} >> '.format(self.green, self.cyan, string, self.green) + error

        return self.error+self.reset

    def ERROR4(self, string: str, _char_ = 'an integer'):
        error = '{}to  {}{}() {}type. {}line: {}{}'.format(self.white, self.yellow, _char_, self.magenta, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ValueError' ).Errors()+'{}impossible to convert {}<< {} >> '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR5(self, string: list, key: str):
        string = list(string)
        if len(string) <= 4 : 
            pass 
        else:
            a, b, c = string[0], string[2], string[4]
            string  = f"[{a}, ..., {b}, ..., {c}]"
        error = '{}was not found in {}<< {} >>. {}line: {}{}'.format(self.white, self.red, string, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'KeyError' ).Errors()+'{}<< {} >> '.format(self.cyan, key) + error

        return self.error+self.reset

    def ERROR6(self, value):
        error = '{}a tuple(), {}or a string(), {}type. {}line: {}{}'.format(self.cyan, self.magenta, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> {}is not {}a list(), '.format(self.cyan, value, self.white, self.yellow) + error
        return self.error+self.reset

    def ERROR7(self, op, ob1, ob2):
        error = '{}<< {}{} >>, {} and {}<< {}{} >>. {}type. {}line: {}{}'.format(self.white, ob1, self.white, self.magenta, 
                                                    self.white, ob2, self.white, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}<< {}{}{} >> {}not supported between '.format(self.cyan, self.yellow, op, 
                                                                                            self.cyan, self.green) + error
        return self.error+self.reset

    def ERROR8(self, value):
        error = '{}<< EMPTY >>. {}line: {}{}'.format(self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}<< {} >> {}is '.format(self.cyan, value, self.white) + error
        return self.error+self.reset

    def ERROR9(self, string: str = 'float' ):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'OverFlowError' ).Errors()+'{}infinity {}{} {}number. '.format(self.yellow, self.magenta, string, 
                                                                                                   self.green) + error

        return self.error+self.reset

class CHECK:
    def __init__(self, operators : list):
        self.op = operators 
    def CHECK(self):
        self.key = []
        self.doubleCheck = False
        
        for i, op in enumerate(self.op):
            if op is None: 
                self.key.append((i, False))
                if self.doubleCheck is True: pass 
                else: pass
            else: 
                self.key.append((i, True))
                self.doubleCheck = True
        
        return self.key, self.doubleCheck
