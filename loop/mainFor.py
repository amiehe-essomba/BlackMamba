from os import strerror
from script.PARXER                          import numerical_value
from script.PARXER.LEXER_CONFIGURE          import numeric_lexer, partial_lexer
from script                                 import control_string
from loop import error as er


class MAIN_FOR          :
    def __init__(self,
        master         : dict,             #
        data_base      : dict,             #
        line           : int               #
        ):
        self.line           = line
        self.master         = master
        self.data_base      = data_base
        self.num_lex        = numeric_lexer
        self.num            = numerical_value
        self.control        = control_string.STRING_ANALYSE(self.data_base, self.line)
        self.all_data       = self.master['all_data']
        self.logical_op     = self.all_data['logical_operator']
        self.boolean_op     = self.all_data['bool_operator']
        self.arithmetic_op  = self.all_data['arithmetic_operator']
        self.if_egal        = self.master['if_egal']

    def BOCKS(self, main_string: strerror):
        self.error          = None
        self._return_name_  = None
        self._return_value_ = None
        self._return_op_    = None
        self.values         = self.all_data['value']

        if self.if_egal is not True:
            if len(self.boolean_op) == 1:
                if self.boolean_op[0] is None:
                    if len(self.logical_op) == 1:
                        if type(self.logical_op[0]) == type(list()):
                            self.sub_logical_op = self.logical_op[0][0]
                            if self.sub_logical_op in ['in']:
                                self._return_op_ = 'in'
                                self.arithmetic_op = self.arithmetic_op[0]
                                if self.arithmetic_op[0] is None:
                                    self.arithmetic_op  = [self.arithmetic_op[1]]
                                    self.values         = self.values[0]
                                    if len(self.values) > 1:
                                        self._return_name_, self.error = VARIABLE_CHECKING(self.values[0],
                                                                            self.data_base, self.line).CHECK(main_string)
                                        if self.error is None:
                                            self.data_analyze   = self.values[0]
                                            self.values         = [self.values[1:]]
                                            self._values_       = {
                                                'value'                 : self.values,
                                                'bool_operator'         : [None],
                                                'logical_operator'      : [None],
                                                'arithmetic_operator'   : self.arithmetic_op,
                                            }
                                            self.rebuild_value  = {
                                                'all_data'      : self._values_,
                                                'if_egal'       : None
                                            }
                                            
                                            self.get_values, self.error = self.num.NUMERICAL(self.rebuild_value,
                                                        self.data_base, self.line).ANALYSE( main_string, loop=True )
                                            
                                            if self.error is None:
                                                if type(self.get_values[0]) in [type(tuple()), type(list()),
                                                                                type(str()), type(range(1))]:
                                                    if self.get_values[0]: self._return_value_ = self.get_values[0]
                                                    else:  self.error = er.ERRORS(self.line).ERROR5(self.get_values[0])
                                                else:  self.error = er.ERRORS(self.line).ERROR5(self.get_values[0])
                                            else: pass
                                        else: pass
                                    else: self.error = er.ERRORS(self.line).ERROR0(main_string)
                                else: self.error = er.ERRORS(self.line).ERROR0(main_string)
                            else: self.error = er.ERRORS(self.line).ERROR0(main_string)
                        else: self.error = er.ERRORS(self.line).ERROR0(main_string)
                    else: self.error = er.ERRORS(self.line).ERROR0(main_string)
                else: 'to do'
            else: self.error = er.ERRORS(self.line).ERROR0(main_string)
        else: self.error = er.ERRORS(self.line).ERROR0(main_string)

        return self._return_value_, self._return_name_, self._return_op_, self.error

class VARIABLE_CHECKING :
    def __init__(self,
                 master         : any,              #
                 data_base      : dict,             #
                 line           : int               #
                 ):
        self.master             = master
        self.line               = line
        self.data_base          = data_base
        self.control            = control_string.STRING_ANALYSE( self.data_base, self.line )

    def CHECK(self,
              main_string       : str               #
              ):
        self.error              = None
        self._return_name_      = None

        if type( self.master ) == type( dict() ):
            if self.master[ 'numeric' ] is not None:
                try:
                    self.name_var = self.master[ 'numeric' ][ 0 ]
                    if self.name_var:
                        self.name_var, self.error = self.control.CHECK_NAME( self.name_var )
                        if self.error is None: self._return_name_ = self.name_var
                        else: pass
                    else: self.error = er.ERRORS( self.line ).ERROR0( main_string )
                except IndexError: self.error = er.ERRORS( self.line ).ERROR0( main_string )
            else: self.error = er.ERRORS( self.line ).ERROR0( main_string )
        else: self.error = er.ERRORS( self.line ).ERROR0( main_string )

        return self._return_name_, self.error

class FOR_BLOCK         :
    def __init__(self,
                data_base      : dict,             #
                line           : int ,             #
                normal_string  : str               #
                ):
        self.data_base          = data_base
        self.line               = line
        self.normal_string      = normal_string
        self.control            = control_string.STRING_ANALYSE(self.data_base, self.line)

    def FOR(self,
            function            : any   = None,     #
            interpreter         : bool  = False,    #
            locked              : bool  = False
            ):
        self.error          = None
        self._return_       = None
        self.value          = None
        self.key            = None

        try:
            if self.normal_string[ -1 ] == ':':
                self.key = True
                self.new_normal_string = self.normal_string[ 3 : -1 ]
                self.new_normal_string, self.error = self.control.DELETE_SPACE(self.new_normal_string)
            else:
                self.key = False
                self.new_normal_string = self.normal_string[ 3 : ]
                self.new_normal_string, self.error = self.control.DELETE_SPACE(self.new_normal_string)

            if self.error is None:
                if self.key is True:
                    self._return_           = 'for:'
                    self.new_normal_string  += ':'
                    self.lex, self.error    = partial_lexer.LEXER(self.normal_string, self.data_base,
                                                               self.line).MAIN_LEXER( self.normal_string )
                    if self.error is None:
                        if locked is False:
                            self._values_, self.var_name, self.operator, self.error = MAIN_FOR(self.lex, self.data_base,
                                                                    self.line).BOCKS( self.new_normal_string )
                            if self.error is None:  self.value = {'value': self._values_, 'variable': self.var_name}
                            else:  pass
                        else: self.value = {'value': None, 'variable': None}
                    else: pass
                else:
                    self.value      = self.control.DELETE_SPACE(self.normal_string)
                    self._return_   = 'any'
            else:
                if self.key is True: self.error = er.ERRORS(self.line).ERROR0(self.normal_string)
                else: self.error = er.ERRORS(self.line).ERROR1( 'for' )
        except IndexError:
            if self.normal_string[-1] == ':': self.error = er.ERRORS(self.line).ERROR0(self.normal_string)
            else:  self.error = er.ERRORS(self.line).ERROR1( 'for' )

        return self._return_, self.value, self.error