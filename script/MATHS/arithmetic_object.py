from script.PARXER                      import numerical_value
from script.PARXER.LEXER_CONFIGURE      import numeric_lexer
from script.STDIN.LinuxSTDIN            import bm_configure as bm
from CythonModules.Linux                import fileError as fe 
from CythonModules.Linux                import making_arr as ma

class ARITHMETICS:

    def __init__(self, data_base:dict, line:int)            :
        self.line           = line
        self.daba_base      = data_base
        self.type1          = [type( int() ), type( float() ), type( complex() ), type( bool() )]
        self.type2          = [type( list() ), type( tuple() )]
        self.type3          = [type( str() )]

    def OBJECT_ADD(self, object1: any, object2: any)        :
        
        self.error          = None
        self.get_type1      = type( object1 )
        self.get_type2      = type( object2 )
        self.result         = None

        if self.get_type1 in self.type1 and self.get_type2 in self.type1                    :                                             
            self.result = object1 + object2
        elif self.get_type1 in self.type3 and self.get_type2 in self.type3                  : 
            self.result = object1 + object2
        elif self.get_type1 in self.type1 and self.get_type2 in [type( list() )]            :                                                    
            if self.get_type1 == type(float() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).AddListFloat( object1 )
            elif self.get_type1 == type( int() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).AddListInt( object1 )
            elif self.get_type1 == type( complex() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).AddListCPLX( object1 )
            elif self.get_type1 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).AddListBool( object1 )           
        elif self.get_type1 in [type( list() )] and self.get_type2 in self.type1            :                                            
            if self.get_type2 == type(float() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).AddListFloat( object2 )
            elif self.get_type2 == type( int() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).AddListInt( object2 )
            elif self.get_type2 == type( complex() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).AddListCPLX( object2 )
            elif self.get_type2 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).AddListBool( object2 )
        elif self.get_type1 in [type( list() )] and self.get_type2 in [type( list() )]      :                                 
            self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).AddListList( object2[ : ] )
        elif self.get_type1 in [type(tuple())] and self.get_type2 in [type(tuple())]        :                                   
            self.result, self.error = ma.Arithmetic( list( object1[ : ] ), self.line ).AddListList( list( object2[ : ] ), ob_type = 'tuple' )
        elif self.get_type1 in self.type3 and self.get_type2 in [type( list() )]            :    
            self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).AddListString( object1, inv = True )
        elif self.get_type1 in [type( list() )] and self.get_type2 in self.type3            :                                             
            self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).AddListString( object2, inv=False )
        else:self.error = self.error = ERROR( self.line ).ERROR2( object1, object2 )

        return self.result, self.error

    def OBJECT_SOUS(self, object1: any, object2: any)       :
        
        self.error          = None
        self.get_type1      = type( object1 )
        self.get_type2      = type( object2 )
        self.result         = None
       
        if self.get_type1 in self.type1 and self.get_type2 in self.type1                    :
            self.result = object1 - object2
        elif self.get_type1 in self.type3 and self.get_type2 in self.type3                  :
            self.result = []
            self.sum    = ''
            for val in object1:
                if val not in object2:
                    self.result.append( val )
                else: pass
            self.result.append( '|' )
            
            for val in object2:
                if val not in object1:
                    self.result.append( val )   
                else: pass

            for val in self.result:
                self.sum += val
            self.result = self.su
        elif self.get_type1 in self.type1 and self.get_type2 in [type( list() )]            :
            if self.get_type1 == type( int() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).SousListInt( object1, inv = True )
            elif self.get_type1 == type( float() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).SousListFloat( object1, inv = True )
            elif self.get_type1 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).SousListBool( object1, inv = True )
            elif self.get_type1 == type( complex() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).SousListCPLX( object1, inv = True )
            else: self.error = ERROR( self.line ).ERROR2( object1, object2)
        elif self.get_type1 in [type( list() )] and self.get_type2 in self.type1            :
            if self.get_type2 == type( int() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).SousListInt( object2, inv = False )
            elif self.get_type2 == type( float() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).SousListFloat( object2, inv = False )
            elif self.get_type2 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).SousListBool( object2, inv = False )
            elif self.get_type2 == type( complex() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).SousListCPLX( object2, inv = False )
            else: self.error = ERROR( self.line ).ERROR2( object1, object2)
        elif self.get_type1 in [type( list() )] and self.get_type2 in [type( list() )]      :
            self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).SousListList( object2[ : ], inv = False )
        elif self.get_type2 in self.type3 and self.get_type1 in [ type( list() ) ]          :
            self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).SousListString( object2, inv = False )
        elif self.get_type2 in [ type( list() ) ] and self.get_type1 in self.type3          :
            self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).SousListList( object1, inv = True )
        elif self.get_type1 in [type(tuple())] and self.get_type2 in [type(tuple())]        :                                   
            self.result, self.error = ma.Arithmetic( list( object1[ : ] ), self.line ).SousListList( list( object2[ : ] ), ob_type = 'tuple', inv = False )
        else: self.error = ERROR( self.line ).ERROR2( object1, object2 )

        return self.result, self.error

    def OBJECT_MUL(self, object1: any, object2: any)        :
        self.error          = None
        self.get_type1      = type( object1 )
        self.get_type2      = type( object2 )
        self.result         = None

        if self.get_type1 in self.type1 and self.get_type2 in self.type1                            :    
            self.result = object1 * object2
        elif self.get_type1 in self.type1 and self.get_type2 in [type( list() )]                    :                                             
            if self.get_type1 == type( int() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).MulListInt( object1 )
            elif self.get_type1 == type( float() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).MulListFloat( object1 )
            elif self.get_type1 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).MulListBool( object1 )
            elif self.get_type1 == type( complex() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).MulListCPLX( object1 )
            else: self.error = ERROR( self.line ).ERROR2( object1, object2) 
        elif self.get_type1 in [ type( list() ) ] and self.get_type2 in self.type1                  :                                             
            if self.get_type2 == type( int() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).MulListInt( object2 )
            elif self.get_type2 == type( float() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).MulListFloat( object2 )
            elif self.get_type2 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).MulListBool( object2 )
            elif self.get_type2 == type( complex() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).MulListCPLX( object2 )
            else: self.error = ERROR( self.line ).ERROR2( object1, object2)
        elif self.get_type1 in [type( int() ), type( bool() ) ] and self.get_type2 in self.type3    :
            self.result = object1 * object2
        elif self.get_type2 in [type( int() ), type( bool() ) ] and self.get_type1 in self.type3    :
            self.result = object1 * object2      
        elif self.get_type1 in self.type3 and self.get_type2 in [ type( list() ) ]                   :
            self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).MulListString( object1  )
        elif self.get_type2 in self.type3 and self.get_type1 in [ type( list() ) ]                   :
            self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).MulListString( object2 )
        elif self.get_type2 in [ type( list() ) ] and self.get_type1 in [ type( list() ) ]           :
            self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).MulListList( object2[ : ] )
        else: self.error =  ERROR( self.line ).ERROR2( object1, object2 )

        return self.result, self.error

    def OBJECT_DIV(self, object1: any, object2: any)        :
        self.error          = None
        self.get_type1      = type( object1 )
        self.get_type2      = type( object2 )
        self.result         = None

        if self.get_type1 in self.type1 and self.get_type2 in self.type1                    :  
            try:
                self.result = object1 / object2
            except ZeroDivisionError:
                self.error = ERROR( self.line ).ERROR4( )
        elif self.get_type1 in self.type1 and self.get_type2 in [ type( list() )]           :
            if self.get_type1 == type( int() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).DivListInt( object1 )
            elif self.get_type1 == type( float() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).DivListFloat( object1 )
            elif self.get_type1 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).DivListBool( object1 )
            elif self.get_type1 == type( complex() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).DivListCPLX( object1 )
            else: self.error = ERROR( self.line ).ERROR2( object1, object2)     
        elif self.get_type1 in [type( list() )] and self.get_type2 in self.type1            : 
            if self.get_type2 == type( int() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).DivListInt( object2 )
            elif self.get_type2 == type( float() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).DivListFloat( object2 )
            elif self.get_type2 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).DivListBool( object2 )
            elif self.get_type2 == type( complex() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).DivListCPLX( object2 )
            else: self.error = ERROR( self.line ).ERROR2( object1, object2)      
        elif self.get_type1 in [ type( list() )] and self.get_type2 in [ type( list() )]    :
            self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).DivListList( object2[ : ] )
        else: self.error = ERROR( self.line ).ERROR2( object1, object2 )

        return self.result, self.error

    def OBJECT_SQUARE(self, object1: any, object2: any)     :
        self.error          = None
        self.get_type1      = type( object1 )
        self.get_type2      = type( object2 )
        self.result         = None

        if self.get_type1 in self.type1 and self.get_type2 in self.type1                    :
            self.result = object1 ** object2
        elif self.get_type1 in self.type1 and self.get_type2 in [ type( list() )]           :
            if self.get_type1 == type( int() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).SquareListInt( object1, inv = True)
            elif self.get_type1 == type( float() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).SquareListFloat( object1, inv = True)
            elif self.get_type1 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).SquareListBool( object1, inv = True)
            elif self.get_type1 == type( complex() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).SquareListCPLX( object1, inv = True)
            else:
                self.error = ERROR( self.line ).ERROR2( object1, object2)
        elif self.get_type1 in [type( list() )] and self.get_type2 in self.type1            : 
            if self.get_type2 == type( int() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).SquareListInt( object2, inv = False)
            elif self.get_type2 == type( float() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).SquareListFloat( object2, inv = False)
            elif self.get_type2 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).SquareListBool( object2, inv = False)
            elif self.get_type2 == type( complex() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).SquareListCPLX( object2, inv = False)
            else:
                self.error = ERROR( self.line ).ERROR2( object1, object2)
        elif self.get_type1 in [ type( list() )] and self.get_type2 in [ type( list() )]    :
            self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).SquareListList( object2[ : ], inv = False)
        else: self.error = ERROR( self.line ).ERROR2( object1, object2 )

        return self.result, self.error

    def OBJECT_MOD(self, object1: any, object2: any)        :
        self.error          = None
        self.get_type1      = type(object1)
        self.get_type2      = type(object2)
        self.result         = None

        if self.get_type1 in self.type1 and self.get_type2 in self.type1                        : 
            try:
                self.result = object1 % object2

            except ZeroDivisionError:
                self.error = ERROR( self.line ).ERROR3( )
            except TypeError:
                self.type1 = type( object1 )
                self.type2 = type( object2 )

                if self.type1 == type( complex() ):
                    if self.type2 == type( complex() ):
                        self.error = ERROR( self.line ).ERROR2( object1, object2 )
                    else:
                        self.result = ARITHMETICS( self.daba_base, self.line ).COMPLEX( object1, object2 )

                else:
                    if self.type2 == type( complex() ) :
                        self.result = ARITHMETICS( self.daba_base, self.line ).COMPLEX( object2, object1 )
        elif self.get_type1 in self.type1 and self.get_type2 in [type( list() )]                :
            
            if self.get_type1 == type( int() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).ModListInt( object1, inv = True)
            elif self.get_type1 == type( float() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).ModListFloat( object1, inv = True)
            elif self.get_type1 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object2[ : ], self.line ).ModListBool( object1, inv = True)
            else:
                self.error = ERROR( self.line ).ERROR2( object1, object2)        
        elif self.get_type1 in [type( list() )] and self.get_type2 in self.type1                :
            
            if self.get_type2 == type( int() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).ModListInt( object2, inv = False)
            elif self.get_type2 == type( float() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).ModListFloat( object2, inv = False)
            elif self.get_type2 == type( bool() ):
                self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).ModListBool( object2, inv = False)
            else:
                self.error = ERROR( self.line ).ERROR2( object1, object2)           
        elif self.get_type1 in [type( list() )] and self.get_type2 in [type( list() )]          :
            self.result, self.error = ma.Arithmetic( object1[ : ], self.line ).ModListList( object2[ : ], inv = False)
        else: self.error = ERROR( self.line ).ERROR2( object1, object2 )

        return self.result, self.error

    def COMPLEX(self, object1: complex, object2: any)       :
        self._string_ = str( object1 )
        self.op     = ''
        self.sous   = ''
        if '-' in self._string_: self.op = '-'
        elif '+' in self._string_: self.op = '+'
        else:self.op = None

        try:
            if '-' == self._string_[ 1 ]:    self.sous = '-'
            else: self.sous = None
        except IndexError: pass

        self.real   = object1.real % object2
        self.img    = object1.imag % object2

        if self.op is None:
            self.imag = str( self.img ) + 'j'
            self.result = complex( self.imag )
        else:
            self.string = ''
            if self.sous is None:
                self.string = str( self.real ) + self.op + str( self.img ) + 'j'
            else:
                self.string = self.sous + str(self.real) + self.op + str(self.img) + 'j'

            self.result = complex( self.string )

        return self.result

