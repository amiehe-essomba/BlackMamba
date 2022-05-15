from script.PARXER          import numeric_value as nv
from colorama               import Fore, Style
from script.MATHS           import mathematics
import NumeriCal  as nc


cdef class ARITHMETIC:
    cdef :
        public dict     master
        public list     Value
        public list     ArithmeticOperators
        public dict     DataBase
        public int      line
    
    cdef :
        list numeric 
        list calculation 

    def __init__( self, master, DataBase, Value, ArithmeticOperators, line ):
        self.line                       = line 
        self.Value                      = Value
        self.master                     = master
        self.numeric                    = []
        self.DataBase                   = DataBase
        self.calculation                = []
        self.ArithmeticOperators        = ArithmeticOperators

    cpdef CHECK( self, str MainString ):

        cdef :
            str     error
            int     i, j 
            int     length
            str     historyOfOperators
            str     sign
            bint    key = False
            operators, _return_ , string, 


        error               = ''
        historyOfOperators  = ''

        for i, operators in enumerate( self.ArithmeticOperators ):
            if operators is None:
                _return_, error = nv.TYPE( self.master, self.Value[ i ][ 0 ], self.DataBase, self.line ,
                                                                self.Value[ i ][ 0 ][ 'type' ] ).TYPE( MainString )
                if error in [ '', None ]:
                    self.numeric.append( _return_ )
                else: break 

            else: 
                if len( self.Value[ i ] ) >  len( operators )  :
                    length  = len( self.Value[ i ] )

                    for j in range( length ) :
                        _return_, error = nv.TYPE( self.master, self.Value[ i ][ j ], self.DataBase, self.line ,
                                                                self.Value[ i ][ j ][ 'type' ] ).TYPE( MainString )
                        
                        if error in [ '', None ]:
                            if j != length - 1:
                                self.numeric.append( [ _return_ ] )
                                self.calculation.append( operators[ j ] )
                            else:
                                self.calculation.append( [ _return_ ] )
                        else : break

                    if error in [ '', None ]:
                        for string in self.calculation:
                            if type( string ) == type( str() ):
                                historyOfOperators += string 
                            else: pass 

                        _return_ , error  = mathematics.MAGIC_MATH_BASE( self.calculations, self.DataBase,
                                                                historyOfOperators, self.line ).MATHS_OPERATIONS( )
                        if error  in [ '', None ]:
                            self.numeric.append( _return_ )
                            self.calculations   = []
                            historyOfOperators  = ''
                        else : break 
                    else: break
                
                elif len( self.Value[ i ] ) == len( operators )  :
                    if type( operators[ 0 ] ) == type( list() ): sign  = '+'
                    else:
                        if len( operators ) == 1: sign   = operators[ 0 ]
                        else: 
                            key = False
                            for string in operators:
                                if type( string ) == type( list( ) ):
                                    key = True
                                    break
                            if key is False: sign = operators[ 0 ]
                            else: sign = ''

                    if sign in [ '-' ]: self.calculations.append( sign )
                    else: pass 

                    length = len( self.Value[ i ] )

                    if len( operators ) == 1:

                        try:
                            _return_, error   = nv.TYPE( self.master, self.Values[ i ][ 0 ], self.DataBase, self.line,
                                                                        self.Values[ i ][ 0 ][ 'type' ] ).TYPE( MainString )
                            if error in [ '', None ]:
                                self.calculations.append( [ _return_ ] )
                            
                                for string in self.calculations:
                                    if type( string ) == type( str() ):
                                        historyOfOperators += string
                                    else: pass 
                                    
                                _return_ , error  = mathematics.MAGIC_MATH_BASE( self.calculations, self.DataBase,
                                                                    historyOfOperators, self.line ).MATHS_OPERATIONS( )
                                if error  in [ '', None ]:
                                    self.numeric.append( _return_ )
                                    self.calculations   = []
                                    historyOfOperators  = ''
                                else : break
                            else : break
                        
                        except TypeError:
                            _return_, error =  ARRITHMETIC_DEEP_CHECKING( self.master, self.Values[ i ][ 0 ],
                                                            operators[ 0 ], self.DataBase, self.line ).INIT( MainString )

                            if error in [ None, '' ]:
                                self.calculations.append( [ _return_[ 0 ] ])
                                for string in self.calculations:
                                    if type( string ) == type( str() ):
                                        historyOfOperators += string
                                    else: pass
                                 
                                _return_, error = mathematics.MAGIC_MATH_BASE( self.calculations,
                                                    self.DataBase, historyOfOperators, self.line ).MATHS_OPERATIONS()

                                if error [ None, '' ]:
                                    self.numeric.append( _return_ )
                                    self.calculations   = []
                                    historyOfOperators  = ''
                                else: break
                            else: break
                            
                    else: 
                        for j in range( length ):
                            if type( self.Value[ i ][ j ] ) == type( dict() ) :
                                _return_, error = nv.TYPE( self.master, self.Value[ i ][ j ] , self.DataBase, self.line,
                                                            self.Value[ i ][ j ][ 'type' ]  ).TYPE( MainString )

                                if error in [ '', None ]:
                                    if j != length - 1:
                                        try:
                                            self.calculations.append( [ _return_ ] )
                                            if self.calculations[ 0 ] == '-':
                                                self.calculations.append( operators[ j + 1 ] )
                                            else:
                                                self.calculations.append( operators[ j + 1 ] )
                                        except TypeError:
                                            self.calculations.append( [ _return_ ] )
                                            self.calculations.append( operators[ j ] )
                                    else: self.calculations.append( [ _return_ ] )
                                else: break
                            
                            else:
                                _return_, error = ARRITHMETIC_DEEP_CHECKING( self.master, self.Values[ i ][ j ],
                                                            operators[ j ], self.DataBase, self.line).INIT( MainString )
                                
                                if error in [ '', None ]:
                                    if j != length - 1:
                                        try:
                                            self.calculations.append( [ _return_[ 0 ] ] )
                                            self.calculations.append( operators[ j + 1 ] )

                                        except TypeError:
                                            self.calculations.append( [ _return_[ 0 ] ] )
                                            self.calculations.append( operators[ j ] )
                                    else: self.calculations.append( [ _return_[ 0 ] ] )
                                else: break
                        
                        if error in ['', None ]:
                            historyOfOperators  = ''
                            for string in self.calculations:
                                if type( string ) == type( str() ):
                                    historyOfOperators += string
                                else: pass

                            _return_, error = mathematics.MAGIC_MATH_BASE( self.calculations,
                                                self.DataBase, historyOfOperators, self.line ).MATHS_OPERATIONS()

                            if error in ['', None ]:
                                self.numeric.append( _return_ )
                                self.calculations   = []
                                historyOfOperators  = ''
                            else: break
                        else: break
                
                else:
                    sign                = ''
                    operators           = operators[ : ]
                    _return_, error     = ARRITHMETIC_DEEP_CHECKING( self.master, self.Value[ i ],
                                                        self.operators, self.DataBase, self.line ).INIT( MainString )

                    if error in [ '', None ]:
                        historyOfOperators  = ''
                        self.calculations.append( [ _return_[ 0 ] ] )
                        for string in self.calculations:
                            if type( string ) == type( str() ):
                                historyOfOperators += string
                            else: pass

                        _return_, error = mathematics.MAGIC_MATH_BASE( self.calculations,
                                            self.DataBase, historyOfOperators, self.line ).MATHS_OPERATIONS( )

                        if error is None:
                            self.numeric.append( self._return_[ 0 ] )
                            self.calculations   = []
                            historyOfOperators  = ''
                        else: break
                    else: break


