from script                                     import control_string
from script.PARXER.LEXER_CONFIGURE              import numeric_lexer, partial_lexer
from script.PARXER                              import numerical_value
from script.PARXER.PARXER_FUNCTIONS._TRY_       import end_except_finaly_else
from script.STDIN.LinuxSTDIN                    import bm_configure as bm
try:
    from CythonModules.Windows                  import fileError as fe
except ImportError:
    from CythonModules.Linux                    import fileError as fe

class EXTERNAL_BLOCKS:
    def __init__(self, string: str, normal_string, data_base: dict, line: int):
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_parxer     = numeric_lexer

    def BLOCKS(self, tabulation: int):
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
                    if   self.normal_string[ : 3 ] == 'end'  :
                        if  self.normal_string[ -1 ] == ':':
                            self.error = EXTERNAL_BLOCKS( self.string, self.normal_string, self.data_base,
                                                          self.line ).END_BLOCK_TREATMENT( )
                            if self.error is None:  self._return_ = 'end:'
                            else:   self.error = self.error
                        else:   self.error = ERRORS(self.line).ERROR1( 'end' )
                    else:   self.error = ERRORS( self.line ).ERROR4()
                except IndexError:  self.error = ERRORS( self.line ).ERROR0( self.normal_string )
            else:
                self._return_ = 'empty'
                self.error = None

        except IndexError:
            self._return_ = 'empty'
            self.error = None

        return self._return_, self.value, self.error

    def END_BLOCK_TREATMENT( self ):
        self.error                          = None

        self.new_normal_string              = self.normal_string[ 3 : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None:  self.error = ERRORS( self.line ).ERROR0( self.normal_string )
        else:   self.error = None

        return  self.error

class INTERNAL_BLOCKS:
    def __init__(self, string: str, normal_string, data_base: dict, line: int):
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_parxer     = numeric_lexer

    def BLOCKS(self, tabulation: int, class_name :str = '', class_key: bool = False, func_name: str='', loop = None, inter : bool = False):
        self.err            = '{} / {}class {}{}( )'.format( bm.fg.white_L, bm.fg.red_L, bm.fg.blue_L,
                                                                                        class_name)+bm.init.reset
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
                    if self.normal_string[ : 2 ]   == 'if'    :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                self.data_base, self.line).BLOCK_TREATMENT( num = 2)
                            if self.error is None:
                                self._return_   = 'if:'
                                self.value      = self._value_
                            else: pass
                        else: self.error = ERRORS(self.line).ERROR1( 'if' )

                    elif self.normal_string[ : 3 ] == 'for'   :
                        self._return_, self.value, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                                   self.data_base, self.line).FOR_BLOCK_TREATMENT( inter = inter)
                    
                    elif self.normal_string[ : 6 ] == 'unless':
                        if self.normal_string[-1] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                                       self.data_base, self.line).BLOCK_TREATMENT( num = 6 )
                            if self.error is None:
                                self._return_   = 'unless:'
                                self.value      = self._value_
                            else:
                                self.error = self.error
                        else:
                            self.error = ERRORS(self.line).ERROR1( 'unless' )

                    elif self.normal_string[ : 5 ] == 'until' :
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS( self.string, self.normal_string,
                                                                self.data_base, self.line).BLOCK_TREATMENT( num = 5 )
                            if self.error is None:
                                self._return_   = 'until:'
                                self.value      = self._value_
                            else:
                                self.error = self.error
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
                                self.error = self.error
                        else:
                            self.error = ERRORS(self.line).ERROR1( 'while' )

                    elif self.normal_string[ : 6 ] == 'switch':
                        if self.normal_string[ -1 ] == ':':
                            self._value_, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                            self.data_base, self.line).BLOCK_TREATMENT(num = 6)
                            if self.error is None:
                                self._return_ = 'switch:'
                                self.value = self._value_
                            else:
                                self.error = self.error
                        else:
                            self.error = ERRORS( self.line ).ERROR1( 'switch' )

                    elif self.normal_string[ : 3  ] == 'try'  :
                        self._return_, self.value, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                            self.data_base, self.line).TRY_BLOCK_TREATMENT( )

                    elif self.normal_string[ : 5  ] == 'begin':
                        self._return_, self.value, self.error = INTERNAL_BLOCKS(self.string, self.normal_string,
                                                     self.data_base, self.line).TRY_BLOCK_TREATMENT( num = 5)
                    
                    elif self.normal_string[ : 3  ] == 'def'  :
                        if self.normal_string[ 3 ] == ' ':
                            self._return_   = 'def:'
                            self.value      = self.normal_string
                        else:
                            self._return_   = 'any'
                            self.value      = 't'*self.back_end+self.normal_string
                   
                    elif self.normal_string[ : 3]   == 'end'  :
                        if loop == True:
                            self.error = EXTERNAL_BLOCKS(self.string, self.normal_string, self.data_base, self.line).END_BLOCK_TREATMENT()
                            if self.error is None:
                                self._return_ = 'end:'
                            else: pass
                        else: self.error = ERRORS(self.line).ERROR4()
                   
                    else:
                        if self.normal_string[ -1 ] != ':' :
                            if self.normal_string not in [ 'elif', 'else', 'end', 'def', 'func', 'class']:
                                if class_key is False:
                                    self._return_   = 'any'
                                    self.value      = 't'*self.back_end+self.normal_string
                                elif class_key is True:
                                    self._return_ = 'any'
                                    self.value, self.error = SELF_METHOD( self.normal_string, self.data_base,
                                                                                    self.line ).SELF_METHOD()
                                    if self.error == None:
                                        self.value = 't'*self.back_end+self.value
                                    else: pass
                            else:
                                _, self.error = self.control.CHECK_NAME( self.normal_string )
                        else: self.error = ERRORS(self.line).ERROR0( self.normal_string )

                except IndexError:
                    self.error = ERRORS(self.line).ERROR4()
            else:
                self._return_   = 'empty'
                self.error      = None

        except IndexError:
            self.error      = None
            self._return_   = 'empty'

        if self.error is None: pass
        else:
            if class_name:
                self.error += bm.fg.rbg(0, 255, 0) + ' in {}( )'.format( func_name ) + bm.init.reset
                self.error += self.err
            else:
                self.error += bm.fg.rbg(0, 255, 0) + ' in {}( )'.format( func_name ) + bm.init.reset

        return self._return_, self.value, self.error

    def BLOCK_TREATMENT(self, num :int, function : any = 'def' ):
        self.error                          = None
        self._return_                       = None
        self.type                           = [ type( int()), type(float()), type(complex())]
        self.new_normal_string              = self.normal_string[ num : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None:
            self._return_, self.error = self.lex_parxer.NUMERCAL_LEXER( self.new_normal_string,
                                                                self.data_base, self.line ).LEXER( self.normal_string )
            if self.error is None:
                if   type(self._return_) == type(bool())    :   self._return_ = self._return_
                elif type(self._return_) in self.type       :   self._return_ = True
                elif type(self._return_) in [ type( list() ), type( tuple() ) ] :
                    if  self._return_:      self._return_ = True
                    else:                   self._return_ = False
                elif type(self._return_) == type(range(1))  :   self._return_ = True
                elif type(self._return_) == type(None)      :   self._return_ = False
                elif type(self._return_) == type(str())     :   self._return_ = [True if self._return_ else False][0]
                elif type(self._return_) == type(dict())    :   self._return_ = [True if list(self._return_.keys()) else False][0]
            else:
                if function is None: pass
                elif function in ['def', 'class', 'for']:
                    self._error_ = fe.FileErrors(self.error).initError()
                    if self._error_ not in [ 'SyntaxError' ]: self.error = None
                    else: pass
        else: self.error = ERRORS( self.line ).ERROR0( self.normal_string )

        return self._return_, self.error

    def TRY_BLOCK_TREATMENT(self, num:int = 3):
        self.error                          = None
        self._return_                       = None
        self.key                            = None
        self.new_normal_string              = None
        self.value                          = None
        self.func                           = [ 'begin' if num == 5 else 'try' ][ 0 ]

        try:
            if self.normal_string[ -1 ] == ':':
                self.key                            = True
                self.new_normal_string              = self.normal_string[ num : -1 ]
                self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

            else:
                self.key = False
                self.new_normal_string = self.normal_string[ num : ]
                self.new_normal_string, self.error = self.control.DELETE_SPACE(self.new_normal_string)

            if self.error is None:
                if self.key is True:    self.error = ERRORS( self.line ).ERROR0( self.normal_string )
                else:
                    self.value = self.control.DELETE_SPACE( self.normal_string )
                    self._return_ = 'any'

            else:
                if self.key is True:
                    self.error      = None
                    self._return_   = self.func+':'
                else:   self.error = ERRORS( self.line ).ERROR1( self.func )
        except IndexError:
            if self.normal_string[ -1 ] == ':':
                self.error = None
                self._return_ = self.func+':'
            else:   self.error = ERRORS( self.line ).ERROR1( self.func )

        return self._return_, self.value, self.error

    def FOR_BLOCK_TREATMENT(self, inter : bool = False):
        self.error              = None
        self._return_           = None
        self.value              = None
        self.key                = None

        try:
            if self.normal_string[ -1 ] == ':':
                self.key                            = True
                self.new_normal_string              = self.normal_string[ 3 : -1 ]
                self.new_normal_string, self.error  = self.control.DELETE_SPACE(self.new_normal_string)
            else:
                self.key                            = False
                self.new_normal_string              = self.normal_string[3 : ]
                self.new_normal_string, self.error  = self.control.DELETE_SPACE(self.new_normal_string)

            if self.error is None:
                if self.key is True:
                    self._return_                = 'for:'
                    self.new_normal_string      += ':'
                    self.lex, self.error         = partial_lexer.LEXER( self.normal_string, self.data_base,
                                                                self.line ).MAIN_LEXER(main_string = self.normal_string)
                    
                    if self.error is None:
                        self._values_, self.var_name, self.operator, self.error = MAIN_FOR( self.lex, self.data_base,
                                                                            self.line).BOCKS( self.new_normal_string )
                        if self.error is None:
                            self.value = {'value' : self._values_, 'variable' : self.var_name}
                        else: 
                            if inter is False:
                                self._error_ = fe.FileErrors( self.error  ).initError()
                                if self._error_ not in  [ 'SyntaxError' ] : self.error = None
                                else: pass
                            else: pass
                    else: pass
                else:
                    self.value = self.control.DELETE_SPACE( self.normal_string )
                    self._return_ = 'any'
            else:
                if self.key is True:    self.error = ERRORS( self.line ).ERROR0( self.normal_string )
                else:   self.error = ERRORS(self.line).ERROR1('for')
        except IndexError:
            if self.normal_string[ -1 ] == ':': self.error = ERRORS(self.line).ERROR0(self.normal_string)
            else:   self.error = ERRORS(self.line).ERROR1('for')
            

        return self._return_, self.value, self.error

class MAIN_FOR:
    def __init__(self, master: dict, data_base:dict, line:int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.num_lex            = numeric_lexer
        self.num                = numerical_value
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.all_data           = self.master[ 'all_data' ]
        self.logical_op         = self.all_data[ 'logical_operator' ]
        self.boolean_op         = self.all_data[ 'bool_operator' ]
        self.arithmetic_op      = self.all_data[ 'arithmetic_operator' ]
        self.if_egal            = self.master[ 'if_egal' ]

    def BOCKS(self, main_string:str):
        self.error                  = None
        self._return_name_          = None
        self._return_value_         = None
        self._return_op_            = None
        self.values                 = self.all_data[ 'value' ]


        if self.if_egal is not True:
            if len( self.boolean_op ) == 1:
                #if self.boolean_op[ 0 ] is None:
                if len( self.logical_op ) == 1:
                    if type( self.logical_op[ 0 ] ) == type( list()):
                        self.sub_logical_op = self.logical_op[ 0 ][ 0 ]
                        if self.sub_logical_op in [ 'in' ]:
                            self._return_op_ = 'in'
                            self.arithmetic_op = self.arithmetic_op[ 0 ]
                            if self.arithmetic_op[ 0 ] is None:
                                self.arithmetic_op  = [ self.arithmetic_op[ 1 ] ]
                                self.values         = self.values[ 0 ]
                                if len( self.values ) > 1:
                                    self._return_name_, self.error = VARIABLE_CHECKING( self.values[ 0 ],
                                                                        self.data_base, self.line ).CHECK( main_string )
                                    if self.error is None:
                                        self.data_analyze   = self.values[ 0 ]
                                        self.values         = [ self.values[ 1 : ]]
                                        self._values_       = {
                                            'value'                 : self.values,
                                            'bool_operator'         : [ None ],
                                            'logical_operator'      : [ None ],
                                            'arithmetic_operator'   : self.arithmetic_op,

                                        }
                                        self.rebuild_value  = {
                                            'all_data'              : self._values_,
                                            'if_egal'               : None
                                        }

                                        self.get_values, self.error = self.num.NUMERICAL( self.rebuild_value, self.data_base,
                                                    self.line ).ANALYSE( main_string, loop = True )

                                        if self.error is None:
                                            if type( self.get_values[ 0 ] ) in [ type( tuple()), type(list()),
                                                                                 type(str()), type( range(0, 1))]:
                                                self._return_value_ = self.get_values[ 0 ]
                                            else: self.error = ERRORS( self.line ).ERROR5( self.get_values )
                                        else: pass
                                    else: pass
                                else: self.error = ERRORS( self.line ).ERROR0( main_string )
                            else: self.error = ERRORS( self.line ).ERROR0( main_string )
                        else: self.error = ERRORS( self.line ).ERROR0( main_string )
                    else: self.error = ERRORS( self.line ).ERROR0( main_string )
                else: self.error = ERRORS( self.line ).ERROR0( main_string )

                if self.error is None:
                    if self.boolean_op[ 0 ] is None: pass
                    else: 'to do'
                else: pass
            else: self.error = ERRORS( self.line ).ERROR0( main_string )
        else: self.error = ERRORS( self.line ).ERROR0( main_string )

        return self._return_value_,  self._return_name_, self._return_op_, self.error

class VARIABLE_CHECKING:
    def __init__(self, master:any, data_base:dict, line:int):
        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )

    def CHECK(self, main_string: str):
        self.error              = None
        self._return_name_      = None

        if type( self.master ) == type( dict() ):
            if self.master[ 'numeric' ] is not None:
                try:
                    self.name_var = self.master[ 'numeric' ][ 0 ]
                    if self.name_var:
                        self.name_var, self.error = self.control.CHECK_NAME( self.name_var )
                        if self.error is None:  self._return_name_ = self.name_var
                        else:   self.error = self.error
                    else:   self.error = ERRORS( self.line ).ERROR0( main_string )
                except IndexError:  self.error = ERRORS( self.line ).ERROR0( main_string )
            else:   self.error = ERRORS( self.line ).ERROR0( main_string )
        else:   self.error = ERRORS( self.line ).ERROR0( main_string )

        return self._return_name_, self.error

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

        else:
            pass

        return  self.error

class SELF_METHOD:
    def __init__(self, master: str, data_base: dict, line: int):
        self.master     = master
        self.line       = line
        self.data_base  = data_base
        self.control    = control_string.STRING_ANALYSE(self.data_base, self.line)

    def SELF_METHOD( self ):
        self.error      = None
        self.newString  = ''
        try:
            if self.master[ : 5] == 'self.':
                self.newString = self.master[ 5 : ]
                self.newString, self.error = self.control.DELETE_SPACE( self.newString )
                if self.error is None: pass
                else: self.error = ERRORS( self.line ).ERROR0( self.master )
            else: self.error = ERRORS( self.line ).ERROR6( self.master )
        except IndexError:
            self.error = ERRORS( self.line ).ERROR6( self.master )

        return self.newString, self.error

class ERRORS:
    def __init__(self, line: int):
        self.line           = line
        self.cyan           = bm.fg.cyan_L
        self.red            = bm.fg.red_L
        self.green          = bm.fg.green_L
        self.yellow         = bm.fg.yellow_L
        self.magenta        = bm.fg.magenta_M
        self.white          = bm.fg.white_L
        self.blue           = bm.fg.blue_L
        self.reset          = bm.init.reset

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >>. '.format(self.white,
                                                                self.cyan, string) + error
        return self.error+self.reset

    def ERROR1(self, string: str = 'else'):
        error = '{}<< : >> {}is not defined at the {}end. {}line: {}{}'.format(self.red, self.white, self.green,
                                                                            self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError' ).Errors()+ '{}invalid syntax in {}<< {} >> {}block. '.format(self.white,
                                                                            self.cyan, string, self.yellow) + error
        return self.error+self.reset

    def ERROR4(self):
        self.error = fe.FileErrors('IndentationError').Errors() + '{}unexpected an indented block, {}line: {}{}'.format(
            self.yellow, self.white, self.yellow, self.line)
        return self.error + self.reset

    def ERROR5(self, value ):
        error = '{}a tuple(), {}a range(), {}or a string(), {}type. {}line: {}{}'.format(self.blue, self.green,
                                                                self.cyan, self.yellow, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'TypeErrorError' ).Errors()+'{}<< {} >> {}is not {}a list(), '.format(self.cyan,
                                                value, self.white, self.yellow) + error

        return self.error+self.reset

    def ERROR6( self, string : str):
        error = '{}use {}self method {}to define variables in {}initialize( ). {}line {}{}'.format( self.white, self.magenta,
                                                            self.white, self.red, self.white, self.yellow, self.line)
        self.error = fe.FileErrors( 'SyntaxError'  ).Errors() + '{}invalid syntax in {}<< {} >>. '.format(self.white, self.cyan,
                                                                                                   string)+error
        return self.error + self.reset