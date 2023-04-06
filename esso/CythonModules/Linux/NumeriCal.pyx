from script                         import control_string as ctrl
from colorama                       import Fore, Style
from script.LEXER                   import particular_str_selection as pss
from script.STDIN.LinuxSTDIN        import bm_configure as bm

cdef list  String() :
    cdef :
        list type1
        list type2
        list _return_

    type1 = list( "abcdefghijklmnopqrstuvwxyz" )
    type2 = list( "ABCDEFGHIJKLMNOPQRSTUVWXYZ_" )

    _return_ = type1 + type2

    return _return_


cdef tuple ExpValue ( dict DictValue, list variables, list _values_, int line, dict DataBase ) :
    cdef :
        str     error     
        list    operators   = DictValue[ 'operators' ]
        bint    key         = False
        str     FirstPart   = DictValue[ 'values' ][ 0 ]
        list    SecondPart  = DictValue[ 'values' ][ 1 ]
        list    _value_
        str     char1
        int     index
        str     var
        str     string
        long    numeric2
        complex numeric1
        str     sign
        numeric = None

    _value_, error = pss.SELECTION( FirstPart, FirstPart, DataBase, line ).CHAR_SELECTION( '.' )

    if error in [ '', None ]:
        if   len( _value_ ) == 1 :key = False 
        elif len( _value_ ) == 2 :key = True 
        else: errorr = ERRORS( line ).ERROR1( FirstPart )
            
        if error in [ '', None ]:
            char1   = FirstPart

            if type( SecondPart[ 0 ] ) == type( dict()):
                var = SecondPart[ 0 ][ 'numeric' ][ 0 ]
            
                if SecondPart[ 0 ][ 'type' ] is None        :
                        
                    if variables:
                        if var in variables:
                            index       = variables.index( var )
                        
                            if type( _values_[ index ] ) in [ type(int()), type(complex()) ]:
                                string      = FirstPart + operators[ 0 ] + str( _values_[ index ] ) 

                                if type( _values_[ index ] ) == type( int() ):
                                    
                                    try: 
                                        if key is False:
                                            numeric = float( string )
                                        elif key is True:
                                            numeric = float( string )
                                        
                                        numeric, error = FLOAT_ANALYZE( numeric, line ).FLOAT()
                                    except (SyntaxError, ValueError) : 
                                        if key in [ False, True ]:
                                            error = ERRORS( line ).ERROR4( string, 'a float' )
                                        else: pass
                                    except OverflowError:
                                        error = ERRORS( line ).ERROR9( 'float' )

                                else:
                                    
                                    try:
                                        numeric1        = complex( string )
                                        numeric , error = COMPLEX_ANALYZE( numeric1, line ).COMPLEX()

                                    except (SyntaxError, ValueError) :
                                        error = ERRORS( line ).ERROR4( string, 'a complex' )
                                    except OverflowError:
                                        error = ERRORS( line ).ERROR9( 'complex' )

                            else: error = ERRORS( line ).ERROR3( var )

                        else: error = ERRORS( line ).ERROR2( var )

                    else: error = ERRORS( line ).ERROR2( var )

                
                elif SecondPart[ 0 ][ 'type' ] == 'numeric' :

                    _value_, error = pss.SELECTION( var, var, DataBase, line).CHAR_SELECTION( '.' )
                    if error in [ '', None ]:
                        if len( _value_ ) == 1:
                            try: pass
                            except SyntaxError:
                                error = ERRORS( line ).ERROR4( var )
                        
                            if error in ['', None ]:
                                string = FirstPart + operators[ 0 ] + str( int(float( var )) )
                                    
                                try:
                                    if key is False:
                                        numeric = float( string )
                                    elif key is True:
                                        numeric = float( string )
                                    
                                    numeric, error = FLOAT_ANALYZE( numeric, line ).FLOAT()
                                except ( ValueError, SyntaxError):
                                    if key in [ True, False ]:
                                        error = ERRORS( line ).ERROR4( string, 'a float' )
                                    else: pass
                            else: pass 
                        else: error = ERRORS( line ).ERROR1( var )
                    else: pass

                elif SecondPart[ 0 ][ 'type' ] == 'complex' :
                    try:
                        numeric        = complex( var )
                        numeric, error = COMPLEX_ANALYZE(numeric, line).COMPLEX()

                    except (ValueError, SyntaxError):
                        error = ERRORS( line ).ERROR4( var, 'a complex' )

                    if error in ['', None]:
                        string = FirstPart + operators[ 0 ] + str( numeric )
                    
                        try:
                            numeric             = complex( string )
                            numeric, error      = COMPLEX_ANALYZE( numeric, line ).COMPLEX()

                        except (ValueError, SyntaxError):
                            error = ERRORS( line ).ERROR4( string, 'a complex')
                
                    else: pass
           
            elif type( SecondPart[ 0 ] ) == type( list() )  :
                sign        = operators[ 0 ]
                operators   = operators[ 1 : ]
      
        else : pass
    else: pass
    
    return numeric, error 


