from script                                     import control_string
from script.PARXER.LEXER_CONFIGURE              import numeric_lexer
from script.STDIN.LinuxSTDIN                    import bm_configure as bm
from CythonModules.Windows                      import fileError as fe 
import numpy as np

class EXTERNAL_BLOCKS:
    def __init__(self, 
                string         : str,         # concatenated string 
                normal_string  : str,         # normal string 
                data_base      : dict,        # data base
                line           : int          # current line 
                ):
        
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_parxer     = numeric_lexer

    def BLOCKS(self, 
               tabulation   : int,          # tabulation number
               function     : any  = None,  # function type ('loop', 'conditional', 'def', 'class')
               inter        : bool = False  # interpreter 
               
               ):
        
        self.tabulation                 = tabulation
        self.back_end                   = self.tabulation - 1
        self._return_                   = None
        self.value                      = None
        self.error                      = None
        self.s                          = self.string 
        self.string                     = self.string[ self.back_end : ]
        self.normal_string              = self.normal_string[ self.back_end : ]

        try:
            self.string, self.error         = self.control.DELETE_SPACE( self.string )
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )
            if self.error is None:
                try:
                    if   self.normal_string[ : 3 ] == 'end'  :
                        if  self.normal_string[ -1 ] == ':':
                            self.error = EXTERNAL_BLOCKS( self.string, self.normal_string, self.data_base,
                                                          self.line ).END_BLOCK_TREATMENT( )
                            if self.error is None:  self._return_ = 'end:'
                            else:   pass
                        else:   
                            if self.normal_string in [ 'end' ]: self.error = ERRORS(self.line).ERROR1( 'end' )
                            else:   self.error = ERRORS( self.line ).ERROR4()
                            
                    elif self.normal_string[ : 4 ] == 'elif' :
                        if self.normal_string[ - 1 ] == ':':
                            self._value_ , self.error = EXTERNAL_BLOCKS( self.string, self.normal_string,
                                                    self.data_base, self.line ).ELIF_BLOCK_TREATMENT( function, inter = inter )
                            if self.error is None:
                                self._return_   = 'elif:'
                                self.value      = self._value_
                            else:   pass
                        else:   self.error = ERRORS( self.line ).ERROR1( 'elif' )
                    
                    elif self.normal_string[ : 4 ] == 'else' :
                        if self.normal_string[ - 1] == ':':
                            self.error = EXTERNAL_BLOCKS( self.string, self.normal_string,
                                                    self.data_base, self.line ).ELSE_BLOCK_TREATMENT( )
                            if self.error is None:  self._return_ = 'else:'
                            else:   pass
                        else:   self.error = ERRORS( self.line ).ERROR1( 'else')
                          
                    else:   self.error = ERRORS( self.line ).ERROR4()
                    
                except IndexError:  self.error = ERRORS( self.line ).ERROR0( self.normal_string )
            else:
                self._return_   = 'empty'
                self.error      = None
        except IndexError:
            self._return_       = 'empty'
            self.error          = None

        return self._return_, self.value, self.error

    def ELIF_BLOCK_TREATMENT( self, function : any = None, inter : bool = False )     :
        self.error                     = None
        self._return_                  = None
        self.type                      = [ type( int()), type(float()), type(complex())]

        self.new_normal_string         = self.normal_string[4 : -1 ]
        if self.new_normal_string[ 0 ] in [ ' ' ]:
            self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

            if self.error is None:
                self._return_, self.error = self.lex_parxer.NUMERCAL_LEXER( self.new_normal_string,
                                                                    self.data_base, self.line ).LEXER( self.normal_string )
                if self.error is None:
                    if   type( self._return_ ) == type( bool() )                    :   self._return_   = self._return_
                    elif type( self._return_ ) in self.type                         :   self._return_   = True
                    elif type( self._return_ ) in [type( list() ), type( tuple() )] :
                        if len( self._return_ ) == 0 :  self._return_ = False
                        else:                           self._return_ = True
                    elif type( self._return_ ) == type( range( 1 ) )                :   self._return_   = True
                    elif type( self._return_ ) == type( None )                      :   self._return_   = False
                    elif type( self._return_ ) == type( str() )                     :   self._return_   = [ True if self._return_ else False ][ 0 ]
                    elif type( self._return_ ) == type( dict() )                    :   self._return_   = [ True if list( self._return_.keys() ) else False][ 0 ]
                else:
                    if inter is False:
                        if function is None:    pass
                        elif function in [ 'def', 'class', 'loop' ]:
                            self._error_ = fe.FileErrors( self.error  ).initError()
                            if self._error_ not in  [ 'SyntaxError' ] :     self.error = None
                            else:   pass
                    else : pass
            else:   self.error = ERRORS( self.line ).ERROR0( self.normal_string )
        else:   self.error = ERRORS( self.line ).ERROR4()

        return self._return_, self.error

    def ELSE_BLOCK_TREATMENT( self )    :
        self.error                          = None
        self._return_                       = None

        self.new_normal_string              = self.normal_string[ 4 : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None:  self.error  = ERRORS( self.line ).ERROR0( self.normal_string )
        else:   self.error = None

        return self.error

    def END_BLOCK_TREATMENT( self )     :
        self.error                          = None

        self.new_normal_string              = self.normal_string[ 3 : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None:  self.error  = ERRORS( self.line ).ERROR0( self.normal_string )
        else:   self.error = None

        return  self.error

class INTERNAL_BLOCKS:
    def __init__(self, 
                string          : str, 
                normal_string   : str, 
                data_base       : dict, 
                line            : int
                ):
        
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_parxer     = numeric_lexer
        self.chars          = self.control.LOWER_CASE()+self.control.UPPER_CASE()+['_']

    def BLOCKS(self, 
            tabulation  : int,
            function    : any   = None,
            inter       : bool  = False
            ):
        self.tabulation     = tabulation
        self.back_end       = self.tabulation - 1
        self._return_       = None
        self.error          = None
        self.value          = None

        self.string                 = self.string[ self.back_end : ]
        self.normal_string          = self.normal_string[ self.back_end : ]

        try:
            self.string, self.error         = self.control.DELETE_SPACE( self.string )
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                try:
                    if   self.normal_string[ : 2 ] == 'if'    :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS( self.string, self.normal_string,
                                                self.data_base, self.line ).BLOCK_TREATMENT( num = 2, function = function, inter = inter )
                            if self.error is None:
                                self._return_   = 'if:'
                                self.value      = self._value_
                            else:   pass
                        else:  
                            try: 
                                if self.normal_string[ 2 ] in [ ' ' ]:
                                    self.error = ERRORS(self.line).ERROR1( 'if' )
                                else:
                                    self._return_   = 'any'
                                    self.value      = self.normal_string
                            except IndexError: ERRORS(self.line).ERROR1( 'if' )

                    elif self.normal_string[ : 3 ] == 'for'   :
                        pass
                    elif self.normal_string[ : 6 ] == 'unless':
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS( self.string, self.normal_string,
                                                                       self.data_base, self.line ).BLOCK_TREATMENT( num = 6, function = function, inter = inter )
                            if self.error is None:
                                self._return_   = 'unless:'
                                self.value      = self._value_
                            else:   pass
                        else:   self.error = ERRORS(self.line).ERROR1( 'unless' )

                    elif self.normal_string[ : 5 ] == 'until' :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS( self.string, self.normal_string,
                                                                self.data_base, self.line).BLOCK_TREATMENT( num = 5 )
                            if self.error is None:
                                self._return_   = 'until:'
                                self.value      = self._value_
                            else:   pass
                        else:   self.error = ERRORS(self.line).ERROR1( 'until' )

                    elif self.normal_string[ : 5 ] == 'while' :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                            self.data_base, self.line).BLOCK_TREATMENT( num = 5 )
                            if self.error is None:
                                self._return_   = 'while:'
                                self.value      = self._value_
                            else:   pass
                        else:   self.error = ERRORS(self.line).ERROR1( 'while' )

                    elif self.normal_string[ : 6 ] == 'switch':
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                            self.data_base, self.line).BLOCK_TREATMENT(num = 6)
                            if self.error is None:
                                self._return_ = 'switch:'
                                self.value = self._value_
                            else:   pass
                        else:   self.error = ERRORS( self.line ).ERROR1( 'switch' )

                    elif self.normal_string[ : 3  ] == 'try'  :
                        self._return_, self.value, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                            self.data_base, self.line).TRY_BLOCK_TREATMENT( )

                    elif self.normal_string[ : 5  ] == 'begin':
                        self._return_, self.value, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                     self.data_base, self.line).TRY_BLOCK_TREATMENT( num = 5)

                    else:
                        self._return_   = 'any'
                        self.value      = self.normal_string

                except IndexError:  self.error = ERRORS(self.line).ERROR0(self.normal_string)
            else:
                self._return_   = 'empty'
                self.error      = None

        except IndexError:
            self.error      = None
            self._return_   = 'empty'

        return self._return_, self.value, self.error

    def INTERPRETER_BLOCKS(self, tabulation: int, function : any = None):
        self.tabulation     = tabulation
        self.back_end       = self.tabulation - 1
        self._return_       = None
        self.error          = None
        self.value          = None

        self.string                 = self.string[ self.back_end : ]
        self.normal_string          = self.normal_string[ self.back_end : ]

        try:
            self.string, self.error         = self.control.DELETE_SPACE( self.string )
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                try:
                    if   self.normal_string[ : 2 ] == 'if'    :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS( self.string, self.normal_string,
                                                self.data_base, self.line ).BLOCK_TREATMENT( num = 2, function = function )
                            if self.error is None:
                                self._return_   = 'if:'
                                self.value      = self._value_
                            else:   pass
                        else:  
                            try: 
                                if self.normal_string[ 2 ] in [ ' ' ]:
                                    self.error = ERRORS(self.line).ERROR1( 'if' )
                                else:
                                    self._return_   = 'any'
                                    self.value      = self.normal_string
                            except IndexError: ERRORS(self.line).ERROR1( 'if' )

                    elif self.normal_string[ : 3 ] == 'for'   :
                        pass
                    
                    elif self.normal_string[ : 6 ] == 'unless':
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS( self.string, self.normal_string,
                                                                       self.data_base, self.line ).BLOCK_TREATMENT( num = 6 )
                            if self.error is None:
                                self._return_   = 'unless:'
                                self.value      = self._value_
                            else:   pass
                        else:   self.error = ERRORS(self.line).ERROR1( 'unless' )

                    elif self.normal_string[ : 5 ] == 'until' :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS( self.string, self.normal_string,
                                                                self.data_base, self.line).BLOCK_TREATMENT( num = 5 )
                            if self.error is None:
                                self._return_   = 'until:'
                                self.value      = self._value_
                            else:   pass
                        else:   self.error = ERRORS(self.line).ERROR1( 'until' )

                    elif self.normal_string[ : 5 ] == 'while' :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                            self.data_base, self.line).BLOCK_TREATMENT( num = 5 )
                            if self.error is None:
                                self._return_   = 'while:'
                                self.value      = self._value_
                            else:   pass
                        else:   self.error = ERRORS(self.line).ERROR1( 'while' )

                    elif self.normal_string[ : 6 ] == 'switch':
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                            self.data_base, self.line).BLOCK_TREATMENT(num = 6)
                            if self.error is None:
                                self._return_ = 'switch:'
                                self.value = self._value_
                            else:   pass
                        else:   self.error = ERRORS( self.line ).ERROR1( 'switch' )

                    elif self.normal_string[ : 3 ] == 'try'  :
                        self._return_, self.value, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                            self.data_base, self.line).TRY_BLOCK_TREATMENT( )

                    elif self.normal_string[ : 5 ] == 'begin':
                        self._return_, self.value, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                     self.data_base, self.line).TRY_BLOCK_TREATMENT( num = 5)

                    elif self.normal_string[ : 3 ] == 'end'  :
                        if  self.normal_string[ -1 ] == ':':
                            self.error = EXTERNAL_BLOCKS( self.string, self.normal_string, self.data_base,
                                                          self.line ).END_BLOCK_TREATMENT( )
                            if self.error is None:  self._return_ = 'end:'
                            else:   pass
                        else:   
                            if self.normal_string in [ 'end' ]: self.error = ERRORS(self.line).ERROR1( 'end' )
                            else:   self.error = ERRORS( self.line ).ERROR4()
                   
                    elif self.normal_string[ : 4 ] == 'elif' :
                        if self.normal_string[ - 1 ] == ':':
                            self._value_ , self.error = EXTERNAL_BLOCKS( self.string, self.normal_string,
                                                    self.data_base, self.line ).ELIF_BLOCK_TREATMENT( function )
                            if self.error is None:
                                self._return_   = 'elif:'
                                self.value      = self._value_
                            else:   pass
                        else:   self.error = ERRORS( self.line ).ERROR1( 'elif' )
                        
                    elif self.normal_string[ : 4 ] == 'else' :
                        if self.normal_string[ - 1] == ':':
                            self.error = EXTERNAL_BLOCKS( self.string, self.normal_string,
                                                    self.data_base, self.line ).ELSE_BLOCK_TREATMENT( )
                            if self.error is None:  self._return_ = 'else:'
                            else:   pass
                        else:   self.error = ERRORS( self.line ).ERROR1( 'else')
                        
                    else:
                        self._return_   = 'any'
                        self.value      = self.normal_string

                except IndexError:  self.error = ERRORS(self.line).ERROR0(self.normal_string)
            else:
                self._return_   = 'empty'
                self.error      = None

        except IndexError:
            self.error      = None
            self._return_   = 'empty'

        return self._return_, self.value, self.error
        
    def BLOCK_TREATMENT(self, num :int, function : any = None, inter : bool = False ):
        self.error                     = None
        self._return_                  = None
        self.type                      = [ type( int()), type(float()), type(complex())]

        self.new_normal_string         = self.normal_string[ num : -1 ]
        if self.new_normal_string[ 0 ] in [ ' ' ] :
            self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )
            if self.error is None:
                self._return_, self.error = self.lex_parxer.NUMERCAL_LEXER( self.new_normal_string,
                                                                    self.data_base, self.line ).LEXER( self.normal_string )
                if self.error is None:
                    if   type( self._return_ ) == type( bool() )                    :   self._return_   = self._return_
                    elif type( self._return_ ) in self.type                         :   self._return_   = True
                    elif type( self._return_ ) in [type( list() ), type( tuple() )] :
                        if self._return_ :              self._return_ = True
                        else:                           self._return_ = False
                    elif type( self._return_ ) == type( range( 1 ) )                :   self._return_   = True
                    elif type( self._return_ ) == type( None )                      :   self._return_   = False
                    elif type( self._return_ ) == type( str() )                     :   self._return_   = [ True if self._return_ else False ][ 0 ]
                    elif type( self._return_ ) == type( dict() )                    :   self._return_   = [ True if list( self._return_.keys() ) else False][ 0 ]
                else:
                    if inter is False:
                        if function is None:    pass
                        elif function in [ 'def', 'class', 'loop', 'try' ]:
                            self._error_ = fe.FileErrors( self.error  ).initError()
                            if self._error_ not in  [ 'SyntaxError' ] : self.error = None
                            else: pass
                    else: pass
            else:   self.error = ERRORS( self.line ).ERROR0( self.normal_string )
        else:   self.error = ERRORS( self.line ).ERROR0( self.normal_string )

        return self._return_, self.error

    def TRY_BLOCK_TREATMENT( self, num: int = 3):
        self.error                          = None
        self._return_                       = None
        self.key                            = None
        self.new_normal_string              = None
        self.value                          = None
        self.func                           = ['begin' if num == 5 else 'try' ][ 0 ]

        try:
            if self.normal_string[ -1 ] == ':':
                self.key = True
                self.new_normal_string              = self.normal_string[ num : -1 ]
                self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

            else:
                self.key = False
                self.new_normal_string              = self.normal_string[ num : ]
                self.new_normal_string, self.error  = self.control.DELETE_SPACE(self.new_normal_string)

            if self.error is None:
                if self.key is True:    self.error  = ERRORS( self.line ).ERROR0( self.normal_string )
                else:
                    self.value      = self.control.DELETE_SPACE( self.normal_string )
                    self._return_   = 'any'

            else:
                if self.key is True:
                    self.error      = None
                    self._return_   = self.func+':'
                else:   self.error  = ERRORS( self.line ).ERROR1( self.func )

        except IndexError:
            if self.normal_string[ -1 ] == ':':
                self.error      = None
                self._return_   = self.func+':'
            else:   self.error  = ERRORS( self.line ).ERROR1( self.func )

        return self._return_, self.value, self.error

