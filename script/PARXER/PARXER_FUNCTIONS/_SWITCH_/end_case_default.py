from colorama import Fore, Style, init
from script import  control_string
from script.PARXER.LEXER_CONFIGURE import numeric_lexer

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
                    if   self.normal_string[ : 3 ] == 'end'     :
                        if  self.normal_string[ -1 ] == ':':
                            self.error = EXTERNAL_BLOCKS( self.string, self.normal_string, self.data_base,
                                                          self.line ).END_DEFAULT_BLOCK_TREATMENT( 3 )
                            if self.error is None:
                                self._return_ = 'end:'
                            else:
                                self.error = self.error
                        else:
                            self.error = ERRORS(self.line).ERROR1( 'end' )

                    elif self.normal_string[ : 4 ] == 'case'    :
                        if self.normal_string[ - 1 ] == ':':
                            self._value_ , self.error = EXTERNAL_BLOCKS( self.string, self.normal_string,
                                                    self.data_base, self.line ).CASE_BLOCK_TREATMENT( 4 )
                            if self.error is None:
                                self._return_   = 'case:'
                                self.value      = self._value_
                            else: pass
                        else:
                            self.error = ERRORS( self.line ).ERROR1( 'elif')

                    elif self.normal_string[ : 7 ] == 'default' :
                        if self.normal_string[ - 1] == ':':
                            if self.normal_string[-1] == ':':
                                self.error = EXTERNAL_BLOCKS(self.string, self.normal_string, self.data_base,
                                                             self.line).END_DEFAULT_BLOCK_TREATMENT( 7 )
                                if self.error is None:
                                    self._return_ = 'default:'
                                else:
                                    self.error = self.error
                            else:
                                self.error = ERRORS( self.line ).ERROR1( 'default' )

                    else:  self.error = ERRORS( self.line ).ERROR4()

                except IndexError:
                    self.error = ERRORS( self.line ).ERROR0( self.normal_string )
            else:
                self._return_   = 'empty'
                self.error      = None

        except IndexError:
            self._return_ = 'empty'
            self.error = None

        return self._return_, self.value, self.error

    def CASE_BLOCK_TREATMENT(self, num: int):
        self.error                     = None
        self._return_                  = None

        self.new_normal_string         = self.normal_string[num : -1 ]
        try:
            if self.new_normal_string[ 0 ] in [ ' ' ]:
                self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

                if self.error is None:
                    self._return_, self.error = self.lex_parxer.NUMERCAL_LEXER( self.new_normal_string,
                                                            self.data_base, self.line ).LEXER( self.normal_string )

                else: self.error = ERRORS( self.line ).ERROR0( self.normal_string )
            else: self.error = ERRORS( self.line ).ERROR4()
        except IndexError: self.error = ERRORS( self.line ).ERROR4()

        return self._return_, self.error

    def END_DEFAULT_BLOCK_TREATMENT(self, num: int):
        self.error                          = None

        self.new_normal_string              = self.normal_string[ num : -1 ]
        self.new_normal_string, self.error  = self.control.DELETE_SPACE( self.new_normal_string )

        if self.error is None:
            self.error = ERRORS( self.line ).ERROR0( self.normal_string )
        else:
            self.error = None

        return  self.error

class INTERNAL_BLOCKS:
    def __init__(self, string: str, normal_string, data_base: dict, line: int):
        self.line           = line
        self.string         = string
        self.normal_string  = normal_string
        self.data_base      = data_base
        self.control        = control_string.STRING_ANALYSE( self.data_base, self.line )
        self.lex_parxer     = numeric_lexer

    def BLOCKS(self, tabulation: int):
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
                self.value      = self.normal_string
                self._return_   = 'any'

            else:
                self._return_   = 'empty'
                self.error      = None

        except IndexError:
            self.error      = None
            self._return_   = 'empty'

        return self._return_, self.value, self.error

class MAIN_SWITCH:
    def __init__(self, master: str, data_base:int, line:int):
        self.line               = line
        self.master             = master
        self.data_base          = data_base
        self.num_lex            = numeric_lexer
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )

    def BOCKS(self):
        self.error              = None
        self._return_           = None
        self.type               = [ type(int()), type(float()), type(complex()) ]

        self.string, self.error = self.control.DELETE_SPACE( self.master[ 6 : -1 ])
        if self.error is None:
            self._return_, self.error = self.num_lex.NUMERCAL_LEXER( self.string, self.data_base,
                                                                     self.line ).LEXER( self.master )
        else:
            self.error = ERRORS( self.line ).ERROR0( self.master )

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

class ERRORS:
    def __init__(self, line: int):
        self.line           = line

    def ERROR0(self, string: str):
        error = '{}line: {}{}'.format(we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >>. '.format(ke, 'SyntaxError', ae, string) + error

        return self.error

    def ERROR1(self, string: str = 'else'):
        error = '{}<< : >> {}is not defined at the {}end. {}line: {}{}'.format(ne, ke, ve, we, ke, self.line)
        self.error = '{}{} : invalid syntax in {}<< {} >> {}block. '.format(ke, 'SyntaxError', ae, string, ke) + error

        return self.error

    def ERROR4(self):
        self.error = '{}{} : {}unexpected an indented block, {}line: {}{}'.format(ie, 'IndentationError',
                                                                                  ne, we, ke, self.line)
        return self.error