class ERROR:
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

    def ERROR0(self, value):
        error = '{}type. {}line: {}{}'.format(self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError').Errors()+'{}<< {} >> {}is not {}a string() '.format(self.cyan, value, self.white, self.blue) + error
        return self.error+self.reset

    def ERROR1(self, value):
        error = '{}a float(), {}a complex(), {}or a boolean(), {}type. {}line: {}{}'.format(self.green, self.cyan, self.magenta, self.yellow, 
                                                                                            self.white, self.yellow, self.line)    
        self.error = fe.FileErrors( 'TypeError').Errors()+'{}<< {} >> {}is not {}an integer(), '.format(self.cyan, value, self.white, self.red ) + error 
        return self.error+self.reset

    def ERROR2(self, type1: any, type2: any):
        
        
        type11 = numerical_value.FINAL_VALUE( type1, {}, self.line, None ).CONVERSION()
        type22 = numerical_value.FINAL_VALUE( type2, {}, self.line, None ).CONVERSION()
        
        type1, type2 = ERROR( self.line ).TYPE( type1, type2)
        
        error = '{}unsupported operand between {}<< {}{} : {} >> {} and {}<< {}{} : {} >>. {}line: {}{}'.format(self.yellow, self.white, type11, self.white, type1,
                                                    self.yellow, self.white, type22, self.white, type2, self.white, self.yellow, self.line )
        self.error = fe.FileErrors( 'ArithmeticError' ).Errors()  + error
        return self.error+self.reset 

    def ERROR3(self):
        self.error = fe.FileErrors( 'ZeroDivisionError' ).Errors() +'{}modulo by zero. {}line: {}{}'.format(self.yellow, self.white, 
                                                                                                            self.yellow, self.line)
        return self.error+self.reset

    def ERROR4(self):
        self.error = fe.FileErrors( 'ZeroDivisionError' ).Errors() +'{}division by zero. {}line: {}{}'.format(self.yellow, self.white, 
                                                                                                            self.yellow, self.line)
        return self.error+self.reset

    def ERROR5(self, value):
        error = '{} is negative. {}line: {}{}'.format(self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'DomainError' ).Errors() + '{}<< {} >>'.format( self.cyan, value) + error
        return self.error+self.reset


    def TYPE(self, object1: any, object2: any ):
        result1 = None 
        result2 = None 
        
        if type( object1 ) in [ type( list() ), type( tuple()) ]:
            if len( object1 ) < 4 : result1 = object1
            else: 
                if type( object1 ) in [ type( list() ) ] :
                    result1 = f'[{object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]}]'
                else:
                    result1 = f'({object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]})'
        elif type( object1 ) == type( str() ):
            if object1:
                if len( object1 ) < 6: pass 
                else:
                    result1 = object1[ : 2] + ' ... ' + object1[ -2 : ]
            else: pass
        else: result1 = object1
        
        if type( object2 ) in [ type( list() ), type( tuple()) ]:
            if len( object2 ) < 4 : result2 = object2
            else: 
                if type( object2 ) in [ type( list() ) ] :
                    result2 = f'[{object2[0]}, {object2[1]}, ....., {object2[-2]}, {object2[-1]}]'
                else:
                    result2 = f'({object1[0]}, {object1[1]}, ....., {object1[-2]}, {object1[-1]})'
        elif type( object2 ) == type( str() ):
            if object2:
                if len( object2 ) < 6: pass 
                else:
                    result2 = object2[ : 2 ] + ' ... ' + object2[ -2 : ]
            else: pass
      
        else: result2 = object2
                
        return result1, result2