class MAIN_IF:
    def __init__(self, 
                 master         :str,
                 data_base      :int, 
                 line           :int
                 ):
        
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.num_lex            = numeric_lexer
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )

    def BOCKS( self, typ = 'if' ):
        self.error              = None
        self._return_           = None
        self.type               = [ type(int()), type(float()), type(complex()),  np.float16, 
                                    np.float32, np.float64 , np.int8, np.int16, np.int32, np.int64, 
                                    np.complex64, np.complex128, np.complex64 ]
        self.strin              = ''

        if typ == 'if': self.string, self.error = self.control.DELETE_SPACE( self.master[ 2 : -1 ])
        else:  self.string, self.error = self.control.DELETE_SPACE( self.master[ 5 : -1 ])
        
        if self.error is None:
            self._return_, self.error = self.num_lex.NUMERCAL_LEXER( self.string, self.data_base,
                                                                     self.line ).LEXER( self.master )
            if self.error is None:
                if   type( self._return_ ) == type( bool() )                    :   self._return_   = self._return_
                elif type( self._return_ ) in self.type                         :   self._return_   = True
                elif type( self._return_ ) in [type( list() ), type( tuple() )] :
                    if len( self._return_ ) == 0 :  self._return_ = False
                    else:                           self._return_ = True
                elif type( self._return_ ) == type( np.array([1])):
                    if self._return_.size == 0 :    self._return_ = False
                    else:                           self._return_ = True
                elif type( self._return_ ) == type( range( 1 ) )                :   self._return_   = True
                elif type( self._return_ ) == type( None )                      :   self._return_   = False
                elif type( self._return_ ) == type( str() )                     :   self._return_   = [ True if self._return_ else False ][ 0 ]
                elif type( self._return_ ) == type( dict() )                    :   self._return_   = [ True if list( self._return_.keys() ) else False][ 0 ]
            
            else:   pass 
        else:   self.error = ERRORS( self.line ).ERROR0( self.master )

        return self._return_, self.error