cdef class ARRITHMETIC_DEEP_CHECKING:
    cdef :
        public list operators 
        public list values 
        public dict master
        public dict DataBase
        public int  line 

    def __init__( self, master, values, operators, DataBase, line):
        self.operators          = operators
        self.values             = values
        self.DataBase           = DataBase
        self.line               = line
        self.master             = master 

    cdef tuple INIT( self, str MainString ):
        cdef :
            str     error
            list    index 
            list    calculations 
            str     historyOfOperators
            list    numeric
            int     lengthValues, lengthOperators 
            int     k , i, idd
            str     sign
            bint    key
            _return_, string, _op_

        error               = ''
        calculations        = []
        index               = []
        numeric             = []
        historyOfOperators  = ''
        lengthValues        = len( self.values )
        lengthOperators     = len( self.operators )


        if lengthValues > lengthOperators:
            for k in range( lengthValues ):
                if type( self.values[ k ] ) == type( dict() ):
                    _return_, error = nv.TYPE( self.master, self.values[ k ], self.DataBase, self.line,
                                                                                self.values[ k ][ 'type' ] ).TYPE( MainString )
                    if error in [ '', None]:
                        if k != lengthValues - 1 :
                            calculations.append( [ _return_ ] )
                            calculations.append( self.operators[ k ] )

                        else: calculations.append( [ _return_ ] )
                    else: break
                else:
                    _return_, error = ARRITHMETIC_DEEP_CHECKING( self.master, self.values[ k ],
                                        self.operators[ 0 ][ k ], self.DataBase, self.line).INIT_INIT( MainString )

                    if error in [ '', None] :
                        if k != lengthValues - 1:
                            calculations.append( [ _return_[ 0 ] ] )
                            calculations.append( self.operators[ k ] )

                        else: calculations.append( [ _return_[ 0 ] ] )
                    else: break
            
            if error in [ '', None]:
                historyOfOperators = ''
                for string in calculations:
                    if type( string ) == type( str() ):
                        historyOfOperators += string
                    else: pass

                _return_, error = mathematics.MAGIC_MATH_BASE( calculations, self.DataBase,
                                                            historyOfOperators ,self.line ).MATHS_OPERATIONS( )
                if error is None:
                    numeric.append( _return_ )
                    historyOfOperators = ''
                else: pass
            else: pass

        else:
            if type( self.operators[ 0 ] ) == type( list() ):
                sign        = '+'
                self.operators   = self.operators[ : ]

            else:
                calculations.append( self.operators[ 0 ] )
                self.operators  = self.operators[ 1 : ]

            for k in range( lengthValues ):
                if type( self.values[ k ] ) == type( dict() ):
                    _return_, error = nv.TYPE( self.master, self.values[ k ], self.DataBase, self.line,
                                                    self.values[ k ][ 'type' ] ).TYPE( MainString )
                    
                    if error in [ '', None ]:
                        if k != lengthValues - 1:
                            if not index:
                                try:
                                    calculations.append( [ _return_ ] )
                                    calculations.append( self.operators[ k + 1 ])
                                except IndexError:
                                    calculations.append( self.operators[ k ] )
                            else:
                                calculations.append( [ _return_ ] )
                                calculations.append( self.operators[ k + index[ -1 ] + 1 ])
                        else:  calculations.append( [ _return_ ] )
                    else: break

                else:
                    if type( self.operators[ k ] ) == type( list() ):
                        _return_, error = ARRITHMETIC_DEEP_CHECKING(self.master, self.values[ k ],
                                            self.operators[ k ], self.DataBase, self.line ).INIT_INIT( MainString )

                    else:
                        idd  = 0
                        for i, _op_ in enumerate( self.operators[ k : ] ):
                            if type( _op_ ) == type( list() ):
                                idd = i
                                break
                            else: pass
                        
                        index.append( idd )
                        _return_, error = ARRITHMETIC_DEEP_CHECKING( self.master, self.values[ k ],
                                    self.operators[ k + idd ], self.DataBase, self.line).INIT_INIT( MainString )
                
                    if error in [ '' , None ]:
                        key = True
                        if k != lengthValues - 1:
                            try:
                                calculations.append( [ _return_[ 0 ] ] )
                                calculations.append( self.operators[ k + 1 ] )

                            except TypeError:
                                calculations.append( [ _return_[ 0 ] ] )
                                calculations.append( self.operators[ k + 2 ] )
                        else:
                            calculations.append( [ _return_[ 0 ] ] )
                    else: break
            
            if error in [ '' , None ]:
                historyOfOperators = ''
                for string in calculations:
                    if type( string ) == type( str() ):
                        historyOfOperators += string
                    else: pass
                _return_, error = mathematics.MAGIC_MATH_BASE( calculations, self.DataBase,
                                                            historyOfOperators, self.line ).MATHS_OPERATIONS( )

                if error in [ '' , None ]:
                    numeric.append( _return_ )
                    historyOfOperators = ''
                else: pass

        
        return numeric, error

    cdef tuple INIT_INIT( self, str MainString ):

        cdef :
            str     error
            list    index 
            list    calculations 
            str     historyOfOperators
            list    numeric
            int     lengthValues, lengthOperators 
            int     k , i
            str     sign
            int     idd 
            bint    key
            _return_, string

        error               = ''
        calculations        = []
        index               = []
        numeric             = []
        historyOfOperators  = ''
        lengthValues        = len( self.values )
        lengthOperators     = len( self.operators )

        if lengthValues > lengthOperators :
            for k in range( lengthValues ):
                if type( self.values[ k ] ) == type( dict() ):
                    _return_, error = nv.TYPE( self.master, self.values[ k ], self.DataBase, self.line,
                                                            self.values[ k ][ 'type' ] ).TYPE( MainString )

                    if error in [ '', None]:
                        if k != lengthValues - 1 :
                            calculations.append( [ _return_ ] )
                            calculations.append( self.operators[ k ] )
                        else: calculations.append( [ _return_ ] )
                    else: break
                else:
                    _return_, error = ARRITHMETIC_DEEP_CHECKING( self.master, self.values[ k ],
                                        self.operators[ k ], self.DataBase, self.line ).INIT_INIT( MainString )

                    if error in [ '', None] :
                        if k != lengthValues - 1:
                            calculations.append( [ _return_[ 0 ] ] )
                            calculations.append( self.operators[ k ] )
                        else: calculations.append( [ _return_[ 0 ] ] )
                    else: break

            if error in [ '', None]:
                historyOfOperators = ''
                for string in calculations:
                    if type( string ) == type( str() ):
                        historyOfOperators += string
                    else: pass

                _return_, error = mathematics.MAGIC_MATH_BASE( calculations, self.DataBase,
                                                            historyOfOperators ,self.line ).MATHS_OPERATIONS( )
                if error is None:
                    numeric.append( _return_ )
                    historyOfOperators = ''
                else: pass
            else: pass

        elif lengthValues == lengthOperators:
            if type(  self.operators[ 0 ] ) == type( list() ):
                sign       = ''
            else:
                if self.operators[ 0 ] in [ '-' ]:
                    calculations.append( self.operators[ 0 ] )
                else: pass
                self.operators  = self.operators[ 1 : ]

            for k in range( lengthValues ):
                if type( self.values[ k ] ) == type( dict() ):
                    _return_, error = nv.TYPE( self.master, self.values[ k ], self.DataBase, 
                                        self.line, self.values[ k ][ 'type' ] ).TYPE( MainString )

                    if error in [ '', None ]:
                        if k != lengthValues - 1:
                            calculations.append( [ _return_ ] )
                            calculations.append( self.operators[ k ] )
                        else: calculations.append( [ _return_ ] )
                    else: break

                else:
                    _return_, error = ARRITHMETIC_DEEP_CHECKING(self.master, self.values[ k ],
                                    self.operators[ k ], self.DataBase, self.line).INIT( MainString )

                    if error in ['', None ]:
                        if k != lengthValues - 1:
                            calculations.append( [ _return_[ 0 ] ] )
                            calculations.append( self.operators[ k ] )
                        else: calculations.append( [ _return_[ 0 ] ] )
                    else: break

            if error in [ '', None ]:
                historyOfOperators = ''
                for string in calculations:
                    if type( string ) == type( str() ):
                        historyOfOperators += string
                    else: pass

                _return_, error = mathematics.MAGIC_MATH_BASE( calculations, self.DataBase,
                                                        historyOfOperators, self.line).MATHS_OPERATIONS( )

                if error in [ '', None ]:
                    numeric.append( _return_ )
                    historyOfOperators = ''
                else: pass
            else: pass
        
        else:
            if type( self.operators[ 0 ] ) == type( list() ):
                sign       = '+'
                self.operators  = self.operators[ : ]
            else:
                if self.operators[ 0 ] in [ '-' ]:
                    calculations.append( self.operators[ 0 ] )
                else: pass
                self.operators  = self.operators[ 1 : ]

            for k in range( lengthValues ):
                if type( self.values[ k ] ) == type( dict() ):
                    _return_, error    = nv.TYPE( self.master, self.values[ k ], self.DataBase, self.line,
                                                                    self.values[ k ][ 'type' ] ).TYPE( MainString )

                    if error in [ '', None ]:
                        if k != lengthValues - 1:
                            try:
                                calculations.append( [ _return_ ] )
                                calculations.append( self.operators[ k + 2 ] )
                            except TypeError:
                                calculations.append( [ _return_ ] )
                                calculations.append( self.operators[k + 1] )
                            except IndexError:
                                calculations.append( [ _return_ ] )
                                calculations.append( self.operators[ k ] )
                        else:
                            calculations.append( [ self._return_ ] )
                    else: break
                else:
                    _return_, error = ARRITHMETIC_DEEP_CHECKING(self.master, self.values[ k ],
                                                self.operators[ k ], self.DataBase, self.line).INIT( MainString )

                    if error in [ '', None] :
                        if k != lengthValues- 1:
                            try:
                                calculations.append( [ _return_[ 0 ] ] )
                                calculations.append( self.operators[ k + 1 ] )
                            except TypeError:
                                calculations.append( [ _return_[ 0 ] ] )
                                calculations.append( self.operators[ k + 2 ] )
                        else:  calculations.append( [ _return_[ 0 ] ] )
                    else: break

            if error in [ '', None]:
                historyOfOperators = ''
                for string in calculations:
                    if type( string ) == type( str() ):
                        historyOfOperators+= string
                    else: pass

                _values_ , serror = mathematics.MAGIC_MATH_BASE( calculations, self.DataBase,
                                                        historyOfOperators, self.line).MATHS_OPERATIONS( )
                if error in [ '', None ]:
                    numeric.append( _return_ )
                    historyOfOperators = ''
                else: pass
            else: pass

        
        return numeric, error


