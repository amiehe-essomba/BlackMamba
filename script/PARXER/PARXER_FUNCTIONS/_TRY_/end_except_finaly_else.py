from script                                         import control_string
from script.PARXER.LEXER_CONFIGURE                  import numeric_lexer
from script.LEXER                                   import particular_str_selection
from script.STDIN.LinuxSTDIN                        import bm_configure as bm
from script.PARXER.PARXER_FUNCTIONS.FUNCTIONS       import def_end
try:
    from CythonModules.Windows                      import fileError as fe 
except ImportError:
    from CythonModules.Linux                        import fileError as fe 
    

class EXTERNAL_BLOCKS:
    def __init__(self, string: str, normal_string, data_base: dict, line: int):
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_parxer     = numeric_lexer
        self.selection      = particular_str_selection

    def BLOCKS(self, tabulation: int)   :
        self.tabulation                 = tabulation
        self.back_end                   = self.tabulation - 1
        self._return_                   = None
        self.value                      = None
        self.error                      = None
        self.string                     = self.string[ self.back_end : ]
        self.normal_string              = self.normal_string[ self.back_end : ]

        try:
            self.string, self.error         = self.control.DELETE_SPACE( self.string )
            self.normal_string, self.error  = self.control.DELETE_SPACE( self.normal_string )

            if self.error is None:
                try:
                    if   self.normal_string[ : 3 ] == 'end'    :
                        if  self.normal_string[ -1 ] == ':':
                            self.error = EXTERNAL_BLOCKS( self.string, self.normal_string, self.data_base,
                                                          self.line ).END_BLOCK_TREATMENT( )
                            if self.error is None: self._return_ = 'end:'
                            else:  self.error = self.error
                        else:  self.error = ERRORS(self.line).ERROR1( 'end' )
                    elif self.normal_string[ : 6 ] == 'except' :
                        if self.normal_string[ - 1 ] == ':':
                            self._value_ , self.error = EXTERNAL_BLOCKS( self.string, self.normal_string,
                                                    self.data_base, self.line ).EXCEPT_BLOCK_TREATMENT()

                            if self.error is None:
                                self._return_   = 'except:'
                                self.value      = self._value_
                            else: pass
                        else: self.error = ERRORS( self.line ).ERROR1( 'except' )
                    elif self.normal_string[ : 7 ] == 'finally':
                        if self.normal_string[ - 1] == ':':
                            self.error = EXTERNAL_BLOCKS( self.string, self.normal_string,
                                                    self.data_base, self.line ).FINALLY_BLOCK_TREATMENT()
                            if self.error is None: self._return_ = 'finally:'
                            else: self.error = self.error
                        else: self.error = ERRORS( self.line ).ERROR1( 'else')
                    else: self.error = ERRORS( self.line ).ERROR4()
                except IndexError: pass
                    #self.error = ERRORS( self.line ).ERROR0( self.normal_string )
            else:
                self._return_ = 'empty'
                self.error = None
        except IndexError:
            self._return_ = 'empty'
            self.error = None

        return self._return_, self.value, self.error

    def EXCEPT_BLOCK_TREATMENT(self)    :
        self.error                     = None
        self._return_                  = None
        self.exception_names = ['SyntaxError', 'ValueError', 'EOFError', 'OSError',
                                'KeyError','NameError', 'TypeError', 
                                'ArithmeticError','IndexError', 'FileModeError',
                                'OverFlowError', 'AttributeError','ModuleError',
                                'DomainError','ModuleLoadError', 'FileError',
                                'ExceptionNameError', 'EncodingError', 
                                'IndentationError', 'ZeroDivisionError', 'DecodingError',
                                'UnicodeError', 'DirectoryNotFoundError', 'FileNotFoundError',
                                'CircularLoadingError'
                                ]

        self.new_normal_string         = self.normal_string[6 : -1 ]
        
        if self.new_normal_string != '':
            if self.new_normal_string[ 0 ] in [ ' ' ]:
                self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )
                if self.error is None:
                    self.all_exceptions , self.error = self.selection.SELECTION( self.new_normal_string,
                                                self.new_normal_string, self.data_base, self.line).CHAR_SELECTION( ',' )
                    if self.error is None:
                        for i, _exceptions_ in enumerate( self.all_exceptions):
                            self.name, self.error = self.control.DELETE_SPACE( _exceptions_ )
                            if self.error is None:
                                self.name, self.error = self.control.CHECK_NAME( self.name )
                                if self.error is None:
                                    self.all_exceptions[ i ] = self.name
                                else:break
                            else:
                                self.error = ERRORS( self.line ).ERROR0( self.new_normal_string )
                                break

                        if self.error is None:
                            for i, _exceptions_ in enumerate( self.all_exceptions ):
                                if _exceptions_ in self.exception_names: pass
                                    #self.all_exceptions[ i ] = EXCEPTION_TRANSFORM( _exceptions_ ).GET_EXCEPTION()
                                else:
                                    self.error = ERRORS(self.line).ERROR5( _exceptions_ )
                                    break

                            if self.error is None:
                                if len( self.all_exceptions ) == 1: self._return_ = self.all_exceptions[ 0 ]
                                else: self._return_ = tuple( self.all_exceptions )
                            else: pass
                        else: pass
                    else: pass
                else:
                    self.error = None
                    self._return_ = self.exception_names[ : ]
            else: self.error = ERRORS( self.line ).ERROR4()
        else: self._return_ = self.exception_names[ : ]
            
        return self._return_, self.error

    def ELSE_BLOCK_TREATMENT(self)      :
        self.error                          = None
        self._return_                       = None

        self.new_normal_string              = self.normal_string[ 4 : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None: self.error   = ERRORS( self.line ).ERROR0( self.normal_string )
        else: self.error = None

        return self.error

    def END_BLOCK_TREATMENT(self)       :
        self.error                          = None

        self.new_normal_string              = self.normal_string[ 3 : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None: self.error   = ERRORS( self.line ).ERROR0( self.normal_string )
        else: self.error = None

        return  self.error

    def FINALLY_BLOCK_TREATMENT(self)   :
        self.error                          = None

        self.new_normal_string              = self.normal_string[ 7 : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None:
            self.error = ERRORS( self.line ).ERROR0( self.normal_string )
        else: self.error = None

        return  self.error

class INTERNAL_BLOCKS:
    def __init__(self, string: str, normal_string, data_base: dict, line: int):
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_parxer     = numeric_lexer

    def BLOCKS(self, tabulation: int, inter : bool = False):
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
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                self.data_base, self.line).BLOCK_TREATMENT( num = 2, function = None )
                            if self.error is None:
                                self._return_   = 'if:'
                                self.value      = self._value_
                            else:
                                self._return_   = 'if:'
                                self.value      = False
                        else:
                            self.error = ERRORS(self.line).ERROR1( 'if' )

                    elif self.normal_string[ : 3 ] == 'for'   :
                        self._return_, self.value, self.error = def_end.INTERNAL_BLOCKS(self.normal_string, self.normal_string,
                                                                   self.data_base, self.line).FOR_BLOCK_TREATMENT( inter = inter)
                        
                    elif self.normal_string[ : 6 ] == 'unless':
                        if self.normal_string[-1] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                                       self.data_base, self.line).BLOCK_TREATMENT( num = 6, function = None )
                            if self.error is None:
                                self._return_   = 'unless:'
                                self.value      = self._value_
                            else:
                                self._return_   = 'if:'
                                self.value      = True
                        else:
                            self.error = ERRORS(self.line).ERROR1( 'unless' )

                    elif self.normal_string[ : 5 ] == 'until' :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS( self.string, self.normal_string,
                                                                self.data_base, self.line).BLOCK_TREATMENT( num = 5, function = None )
                            if self.error is None:
                                self._return_   = 'until:'
                                self.value      = self._value_
                            else:
                                self._return_   = 'if:'
                                self.value      = True
                        else:
                            self.error = ERRORS(self.line).ERROR1( 'until' )

                    elif self.normal_string[ : 5 ] == 'while' :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                            self.data_base, self.line).BLOCK_TREATMENT( num = 5 )
                            if self.error is None:
                                self._return_   = 'while:'
                                self.value      = self._value_
                            else:
                                self._return_   = 'if:'
                                self.value      = False
                        else:
                            self.error = ERRORS(self.line).ERROR1( 'while' )

                    elif self.normal_string[ : 6 ] == 'switch':
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                            self.data_base, self.line).BLOCK_TREATMENT(num = 6, function = None)
                            if self.error is None:
                                self._return_ = 'switch:'
                                self.value = self._value_
                            else:
                                self._return_   = 'if:'
                                self.value      = False
                        else:
                            self.error = ERRORS( self.line ).ERROR1( 'switch' )

                    elif self.normal_string[ : 3  ] == 'try'  :
                        self._return_, self.value, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                            self.data_base, self.line).TRY_BLOCK_TREATMENT( )

                    elif self.normal_string[ : 5  ] == 'begin':
                        self._return_, self.value, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                     self.data_base, self.line).TRY_BLOCK_TREATMENT( num = 5)

                    else:
                        self._return_   = 'any'
                        self.value      = self.normal_string

                except IndexError:
                    self.error = ERRORS(self.line).ERROR0(self.normal_string)
            else:
                self._return_   = 'empty'
                self.error      = None

        except IndexError:
            self.error      = None
            self._return_   = 'empty'

        return self._return_, self.value, self.error

    def BLOCK_TREATMENT(self, num :int, function: any = None):
        
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
                        if len( self._return_ ) == 0 :  self._return_ = False
                        else:                           self._return_ = True
                    elif type( self._return_ ) == type( range( 1 ) )                :   self._return_   = True
                    elif type( self._return_ ) == type( None )                      :   self._return_   = False
                    elif type( self._return_ ) == type( str() )                     :   self._return_   = [ True if self._return_ else False ][ 0 ]
                    elif type( self._return_ ) == type( dict() )                    :   self._return_   = [ True if list( self._return_.keys() ) else False][ 0 ]
                else:
                    
                    if function is None:    pass
                    elif function in [ 'def', 'class', 'for' ]:
                        self._error_ = fe.FileErrors( self.error  ).initError()
                        if self._error_ not in  [ 'SyntaxError' ] : self.error = None
                        else: pass
            else:   self.error = ERRORS( self.line ).ERROR0( self.normal_string )
        else:   self.error = ERRORS( self.line ).ERROR0( self.normal_string )

        return self._return_, self.error
    
    def TRY_BLOCK_TREATMENT(self, num:int = 3):
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
                self.new_normal_string = self.normal_string[ num : ]
                self.new_normal_string, self.error = self.control.DELETE_SPACE(self.new_normal_string)

            if self.error is None:
                if self.key is True: self.error = ERRORS( self.line ).ERROR0( self.normal_string )
                else:
                    self.value = self.control.DELETE_SPACE( self.normal_string )
                    self._return_ = 'any'

            else:
                if self.key is True:
                    self.error = None
                    self._return_ = self.func+':'
                else:  self.error = ERRORS( self.line ).ERROR1( self.func )

        except IndexError:
            if self.normal_string[ -1 ] == ':':
                self.error = None
                self._return_ = self.func+':'
            else: self.error = ERRORS( self.line ).ERROR1( self.func )

        return self._return_, self.value, self.error