class CHECK_VALUES:
    def __init__(self, data_base: dict):
        self.data_base      = data_base

    def BEFORE(self):
        self._return_ = {
            'variables_vars'     : self.data_base[ 'variables' ][ 'vars'][ : ],
            'variables_vals'     : self.data_base[ 'variables' ][ 'values' ][ : ],
            'global_vars'        : self.data_base[ 'global_vars' ][ 'vars' ][ : ],
            'global_vals'        : self.data_base[ 'global_vars' ][ 'values' ][ : ]
        }

        return self._return_

    def AFTER(self):
        self._return_ = {
            'variables_vars'        : self.data_base[ 'variables' ][ 'vars' ][ : ],
            'variables_vals'        : self.data_base[ 'variables' ][ 'values' ][ : ],
            'global_vars'           : self.data_base[ 'global_vars' ][ 'vars' ][ : ],
            'global_vals'           : self.data_base[ 'global_vars' ][ 'values' ][ : ]
        }

        return self._return_

    def UPDATE(self, before: dict, after: dict, error: str):
        self.error                  = error

        if self.error is not None:
            self.values_before          = before[ 'variables_vals' ]
            self.variables_before       = before[ 'variables_vars' ]
            self.global_vars_before     = before[ 'global_vars' ]
            self.global_values_before   = before[ 'global_vals' ]

            self.values_after           = after[ 'variables_vals' ]
            self.variables_after        = after[ 'variables_vars' ]
            self.global_vars_after      = after[ 'global_vars' ]
            self.global_values_after    = after[ 'global_vals' ]

            if self.variables_after:
                for i, vars in enumerate( self.variables_after ):
                    if vars in self.variables_before:
                        self.idd = self.variables_after.index( vars )
                        if self.values_after[ self.idd ] == self.values_before[ self.idd ]:     pass
                        else:   self.values_after[ self.idd ] = self.values_before[ self.idd ]
                    else:
                        self.idd = self.variables_after.index( vars )
                        del self.values_after[ self.idd ]
                        del self.variables_after[ self.idd ]

            else:
                self.values_after       = self.values_after
                self.variables_after    = self.variables_after

            if self.global_vars_after:
                for i, vars in enumerate( self.global_vars_after ):
                    if vars in self.global_vars_before:
                        self.idd = self.global_vars_after.index( vars )

                        if self.global_values_after[ self.idd ] == self.global_values_before[ self.idd ]:   pass
                        else:   self.global_values_after[ self.idd ] = self.global_values_before[ self.idd ]
                    else:
                        self.idd = self.global_vars_after.index( vars )
                        del self.global_values_after[ self.idd ]
                        del self.global_vars_after[ self.idd ]

            else:
                self.global_values_after    = self.global_values_after
                self.global_vars_after      = self.global_vars_after


            self.final_variables        = {
                'vars'                  : self.variables_after,
                'values'                : self.values_after
            }
            self.final_global_vars      = {
                'vars'                  : self.global_vars_after,
                'values'                : self.global_values_after
            }
            self.data_base[ 'variables' ]   = self.final_variables
            self.data_base[ 'global_vars' ] = self.final_global_vars

        else:   pass

        return  self.error

class ERRORS:
    def __init__(self, line: int):
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan, string) + error

        return self.error+self.reset

    def ERROR1(self, string: str = 'else'):
        error = '{}<< : >> {}is not defined at the {}end. {}line: {}{}'.format(self.red, self.white, self.green, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> {}block. '.format(self.white, self.cyan,
                                                                                                                    string, self.yellow) + error

        return self.error+self.reset

    def ERROR4(self):
        self.error =  fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                    self.white, self.yellow, self.line )
        return self.error+self.reset
       