cdef tuple NumeriCal( dict DictValue, list variables, list _values_, int line, dict DataBase ) :
    cdef :
        str     error       = ''
        str     Value       = DictValue[ 'numeric' ][ 0 ]
        list    TypeOfValue = [ DictValue[ 'type'] ]
        list    Chars       = String()
        list    Lists       = [ '_int_', '_float_', '_complex_', '_string_', '_list_', '_tuple_' ]
        bint    key         = False
        int     index
        list    data
        str     VarName
        numeric = None

    
    if TypeOfValue[ 0 ] in [ None, 'numeric' ]:
        if Value[ 0 ] in Chars:
            VarName, error = ctrl.STRING_ANALYSE( DataBase, line).CHECK_NAME( Value )

            if error in [ '', None ]:
                Value   = VarName
            else:
                if Value in Lists: error = ''
                else: pass


            if error in [ '', None ]:
                if variables:
                    if Value in variables:
                        index       = variables.index( Value )
                        numeric     = _values_[ index ]

                    else: error     = ERRORS( line ).ERROR2( Value )
                else: error         = ERRORS( line ).ERROR2( Value )
            else : pass
        else:
            data, error = pss.SELECTION( Value, Value, DataBase, line).CHAR_SELECTION( '.' )
            
            if error in [ '', None ]:
                if   len( data ) == 1  : key = False
                elif len( data ) == 2  : key = True
                else: error = ERRORS( line ).ERROR1( Value )
                
                if error in [ '', None ]:
                    try:
                        if key is False:
                            if 'e' in Value:
                                numeric         = float( Value )
                                numeric, error  = FLOAT_ANALYZE( numeric, line ).FLOAT()
                            elif 'E' in Value:
                                numeric         = float( Value )
                                numeric, error  = FLOAT_ANALYZE( numeric, line ).FLOAT()
                            else:
                                numeric         = int( float( Value ) )
                        elif key is True:
                            numeric             = float( Value )
                            numeric, error      = FLOAT_ANALYZE( numeric, line ).FLOAT()

                    except ValueError:
                        if   key is False : error = ERRORS( line ).ERROR4( Value )
                        elif key is True  : error = ERRORS( line ).ERROR4( Value, 'a float' )
                    
                    except SyntaxError:
                        if   key is False : error = ERRORS( line ).ERROR4( Value )
                        elif key is True  : error = ERRORS( line ).ERROR4( Value, 'a float' )

                    except OverflowError:
                        error = ERRORS( line ).ERROR9( 'float' )

                else: pass 
            else : pass
    else:
        try:
            numeric         = complex( Value )
            numeric, error  = COMPLEX_ANALYZE( numeric, line ).COMPLEX()

        except ( ValueError, SyntaxError ): error = ERRORS( line ).ERROR4( Value, 'a complex' )
        except OverflowError : error = ERRORS( line ).ERROR9( 'complex' )


    return numeric, error
    
cdef class NUMERICAL:
    cdef public:
        dict DataBase
        dict ListOfValues
        list variables
        list _values_
        int line


    def __init__( self, ListOfValues, DataBase, line ):
        self.ListOfValues           = ListOfValues
        self.DataBase               = DataBase
        self.variables              = self.DataBase[ 'variables' ][ 'vars' ]
        self._values_               = self.DataBase[ 'variables' ][ 'values' ]
        self.line                   = line
        
    
    cpdef CHECK( self ):
        
        cdef list KeysOfValues

        KeysOfValues = list( self.ListOfValues.keys() )

        if 'values' in KeysOfValues:
            return ExpValue( self.ListOfValues, self.variables, self._values_, self.line, self.DataBase )
        else:
            return NumeriCal( self.ListOfValues, self.variables, self._values_, self.line, self.DataBase )