class GET_ERROR:
    def __init__(self, master: str, data_base:dict, line:int):
        self.master         = master
        self.line           = line
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )

    def ERROR(self):
        self.string         = ''

        for str_ in self.master:
            if str_ == ':': break
            else: self.string += str_

        self.master, self.error = self.control.DELETE_SPACE( self.string )

        return self.master

"""
class EXCEPTION_TRANSFORM:
    def __init__(self, master):
        self.master         = master

    def GET_EXCEPTION(self):

        if self.master == 'IndexError':
            self.master = '{}{}'.format(ie, self.master )
        elif self.master == 'ValueError':
            self.master = '{}{}'.format(ve, self.master)
        elif self.master == 'NameError':
            self.master = '{}{}'.format(ne, self.master)
        elif self.master == 'AttributeError':
            self.master = '{}{}'.format(ae, self.master)
        elif self.master == 'SyntaxError':
            self.master = '{}{}'.format(ke, self.master)
        elif self.master == 'OverFlowError':
            self.master = '{}{}'.format(te, self.master)
        elif self.master == 'KeyError':
            self.master = '{}{}'.format(ke, self.master)
        elif self.master == 'ArithmeticError':
            self.master = '{}{}'.format(ie, self.master)
        elif self.master == 'IndentationError':
            self.master = '{}{}'.format(ie, self.master)
        elif self.master == 'ExceptionNameError':
            self.master = '{}{}'.format(le, self.master)
        elif self.master == 'ZeroDivisionError':
            self.master = '{}{}'.format(ne, self.master)
        else:
            self.master = '{}{}'.format(me, self.master)


        return self.master
"""

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

                        if self.values_after[ self.idd ] == self.values_before[ self.idd ]:
                            pass
                        else:
                            self.values_after[ self.idd ] = self.values_before[ self.idd ]
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

                        if self.global_values_after[ self.idd ] == self.global_values_before[ self.idd ]:
                            pass
                        else:
                            self.global_values_after[ self.idd ] = self.global_values_before[ self.idd ]
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
            self.data_base[ 'print' ]       = []

        else:
            pass

        return  self.error

class ERRORS:
    def __init__(self, line: int):
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
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >>. '.format(self.white,
                                                                                                       self.cyan, string) + error
        return self.error+self.reset

    def ERROR1(self, string: str = 'else'):
        error = '{}<< : >> {}is not defined at the {}end. {}line: {}{}'.format(self.red, self.white, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+'{}invalid syntax in {}<< {} >> {}block. '.format(self.white, 
                                                                                self.cyan, string, self.white) + error

        return self.error+self.reset

    def ERROR4(self):
        self.error =  fe.FileErrors( 'IndentationError' ).Errors()+'{}unexpected an indented block, {}line: {}{}'.format(self.yellow,
                                                                                    self.white, self.yellow, self.line )
        return self.error+self.reset

    def ERROR5(self, string:str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'ExceptionNameError' ).Errors()+'{}<< {} >>. '.format( self.cyan, string ) + error

        return self.error+self.reset

    def ERROR6(self, value):
        error = '{}a tuple(), {}or a string(), {}type. {}line: {}{}'.format(self.blue, self.cyan, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeError' ).Errors()+'{}<< {} >> {}is not '.format(self.magenta, value, self.white) + error

        return self.error+self.reset