cdef class FINAL_VALUE:
    cdef :
        public list master 
        public dict DataBase
        public list logical
        public int  line 

    def __init__(self, master: list, data_base: dict, line: int, logical: list):
        self.master         = master
        self.logical        = logical
        self.line           = line
        self.data_base      = data_base

    cdef GET_DATA( self , _object_, bint out_side = True) :
        cdef :
            list    _return_ 
            str     error 
            list    number 
            list    partial_type
            int     i
            result

        _return_       = []
        error          = ''
        number         = []
        partial_type   = [ type( list() ), type( dict() ), type( str() ), type( tuple() ) ]

        if self.master:
            for i in range( len( self.master ) ):
                result = None
                try:
                    
                    if   self.logical == '==':          result = self.master[ i ] == _object_
                    elif self.logical == '>=':          result = self.master[ i ] >= _object_
                    elif self.logical == '<=':          result = self.master[ i ] <= _object_
                    elif self.logical == '!=':          result = self.master[ i ] != _object_
                    elif self.logical == '<' :          result = self.master[ i ] <  _object_
                    elif self.logical == '>' :          result = self.master[ i ] >  _object_

                    if result is True:
                        number.append( i )
                        if out_side is False:
                            _return_.append( True )
                        else:
                            _return_.append( self.master[ i ] )
                    else:
                        if out_side is False:
                            _return_.append( False )
                        else: pass

                except TypeError:
                    ob1     = FINAL_VALUE( self.master[ i ], self.DataBase, self.line, self.logical ).CONVERSION( self.master[ i ] )
                    ob2     = FINAL_VALUE( _object_, self.DataBase, self.line, self.logical ).CONVERSION( _object_ )
                    error   = nc.ERRORS( self.line ).ERROR7( self.logical, ob1, ob2)
                    break
        else: error = nc.ERRORS( self.line ).ERROR8( self.master )

        if type( self.master ) == type( list() ):  return _return_, number, error
        else: return tuple( _return_ ), number, error

    cdef str CONVERSION( self, master_init ):
        cdef str _return_
        
        if   type( master_init ) == type( int() )       :   _return_ = '{}{}integer(){}'.format(color.be, color.ne, color.be)
        elif type( master_init ) == type( float() )     :   _return_ = '{}{}float(){}'.format(color.be, color.ve, color.be)
        elif type( master_init ) == type( bool() )      :   _return_ = '{}{}boolean(){}'.format(color.be, color.ae, color.be)
        elif type( master_init ) == type( complex() )   :   _return_ = '{}{}complex(){}'.format(color.be, color.me, color.be)
        elif type( master_init ) == type( list() )      :   _return_ = '{}{}list(){}'.format(color.be, color.ke, color.be)
        elif type( master_init ) == type( tuple() )     :   _return_ = '{}{}tuple(){}'.format(color.be, color.ie, color.be)
        elif type( master_init ) == type( dict() )      :   _return_ = '{}{}dictionary(){}'.format( color.be, color.te, color.be)
        elif type( master_init ) == type( str() )       :   _return_ = '{}{}string(){}'.format(color.be, color.be, color.be)
        elif type( master_init ) == type( range( 1 ) )  :   _return_ = '{}{}range(){}'.format(color.be, color.ge, color.be)
        elif type( master_init ) == type( None )        :   _return_ = '{}{}none(){}'.format(color.be, color.le, color.be)

        return _return_ + color.reset


cdef class color:
    cdef public :
        str ve      
        str ne      
        str te      
        str we      
        str ke      
        str ie      
        str ae      
        str le      
        str be      
        str ge      
        str me      
        str reset   

    
    def __init__( self ) :
        self.ve      = Fore.LIGHTGREEN_EX
        self.ne      = Fore.LIGHTRED_EX
        self.te      = Fore.MAGENTA
        self.we      = Fore.LIGHTWHITE_EX
        self.ke      = Fore.LIGHTYELLOW_EX
        self.ie      = Fore.LIGHTBLUE_EX
        self.ae      = Fore.CYAN
        self.le      = Fore.RED
        self.be      = Fore.BLUE
        self.ge      = Fore.GREEN
        self.me      = Fore.LIGHTCYAN_EX
        self.reset   = Style.RESET_ALL