cdef class ERRORS:
    cdef public int line 
    cdef :
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

    
    def __init__( self, line ) :
        self.line    = line 
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


    cdef str ERROR0(self, str string ):
        cdef :
            str err, error

        err     = '{}line: {}{}'.format(self.we, self.ke, self.line)
        error   = '{}{} : invalid syntax in {}<< {} >>. '.format(self.ke, 'SyntaxError', self.ae, string) + err + self.reset

        return error 

    cdef str ERROR1(self, str string):
        err     = '{}due to {}<< . >> .{}line: {}{}'.format(self.ke, self.ne, self.we, self.ke, self.line)
        error   = '{}{} : invalid syntax in {}<< {} >> '.format(self.ke, 'SyntaxError', self.ae, string) + err + self.reset

        return error

    cdef str ERROR2(self, str string ):
        err     = '{}was not found. {}line: {}{}'.format(self.ne, self.we, self.ke, self.line)
        error   = '{}{} : {}<< {} >> '.format(self.ne, 'NameError', self.ae, string) + err + self.reset

        return error
    
    cdef str ERROR3(self, str string, str _char_ = 'an integer()' ):
        err     = '{}is not {}{} {}type. {}line: {}{}'.format(self.te, self.ie, _char_, self.te, self.we, self.ke, self.line)
        error   = '{}{} : {}<< {} >> '.format(self.te, 'TypeError', self.ae, string) + err + self.reset

        return error

    cdef str ERROR4(self, str string, str _char_ = 'an integer'):
        err     = '{}to  {}{}() {}type. {}line: {}{}'.format(self.ve, self.ke, _char_, self.ae, self.we, self.ke, self.line)
        error   = '{}{} : {}impossible to convert {}<< {} >> '.format(self.ve, 'ValueError', self.we, self.ae, string) + err + self.reset

        return error

    cdef str ERROR5(self, str string , str key ):
        err     = '{}was not found in {}<< {} >>. {}line: {}{}'.format(self.ke, self.ne, string, self.we, self.ke, self.line)
        error   = '{}{} : {}<< {} >> '.format(self.ke, 'KeyError', self.ae, key) + err + self.reset

        return error

    cdef str ERROR6(self, value):
        err     = '{}a tuple(), {}or a string(), {}type. {}line: {}{}'.format(self.ie, self.ne, self.te, self.we, self.ke, self.line)
        error   = '{}{} : {}<< {} >> {}is not {}a list(), '.format(self.te, 'TypeError', self.ae, value, self.te, self.ke) + err + self.reset
        
        return error

    cdef ERROR7(self, op, ob1, ob2):
        err     = '{}<< {}{} >>, {} and {}<< {}{} >>. {}type. {}line: {}{}'.format( self.we, ob1, self.we, self.te, self.we, ob2, self.we, self.te, self.we, self.ke, self.line)
        error   = '{}{} : {}<< {}{}{} >> {}not supported between '.format(self.te, 'TypeError', self.ae, self.ke, op, self.ae, self.te) + err + self.reset
        
        return error

    cdef ERROR8(self, value):
        err     = '{}<< EMPTY >>. {}line: {}{}'.format( self.te, self.we, self.ke, self.line)
        error   = '{}{} : {}<< {} >> {}is '.format(self.ke, 'SyntaxError', self.ae, value, self.ke) + err + self.reset
        
        return error

    cdef ERROR9(self, str string = 'float' ):
        err     = '{}line: {}{}'.format(self.we, self.ke, self.line)
        error   = '{}{} : {}infinity {}{} {}number. '.format(self.te, 'OverFlowError', self.ke, self.te, string, self.ke) + err + self.reset

        return error



cdef class COMPLEX_ANALYZE:
    cdef :
        public complex master
        public int line

    def __init__(self, master, line ):
        self.master         = master
        self.line           = line 

    cdef tuple COMPLEX( self ):

        cdef :
            str error 
            str real
            str imag

        real    = str( self.master.real )
        imag    = str( self.master.imag )
        error   = ''

        if real[ 0 ] in [ '-' ]:
            if real[ 1 ] not in [ 'i', 'n' ]:
                if imag[ 0 ] in [ '-' ]:
                    if imag[ 1 ] not in [ 'i', 'n' ]: pass 
                    else: 
                        error = ERRORS( self.line ).ERROR9( 'complex' )
                else :
                    if imag[ 0 ] in [ 'i', 'n' ]:
                        error = ERRORS( self.line ).ERROR9( 'complex' )
                    else : pass
            else: 
                error = ERRORS( self.line ).ERROR9( 'complex' )
        else:
            if real[ 0 ] in [ 'i', 'n' ]:
                error = ERRORS( self.line ).ERROR9( 'complex' )
            else:
                if imag[ 0] in [ '-' ]:
                    if imag[ 1 ] not in [ 'i', 'n' ]: pass 
                    else: 
                        error = ERRORS( self.line ).ERROR9( 'complex' )
                else:
                    if imag[ 0 ] in [ 'i', 'n' ]:
                        error = ERRORS(self.line).ERROR9('complex')
                    else: pass
       
        return self.master, error


cdef class FLOAT_ANALYZE:
    cdef :
        public float master 
        public int line 
  
    def __init__(self, master, line ):
        self.master         = master
        self.line           = line 

    cdef tuple FLOAT( self ):

        cdef :
            str error 
            str real

        real    = str( self.master )
        error   = ''

        if real[ 0 ] in [ '-' ]:
            if real[ 1 ] not in [ 'i', 'n' ]: pass
            else:  error = ERRORS( self.line ).ERROR9( )
        else:
            if real[ 0 ] in [ 'i', 'n' ]:
                error = ERRORS( self.line ).ERROR9( )

            else: pass
       
        return self.master, error